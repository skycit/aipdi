# Public-evidence case scores: Jasper, Windsurf, and Harvey

Supplementary material for the paper "AI-Dependent or AI-Enabled? A
Reliability-Oriented Index for Measuring Downstream Reliance on
Foundation-Model Providers" (IEEE Transactions on Reliability, under
review). This file contains indicator-level coding sheets for three named
firms whose provider-dependency configurations and outcomes are unusually
well documented in public sources, scored on the paper's Table II anchors.

Status and honesty notes:

- These are PUBLIC-EVIDENCE CASE SCORES: every indicator is coded from the
  cited public disclosures below; where public evidence is insufficient the
  indicator is set at its segment-typical value and flagged, following the
  paper's Section IV-C protocol. They are not audited internal
  measurements.
- Coding status: coder 1 complete; second-coder review in progress
  (author). Scores are reported with the 5th to 95th percentile interval
  under Dirichlet weight uncertainty (concentration 60) from
  `aipdi.sensitivity.dirichlet_uncertainty`.
- Naming precedent: the Foundation Model Transparency Index scores named
  developers and the AIIVI scores named labs; scoring named firms on cited
  public evidence with disclosed methodology is standard in this
  literature.

## Headline results

| Case | T (0-50) | C (0-50) | AIPDI | Geometric | Weight-uncertainty 5-95% | Realized outcome |
|---|---|---|---|---|---|---|
| Jasper, 2022 configuration | 34.0 | 40.5 | 74.5 | 83.5 | 71-78 | Sherlocked by ChatGPT (2023): ARR forecast cut 30%+, layoffs, valuation cut |
| Windsurf, pre-cutoff (May 2025) | 26.3 | 37.6 | 63.9 | 71.5 | 61-67 | Provider withdrew first-party capacity with <5 days notice (Jun 2025) |
| Harvey, pre (OpenAI-only, early 2025) | 36.1 | 27.1 | 63.2 | 69.4 | 61-66 | (configuration replaced by choice, below) |
| Harvey, post (multi-model, from May 2025) | 22.9 | 25.5 | 48.5 | 53.0 | 46-51 | Absorbed the mid-2025 provider turbulence |

Two structural observations:

1. The axis decomposition anticipated the failure type. Windsurf's score
   was commercially loaded (C 37.6 vs T 26.3, driven by Sherlocking
   exposure and AI share of value), and its realized event was strategic:
   a provider withdrawal amid competitive dynamics, not an outage.
   Harvey's score was technically loaded (T 36.1 vs C 27.1, driven by
   single-provider concentration and fine-tuning lock-in), and its chosen
   remedy was technical: multi-model routing.
2. Mitigation moves the index by a measurable amount on a real firm:
   Harvey's May 2025 architecture change cuts its score from 63.2 to 48.5
   (14.7 points), with the technical sub-index falling by more than a
   third.

## Coding sheet: Jasper (2022 configuration, scored retrospectively)

