# Documented provider incidents and the availability arithmetic (2024-2025)

Supplementary material for the paper "AI-Dependent or AI-Enabled? A
Reliability-Oriented Index for Measuring Downstream Reliance on
Foundation-Model Providers" (IEEE Transactions on Reliability, under
review). This file documents the incident inventory and the computation
behind the empirical availability passage in the paper's Section V-D, and
reproduces the numbers with the package's own reliability functions
(equations (6) and (7) of Section III-F).

## Incident inventory (documented, with primary sources)

Machine-readable copy: [provider_incidents.csv](provider_incidents.csv).

| Date | Provider or platform | Event | Documented duration and severity | Primary source |
|---|---|---|---|---|
| 2024-12-11 | OpenAI | Full outage of API, ChatGPT, and Sora; new telemetry deployment saturated Kubernetes control planes | 4 h 22 min, significant degradation or complete unavailability (15:16 to 19:38 PST; API full recovery 19:38) | https://status.openai.com/incidents/01JMYB483C404VMPCW726E8MET (postmortem); press: https://techcrunch.com/2024/12/13/openai-blames-its-massive-chatgpt-outage-on-a-new-telemetry-service/ |
| 2025-06-10 | OpenAI | Elevated error rates and latency across API, ChatGPT, and Sora | More than 10 hours of elevated error rates (status page; press reports 10 to 15 hours to full recovery) | https://status.openai.com/incidents/01JXCAW3K3JAE0EP56AEZ7CBG3 |
| 2025-06-12 | Google Cloud | Service Control binary crash (null pointer on blank policy fields); external API requests rejected globally | 3 h main window (10:49 to 13:49 PDT), 50+ products affected including Vertex AI Online Prediction and the Vertex Gemini API; us-central1 recovery extended | https://status.cloud.google.com/incidents/ow5i3PPK96RduMcb1SsW |
| 2025-06-12 | Cloudflare (downstream of the same GCP event) | Workers KV unavailable; KV had recently been consolidated onto a single third-party cloud backend | 2 h 28 min; cascaded into Access, WARP, Gateway, and dependent third-party AI platforms | https://blog.cloudflare.com/cloudflare-service-outage-june-12-2025/ |
| 2025-08-05 to 2025-09-16 | Anthropic | Three overlapping infrastructure bugs silently degrading Claude output quality (routing error, output corruption, XLA:TPU miscompilation) | Weeks of partial degradation; 0.8% of Sonnet 4 requests rising to 16% at the worst hour (Aug 31); Haiku 3.5 affected for almost two weeks | https://www.anthropic.com/engineering/a-postmortem-of-three-recent-issues |
| 2025-09-10 | Anthropic | API, Console, and Claude outages, restored within the day | Brief (provider statement); repeated short events that week | https://techcrunch.com/2025/09/10/anthropic-reports-outages-claude-and-console-impacted/ |

## The computation used in the paper (Section V-D)

Conservative, incidents-only bound for one major provider (OpenAI), window
December 1, 2024 to June 30, 2025 (212 days, 5,088 hours). Documented
degraded or unavailable time: 4.37 h (2024-12-11, full outage) + 10 h
(2025-06-10, elevated errors, conservative end of the reported range)
= 14.4 h.

```python
from aipdi.scoring import availability_series, availability_parallel

A = 1 - 14.4 / (212 * 24)          # 0.99718 -> 99.72%
availability_series([A])            # eq (6): single provider = 99.72%
(1 - A) * 8766                      # 24.8 h expected downtime per year
A2 = availability_parallel([A, A])  # eq (7): two independent providers
(1 - A2) * 8766 * 60                # 4.2 minutes per year; a 354x reduction
```

Single-provider critical path: about 25 hours of expected degraded or
unavailable service per year. Two independently routed providers of equal
availability: about 4 minutes per year, a gain of more than two orders of
magnitude. This is the quantified reading of the paper's Fig. 8.

## Caveats (stated in the paper and repeated here)

1. Status pages are self-reported and historically under-count partial
   degradations, so incident-derived availability is an upper bound.
2. The 2025-06-10 event was elevated error rates, not a hard outage; we
   count 10 of the reported 10 to 15 hours, which is conservative in the
   other direction.
3. The parallel-architecture gain assumes independent failures. The
   2025-06-12 chain (Google Cloud, then Cloudflare Workers KV, which had
   consolidated onto that single cloud, then dependent AI platforms) is a
   documented common-cause violation of that assumption: redundancy at the
   model layer does not protect a critical path that remains serial in a
   shared component.
4. Availability metrics do not capture silent quality degradation; the
   Anthropic August to September 2025 postmortem is the documented example
   of this partial-failure mode.
