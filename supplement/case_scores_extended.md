# Extended public-evidence case scores: ten further catalogue firms

Supplementary material for the paper "AI-Dependent or AI-Enabled? A
Reliability-Oriented Index for Measuring Downstream Reliance on
Foundation-Model Providers" (IEEE Transactions on Reliability, under
review). Extends [case_scores.md](case_scores.md) (Jasper, Windsurf,
Harvey, Cursor) with compact coding sheets for ten further catalogue firms
whose provider architecture is sufficiently disclosed in public sources.

Method and provenance: evidence dossiers were compiled with LLM-assisted
web research (two independent tools), with every scoring-relevant claim
carrying a source URL and a confidence tag; load-bearing claims were
spot-verified against primary sources before coding; unverified or
weakly-sourced claims are flagged and the affected indicator is coded at
or near its segment-typical value. Scores follow the paper's Table II
anchors and Section IV-C protocol. Coder 1 complete; second-coder review
pending (author). Intervals are 5th to 95th percentiles under Dirichlet
weight uncertainty (concentration 60).

## Headline results (current configurations, dates as noted)

| Firm | Posture | T | C | AIPDI | 5-95% | Key dependency facts (sourced in dossier notes below) |
|---|---|---|---|---|---|---|
| Perplexity | M | 12.4 | 33.6 | 46.0 | 43-49 | Default Sonar model built on open weights (Llama 3.3 70B), own index and inference; frontier models resold on paid tiers; direct first-party search competition |
| Cognition (Devin) | M | 16.3 | 33.3 | 49.6 | 46-53 | Own SWE-1.x model line plus Claude for key features; inherited the documented June 2025 access cut via Windsurf |
| Sierra | M | 22.3 | 33.7 | 56.0 | 53-59 | OpenAI, Anthropic, and Meta "constellation" with supervisor model; CEO simultaneously chairs OpenAI's board (unique governance entanglement) |
| Lovable | M | 25.4 | 40.0 | 65.3 | 63-67 | OpenAI, Gemini, and Claude via a multi-year Google Cloud contract; Google is investor, cloud, and model supplier; documented churn to Claude Code |
| Clay | M | 21.5 | 25.5 | 47.0 | 45-49 | Firm FAQ: OpenAI, Gemini, Claude, no own models; data-marketplace moat; OpenAI Frontier program partner |
| Rogo | M | 30.6 | 31.4 | 62.0 | 59-65 | Clearest provider-hosted fine-tuning disclosure in the sample (named OpenAI models per function); multi-cloud infra; model toggle |
| Khan Academy (Khanmigo) | S | 33.5 | 33.3 | 66.8 | 64-70 | GPT-4 only; subscription priced to cover GPT-4 costs (disclosed pass-through); education distribution moat |
| Writer | O | 9.5 | 26.2 | 35.7 | 33-39 | Own closed Palmyra models, customer fine-tunes on own infra, VPC deployment |
| Suno | O | 7.6 | 29.2 | 36.8 | 34-40 | Own music foundation models (plus earlier OSS Bark); provider risk minimal, legal risk separate |
| Character.AI | O | 8.3 | 35.3 | 43.6 | 42-46 | Own models, but documented serving-cost crisis and the Google licensing acquihire (founders departed) load the commercial axis |

## Two findings

1. Empirical validation of the Table V rule bands. Across all
   evidence-scored current configurations (including Cursor, Windsurf, and
   post-move Harvey from the flagship set): multi-model AI-natives average
   53.8 against a band value of 55; own-model firms average 38.7 against
   45; the two disclosed single-provider products average 65.3 against 90.
   The rule bands are directionally correct locators, near-exact for the M
   posture, slightly conservative for O, and overstated only in the S
   corner, where the band is calibrated to the undisclosed thin-wrapper
   worst case while every disclosed S firm shows partial mitigations.
2. The sector's residual dependency is commercial. In 12 of 13 current
   configurations the commercial sub-index exceeds the technical one,
   often by a wide margin (Perplexity 33.6 vs 12.4; Character.AI 35.3 vs
   8.3); the single exception, Khanmigo, is technically tilted by 0.2
   points. Firms have engineered down technical dependency (routing, own
   models, open weights) faster than they have escaped commercial exposure
   (AI share of value, provider first-party competition, margin
   pass-through, entangled cap tables). Diversification relocates
   dependency toward the commercial axis; it does not remove it.

## Dossier notes and flags (evidence highlights per firm)

- Perplexity: Sonar on Llama 3.3 70B and R1 1776 disclosed (firm blog,
  Wikipedia); own crawling and index; paid-tier frontier model selection
  (docs.perplexity.ai). Reported $750M Azure commitment is LOW-AUTHORITY
  ONLY and was NOT used in coding (margin coded near segment-typical,
  flagged). Sherlocking coded high: Google AI Overviews, ChatGPT search.
- Cognition: firm blog discloses burn under $20M and ARR trajectory; SWE
  line and in-house retrieval per docs; the claim that own models carry
  most traffic is aggregator-sourced, so concentration is coded
  conservatively at 0.4. Access-cut exposure documented via the Windsurf
  acquisition (firm blog).
- Sierra: CNBC-sourced provider constellation and fine-tuned proprietary
  layers; fine-tuning host not disclosed, coded 0.5 flagged. Contractual
  indicator (0.7) reflects the OpenAI board-chair dual role plus GV
  investment, a governance entanglement no other sampled firm has.
- Lovable: founder-disclosed provider mix (TechCrunch); Google Cloud
  multi-year contract and 2026 expansion (press); CapitalG investment.
  The churn episode after a frontier coding-model release is
  aggregator-relayed (flagged) but consistent with category dynamics.
- Clay: firm FAQ answers "does Clay have its own AI models?" with "No"
  and names the three providers; OpenAI case study documents Claygent on
  GPT-4; Frontier-program membership via public post. Moat coded low-mid:
  the 200-vendor data marketplace is a genuine non-model asset.
- Rogo: OpenAI case study names GPT-4o, o1-mini, and o1 per function and
  documents provider-hosted fine-tuning (finetuning_lockin 0.85, highest
  coded); firm discloses AWS, Azure OpenAI, Together, and Anthropic
  infrastructure; Bloomberg-relayed model toggle (flagged, aggregator).
- Khanmigo: OpenAI case study and Khan blog disclose GPT-4 dependence;
  the $9 per month price "helps cover the cost of running on GPT-4"
  (Quartz), a disclosed margin pass-through. Education content and
  district relationships temper the moat indicator.
- Writer: Palmyra proprietary models and CoWrite customer fine-tunes on
  own infrastructure (firm blog, TechCrunch); enterprise VPC deployment.
  Structurally closer to a provider than a dependent; scored as the
  low-dependency O anchor.
- Suno: own music models, earlier open-source Bark, Cambridge MA; main
  risks (copyright litigation) are outside provider dependency and are
  not scored by AIPDI.
- Character.AI: proprietary models; documented cost crisis and
  sale-or-raise talks (2025 press); August 2024 Google licensing and
  founder acquihire coded into contractual_lockin (0.65) and margin
  exposure (0.75).

Unscored from the dossier batches, with reasons: Gamma (no evidence
returned this round), 11x (no provider-side disclosure found),
Legora (provider identity weakly evidenced, aggregators only), Hebbia,
Decagon, Glean, Synthesia, Bolt, Replit Agent, Granola (partial evidence;
scoreable at lower confidence in a future round; Decagon's key claim that
80 percent of traffic runs in-house is aggregator-only and unverified).