Segment: AI-native application (marketing copy). Sources: Fortune coverage
of the ChatGPT impact (paper ref [29]); Voicebot.ai, 2023-07-17, layoffs
nine months after the $125M raise
(https://voicebot.ai/2023/07/17/jasper-ai-laying-off-staff-9-months-after-125m-raise/);
Maginative, CEO change and internal valuation cut
(https://www.maginative.com/article/jasper-cuts-internal-valuation-as-ai-growth-slows/).

| Indicator | Score | Evidence |
|---|---|---|
| single_provider_concentration | 0.9 | Product built on GPT-3 via OpenAI API (widely documented; Fortune) |
| no_abstraction_layer | 0.8 | Direct API integration era; no gateway layer disclosed |
| prompt_tool_nonportability | 0.5 | Template and prompt library tuned to GPT-3 behavior |
| finetuning_lockin | 0.4 | Reported use of provider-hosted customization; partial evidence, near segment-typical |
| data_embeddings_lockin | 0.4 | Segment-typical (flagged: insufficient public evidence) |
| no_open_weight_fallback | 0.9 | No competitive open-weight alternative existed in 2022 |
| sla_criticality | 0.8 | Copy generation was the product; API loss stops core value |
| ai_share_of_value | 0.95 | Near-total: the product was AI copywriting |
| weak_moat | 0.9 | Thin workflow layer over the model; low switching costs for users |
| margin_exposure | 0.6 | Inference-heavy COGS; partial evidence, near segment-typical |
| sherlocking_exposure | 0.95 | Provider's own chat product could (and did) absorb the use case |
| contractual_lockin | 0.3 | No unusual lock-in disclosed |

## Coding sheet: Windsurf (pre-cutoff configuration, May 2025)

Segment: AI-native application (agentic coding IDE). Sources: TechCrunch,
2025-06-03, Anthropic limiting direct access
(https://techcrunch.com/2025/06/03/windsurf-says-anthropic-is-limiting-its-direct-access-to-claude-ai-models/);
Forbes, 2025-06-05
(https://www.forbes.com/sites/johanmoreno/2025/06/05/anthropic-cuts-windsurfs-claude-access-before-openai-acquisition/);
TechCrunch, 2025-06-07, Kaplan quote
(https://techcrunch.com/2025/06/07/week-in-review-why-anthropic-cut-access-to-windsurf/);
TechCrunch, 2025-05-15, SWE-1 in-house models
(https://techcrunch.com/2025/05/15/vibe-coding-startup-windsurf-launches-in-house-ai-models/);
TechCrunch, 2025-08-07, category margin pressure
(https://techcrunch.com/2025/08/07/the-high-costs-and-thin-margins-threatening-ai-coding-startups/).

| Indicator | Score | Evidence |
|---|---|---|
| single_provider_concentration | 0.7 | Claude family carried the flagship experience ("nearly all first-party capacity" was Anthropic's to withdraw); multiple model options existed in-product |
| no_abstraction_layer | 0.4 | Multi-model menu and rapid rerouting to Gemini 2.5 Pro within days imply real routing capability |
| prompt_tool_nonportability | 0.6 | Agentic scaffolding (Cascade) tuned per model family; re-validation cost real |
| finetuning_lockin | 0.2 | In-house SWE-1 training; no provider-hosted fine-tunes disclosed |
| data_embeddings_lockin | 0.3 | In-house codebase indexing |
| no_open_weight_fallback | 0.5 | SWE-1 family is a partial in-house standby but lagged top-tier models at launch |
| sla_criticality | 0.9 | AI coding is the product; capacity loss degrades it immediately |
| ai_share_of_value | 0.9 | Near-total |
| weak_moat | 0.6 | IDE and enterprise relationships, but a crowded, commoditizing category |
| margin_exposure | 0.7 | Category-level inference-cost pressure documented; firm-specific reports conflict (band 0.5-0.8, flagged) |
| sherlocking_exposure | 0.9 | Provider shipped a directly competing product (Claude Code); withdrawal occurred amid acquisition by a rival provider |
| contractual_lockin | 0.5 | First-party capacity arrangement whose withdrawal proved decisive |

## Coding sheet: Harvey (pre and post, 2025)

Segment: AI-native application (legal). Sources: Harvey, 2025-05-13,
expanding model offerings and multi-model design
(https://www.harvey.ai/blog/expanding-harveys-model-offerings ;
https://www.harvey.ai/blog/why-harvey-is-multi-model-by-design);
TechCrunch, 2025-05-13
(https://techcrunch.com/2025/05/13/anthropic-google-score-win-by-nabbing-openai-backed-harvey-as-a-user/).

| Indicator | Pre | Post | Evidence |
|---|---|---|---|
| single_provider_concentration | 0.9 | 0.45 | OpenAI-only originally (OpenAI Startup Fund portfolio); then Anthropic and Google models added via AWS Bedrock and Google Vertex |
| no_abstraction_layer | 0.6 | 0.3 | Post: cloud model platforms (Bedrock, Vertex) provide routing abstraction |
| prompt_tool_nonportability | 0.6 | 0.4 | Post: BigLaw Bench evaluation suite run across seven models demonstrates portable evaluation |
| finetuning_lockin | 0.8 | 0.5 | Custom case-law model built with OpenAI; post-move less central |
| data_embeddings_lockin | 0.5 | 0.4 | Segment-typical (flagged: limited public evidence) |
| no_open_weight_fallback | 0.8 | 0.6 | Closed frontier models throughout; multi-cloud reduces but does not remove |
| sla_criticality | 0.8 | 0.6 | Post: parallel providers reduce single-provider criticality |
| ai_share_of_value | 0.85 | 0.85 | Unchanged: AI is the product |
| weak_moat | 0.35 | 0.30 | Elite-firm distribution, legal workflow depth, proprietary evaluation |
| margin_exposure | 0.5 | 0.5 | Segment-typical (flagged) |
| sherlocking_exposure | 0.4 | 0.35 | Deep vertical workflow less absorbable by providers |
| contractual_lockin | 0.5 | 0.4 | Investor relationship with its primary provider (OpenAI Startup Fund) |

## Scoreability comparison: can adjacent frameworks score these firms?

The paper's central novelty claim, made concrete on the three cases:

| Framework | Jasper | Windsurf | Harvey | Why |
|---|---|---|---|---|
| AIPDI (this work) | 74.5 [71-78] | 63.9 [61-67] | 63.2 -> 48.5 | Downstream firm-level dependency is its object |
| AIIVI (upstream vulnerability) | no score | no score | no score | Scores FM producers, not dependents; authors state downstream is open |
| FMTI (transparency) | no score | no score | no score | Scores their PROVIDERS' disclosure practices (OpenAI, Anthropic) |
| CVL (cloud lock-in) | no score | no score | no score | Cloud infrastructure consumers; no FM-specific vectors, no commercial axis |
| AIDI (country index) | no score | no score | no score | Countries, not firms |
| GAIDS (psychometric) | no score | no score | no score | Individuals, not firms |
| ACI, LinkedIn AIDI (qualitative) | no number | no number | no number | Discussion frameworks without reproducible scoring |
| AIAS and AIHI (provider health) | no score | no score | no score | Score the providers' live health, not any dependent's exposure |

Complementarity note: a complete risk picture for, say, Windsurf in May
2025 combines its AIPDI (downstream exposure, this work), its provider's
transparency (FMTI scores Anthropic), its provider's live health (AIAS),
and the industry's upstream fragility (AIIVI). Only the first leg existed
nowhere before this paper.
