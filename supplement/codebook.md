# AIPDI scoring codebook, version 1.0 (frozen 2026-07-11)

Indicator-level scoring anchors for the AI-Provider Dependency Index.
This codebook operationalizes the paper's Table II rubric: the weights say
how much an indicator counts; these anchors say what observed evidence
earns each score. Version 1.0 documents the anchors as applied to the
eighteen evidence-coded configurations in
[case_scores.md](case_scores.md) and
[case_scores_extended.md](case_scores_extended.md). Any future change is
a new version; scores are always reported against a stated version.

## General rules

- Unit of analysis: one product configuration at a stated time window
  (firm-level only when the firm is effectively one product). Historical
  configurations are scored on evidence available for that window.
- Scale: each indicator is scored in [0, 1]; the five ordinal anchors
  0, 0.25, 0.50, 0.75, 1.00 are the reference points, and intermediate
  values are permitted where evidence clearly places a case between
  anchors.
- Evidence hierarchy (descending): firm primary disclosures (engineering
  blogs, documentation, filings); provider primary documents (case
  studies, incident reports); top-tier press (named outlets with
  editorial standards); aggregators and secondary analyses (admissible
  only with a flag). Conflicts resolve upward: primary beats press beats
  aggregator; ties resolve to the more recent source.
- Missing evidence: score at the segment-typical anchor AND flag. Flagged
  values are uncertainty, not facts: they are reported per configuration
  and stress-tested in the sensitivity analysis.
- Indicator character: indicators 1, 4, 5, 6, 7, 10, 12 are largely
  factual (directly observable architecture or contract facts);
  indicators 2, 3, 8, 9, 11 require structured judgment against the
  anchors below.
- Workload weighting: provider counts and shares always refer to
  production traffic on critical calls (calls whose failure stops or
  materially degrades the primary user job), not to configured or
  advertised providers.

## Technical and operational indicators (sub-index T)

1. single_provider_concentration (weight 0.22). Share of critical model
   calls routed to the largest provider.
   0: 20% or less | 0.25: 20-40% | 0.50: 40-60% | 0.75: 60-80% |
   1.00: above 80%.
   Failure mechanism captured: series exposure to one provider's outage,
   withdrawal, or repricing. Evidence: routing disclosures, case studies,
   incident behaviour.

2. no_abstraction_layer (weight 0.12). Ability to reroute without
   rewriting application logic.
   0: provider-neutral interface plus tested automated failover |
   0.25: abstraction plus tested manual failover | 0.50: partial
   abstraction, some provider-specific paths | 0.75: major
   provider-specific rewrites required | 1.00: provider hard-coded on the
   critical path.
   Note: an abstraction layer without tested failover does not earn 0 or
   0.25; coverage matters, not the library.

3. prompt_tool_nonportability (weight 0.14). Re-validation cost of
   prompts, tool schemas, and agent scaffolding on another model family.
   0: portable formats, evaluation suite passes on 2+ families |
   0.25: minor tuning, evaluation exists | 0.50: substantial tuning, no
   cross-family evaluation | 0.75: deep single-family tuning |
   1.00: behaviour effectively specified against one model's quirks.

4. finetuning_lockin (weight 0.12). Portability of fine-tuned assets.
   0: no fine-tunes, or recipes reproducible on any base | 0.25: exportable
   adapters | 0.50: provider-hosted fine-tunes with documented migration
   path | 0.75: provider-hosted, no migration path, moderate role |
   1.00: provider-hosted fine-tunes central to the product.

5. data_embeddings_lockin (weight 0.16). Re-embedding and retrieval
   migration cost.
   0: own embedding pipeline or provider-neutral store with raw corpus
   retained | 0.25: neutral store, provider embeddings, corpus retained |
   0.50: partial; re-embedding feasible at material cost | 0.75: large
   provider-specific index, migration untested | 1.00: retrieval quality
   depends on a provider's embedding space with no retained raw corpus.

6. no_open_weight_fallback (weight 0.12). Readiness, not existence, of an
   independently operable fallback.
   0: deployed, capacity-provisioned, regularly tested fallback |
   0.25: pre-integrated warm standby | 0.50: validated deployment path,
   no reserved capacity | 0.75: plausible candidate only | 1.00: no
   credible fallback.
   (Example from the case set: Windsurf's in-house SWE-1 line at launch
   scored 0.50, validated but below frontier and not capacity-proven.)

7. sla_criticality (weight 0.12). Impact of provider loss on the primary
   user job, at a one-hour horizon unless stated.
   0: negligible user impact | 0.25: optional feature degraded |
   0.50: material feature unavailable | 0.75: core workflow severely
   degraded | 1.00: product cannot deliver its primary function.

## Commercial and strategic indicators (sub-index C)

8. ai_share_of_value (weight 0.28). Share of the product's primary user
   value that disappears without model capability. Use one disclosed
   proxy per case (jobs-to-be-done, revenue, or usage share) and state
   which; do not mix proxies silently.
   0: under 10% | 0.25: 10-35% | 0.50: 35-60% | 0.75: 60-85% |
   1.00: above 85%.

9. weak_moat (weight 0.24). Absence of model-independent defensibility.
   0: strong proprietary data, workflow, distribution, or compliance
   assets, demonstrated switching costs | 0.25: two or more such assets |
   0.50: one meaningful asset | 0.75: thin workflow layer, replicable |
   1.00: no defensibility beyond the model relationship.

10. margin_exposure (weight 0.18). Inference cost as a share of gross
    profit plus pass-through ability.
    0: immaterial cost share | 0.25: material but hedged or passed
    through | 0.50: material, partial pass-through | 0.75: large share,
    fixed customer pricing | 1.00: provider repricing directly threatens
    viability. A low cost share with contractually fixed customer pricing
    scores higher than the raw share suggests.

11. sherlocking_exposure (weight 0.20). Plausibility of the provider's own
    roadmap absorbing the use case.
    0: deep regulated or vertical workflow, no provider entry signals |
    0.25: adjacent but differentiated | 0.50: partially overlapping
    category | 0.75: provider has shipped adjacent first-party features |
    1.00: provider ships a directly competing product.

12. contractual_lockin (weight 0.10). Terms that penalize switching.
    0: none disclosed | 0.25: standard commitments | 0.50: material
    committed spend or provider equity on the cap table | 0.75: exclusivity
    or deep GTM coupling | 1.00: contractual dependence a provider could
    weaponize.

## Change log

- v1.0 (2026-07-11): anchors frozen as applied to the 18-configuration
  case set; fallback indicator explicitly defined as readiness maturity;
  critical-call share defined as the concentration basis.
