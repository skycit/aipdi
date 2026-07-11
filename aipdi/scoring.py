"""Scoring functions for the AI-Provider Dependency Index (AIPDI).

This module implements, one-to-one, the equations of Section III-F of

    "AI-Dependent or AI-Enabled? A Reliability-Oriented Index for Measuring
     Downstream Reliance on Foundation-Model Providers."

Each public function notes the equation it realises. Indicators are scored on
a normalized [0, 1] scale (1 = most dependent); the composite AIPDI lies in
[0, 100] (higher = more dependent).
"""

from __future__ import annotations

from typing import Mapping, Sequence

import numpy as np

from .weighting import TECHNICAL_INDICATORS, COMMERCIAL_INDICATORS, DEFAULT_WEIGHTS

__all__ = [
    "normalize",
    "technical_subindex",
    "commercial_subindex",
    "aipdi",
    "aipdi_geometric",
    "survivability",
    "single_supplier_share",
    "hhi",
    "availability_series",
    "availability_parallel",
    "unavailability_parallel",
    "expected_loss",
]


def _as_array(x) -> np.ndarray:
    return np.asarray(x, dtype=float)


# --------------------------------------------------------------------------- #
# (1) min-max normalization                                                   #
# --------------------------------------------------------------------------- #
def normalize(x, x_min, x_max):
    """Equation (1): n_i = (x_i - x_min) / (x_max - x_min), clipped to [0, 1].

    `x` may be a scalar or array. Raises if x_max == x_min.
    """
    x = _as_array(x)
    x_min = float(x_min)
    x_max = float(x_max)
    if x_max == x_min:
        raise ValueError("x_max must differ from x_min for normalization (1).")
    n = (x - x_min) / (x_max - x_min)
    return np.clip(n, 0.0, 1.0)


def _weighted_subindex(scores: Mapping[str, float],
                       weights: Mapping[str, float],
                       indicators: Sequence[str],
                       name: str) -> float:
    """Weighted arithmetic mean on [0, 1] scaled to [0, 50] (eqs. 2, 3).

    `scores` maps indicator name -> value in [0, 1]. Weights must be
    nonnegative and sum to one over `indicators` (Assumption A2).
    """
    missing = [k for k in indicators if k not in scores]
    if missing:
        raise KeyError(f"{name}: missing scores for indicators {missing}")
    w = np.array([weights[k] for k in indicators], dtype=float)
    n = np.array([scores[k] for k in indicators], dtype=float)
    if (w < 0).any():
        raise ValueError(f"{name}: weights must be nonnegative (A2).")
    if (n < 0).any() or (n > 1).any():
        raise ValueError(f"{name}: indicator scores must lie in [0, 1] (A1).")
    if not np.isclose(w.sum(), 1.0, atol=1e-6):
        raise ValueError(f"{name}: weights must sum to one (got {w.sum():.4f}).")
    return float(50.0 * np.dot(w, n))


# --------------------------------------------------------------------------- #
# (2) technical / operational sub-index  T in [0, 50]                          #
# --------------------------------------------------------------------------- #
def technical_subindex(scores: Mapping[str, float],
                       weights: Mapping[str, float] | None = None) -> float:
    """Equation (2): T = 50 * sum_i w_i^T n_i."""
    weights = (weights or DEFAULT_WEIGHTS)
    return _weighted_subindex(scores, weights, TECHNICAL_INDICATORS, "technical")


# --------------------------------------------------------------------------- #
# (3) commercial / strategic sub-index  C in [0, 50]                           #
# --------------------------------------------------------------------------- #
def commercial_subindex(scores: Mapping[str, float],
                        weights: Mapping[str, float] | None = None) -> float:
    """Equation (3): C = 50 * sum_j w_j^C n_j."""
    weights = (weights or DEFAULT_WEIGHTS)
    return _weighted_subindex(scores, weights, COMMERCIAL_INDICATORS, "commercial")


# --------------------------------------------------------------------------- #
# (4) additive composite  AIPDI = T + C in [0, 100]                            #
# --------------------------------------------------------------------------- #
def aipdi(scores: Mapping[str, float],
          weights: Mapping[str, float] | None = None) -> float:
    """Equation (4): AIPDI = T + C, the fully compensatory composite."""
    return technical_subindex(scores, weights) + commercial_subindex(scores, weights)


# --------------------------------------------------------------------------- #
# (8) multiplicative survivability of the technical sub-index                  #
# --------------------------------------------------------------------------- #
def survivability(scores: Mapping[str, float],
                  weights: Mapping[str, float] | None = None) -> float:
    """Equation (8): R = prod_i (1 - n_i) ** w_i^T over the technical indicators.

    R in [0, 1]; R -> 0 as any single lock-in indicator -> 1 (weakest link).
    """
    weights = (weights or DEFAULT_WEIGHTS)
    n = np.array([scores[k] for k in TECHNICAL_INDICATORS], dtype=float)
    w = np.array([weights[k] for k in TECHNICAL_INDICATORS], dtype=float)
    return float(np.prod(np.power(np.clip(1.0 - n, 0.0, 1.0), w)))


