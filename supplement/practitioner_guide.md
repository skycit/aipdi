# AIPDI practitioner guide: self-assessing your product's AI-provider dependency

A step-by-step guide for founders, product leads, and platform engineers who
want to compute an AI-Provider Dependency Index (AIPDI) score for a specific
product and act on it. It accompanies the paper "AI-Dependent or AI-Enabled?
A Reliability-Oriented Index for Measuring Downstream Reliance on
Foundation-Model Providers" and the reference implementation in this
repository. The paper's Table II defines the indicator rubric; this guide
turns it into a working session you can run in roughly an hour.

Dependency is not static. Scores drift as you ship features, as providers
change models, prices, and terms, and as regulation moves. Re-score after
every major architecture change, provider announcement that affects you, or
at least quarterly.

## Step 0: two thought experiments (five minutes)

- Substitution test: if you had to replace your primary model provider in 30
  days, what breaks, what degrades, and what does it cost? If the honest
  answer is "the product stops working," you are in high-dependency
  territory regardless of any score.
- Withdrawal test: if your primary provider cut your access tomorrow (it has
  happened; see the 2025 Anthropic and Windsurf case in the paper), does the
  business survive the quarter?

## Step 1: gather the evidence (15-30 minutes)

You need honest answers, not aspirations. Useful artifacts: your API call
logs by provider, your prompt and tool-schema inventory, fine-tuning and
embedding assets, provider contracts, and revenue attribution for
AI-powered features.

## Step 2: score the twelve indicators in [0, 1]

Each indicator is scored between 0 (no dependency) and 1 (maximum
dependency). Anchors below paraphrase the paper's Table II rubric.

Technical and operational (sub-index T, weights in parentheses):

1. single_provider_concentration (0.22): share of AI inference on your
   single largest provider. All calls to one provider = 1.0; balanced
   multi-provider routing = low.
2. no_abstraction_layer (0.12): direct SDK calls hard-wired to one vendor
   = 1.0; a gateway or abstraction layer that can reroute = low.
3. prompt_tool_nonportability (0.14): prompts, tool schemas, and agent
   scaffolding tuned to one model family that would need full re-validation
   elsewhere = high.
4. finetuning_lockin (0.12): provider-hosted fine-tunes that cannot be
   exported = high; no fine-tunes or reproducible-on-any-base recipes = low.
5. data_embeddings_lockin (0.16): embeddings and retrieval indexes in a
   provider-specific space that would need full re-embedding = high.
6. no_open_weight_fallback (0.12): no tested open-weight fallback path
   = 1.0; a benchmarked, deployable open-weight spare = low.
7. sla_criticality (0.12): provider outage stops your core user journey
   immediately = high; graceful degradation = low.

Commercial and strategic (sub-index C):

8. ai_share_of_value (0.28): fraction of your product's user value that
   disappears if the AI capability disappears.
9. weak_moat (0.24): nothing proprietary between you and a clone built on
   the same API = 1.0; proprietary data, workflow, distribution, or
   compliance moat = low.
10. margin_exposure (0.18): inference spend as a share of gross margin, and
    your exposure to provider re-pricing.
11. sherlocking_exposure (0.20): how plausibly the provider's own product
    roadmap absorbs your use case (the paper's 2023 Jasper case is the
    canonical example).
12. contractual_lockin (0.10): committed spend, exclusivity, or terms that
    penalize switching.

## Step 3: compute the score

```bash
git clone https://github.com/skycit/aipdi.git && cd aipdi && pip install -e .
```

```python
from aipdi import aipdi, aipdi_geometric, technical_subindex, commercial_subindex

scores = {
    "single_provider_concentration": 0.9, "no_abstraction_layer": 0.7,
    "prompt_tool_nonportability": 0.6, "finetuning_lockin": 0.2,
    "data_embeddings_lockin": 0.5, "no_open_weight_fallback": 0.8,
    "sla_criticality": 0.9,
    "ai_share_of_value": 0.8, "weak_moat": 0.6, "margin_exposure": 0.5,
    "sherlocking_exposure": 0.6, "contractual_lockin": 0.3,
}
print("T =", technical_subindex(scores))     # 0-50
print("C =", commercial_subindex(scores))    # 0-50
print("AIPDI =", aipdi(scores))              # 0-100, additive
print("AIPDI_g =", aipdi_geometric(scores))  # weakest-link variant
```

