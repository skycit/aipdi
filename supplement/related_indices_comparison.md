# AIPDI versus adjacent dependency instruments

Supplementary material for the paper "AI-Dependent or AI-Enabled? A
Reliability-Oriented Index for Measuring Downstream Reliance on
Foundation-Model Providers" (IEEE Transactions on Reliability, under
review). This table expands the differentiation summarized in the paper's
Section II. The label "AI dependency" attaches to many instruments that
measure different objects; none of the instruments below measures what the
AIPDI measures, namely the dependency of a specific downstream AI product
or firm on its foundation-model providers, expressed as a transparent,
reproducible composite score with a reliability interpretation.

| Instrument | What it measures | Unit of analysis | Direction | Formalization | How AIPDI differs |
|---|---|---|---|---|---|
| AIPDI (this work) | Downstream product dependency on foundation-model providers, technical plus commercial | Product or firm | Downstream (consumer) | 0-100 composite, weighted indicators, additive and geometric variants, reliability block diagrams, Sobol' sensitivity | - |
| AIIVI, Pirrone, Fricano, and Fazio (arXiv:2510.23421) | Systemic vulnerability of foundation-model PRODUCTION (compute, data, talent, capital, energy), O-Ring theory | FM producers (industry) | Upstream (supply side) | Geometric composite (0-1) | AIPDI is the stated converse: it measures the downstream consumer exposure that AIIVI explicitly leaves open |
| Foundation Model Transparency Index, Bommasani et al. (2023-2025) | Developer disclosure practices across 100 indicators | FM developers | Producer disclosure | 0-100 composite | Same composite machinery, different object: transparency of producers, not dependency of consumers |
| Ecosystem Graphs, Stanford CRFM (arXiv:2303.15772) | Assets and dependency relations in the FM ecosystem | Ecosystem assets | Descriptive (both) | Knowledge graph, no score | Maps who depends on whom; produces no scalar dependency score |
| CVL cloud vendor lock-in model (Mathematics, vol. 12, art. 387, 2024) | Cloud vendor lock-in "dependency degree" (cost, egress, security, compliance, scalability, integration) | Cloud consumer | Downstream (consumer) | Weighted quantitative score | Closest methodological relative, cited and adapted in the paper (Section II-C); it targets cloud infrastructure, lacks FM-specific vectors (prompt and tool-schema portability, fine-tuning and embedding lock-in, open-weight fallback), and has no commercial axis or reliability formalism |
| LLM supply-chain studies (arXiv:2504.20763, arXiv:2507.18105) | Structure and vulnerabilities of open-source package and model dependency graphs | Software packages | Technical supply chain | Graph metrics | Measures code-level dependency graphs, not commercial reliance on a provider's hosted API |
| AIDI, Shengelia et al. (SSRN 4716709, 2024) | National AI dependency (GDP share, adoption, talent, infrastructure, policy) | Countries | Macro | Weighted index | Country-level readiness and reliance, not product-level provider dependency |
| OECD.AI Index; Stanford AI Index | National AI capability, investment, research output, policy | Countries | Macro | Indicator dashboards | AI intensity and progress, not dependency on particular providers |
| Evident Banking AI Index | AI maturity and governance in banking | Firms (sector benchmark) | Capability | Outside-in scoring | AI proficiency ranking, not provider-dependency exposure |
| AI Criticality Index, Corinium (2026) | Enterprise AI dependence, resilience, and strategic importance | Enterprise processes | Operational | Qualitative framework | Discussion framework without normalization, weights, reproducible scoring, or reliability grounding |
| AIAS and AIHI, SecureCoders AI Down | Real-time provider availability and health (latency, error rate, rate limits, status) | Providers | Provider health | 0-100 live scores | Scores the health of providers themselves, not the dependence of any product built on them; complementary to AIPDI |
| GAIDS, Goh, Hartanto, and Majeed (Comput. Hum. Behav. Rep., vol. 20, 2025) | Individual psychological dependency on generative AI tools | Individuals | Behavioral | Psychometric scale | Person-level behavior, orthogonal to system-level provider dependency |
| DORA CTPP regime (EU, 2024-2025) | Designation of critical ICT third parties (systemic impact, substitutability, interconnectedness) | ICT providers to finance | Regulatory oversight | Qualitative criteria plus thresholds | Regulatory designation of providers; AIPDI operationalizes the same concerns as a firm-level score |
| NIST AI RMF and GAI Profile | Third-party AI risk governance | Organizations | Governance | Qualitative controls | Governance checklists, no composite dependency metric |
| UK CMA AI Foundation Models study (2023-2024) | Competition risks in the FM market | Market | Regulatory | Qualitative principles | Market-level competition analysis, no firm-level score |

## Sources

- Pirrone, Fricano, and Fazio, AI Industrial Vulnerability Index: https://arxiv.org/abs/2510.23421
- Bommasani et al., Foundation Model Transparency Index: https://crfm.stanford.edu/fmti/ and https://arxiv.org/abs/2512.10169
- Bommasani et al., Ecosystem Graphs: https://arxiv.org/abs/2303.15772
- CVL: a cloud vendor lock-in prediction framework, Mathematics 12(3):387, 2024: https://www.mdpi.com/2227-7390/12/3/387
- LLM supply chain: https://arxiv.org/abs/2504.20763 and https://arxiv.org/abs/2507.18105
- Shengelia, Gabisonia, Tsiklauri-Shengelia, and Shengelia, Assessing AI Dependency: A Multifactorial Analysis and AIDI Index, SSRN 4716709, 2024: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4716709
- OECD.AI Index: https://www.oecd.org/en/publications/2026/02/oecd-ai-observatory-index_8f5fa0f2.html
- Stanford AI Index: https://hai.stanford.edu/ai-index
- Evident Banking AI Index: https://evidentinsights.com/ai-index/
- Corinium, The AI Criticality Index: https://www.coriniumintelligence.com/content/the-ai-criticality-index-measuring-ai-dependence
- SecureCoders AI Down (AIAS, AIHI): https://aidown.io/about
- Goh, Hartanto, and Majeed, Generative artificial intelligence dependency scale, Computers in Human Behavior Reports 20:100845, 2025: https://doi.org/10.1016/j.chbr.2025.100845
- DORA CTPP designation (ESAs, 18 Nov 2025): https://www.eba.europa.eu/publications-and-media/press-releases/european-supervisory-authorities-designate-critical-ict-third-party-providers-under-digital
- NIST AI 600-1: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
- UK CMA AI Foundation Models: https://www.gov.uk/cma-cases/ai-foundation-models-initial-review
