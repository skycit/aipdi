"""Worked example: score archetypes and reproduce headline numbers.

Run:  python examples/example_scoring.py
"""

from aipdi import (
    aipdi, aipdi_geometric, technical_subindex, commercial_subindex,
    survivability, hhi, single_supplier_share,
    availability_series, availability_parallel, expected_loss,
    indicative_band,
)

# --------------------------------------------------------------------------- #
# Indicator scores in [0, 1] (1 = most dependent) for three illustrative       #
# archetypes from the paper. These are demonstration vectors, not audited      #
# firm measurements.                                                           #
# --------------------------------------------------------------------------- #
THIN_WRAPPER = {  # AI-native, single-provider: high on both axes
    "single_provider_concentration": 1.0, "no_abstraction_layer": 1.0,
    "prompt_tool_nonportability": 0.85, "finetuning_lockin": 0.30,
    "data_embeddings_lockin": 0.40, "no_open_weight_fallback": 1.0,
    "sla_criticality": 1.0,
    "ai_share_of_value": 1.0, "weak_moat": 1.0, "margin_exposure": 0.90,
    "sherlocking_exposure": 0.90, "contractual_lockin": 0.50,
}

DIVERSIFIED_MOAT = {  # AI-native, multi-model, real moat
    "single_provider_concentration": 0.20, "no_abstraction_layer": 0.10,
    "prompt_tool_nonportability": 0.40, "finetuning_lockin": 0.20,
    "data_embeddings_lockin": 0.40, "no_open_weight_fallback": 0.50,
    "sla_criticality": 0.80,
    "ai_share_of_value": 0.80, "weak_moat": 0.30, "margin_exposure": 0.50,
    "sherlocking_exposure": 0.45, "contractual_lockin": 0.30,
}

GATEWAY = {  # infrastructure / routing: low single-provider lock-in
    "single_provider_concentration": 0.10, "no_abstraction_layer": 0.05,
    "prompt_tool_nonportability": 0.20, "finetuning_lockin": 0.10,
    "data_embeddings_lockin": 0.20, "no_open_weight_fallback": 0.20,
    "sla_criticality": 0.90,
    "ai_share_of_value": 0.70, "weak_moat": 0.55, "margin_exposure": 0.40,
    "sherlocking_exposure": 0.60, "contractual_lockin": 0.20,
}

ARCHETYPES = [
    ("Thin single-provider wrapper (AI-native, S)", THIN_WRAPPER, "AI-native", "S"),
    ("Diversified AI-native with moat (AI-native, M)", DIVERSIFIED_MOAT, "AI-native", "M"),
    ("Multi-provider gateway (Infrastructure, M)", GATEWAY, "Infrastructure", "M"),
]


def main():
    print("=" * 74)
    print("AIPDI archetype scores  (T, C in [0,50]; AIPDI in [0,100])")
    print("=" * 74)
    print(f"{'archetype':46s} {'T':>5} {'C':>5} {'AIPDI':>6} {'geom':>6} {'band':>5}")
    for label, s, seg, posture in ARCHETYPES:
        print(f"{label:46s} {technical_subindex(s):5.1f} {commercial_subindex(s):5.1f} "
              f"{aipdi(s):6.1f} {aipdi_geometric(s):6.1f} {indicative_band(seg, posture):5d}")

    print()
    print("Survivability R (eq. 8) of the technical sub-index (lower = more fragile):")
    for label, s, _, _ in ARCHETYPES:
        print(f"  {label:46s} R = {survivability(s):.3f}")

    print()
    menlo_shares = [40, 27, 21, 12]  # Anthropic, OpenAI, Google, residual (Menlo 2025)
    print("Market concentration (Menlo spend shares 40/27/21/12):")
    print(f"  HHI = {hhi(menlo_shares):.0f}  (>2500 => highly concentrated)")
    print(f"  single-supplier share S for a firm routing 80/15/5 = "
          f"{single_supplier_share([80, 15, 5]):.2f}")

    print()
    p = 0.99
    print("Availability (each provider 0.99):")
    print(f"  single provider in series (eq. 6):           {availability_series([p]):.6f}")
    print(f"  three providers in parallel (eq. 7):         {availability_parallel([p, p, p]):.6f}")

    print()
    event_p = [0.30, 0.50, 0.40, 0.10, 0.20]   # outage, deprecation, price, policy, entry
    impact = [20, 15, 25, 30, 40]              # relative impact, scales with dependency
    print("Expected dependency-related loss (eq. 10), relative units:")
    print(f"  L = {expected_loss(event_p, impact):.1f}")
    print("=" * 74)


if __name__ == "__main__":
    main()
