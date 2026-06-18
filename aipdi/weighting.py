"""Indicator weighting schemes for the AIPDI.

The composite weights reported in the paper are author-proposed (a transparent
baseline). As discussed in Section IV-C, weights for a composite indicator may
instead be *derived*, by participatory methods (the budget-allocation process
and the analytic-hierarchy process) or by data-driven methods (principal-
component or information-entropy weighting). This module provides those
alternatives so that results can be re-scored under any scheme and shown not to
depend on one particular weighting.

References
----------
- OECD & EC-JRC, *Handbook on Constructing Composite Indicators* (2008): menu of
  weighting and aggregation methods (equal, budget allocation, AHP, PCA, entropy).
- T. L. Saaty, "How to make a decision: the analytic hierarchy process,"
  *European J. Operational Research*, 1990 (AHP and the consistency ratio).
- S. El Gibari, T. Gomez, F. Ruiz, "Building composite indicators using
  multicriteria methods: a review," *J. Business Economics*, 2019.
"""

from __future__ import annotations

from typing import Dict, Mapping, Sequence

import numpy as np

# --------------------------------------------------------------------------- #
# Canonical indicator sets (order is fixed and used throughout the package).   #
# --------------------------------------------------------------------------- #
TECHNICAL_INDICATORS = (
    "single_provider_concentration",
    "no_abstraction_layer",
    "prompt_tool_nonportability",
    "finetuning_lockin",
    "data_embeddings_lockin",
    "no_open_weight_fallback",
    "sla_criticality",
)

COMMERCIAL_INDICATORS = (
    "ai_share_of_value",
    "weak_moat",
    "margin_exposure",
    "sherlocking_exposure",
    "contractual_lockin",
)

# Author-proposed default weights (Table II). Each block sums to 1.0.
DEFAULT_WEIGHTS: Dict[str, float] = {
    # technical / operational
    "single_provider_concentration": 0.22,
    "no_abstraction_layer": 0.12,
    "prompt_tool_nonportability": 0.14,
    "finetuning_lockin": 0.12,
    "data_embeddings_lockin": 0.16,
    "no_open_weight_fallback": 0.12,
    "sla_criticality": 0.12,
    # commercial / strategic
    "ai_share_of_value": 0.28,
    "weak_moat": 0.24,
    "margin_exposure": 0.18,
    "sherlocking_exposure": 0.20,
    "contractual_lockin": 0.10,
}

__all__ = [
    "TECHNICAL_INDICATORS",
    "COMMERCIAL_INDICATORS",
    "DEFAULT_WEIGHTS",
    "equal_weights",
    "entropy_weights",
    "ahp_weights",
    "consistency_ratio",
    "budget_allocation",
    "validate_weights",
]


def validate_weights(weights: Mapping[str, float],
                     indicators: Sequence[str]) -> None:
    """Raise unless weights over `indicators` are nonnegative and sum to one."""
    w = np.array([weights[k] for k in indicators], dtype=float)
    if (w < 0).any():
        raise ValueError("weights must be nonnegative (Assumption A2).")
    if not np.isclose(w.sum(), 1.0, atol=1e-6):
        raise ValueError(f"weights must sum to one (got {w.sum():.4f}).")


def equal_weights(indicators: Sequence[str]) -> Dict[str, float]:
    """Equal weighting: every indicator receives 1 / n."""
    n = len(indicators)
    return {k: 1.0 / n for k in indicators}


# --------------------------------------------------------------------------- #
# Information-entropy weighting (data-driven; objective).                      #
# --------------------------------------------------------------------------- #
def entropy_weights(score_matrix: np.ndarray,
                    indicators: Sequence[str],
                    eps: float = 1e-12) -> Dict[str, float]:
    """Entropy weights from a matrix of normalized scores.

    `score_matrix` has shape (n_entities, n_indicators) with values in [0, 1],
    columns aligned to `indicators`. An indicator that discriminates more among
    entities (lower entropy) receives a larger weight. This is the standard
    Shannon-entropy scheme used for composite indicators; it complements the
    author weights with a purely data-driven alternative.
    """
    X = np.asarray(score_matrix, dtype=float)
    if X.ndim != 2 or X.shape[1] != len(indicators):
        raise ValueError("score_matrix must be (n_entities, len(indicators)).")
    if X.shape[0] < 2:
        raise ValueError("entropy weighting needs at least two entities.")
    col_sums = X.sum(axis=0)
    col_sums[col_sums == 0] = eps
    P = X / col_sums                       # column-normalized proportions
    k = 1.0 / np.log(X.shape[0])           # entropy normalization constant
    with np.errstate(divide="ignore", invalid="ignore"):
        terms = np.where(P > 0, P * np.log(P), 0.0)
    E = -k * terms.sum(axis=0)             # entropy per indicator in [0, 1]
    d = 1.0 - E                            # degree of diversification
    if d.sum() == 0:
        w = np.full(len(indicators), 1.0 / len(indicators))
    else:
        w = d / d.sum()
    return {ind: float(wi) for ind, wi in zip(indicators, w)}


# --------------------------------------------------------------------------- #
# Analytic-hierarchy process (participatory; subjective).                      #
# --------------------------------------------------------------------------- #
# Saaty's random consistency index by matrix order n (1..10).
_RANDOM_INDEX = {1: 0.0, 2: 0.0, 3: 0.58, 4: 0.90, 5: 1.12, 6: 1.24,
                 7: 1.32, 8: 1.41, 9: 1.45, 10: 1.49}


def ahp_weights(pairwise: np.ndarray,
                indicators: Sequence[str]) -> Dict[str, float]:
    """AHP priority weights from a pairwise-comparison matrix (Saaty).

    `pairwise` is an n x n reciprocal matrix of judgments on Saaty's 1-9 scale
    (a_ij = importance of indicator i relative to j; a_ji = 1 / a_ij). Weights
    are the normalized principal eigenvector. Populate `pairwise` with elicited
    expert judgments; check `consistency_ratio` (< 0.10 is acceptable).
    """
    A = np.asarray(pairwise, dtype=float)
    n = len(indicators)
    if A.shape != (n, n):
        raise ValueError("pairwise must be (len(indicators), len(indicators)).")
    eigvals, eigvecs = np.linalg.eig(A)
    k = int(np.argmax(eigvals.real))
    w = np.abs(eigvecs[:, k].real)
    w = w / w.sum()
    return {ind: float(wi) for ind, wi in zip(indicators, w)}


def consistency_ratio(pairwise: np.ndarray) -> float:
    """Saaty consistency ratio CR = (lambda_max - n) / ((n - 1) * RI).

    CR < 0.10 indicates acceptably consistent judgments. Returns 0.0 for
    n <= 2 (always consistent).
    """
    A = np.asarray(pairwise, dtype=float)
    n = A.shape[0]
    if n <= 2:
        return 0.0
    lam = np.linalg.eigvals(A).real.max()
    ci = (lam - n) / (n - 1)
    ri = _RANDOM_INDEX.get(n, 1.49)
    return float(ci / ri) if ri else 0.0


def budget_allocation(points: Mapping[str, float]) -> Dict[str, float]:
    """Budget-allocation process: experts spread a fixed budget across
    indicators; weights are the normalized point allocations.
    """
    keys = list(points)
    vals = np.array([points[k] for k in keys], dtype=float)
    if (vals < 0).any():
        raise ValueError("allocations must be nonnegative.")
    if vals.sum() <= 0:
        raise ValueError("allocations must contain positive mass.")
    vals = vals / vals.sum()
    return {k: float(v) for k, v in zip(keys, vals)}
