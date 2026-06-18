"""Worked example: weight uncertainty and sensitivity (Section IV-C).

Run:  python examples/example_sensitivity.py
SALib is optional; the Dirichlet and one-at-a-time analyses run with numpy only.
"""

import numpy as np

from aipdi import dirichlet_uncertainty, oat_elasticity, entropy_weights
from aipdi.weighting import TECHNICAL_INDICATORS

# Self-contained archetypes (same vectors as example_scoring.py).
THIN_WRAPPER = {
    "single_provider_concentration": 1.0, "no_abstraction_layer": 1.0,
    "prompt_tool_nonportability": 0.85, "finetuning_lockin": 0.30,
    "data_embeddings_lockin": 0.40, "no_open_weight_fallback": 1.0,
    "sla_criticality": 1.0,
    "ai_share_of_value": 1.0, "weak_moat": 1.0, "margin_exposure": 0.90,
    "sherlocking_exposure": 0.90, "contractual_lockin": 0.50,
}
DIVERSIFIED_MOAT = {
    "single_provider_concentration": 0.20, "no_abstraction_layer": 0.10,
    "prompt_tool_nonportability": 0.40, "finetuning_lockin": 0.20,
    "data_embeddings_lockin": 0.40, "no_open_weight_fallback": 0.50,
    "sla_criticality": 0.80,
    "ai_share_of_value": 0.80, "weak_moat": 0.30, "margin_exposure": 0.50,
    "sherlocking_exposure": 0.45, "contractual_lockin": 0.30,
}
GATEWAY = {
    "single_provider_concentration": 0.10, "no_abstraction_layer": 0.05,
    "prompt_tool_nonportability": 0.20, "finetuning_lockin": 0.10,
    "data_embeddings_lockin": 0.20, "no_open_weight_fallback": 0.20,
    "sla_criticality": 0.90,
    "ai_share_of_value": 0.70, "weak_moat": 0.55, "margin_exposure": 0.40,
    "sherlocking_exposure": 0.60, "contractual_lockin": 0.20,
}


def main():
    print("=" * 74)
    print("Weight uncertainty of the AIPDI (Dirichlet sampling around defaults)")
    print("=" * 74)
    for label, s in [("thin wrapper", THIN_WRAPPER),
                     ("diversified moat", DIVERSIFIED_MOAT),
                     ("gateway", GATEWAY)]:
        u = dirichlet_uncertainty(s, n=20000, concentration=20.0, seed=0)
        print(f"{label:18s} baseline={u['baseline']:5.1f}  "
              f"mean={u['mean']:5.1f}  std={u['std']:.2f}  "
              f"90% CI=[{u['p05']:.1f}, {u['p95']:.1f}]")

    print()
    print("One-at-a-time +/-50% weight perturbation (largest movers), thin wrapper:")
    for row in oat_elasticity(THIN_WRAPPER, delta=0.5)[:5]:
        print(f"  {row['indicator']:32s} ({row['block']:10s})  "
              f"max |dAIPDI| = {row['max_abs_change']:.2f}")

    print()
    print("Entropy weights (data-driven) over the three archetypes, technical block:")
    inds = list(TECHNICAL_INDICATORS)
    X = np.array([[s[k] for k in inds] for s in (THIN_WRAPPER, DIVERSIFIED_MOAT, GATEWAY)])
    ew = entropy_weights(X, inds)
    for k in inds:
        print(f"  {k:32s} {ew[k]:.3f}")

    print()
    try:
        from aipdi import sobol_sensitivity
        print("Sobol' indices (S1, ST) for the thin wrapper [requires SALib]:")
        res = sobol_sensitivity(THIN_WRAPPER, n=512)
        for name, idx in sorted(res.items(), key=lambda kv: kv[1]["ST"], reverse=True)[:5]:
            print(f"  {name:32s} S1={idx['S1']:+.3f}  ST={idx['ST']:+.3f}")
    except ImportError as e:
        print(f"[Sobol skipped] {e}")
    print("=" * 74)


if __name__ == "__main__":
    main()
