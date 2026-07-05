# AIPDI - AI-Provider Dependency Index (reference implementation)

Companion code and data for:

> **AI-Dependent or AI-Enabled? A Reliability-Oriented Index for Measuring
> Downstream Reliance on Foundation-Model Providers.** *IEEE Transactions on
> Reliability* (under review).

The AIPDI is a transparent 0-100 composite that measures how dependent a
downstream AI product is on its foundation-model providers, treated as a
reliability exposure. It combines a **technical / operational** sub-index *T*
(single-provider concentration, abstraction, prompt and fine-tuning
portability, data and embeddings lock-in, service-level reliance, open-weight
fallback) and a **commercial / strategic** sub-index *C* (AI share of value,
moat, margin exposure, platform/Sherlocking risk, contractual lock-in).

This repository **reproduces every score, figure, and sensitivity result in the
paper** and lets you re-score the index under alternative weighting and
aggregation choices. It also ships the full **398-entity named catalogue** used
in the study (`aipdi/data/catalogue.csv`).

---

## Install

```bash
git clone https://github.com/skycit/aipdi.git
cd aipdi
pip install -e .                  # installs the package and numpy
# optional, for variance-based Sobol' sensitivity:
pip install SALib
```

Installing the package (the `pip install -e .` above) is what puts `aipdi` on
the import path; the examples and tests below assume it. If you would rather not
install, run everything from the repo root with `PYTHONPATH=.` prefixed (for
example, `PYTHONPATH=. python examples/example_scoring.py`).

Python >= 3.9. The core depends only on **numpy**; **SALib** is optional and
used solely by `sobol_sensitivity`.

## Quick start

```python
from aipdi import aipdi, aipdi_geometric, technical_subindex, commercial_subindex

scores = {  # each indicator in [0, 1]; 1 = most dependent
    "single_provider_concentration": 1.0, "no_abstraction_layer": 1.0,
    "prompt_tool_nonportability": 0.85, "finetuning_lockin": 0.30,
    "data_embeddings_lockin": 0.40, "no_open_weight_fallback": 1.0,
    "sla_criticality": 1.0,
    "ai_share_of_value": 1.0, "weak_moat": 1.0, "margin_exposure": 0.90,
    "sherlocking_exposure": 0.90, "contractual_lockin": 0.50,
}

aipdi(scores)            # additive composite, eq. (4)
aipdi_geometric(scores)  # geometric (non-compensatory) variant, eq. (9)
```

Run the worked examples:

```bash
python examples/example_scoring.py
python examples/example_sensitivity.py

# tests: either install pytest via the extra, or run the dependency-free runner
pip install -e ".[test]" && python -m pytest -q
python tests/test_scoring.py   # no pytest needed
```

## What maps to what (Section III-F)

| Function | Equation | Meaning |
|---|---|---|
| `normalize(x, xmin, xmax)` | (1) | min-max scaling to [0, 1] |
| `technical_subindex(scores)` | (2) | T = 50 * sum_i w_i n_i |
| `commercial_subindex(scores)` | (3) | C = 50 * sum_j w_j n_j |
| `aipdi(scores)` | (4) | AIPDI = T + C, fully compensatory |
| `single_supplier_share(shares)`, `hhi(shares)` | (5) | concentration measures |
| `availability_series(a)` | (6) | single provider = single point of failure |
| `availability_parallel(a)`, `unavailability_parallel(a)` | (7) | multi-provider redundancy |
| `survivability(scores)` | (8) | R = prod_i (1 - n_i)^w_i, weakest-link |
| `aipdi_geometric(scores)` | (9) | partially non-compensatory composite |
| `expected_loss(p, impact)` | (10) | L = sum_k p_k I_k, business-continuity estimate |

All scores are bounded to [0, 100] (sub-indices to [0, 50]); `survivability`
returns [0, 1].

## Weighting (Section IV-C)

The default weights (`aipdi.DEFAULT_WEIGHTS`, mirrored in
`aipdi/data/weights_default.csv`) are **author-proposed** and act as a transparent
baseline. They are not the only option: `aipdi.weighting` provides the standard
alternatives so conclusions need not depend on one scheme.

