"""Tests for aipdi.scoring and aipdi.weighting.

Run:  python -m pytest -q     (or)     python tests/test_scoring.py
"""

import math
import numpy as np

from aipdi import (
    normalize, technical_subindex, commercial_subindex, aipdi,
    aipdi_geometric, survivability, hhi, single_supplier_share,
    availability_series, availability_parallel, expected_loss,
    equal_weights, entropy_weights, ahp_weights, consistency_ratio,
    budget_allocation, indicative_band, load_catalogue,
    TECHNICAL_INDICATORS, COMMERCIAL_INDICATORS, DEFAULT_WEIGHTS,
)

ALL = list(TECHNICAL_INDICATORS) + list(COMMERCIAL_INDICATORS)


def zeros():
    return {k: 0.0 for k in ALL}


def ones():
    return {k: 1.0 for k in ALL}


def test_default_weights_sum_to_one_per_block():
    assert math.isclose(sum(DEFAULT_WEIGHTS[k] for k in TECHNICAL_INDICATORS), 1.0, abs_tol=1e-9)
    assert math.isclose(sum(DEFAULT_WEIGHTS[k] for k in COMMERCIAL_INDICATORS), 1.0, abs_tol=1e-9)


def test_normalize():
    assert normalize(5, 0, 10) == 0.5
    assert normalize(-3, 0, 10) == 0.0          # clipped
    assert normalize(99, 0, 10) == 1.0          # clipped


def test_aipdi_bounds():
    assert aipdi(zeros()) == 0.0
    assert math.isclose(aipdi(ones()), 100.0, abs_tol=1e-9)
    assert math.isclose(technical_subindex(ones()), 50.0, abs_tol=1e-9)
    assert math.isclose(commercial_subindex(ones()), 50.0, abs_tol=1e-9)


def test_additive_equals_sum_of_subindices():
    s = {k: (i % 5) / 4.0 for i, k in enumerate(ALL)}
    assert math.isclose(aipdi(s), technical_subindex(s) + commercial_subindex(s), abs_tol=1e-9)


def test_geometric_bounds_and_weakest_link():
    assert math.isclose(aipdi_geometric(zeros()), 0.0, abs_tol=1e-9)
    assert math.isclose(aipdi_geometric(ones()), 100.0, abs_tol=1e-9)
    # one maxed lock-in indicator drives the geometric score high even if others are 0
    s = zeros()
    s["single_provider_concentration"] = 1.0
    assert aipdi_geometric(s) > aipdi(s)        # non-compensatory penalty


def test_survivability_monotone():
    assert math.isclose(survivability(zeros()), 1.0, abs_tol=1e-9)
    assert math.isclose(survivability(ones()), 0.0, abs_tol=1e-9)


def test_hhi_and_share():
    assert math.isclose(hhi([40, 27, 21, 12]), 2914.0, abs_tol=1e-6)
    assert math.isclose(hhi([100]), 10000.0, abs_tol=1e-6)
    assert math.isclose(single_supplier_share([80, 15, 5]), 0.80, abs_tol=1e-9)


def test_series_parallel():
    assert math.isclose(availability_series([0.99]), 0.99, abs_tol=1e-12)
    assert math.isclose(availability_series([0.99, 0.99]), 0.9801, abs_tol=1e-9)
    # parallel redundancy strictly improves availability
    assert availability_parallel([0.99, 0.99, 0.99]) > 0.99
    assert math.isclose(availability_parallel([0.9, 0.9]), 0.99, abs_tol=1e-9)


def test_expected_loss():
    assert math.isclose(expected_loss([0.5, 0.5], [10, 20]), 15.0, abs_tol=1e-9)


def test_equal_weights():
    w = equal_weights(TECHNICAL_INDICATORS)
    assert math.isclose(sum(w.values()), 1.0, abs_tol=1e-9)
    assert all(math.isclose(v, 1.0 / len(TECHNICAL_INDICATORS)) for v in w.values())


def test_entropy_weights_sum_to_one():
    X = np.array([[0.1, 0.9, 0.5, 0.2, 0.4, 0.3, 0.7],
                  [0.8, 0.2, 0.5, 0.9, 0.1, 0.6, 0.3],
                  [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]])
    w = entropy_weights(X, list(TECHNICAL_INDICATORS))
    assert math.isclose(sum(w.values()), 1.0, abs_tol=1e-6)


def test_ahp_consistency():
    # perfectly consistent 3x3 matrix => CR == 0 and recovers ratios
    A = np.array([[1, 2, 4], [0.5, 1, 2], [0.25, 0.5, 1]], dtype=float)
    assert consistency_ratio(A) < 1e-6
    w = ahp_weights(A, ["a", "b", "c"])
    assert math.isclose(w["a"] / w["b"], 2.0, rel_tol=1e-6)


def test_budget_allocation():
    w = budget_allocation({"a": 50, "b": 30, "c": 20})
    assert math.isclose(w["a"], 0.5, abs_tol=1e-9)


def test_indicative_band_and_catalogue():
    assert indicative_band("AI-native", "S") == 90
    assert indicative_band("AI-native", "M\u2020") == 55     # dagger ignored
    assert indicative_band("Provider", "O") == 10
    rows = load_catalogue()
    assert len(rows) == 398
    assert {r["segment"] for r in rows} == {"Provider", "Infrastructure", "AI-native", "Incumbent"}




def test_availability_parallel_beta():
    from aipdi.scoring import availability_parallel, availability_parallel_beta
    a = [0.99718, 0.99718]
    assert abs(availability_parallel_beta(a, 0.0) - availability_parallel(a)) < 1e-12
    assert abs(availability_parallel_beta(a, 1.0) - 0.99718) < 1e-9
    mid = availability_parallel_beta(a, 0.3)
    assert availability_parallel(a) > mid > 0.99718

if __name__ == "__main__":
    fns = [v for k, v in sorted(globals().items()) if k.startswith("test_") and callable(v)]
    passed = 0
    for fn in fns:
        fn()
        passed += 1
        print(f"ok  {fn.__name__}")
    print(f"\n{passed}/{len(fns)} tests passed")
