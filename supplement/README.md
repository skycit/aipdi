# AIPDI paper supplement: index and guide for researchers

Citable supplementary material for:

> Keshtkar, M., "AI-Dependent or AI-Enabled? A Reliability-Oriented Index
> for Measuring Downstream Reliance on Foundation-Model Providers,"
> IEEE Transactions on Reliability (under review).

This folder holds everything relocated from the manuscript for the
journal's 15-page limit, plus the evidence base behind the paper's scores.
Nothing was deleted from the paper without being preserved here first.
Bracketed citations anywhere in this folder resolve against
[paper_references.md](paper_references.md).

## Contents

| File | What it is |
|---|---|
| [paper_references.md](paper_references.md) | The submission's complete numbered reference list (72 entries); resolves all [n] citations in this folder |
| [table_V_full_catalogue.md](table_V_full_catalogue.md) / [.csv](table_V_full_catalogue.csv) | The full 398-entity catalogue with the computed Indic. AIPDI column, dagger flags, caption, and legend |
| [case_scores.md](case_scores.md) / [.csv](case_scores.csv) | Flagship indicator-level coding sheets: Jasper 2022, Windsurf pre-cutoff, Harvey pre and post, Cursor, with per-indicator evidence and sources |
| [case_scores_extended.md](case_scores_extended.md) / [.csv](case_scores_extended.csv) | Thirteen further public-evidence case scores; empirical validation of the rule bands; the commercial-residual finding |
| [provider_availability.md](provider_availability.md) / [provider_incidents.csv](provider_incidents.csv) | Documented 2024-2026 provider incident inventory with primary sources, and the availability computation behind Section V-D |
| [related_indices_comparison.md](related_indices_comparison.md) | AIPDI versus 14 adjacent instruments (AIIVI, FMTI, CVL, AIDI, GAIDS, provider-health scores, regulatory regimes) |
| [practitioner_guide.md](practitioner_guide.md) | Step-by-step self-assessment guide for founders and SMEs, including the worked two-business comparison and geopolitical guidance |
| [trimmed_material.md](trimmed_material.md) | Every passage condensed or removed from the submission copy, preserved verbatim with its original location |
| [figures/](figures/) | Full-color originals of all paper figures (IEEE prints grayscale), captions, and machine-readable data behind the data-bearing figures |

## Benchmarking your framework against the AIPDI

If you are developing another dependency, lock-in, or platform-risk
instrument and want to test it against ours:

1. Install the package (repository root): `pip install -e .` (Python 3.9+,
   numpy only). `PYTHONPATH=. python3 tests/test_scoring.py` should report
   14/14.
2. Common test set: score the same entities we score. The 17 evidence-based
   configurations in case_scores*.csv carry full indicator vectors, so you
   can recompute our index under your own weights or aggregation
   (`aipdi.weighting` provides equal, entropy, AHP, and budget-allocation
   schemes) or feed the same evidence into your instrument.
3. Population comparison: `aipdi.catalogue.load_catalogue()` returns all
   398 entities with segment, posture, and the deterministic indicative
   band; compare your instrument's distribution against Table V.
4. Ground truth for validation: provider_incidents.csv lists documented
   dependency events (outages, access withdrawal, silent quality
   degradation, vertical Sherlocking) with dates and primary sources; a
   useful test of any instrument is whether high scores anticipate these
   outcomes (see the paper's Fig. 9 cases: Jasper, Windsurf, Harvey,
   Cursor).
5. Sensitivity: `aipdi.sensitivity` implements Dirichlet weight
   uncertainty, one-at-a-time elasticity, and Sobol' indices, so weight
   choices can be stress-tested identically across instruments.

Coding-protocol note: case scores are public-evidence codings on the
paper's Table II anchors (two-coder protocol; insufficient evidence coded
at segment-typical values and flagged). They are not audited internal
measurements; treat them as reproducible estimates with the stated
uncertainty intervals.

License: MIT (repository root). If you use this material, please cite the
paper (CITATION.cff) and, where relevant, the primary sources listed in
each file.
