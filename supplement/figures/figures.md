# Paper figures: color originals and underlying data

Supplementary material for the paper "AI-Dependent or AI-Enabled? A
Reliability-Oriented Index for Measuring Downstream Reliance on
Foundation-Model Providers" (IEEE Transactions on Reliability, under
review).

This folder holds the full-color originals of Figs. 1-8 exactly as embedded
in the manuscript, plus machine-readable CSVs of the data behind the
data-bearing figures. IEEE prints in grayscale unless color fees are paid,
so the color versions live here; the paper points readers to this folder.

Reference numbers in the captions ([4], [10], [42], [46]) follow the
38-page preprint's reference list. In the trimmed submission manuscript,
four related-index references were inserted as [33]-[36], so preprint
references numbered 33 and above appear there as n+4. Quoted captions keep
the manuscript's original typography.

Correction (2026-07-05): the preprint's Fig. 3 attributed both multi-model
statistics to the a16z 2025 CIO survey. Verified against the primary
sources, the 37% (five or more models, up from 29%) figure is from the
a16z 2025 CIO survey (n=100, May 2025), while the 81% (three or more model
families in testing or production, up from 68%) figure is from the a16z
January 2026 survey of 100 Global 2000 executives. The submission uses the
corrected, grayscale-safe fig3_multimodel_v2.png; fig3_multimodel.csv
carries the corrected attribution per row.

| Figure | File | Underlying data |
|---|---|---|
| Fig. 1 | [fig1_value_chain.png](fig1_value_chain.png) | conceptual diagram, no dataset |
| Fig. 2 | [fig2_concentration.png](fig2_concentration.png) | [fig2_concentration.csv](fig2_concentration.csv) |
| Fig. 3 | [fig3_multimodel.png](fig3_multimodel.png) (preprint) and [fig3_multimodel_v2.png](fig3_multimodel_v2.png) (submission, corrected and grayscale-safe) | [fig3_multimodel.csv](fig3_multimodel.csv) |
| Fig. 4 | [fig4_matrix.png](fig4_matrix.png) | author-assigned archetype positions, illustrative only |
| Fig. 5 | [fig5_aipdi_segments.png](fig5_aipdi_segments.png) | central values listed below |
| Fig. 6 | [fig6_funding.png](fig6_funding.png) | [fig6_funding.csv](fig6_funding.csv) |
| Fig. 7 | [fig7_sample.png](fig7_sample.png) | [fig7_sample_composition.csv](fig7_sample_composition.csv), exact, derived from the packaged catalogue |
| Fig. 8 | [fig8_rbd.png](fig8_rbd.png) | conceptual reliability block diagram; regenerable by `paper/tools/eqs.py` in the paper archive |

## Captions (as in the paper)

> Fig. 1. The four-layer generative-AI value chain. Value accrues upward
> toward applications, while operational dependency runs downward: every
> application layer is, in the limit, dependent on the foundation-model and
> compute layers beneath it.

> Fig. 2. Enterprise foundation-model concentration (2025). Shares are the
> spend-based reading of Menlo Ventures [4]; a usage-based reading differs
> (32/25/20). The implied HHI exceeds the U.S. antitrust threshold for a
> highly concentrated market.

> Fig. 3. Diversification behaviour over time. Multi-model adoption is
> rising [42], yet open-weight self-hosting has not grown and may have
> declined (a16z analysis, reported in [46]), indicating that optionality is
> built into architecture more than it is exercised through self-hosting.

> Fig. 4. The two-axis dependency space. Positions are author-assigned
> archetypes illustrating the framework, not measured firm-level scores. The
> upper-right quadrant denotes existential dependency; the lower-left
> denotes resilience.

> Fig. 5. Illustrative composite AIPDI band by segment. Bands are
> author-proposed archetypes pending calibration. The infrastructure and
> gateway band is deliberately wide, reflecting low single-provider lock-in
> but high systemic criticality.

> Fig. 6. 2025 venture funding (left) concentrates at the foundation-model
> layer, while enterprise spend (right) is largest at the application layer.
> Sources: Crunchbase News [10]; Menlo Ventures [4].

> Fig. 7. Composition of the named-entity catalogue (N = 398) by segment and
> disclosed model posture. Posture coded from public disclosures where
> available (see the Appendix); counts illustrate the purposive sample, not
> a census.

> Fig. 8. Reliability block diagram of provider dependence. A
> single-provider critical path (left) is a series system whose availability
> equals the provider's, a single point of failure. Multi-provider routing
> behind an abstraction layer (right) is a parallel system that fails only
> if all providers fail, the reliability reading of multi-model redundancy;
> a self-hostable open-weight model is the limiting cold-standby spare.

## Fig. 5 central values (author-proposed archetypes, as plotted)

| Archetype | Central AIPDI value | Band as plotted |
|---|---|---|
| Thin single-provider wrapper | 90 | roughly 85-95 |
| Multi-model AI-native with moat | 52 | roughly 45-60 |
| Incumbent with embedded AI | 32 | roughly 25-40 |
| Infrastructure or gateway | 30 | roughly 15-45 (deliberately wide) |
| AI-as-minor-feature incumbent | 15 | roughly 10-20 |

These are the illustrative archetype bands of the paper's Section V, pending
empirical calibration (see the paper's Limitations section); they are not
firm-level measurements. Headline concentration numbers used across the
paper: HHI of roughly 2,914 and a top-3 provider share of roughly 88
percent, both computable from fig2_concentration.csv with
`aipdi.scoring.hhi` and `aipdi.scoring.single_supplier_share`.

Update (2026-07-11, review-driven): grayscale-safe corrected versions
added for the submission: fig2_concentration_v2_grayscale.png (HHI shown
as the 2,770-2,914 interval with the 2023 Merger Guidelines 1,800
threshold) and fig8_rbd_v2_grayscale.png (larger labels, shared-
infrastructure caveat). The submission renumbers figures and tables
sequentially and renames the excerpt table's "Indic. AIPDI" column to
"Rule band"; supplement files keep their historical names.