- `equal_weights(...)`: equal weighting.
- `entropy_weights(score_matrix, indicators)`: data-driven Shannon-entropy
  weights (objective).
- `ahp_weights(pairwise, indicators)` + `consistency_ratio(pairwise)`:
  analytic-hierarchy process from elicited pairwise judgments (Saaty); check
  CR < 0.10.
- `budget_allocation(points)`: budget-allocation process.

Pass any returned dict as the `weights=` argument to the scoring functions.

## Sensitivity (Section IV-C)

- `dirichlet_uncertainty(scores)`: Monte-Carlo spread of an entity's AIPDI when
  the weights are sampled on the simplex around the defaults (numpy only).
- `oat_elasticity(scores)`: one-at-a-time +/-50% weight perturbation, ranked by
  swing (numpy only).
- `sobol_sensitivity(scores)`: first-order (S1) and total-effect (ST) Sobol'
  indices over the weights (requires SALib), following Saisana, Saltelli &
  Tarantola (2005).

## Catalogue and indicative bands

`aipdi/data/catalogue.csv` holds all 398 entities (segment, vertical and role,
disclosed posture S/M/O, segment-typical coding flag, source).
`load_catalogue()` returns the rows and attaches the deterministic
`indicative_band(segment, posture)` value used for the "Indic. AIPDI" column of
Table V. **These bands are coarse locators, not firm-level measurements**
(Sections IV-C, VIII); for an actual score, collect the indicator evidence and
call `aipdi(...)`.

## Paper supplementary material

The `supplement/` folder holds citable supplementary material relocated from
the submission manuscript to meet the journal's 15-page limit:

- [`supplement/table_V_full_catalogue.csv`](supplement/table_V_full_catalogue.csv)
  and [`supplement/table_V_full_catalogue.md`](supplement/table_V_full_catalogue.md):
  the paper's full Table V, all 398 catalogue entries WITH the computed
  Indic. AIPDI column, the segment-typical (dagger) flag, the paper's caption
  and posture-code legend, and each source's reference number in the paper.
- [`supplement/trimmed_material.md`](supplement/trimmed_material.md): passages
  and table rows condensed or removed from the submission copy, preserved
  verbatim with their original location in the paper.
- [`supplement/related_indices_comparison.md`](supplement/related_indices_comparison.md):
  structured comparison of the AIPDI against adjacent dependency instruments
  (AIIVI, FMTI, Ecosystem Graphs, CVL, country-level AIDI, provider-health
  scores, qualitative industry frameworks, psychometric scales, and
  regulatory regimes).
- [`supplement/practitioner_guide.md`](supplement/practitioner_guide.md):
  step-by-step self-assessment guide for startups and SMEs, from the
  substitution and withdrawal tests to a computed AIPDI score and a
  prioritized mitigation list.
- [`supplement/figures/`](supplement/figures/): full-color originals of the
  paper's Figs. 1-8 (IEEE prints in grayscale) with their captions
  ([`figures.md`](supplement/figures/figures.md)) and machine-readable CSVs
  of the underlying figure data. The provider-share CSV reproduces the
  paper's headline HHI (about 2,914) and top-3 share (about 88 percent) via
  `aipdi.scoring.hhi` and `aipdi.scoring.single_supplier_share`; the sample
  composition CSV is derived exactly from the packaged catalogue.

## Methodological references

- OECD & EC-JRC, *Handbook on Constructing Composite Indicators* (2008).
- M. Saisana, A. Saltelli, S. Tarantola, "Uncertainty and sensitivity analysis
  techniques as tools for the quality assessment of composite indicators,"
  *J. Royal Statistical Society A*, 168(2), 2005.
- T. L. Saaty, "How to make a decision: the analytic hierarchy process,"
  *European J. Operational Research*, 1990.
- S. El Gibari, T. Gómez, F. Ruiz, "Building composite indicators using
  multicriteria methods: a review," *J. Business Economics*, 2019.
- M. Mazziotta, A. Pareto, "Methods for constructing composite indices: one for
  all or all for one?," *Rivista Italiana di Economia Demografia e Statistica*, 2013.

## License

MIT - see `LICENSE`. If you use this code or the catalogue, please cite the
paper (see `CITATION.cff`).