# --------------------------------------------------------------------------- #
# (9) geometric (partially non-compensatory) composite                        #
# --------------------------------------------------------------------------- #
def aipdi_geometric(scores: Mapping[str, float],
                    weights: Mapping[str, float] | None = None,
                    indicators: Sequence[str] | None = None) -> float:
    """Equation (9): AIPDI_g = 100 * (1 - prod_i (1 - n_i) ** w_i).

    By default the geometric form is taken over the union of technical and
    commercial indicators with weights renormalized to sum to one across that
    union. A single indicator approaching 1 drives the score toward 100.
    """
    weights = (weights or DEFAULT_WEIGHTS)
    if indicators is None:
        indicators = list(TECHNICAL_INDICATORS) + list(COMMERCIAL_INDICATORS)
    n = np.array([scores[k] for k in indicators], dtype=float)
    w = np.array([weights[k] for k in indicators], dtype=float)
    w = w / w.sum()  # renormalize across the chosen indicator set
    prod = float(np.prod(np.power(np.clip(1.0 - n, 0.0, 1.0), w)))
    return 100.0 * (1.0 - prod)


# --------------------------------------------------------------------------- #
# (5) provider-side concentration: single-supplier share and HHI              #
# --------------------------------------------------------------------------- #
def single_supplier_share(call_shares: Sequence[float]) -> float:
    """Equation (5), first part: S = max_k q_k.

    `call_shares` is a vector of the fraction of model calls routed to each
    provider (need not sum to one; it is normalized defensively).
    """
    q = _as_array(call_shares)
    if q.sum() <= 0:
        raise ValueError("call_shares must contain positive mass.")
    q = q / q.sum()
    return float(q.max())


def hhi(shares: Sequence[float], scale_to_10000: bool = True) -> float:
    """Equation (5), second part: HHI = sum_k s_k^2.

    Shares are normalized to fractions. If `scale_to_10000`, returns the
    market-share-points convention (0-10000, the antitrust scale used in the
    paper); otherwise returns the [0, 1] form.
    """
    s = _as_array(shares)
    if s.sum() <= 0:
        raise ValueError("shares must contain positive mass.")
    s = s / s.sum()
    h = float(np.sum(s ** 2))
    return h * 10000.0 if scale_to_10000 else h


# --------------------------------------------------------------------------- #
# (6) series availability (single point of failure)                           #
# --------------------------------------------------------------------------- #
def availability_series(provider_availabilities: Sequence[float]) -> float:
    """Equation (6): components in series multiply.

    A single provider on the critical path => A_series = A_p. With several
    in-series components, A_series = prod_i A_i.
    """
    a = _as_array(provider_availabilities)
    if ((a < 0) | (a > 1)).any():
        raise ValueError("availabilities must lie in [0, 1].")
    return float(np.prod(a))


# --------------------------------------------------------------------------- #
# (7) parallel (redundant) availability / unavailability                       #
# --------------------------------------------------------------------------- #
def unavailability_parallel(provider_availabilities: Sequence[float]) -> float:
    """Equation (7), unavailability: U_par = prod_j (1 - A_j)."""
    a = _as_array(provider_availabilities)
    if ((a < 0) | (a > 1)).any():
        raise ValueError("availabilities must lie in [0, 1].")
    return float(np.prod(1.0 - a))



def availability_parallel_beta(availabilities, beta):
    """Beta-factor common-cause extension of eq. (7): eq. (8) of the paper.

    U_eff = beta * U_p + (1 - beta) * prod_j U_j, where beta in [0, 1] is
    the fraction of provider unavailability attributable to common causes
    and U_p is the (mean) single-provider unavailability. Returns the
    effective availability 1 - U_eff. With beta = 0 this reduces to
    availability_parallel; with beta = 1 redundancy provides no benefit.
    """
    a = [float(x) for x in availabilities]
    if not a:
        raise ValueError("availabilities must be non-empty")
    if not 0.0 <= float(beta) <= 1.0:
        raise ValueError("beta must be in [0, 1]")
    u_single = sum(1.0 - x for x in a) / len(a)
    u_indep = 1.0
    for x in a:
        u_indep *= (1.0 - x)
    u_eff = float(beta) * u_single + (1.0 - float(beta)) * u_indep
    return 1.0 - u_eff

def availability_parallel(provider_availabilities: Sequence[float]) -> float:
    """Equation (7): A_par = 1 - prod_j (1 - A_j) for k redundant providers."""
    return 1.0 - unavailability_parallel(provider_availabilities)


# --------------------------------------------------------------------------- #
# (10) expected dependency-related loss                                        #
# --------------------------------------------------------------------------- #
def expected_loss(probabilities: Sequence[float],
                  impacts: Sequence[float]) -> float:
    """Equation (10): L = sum_k p_k I_k.

    `probabilities` and `impacts` are aligned vectors over mutually exclusive
    provider-driven event types (Assumption A4). Used for relative comparison.
    """
    p = _as_array(probabilities)
    i = _as_array(impacts)
    if p.shape != i.shape:
        raise ValueError("probabilities and impacts must have the same shape.")
    if ((p < 0) | (p > 1)).any():
        raise ValueError("probabilities must lie in [0, 1].")
    return float(np.dot(p, i))
