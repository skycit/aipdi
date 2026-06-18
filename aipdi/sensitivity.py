"""Uncertainty and sensitivity analysis for the AIPDI weights.

Section IV-C assesses the index by sampling the weights and decomposing the
variance of the resulting scores with Sobol' indices. This module provides
two paths:

* `sobol_sensitivity`  -- variance-based first-order (S1) and total-effect
  (ST) indices via SALib, if SALib is installed.
* `dirichlet_uncertainty` -- a dependency-free fallback that perturbs the
  weights on the simplex (Dirichlet) and reports how much the AIPDI of a fixed
  score vector moves, plus a one-at-a-time (OAT) +/- elasticity per weight.

Both operate on a single entity's normalized indicator scores; the question is
how sensitive that entity's AIPDI is to the choice of weights.

Reference: M. Saisana, A. Saltelli, S. Tarantola, "Uncertainty and sensitivity
analysis techniques as tools for the quality assessment of composite
indicators," J. Royal Statistical Society A, 168(2), 2005.
"""

from __future__ import annotations

from typing import Dict, List, Mapping, Sequence

import numpy as np

from .scoring import aipdi
from .weighting import (TECHNICAL_INDICATORS, COMMERCIAL_INDICATORS,
                        DEFAULT_WEIGHTS)

__all__ = ["dirichlet_uncertainty", "oat_elasticity", "sobol_sensitivity"]

_ALL = list(TECHNICAL_INDICATORS) + list(COMMERCIAL_INDICATORS)


def _block_weights(w_tech: np.ndarray, w_comm: np.ndarray) -> Dict[str, float]:
    """Assemble a weights dict from per-block weight vectors (each sums to 1)."""
    d = {}
    for k, v in zip(TECHNICAL_INDICATORS, w_tech):
        d[k] = float(v)
    for k, v in zip(COMMERCIAL_INDICATORS, w_comm):
        d[k] = float(v)
    return d


def dirichlet_uncertainty(scores: Mapping[str, float],
                          n: int = 20000,
                          concentration: float = 20.0,
                          seed: int | None = 0) -> Dict[str, float]:
    """Monte-Carlo uncertainty of a single entity's AIPDI under weight sampling.

    Each block's weight vector is drawn from a Dirichlet centred on the default
    weights (higher `concentration` = tighter around the baseline). Returns the
    baseline score and the mean / std / 5th / 95th percentiles of the AIPDI.
    """
    rng = np.random.default_rng(seed)
    base_t = np.array([DEFAULT_WEIGHTS[k] for k in TECHNICAL_INDICATORS])
    base_c = np.array([DEFAULT_WEIGHTS[k] for k in COMMERCIAL_INDICATORS])
    out = np.empty(n, dtype=float)
    for i in range(n):
        wt = rng.dirichlet(base_t * concentration)
        wc = rng.dirichlet(base_c * concentration)
        out[i] = aipdi(scores, _block_weights(wt, wc))
    return {
        "baseline": float(aipdi(scores, DEFAULT_WEIGHTS)),
        "mean": float(out.mean()),
        "std": float(out.std()),
        "p05": float(np.percentile(out, 5)),
        "p95": float(np.percentile(out, 95)),
    }


def oat_elasticity(scores: Mapping[str, float],
                   delta: float = 0.5) -> List[Dict[str, float]]:
    """One-at-a-time +/- perturbation of each weight (Section IV-C, +/-50%).

    Each weight is scaled by (1 +/- delta) within its block, the block is
    renormalized to sum to one, and the change in AIPDI is recorded. Returns a
    list sorted by absolute swing (largest mover first).
    """
    base = float(aipdi(scores, DEFAULT_WEIGHTS))
    rows: List[Dict[str, float]] = []
    blocks = {"technical": TECHNICAL_INDICATORS, "commercial": COMMERCIAL_INDICATORS}
    for block, inds in blocks.items():
        base_w = np.array([DEFAULT_WEIGHTS[k] for k in inds], dtype=float)
        for j, ind in enumerate(inds):
            swing = 0.0
            for sign in (+1.0, -1.0):
                w = base_w.copy()
                w[j] = max(w[j] * (1.0 + sign * delta), 0.0)
                w = w / w.sum()
                wd = dict(DEFAULT_WEIGHTS)
                for k, v in zip(inds, w):
                    wd[k] = float(v)
                swing = max(swing, abs(aipdi(scores, wd) - base))
            rows.append({"indicator": ind, "block": block, "max_abs_change": swing})
    rows.sort(key=lambda r: r["max_abs_change"], reverse=True)
    return rows


def sobol_sensitivity(scores: Mapping[str, float],
                      n: int = 1024) -> Dict[str, Dict[str, float]]:
    """First-order (S1) and total-effect (ST) Sobol' indices over the weights.

    Requires SALib (`pip install SALib`). Weights are sampled on [0, 1] per
    indicator then renormalized within each block before scoring, so the Sobol'
    indices describe the influence of each *relative* weight on the AIPDI of the
    given entity. Raises ImportError if SALib is unavailable; use
    `dirichlet_uncertainty` / `oat_elasticity` as a fallback.
    """
    try:
        from SALib.sample import saltelli
        from SALib.analyze import sobol
    except Exception as exc:  # pragma: no cover - optional dependency
        raise ImportError(
            "SALib is required for sobol_sensitivity; install it with "
            "`pip install SALib`, or use dirichlet_uncertainty / oat_elasticity."
        ) from exc

    names = list(_ALL)
    problem = {
        "num_vars": len(names),
        "names": names,
        "bounds": [[0.01, 1.0]] * len(names),
    }
    param_values = saltelli.sample(problem, n, calc_second_order=False)

    nt = len(TECHNICAL_INDICATORS)
    y = np.empty(param_values.shape[0], dtype=float)
    for i, row in enumerate(param_values):
        wt = row[:nt]
        wc = row[nt:]
        wt = wt / wt.sum()
        wc = wc / wc.sum()
        y[i] = aipdi(scores, _block_weights(wt, wc))

    res = sobol.analyze(problem, y, calc_second_order=False, print_to_console=False)
    return {
        name: {"S1": float(res["S1"][i]), "ST": float(res["ST"][i])}
        for i, name in enumerate(names)
    }