Score with two people independently and reconcile differences; that is the
paper's own coding protocol, and disagreements are usually the most
informative part of the exercise.

## Step 4: read the result

- 0-25: structurally resilient. AI enhances the product without controlling
  its fate.
- 25-45: managed dependency, typical of diversified incumbents and
  infrastructure players.
- 45-70: elevated. One provider decision (price, deprecation, competing
  feature) materially moves your economics.
- 70-100: existential zone. The paper's thin single-provider wrapper
  archetype sits near 90; the 2025 Windsurf cutoff shows how this fails.

Also read T and C separately: high T with low C means an engineering
problem (portability); low T with high C means a strategy problem (moat,
Sherlocking); high both is the existential quadrant.

If one indicator is near 1.0, compute the geometric variant too: it refuses
to let strengths average away a single fatal weakness, which is the
reliability (weakest-link) reading.

## Step 5: prioritize mitigations

Ordered by typical return on effort:

1. Add an abstraction or gateway layer (cuts indicator 2, enables 1).
2. Qualify a second provider on your top traffic path (cuts 1, 7).
3. Benchmark one open-weight model as a cold standby, even if worse (cuts 6).
4. Keep prompts and tool schemas in a portable, provider-neutral format and
   re-run your evaluation suite on two model families (cuts 3).
5. Own your embedding pipeline or budget for re-embedding (cuts 5).
6. Build what an API cannot supply: proprietary data loops, workflow depth,
   distribution, and compliance assets (cuts 9, 11; this is the only durable
   answer on the commercial axis).
7. Negotiate exit-friendly terms before you are locked in (cuts 12).

Then re-score. The delta between your current and post-mitigation AIPDI is
a concrete, board-ready risk-reduction number.

## Geopolitical exposure: adjust the probabilities, not the score

The AIPDI measures your exposure structure; geopolitics changes how likely
the disruptive events are. Two products with identical scores face
different expected losses if one depends on a provider whose operations,
data centres, or serving regions sit in an exposed jurisdiction, or whose
government can impose export controls or order access restrictions. When
you estimate expected loss (equation (10) of the paper), ask per provider:

- Where are the data centres and serving regions that actually handle your
  traffic, and how concentrated are they geographically?
- Whose export-control and sanctions regime applies to the provider, and
  could either your government or theirs restrict your access class?
- Is the provider state-linked in a way that couples your access to
  inter-state relations?

Raise the event probabilities for withdrawal and outage accordingly. A
mitigation that reduces the score also reduces the geopolitical exposure:
a second provider only diversifies jurisdictional risk if it is domiciled
and served from a different jurisdiction.

## Worked comparison: two businesses, one question

Business A ships ten features; four run purely on a single provider's API,
direct SDK, no tested fallback, and those features drive growth. Business B
ships ten features; two run on a model it owns and serves itself. A is
currently more profitable.

Scoring both with this package (indicator values in the repository's test
fixtures spirit; adjust to your evidence):

| | T (0-50) | C (0-50) | AIPDI additive | AIPDI geometric |
|---|---|---|---|---|
| Business A (4 of 10 features on one provider) | 33 | 24 | 58 (elevated) | 100 |
| Business B (own model, 2 of 10 features) | 8 | 14 | 22 (resilient) | 23 |

Three readings matter:

1. The additive scores say A carries roughly two and a half times B's
   dependency, sitting in the elevated band where one provider decision
   (price, deprecation, a competing first-party feature, an access cutoff)
   materially moves the business.
2. The geometric (weakest-link) score for A saturates at 100 because one
   indicator is at its maximum: every AI call crosses one provider with no
   fallback. Averages hide single points of failure; the weakest-link
   variant refuses to.
3. Profitability and dependency are different axes. A earns more today,
   and expected-loss thinking (equation (10) of the paper) says exactly
   that: the impact term scales with the revenue at risk, so higher profit
   on a dependent critical path means MORE absolute exposure, not less.
   The pair (profit, AIPDI) reads like (income, credit risk): A is the
   higher-yield, higher-fragility asset; B's earnings are smaller but
   survive provider shocks.

What the score deliberately does not tell you: whether B's in-house model
will stay competitive with frontier APIs, and what it costs B to keep it
so. That is execution and upstream risk, not provider dependency; assess
it separately. AIPDI answers one question precisely: whose revenue is
exposed to someone else's decisions.

For a multi-product portfolio, score each product separately and aggregate
weighted by revenue share; a single blended score hides which product
carries the exposure.
