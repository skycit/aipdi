"""Inter-rater agreement statistics for AIPDI coding sheets.

Computes, per the paper's Section IV-C protocol:
- quadratic-weighted Cohen's kappa per indicator (ordinal anchors
  0, 0.25, 0.5, 0.75, 1.0) with bootstrap 95% confidence intervals;
- absolute-agreement two-way ICC(A,1) for T, C, and AIPDI totals;
- raw agreement and disagreement counts per indicator.

Usage: provide two CSVs with identical layout to
supplement/case_scores*.csv (columns: configuration name + 12 indicator
columns), one per coder, BEFORE adjudication:

    PYTHONPATH=. python3 tools/interrater.py coder1.csv coder2.csv

Numpy only. Anchors are binned to the nearest of the five ordinal levels
for kappa; totals use the package weights.
"""
from __future__ import annotations
import csv, sys
import numpy as np
from aipdi.weighting import DEFAULT_WEIGHTS, TECHNICAL_INDICATORS, COMMERCIAL_INDICATORS

LEVELS = np.array([0.0, 0.25, 0.5, 0.75, 1.0])
IND = list(TECHNICAL_INDICATORS) + list(COMMERCIAL_INDICATORS)


def load(path):
    rows = list(csv.DictReader(open(path)))
    key = 'configuration' if 'configuration' in rows[0] else ('case' if 'case' in rows[0] else 'firm')
    return {r[key]: np.array([float(r[k]) for k in IND]) for r in rows}


def to_level(x):
    return np.argmin(np.abs(LEVELS[None, :] - np.asarray(x)[:, None]), axis=1)


def qw_kappa(a, b, k=5):
    """Quadratic-weighted Cohen's kappa for ordinal categories 0..k-1."""
    a, b = np.asarray(a), np.asarray(b)
    O = np.zeros((k, k))
    for i, j in zip(a, b):
        O[i, j] += 1
    n = O.sum()
    if n == 0:
        return np.nan
    W = np.array([[(i - j) ** 2 / (k - 1) ** 2 for j in range(k)] for i in range(k)])
    E = np.outer(O.sum(1), O.sum(0)) / n
    denom = (W * E).sum()
    return 1.0 - (W * O).sum() / denom if denom > 0 else np.nan


def icc_a1(x, y):
    """Two-way random, absolute agreement, single measures ICC(A,1)."""
    d = np.column_stack([x, y]).astype(float)
    n, k = d.shape
    mean_r = d.mean(1, keepdims=True); mean_c = d.mean(0, keepdims=True); gm = d.mean()
    MSR = k * ((mean_r - gm) ** 2).sum() / (n - 1)
    MSC = n * ((mean_c - gm) ** 2).sum() / (k - 1)
    MSE = ((d - mean_r - mean_c + gm) ** 2).sum() / ((n - 1) * (k - 1))
    return (MSR - MSE) / (MSR + (k - 1) * MSE + k * (MSC - MSE) / n)


def totals(vec):
    wT = np.array([DEFAULT_WEIGHTS[k] for k in TECHNICAL_INDICATORS])
    wC = np.array([DEFAULT_WEIGHTS[k] for k in COMMERCIAL_INDICATORS])
    T = 50 * wT @ vec[:7]; C = 50 * wC @ vec[7:]
    return T, C, T + C


def main(p1, p2, n_boot=2000, seed=0):
    c1, c2 = load(p1), load(p2)
    common = sorted(set(c1) & set(c2))
    print(f"configurations in both files: {len(common)}")
    A = np.array([c1[n] for n in common]); B = np.array([c2[n] for n in common])
    rng = np.random.default_rng(seed)
    print(f"\n{'indicator':32s} {'raw agree':>9s} {'qw-kappa':>9s} {'95% CI':>15s}")
    for j, name in enumerate(IND):
        la, lb = to_level(A[:, j]), to_level(B[:, j])
        raw = (la == lb).mean()
        k0 = qw_kappa(la, lb)
        boots = []
        for _ in range(n_boot):
            idx = rng.integers(0, len(la), len(la))
            boots.append(qw_kappa(la[idx], lb[idx]))
        lo, hi = np.nanpercentile(boots, [2.5, 97.5])
        print(f"{name:32s} {raw:9.2f} {k0:9.2f} [{lo:5.2f}, {hi:5.2f}]")
    for label, idx in (('T', 0), ('C', 1), ('AIPDI', 2)):
        x = np.array([totals(v)[idx] for v in A]); y = np.array([totals(v)[idx] for v in B])
        print(f"ICC(A,1) {label}: {icc_a1(x, y):.3f}")


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
