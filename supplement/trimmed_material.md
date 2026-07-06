# Material trimmed from the submission manuscript

This file preserves, verbatim, every passage, table, or table row that was
removed or heavily condensed from the submission copy of the paper
"AI-Dependent or AI-Enabled? A Reliability-Oriented Index for Measuring
Downstream Reliance on Foundation-Model Providers" (IEEE Transactions on
Reliability) to meet the journal's 15-page limit.

Nothing is deleted from the paper without first being recorded here and
pushed to this repository. Each entry states where the material sat in the
manuscript (section number) and the date it was relocated.

Note: quoted manuscript text below is preserved with its original
typography, which may differ from the ASCII style used elsewhere in this
repository.

---

## 2026-07-04: Appendix, Table V (full catalogue)

The full 398-row Table V was removed from the submission manuscript's
Appendix and replaced by a short illustrative excerpt plus a pointer to this
repository. The complete table, with the paper's caption and legend, is
preserved in [table_V_full_catalogue.md](table_V_full_catalogue.md) and
[table_V_full_catalogue.csv](table_V_full_catalogue.csv).

## 2026-07-04: Appendix wording replaced when Table V became an excerpt

The following original sentences were replaced in the submission copy when
the full table was swapped for an 18-row excerpt. The full caption and
legend are preserved in [table_V_full_catalogue.md](table_V_full_catalogue.md).

Appendix heading (original):

> Appendix. Named-entity catalogue (full sample, N = 398)

Appendix intro, first sentence (original):

> Table V lists all 398 entities in the named-entity catalogue, each coded
> by segment, vertical and role and disclosed model posture, with an
> indicative dependency score and a source.

Table V caption, last sentence (original):

> The full coding sheet is available from the corresponding author.

Code and data availability, last sentence (original):

> Interested readers may also obtain the coding sheet from the
> corresponding author.

## 2026-07-04: Table V excerpt moved from the Appendix into Section IV-B

Per the IEEE T-Rel author guidelines ("all figures and tables embedded in
the paper, rather than listed at the end or in the appendix"), the 18-row
Table V excerpt and its caption were moved from the Appendix into Section
IV-B (Sample construction) of the submission copy. The Appendix remains as
a text-only section holding the coding conventions and the repository
pointer. Nothing was removed in this move.

Section IV-B, last sentence (original, replaced by a Table V callout with a
repository pointer):

> The Appendix lists the full catalogue (all 398 entities) with posture, an
> indicative dependency score and sources.

## 2026-07-04: References [65]-[68] removed from the submission copy

These four references were cited only by rows of the full Table V. After
the table became an 18-row excerpt they were no longer cited anywhere in
the submission manuscript, and IEEE flags uncited references. They are the
last four entries of the reference list, so their removal shifts no other
reference numbers. They remain in the 38-page preprint and in the
`paper_ref` column of
[table_V_full_catalogue.csv](table_V_full_catalogue.csv).

> [65] TrueFoundry, "LiteLLM vs. OpenRouter: choosing an LLM gateway,"
> 2025. [Online]. Available:
> https://www.truefoundry.com/blog/litellm-vs-openrouter
>
> [66] OpenAI, "Introducing OpenAI Frontier," 2026. [Online]. Available:
> https://openai.com/index/introducing-openai-frontier/
>
> [67] Y Combinator, "Startup directory (companies tagged artificial
> intelligence)," 2026. [Online]. Available:
> https://www.ycombinator.com/companies
>
> [68] Forbes, "AI 50 2025 (in partnership with Sequoia Capital and
> Meritech Capital)," 2025. [Online]. Available:
> https://www.forbes.com/lists/ai50/

## 2026-07-05: 15-page trim, round one (Sections II, V-B, VII; Figs. 1, 6, 7)

The passages below were condensed in the submission copy to meet the
15-page limit. They are preserved verbatim as they stood before the trim.
Every bracketed citation resolves against
[paper_references.md](paper_references.md). All citation numbers appearing
in these passages remain cited in the condensed manuscript text, so the
reference list is unchanged.

Figures relocated to the supplement (full-color originals and underlying
data already in [figures/](figures/)): Fig. 1 (value chain, was in II-A),
Fig. 6 (funding and enterprise spend, was in V-E), and Fig. 7 (catalogue
composition, was in V-B-4 and IV-B); remaining figures renumber 1 to 6 in
the submission. Table fonts were reduced to 8.5 pt (IEEE table size); no
table content was removed in this round.

### Section II as it stood before condensation (verbatim)

> II. Background and related work
>
> A. The generative-AI value chain
>
> It is useful to situate dependency within the structure of the generative-AI stack, which is conventionally decomposed into four layers [2], [3]. At the base sits the compute and hardware layer, specialized accelerators, dominated by NVIDIA, and the cloud infrastructure of Amazon Web Services, Microsoft Azure, Google Cloud and specialist GPU clouds such as CoreWeave, on which everything above runs. Above it is the foundation-model layer: the frontier laboratories (OpenAI, Anthropic, Google DeepMind) together with open-weight providers (Meta’s Llama, Mistral, DeepSeek, Cohere, AI21). Above that is an API and platform and middleware layer comprising model gateways and routers (LiteLLM, OpenRouter, Portkey, and cloud-native gateways), orchestration frameworks (LangChain, LlamaIndex), inference providers (Fireworks, Together), and vector databases (Pinecone, Weaviate, Turbopuffer). At the top is the application layer, where AI-native startups and incumbents embedding AI features meet end users. Figure 1 summarizes the stack and the direction in which dependency runs.
>
>
>
> Fig. 1. The four-layer generative-AI value chain. Value accrues upward toward applications, while operational dependency runs downward: every application layer is, in the limit, dependent on the foundation-model and compute layers beneath it.
>
> Two features of this architecture are decisive for our argument. First, dependency is transitive: an application that depends on a model API also inherits the availability, pricing and policy of the cloud and compute beneath it. Second, the layers differ sharply in their competitive structure. The application and middleware layers are crowded and contestable; the foundation-model layer, as we show next, is not.
>
> B. Concentration and economics of the model layer
>
> Survey evidence converges on a highly concentrated model layer. Menlo Ventures’ 2025 enterprise study reports that Anthropic had reached roughly 40% of enterprise LLM API usage, OpenAI around 27% and Google about 21%, together close to 88%, with the remainder spread across Meta’s Llama, Cohere, Mistral and a long tail [4]. A complementary, usage-based reading places the three leaders nearer 32/25/20 [5]; a16z’s 2026 enterprise survey similarly finds the three commanding roughly 89% of enterprise wallet share [6]. The exact figures vary with methodology, but the qualitative picture, oligopoly, is robust across sources.
>
> Applying the Herfindahl–Hirschman Index (HHI = Σ sᵢ²; U.S. Department of Justice thresholds: below 1,500 unconcentrated, 1,500–2,500 moderately concentrated, above 2,500 highly concentrated) to the Menlo shares of 40, 27, 21 and a fragmented 12 residual yields an HHI of approximately 2,914, firmly in the “highly concentrated” range, and an understatement, because the residual is itself divided among many smaller firms [7]. Figure 2 presents the shares and the implied concentration.
>
>
>
> Fig. 2. Enterprise foundation-model concentration (2025). Shares are the spend-based reading of Menlo Ventures [4]; a usage-based reading differs (32/25/20). The implied HHI exceeds the U.S. antitrust threshold for a highly concentrated market.
>
> This concentration is not a transient accident of timing but the expression of underlying economics. Frontier models exhibit very high fixed training costs, near-zero marginal inference cost, and pronounced economies of scale and scope, alongside compounding advantages in data, talent and compute access. Korinek and Vipra [8], in a Brookings/GovAI working paper, argue that these properties push the frontier-model market toward natural monopoly or tight oligopoly and warn of “systemic risks and vulnerabilities” should a small set of models be deployed pervasively across the economy. Bommasani et al. [9], in the foundational treatment of the paradigm, anticipated precisely this, observing that defects in a foundation model are inherited by all models adapted from it, a homogenization that creates single points of failure.
>
> Capital flows reinforce the pattern. Crunchbase News [10] reports that foundation-model companies raised roughly US$80 billion in 2025, about 40% of global AI venture funding and more than double the prior year’s share, with OpenAI and Anthropic alone accounting for an estimated 14% of all global venture investment. Yet the application layer captured the largest share of enterprise spending (~US$19 billion of ~US$37 billion total), and startups reportedly earned roughly two dollars at the application layer for every dollar earned by incumbents [4]. Value creation, in other words, is broad at the top of the stack even as capital concentrates near the bottom, the structural tension at the heart of the dependency question.
>
> Competition authorities have reached congruent conclusions: the UK Competition and Markets Authority warned that control of critical inputs, incumbency advantages, and an “interconnected web” of partnerships among the largest technology firms could entrench market power in foundation models [11], and legal scholars have begun to ask whether such concentration warrants utility-style or antimonopoly treatment [12].
>
> C. Vendor lock-in and switching costs
>
> The economics of lock-in offers the closest established lens. Klemperer [13] and Farrell and Klemperer [14] formalize how switching costs and network effects confer ex-post market power on incumbents, even where ex-ante competition is fierce. In cloud computing specifically, a recent framework (the Cloud Vendor Lock-in, or CVL, model) operationalizes a “dependency degree” by weighting service cost, data-transfer cost, security, compliance, scalability and technical-integration depth [15]. We adapt this weighting logic directly. The translation to the model layer is imperfect, however: where cloud lock-in is dominated by data gravity and egress fees, model lock-in additionally involves prompt and tool-schema portability, provider-specific fine-tuning, embedding-space incompatibility, and the behavioural cost of re-validating safety and output quality after a switch. Classic treatments of switching costs [16], [17] and an empirical study of cloud vendor lock-in [18] inform the indicator design that follows.
>
> D. Concentration, single-supplier and systemic-risk frameworks
>
> Beyond firm-level lock-in lies the question of sector-level concentration risk. The most directly transferable governance precedent is the EU Digital Operational Resilience Act (DORA), which since late 2025 designates “critical ICT third-party providers” (including the major cloud hyperscalers), mandates registers of dependencies, requires tested exit strategies, and obliges assessment of concentration risk at both firm and sector level [19]. DORA treats a handful of providers on which an entire sector depends as objects of direct supervision, precisely the posture a foundation-model concentration regime might adopt. In parallel, a nascent scholarship extends systemic-risk theory from finance to AI and digital platforms: Hacker, Kasirzadeh, and Edwards [20] argue that the EU AI Act and Digital Services Act invoke systemic risk but define it too narrowly, while a recent taxonomy enumerates winner-take-all dynamics among some fifty sources of systemic risk from general-purpose AI [21].
>
> Two recent strands attempt to quantify aspects of this setting, and positioning our contribution against them is essential. A documentation-and-transparency strand scores model producers rather than dependency: the Foundation Model Transparency Index grades developers on disclosure [22], and the Ecosystem Graphs project maps the asset-and-dependency structure of the model supply chain [23]; a parallel software-engineering literature catalogues the open-source LLM supply chain and its security and licensing risks [24]. Closest of all, Pirrone et al. [25] construct an Artificial Intelligence Industrial Vulnerability Index that quantifies the systemic vulnerability of foundation-model producers to their own upstream inputs, compute, energy, data, talent, and capital, finding extreme vulnerability among the frontier developers. Crucially, that index measures the producer end of the value chain; its authors explicitly note that downstream application vulnerability dependent on foundation-model availability “requires investigation.” The present paper addresses precisely that converse, downstream, and arguably more consequential question. To our knowledge, no prior work offers a transparent, reproducible metric for the dependency of downstream AI products on their model providers, the gap this paper fills.
>
> E. The “thin wrapper” and platform-risk debate
>
> A practitioner literature debates the defensibility of products built primarily on others’ models. The skeptical view holds that a system prompt over a public API confers no durable advantage, since anyone can replicate it and the provider can absorb the category outright [26], [27], [28]. The constructive rebuttal locates defensibility not in the model but in proprietary data flywheels, workflow integration, distribution, brand and switching costs. The risk that an upstream provider ships a competing first-party feature, “Sherlocking”, has a long platform-economics pedigree; as one veteran hardware founder observed, the products most vulnerable share a trait: they were single-purpose features built on a platform the builder did not own [29]. We treat both technical commoditization and platform risk as components of the commercial dependency dimension. This debate has, until recently, been conducted almost entirely in practitioner commentary rather than scholarship; we treat the AIPDI commercial sub-index as a first attempt to operationalize it rigorously. The underlying dynamics are nonetheless well theorized in the platform-economics literature on complementor dependence, in which firms building on a platform they do not control face hold-up and appropriation risk and hedge through multi-homing [30], the strategic analogue of the multi-model routing we document, while the specific hazard of a platform owner entering a complementor’s niche has been formalized as the “kill zone” [31]. A related system-level concern is homogenization: when many products rely on the same few models, their errors and failures become correlated, an algorithmic-monoculture risk with welfare consequences [32].
>
> F. Research gap
>
> The dependency label itself requires disambiguation, because several recent instruments share it while measuring different objects. A country-level AI Dependency Index aggregates national adoption, talent, and infrastructure indicators [33]; psychometric scales measure an individual’s behavioural reliance on generative tools [34]; industry frameworks such as the AI Criticality Index discuss enterprise exposure qualitatively, without normalization, weighting, or reproducible scoring [35]; and provider-status monitors score the real-time health of the providers themselves rather than the dependence of any product built on them [36]. None of these measures the object of this paper: the dependency of a specific downstream product on its foundation-model providers, expressed as a transparent composite score with a reliability interpretation.
>
> Three gaps motivate this paper. First, despite abundant commentary, there is no agreed conceptualization that separates the technical from the commercial dimensions of AI-provider dependency while acknowledging their overlap. Second, there is no transparent measurement instrument that converts the qualitative “how dependent are they?” question into a comparable score across products and segments. Third, the lock-in, concentration and operational-resilience literatures, each rich in its own right, have not been integrated and applied to the foundation-model setting. We address all three.

### Section V-B as it stood before condensation (verbatim)

> B. Segmented analysis and case studies
>
> 1) AI-native applications (highest, most variable dependency)
>
> AI-native products span the full range of the index. At the dependent extreme sit single-purpose tools whose value is largely a prompt over one provider’s API. The cautionary archetype is Jasper, the AI-copywriting company that raised US$125 million at a US$1.5 billion valuation in October 2022 [51]; after ChatGPT’s launch commoditized AI writing, Jasper cut the internal value of its common stock by about 20% and reduced its revenue-growth outlook, with layoffs and leadership change following in 2023 [52], [53]. The company subsequently diversified across multiple model providers, a textbook case of high commercial dependency (low defensibility against both the provider’s own product and broad commoditization) prompting a belated technical diversification.
>
> Counter-examples show that AI-native does not entail high dependency. Coding tools such as Cursor (Anysphere) began as wrappers but built defensibility through deep repository context and a deliberately model-agnostic architecture, which let them route across providers and reduced exposure to any single one [54]. The legal-AI company Harvey, originally an OpenAI-only product and an OpenAI Startup Fund portfolio company, integrated Anthropic and Google models via AWS Bedrock and Google Vertex in 2025 and now auto-routes tasks to the best model, reporting that several non-OpenAI models had come to outperform its original system on a legal benchmark [55], [56], [57]. Harvey thus lowered its technical dependency while deepening a commercial moat, proprietary legal evaluations, workflow integration and a data partnership with a legal-research incumbent [58]. The same multi-model pattern recurs across customer-support agents (Decagon, Sierra), search (Perplexity, which blends its own retrieval-tuned model with several third-party LLMs), and app builders (Lovable, Bolt, v0, Replit, Base44), most of which route across providers automatically [54], [59].
>
> 2) Incumbents embedding LLMs (lower, additive dependency)
>
> For established software firms, AI is typically additive to a product that functions without it, and most have adopted multi-model architectures. Notion states that it uses models hosted by itself and by both Anthropic and OpenAI, exposes a model picker, and routes automatically; its retrieval stack pairs a third-party embeddings model with an independent vector database [38], [60]. Microsoft 365 Copilot is deeply integrated with OpenAI yet also offers multi-model hosting through its model platform, which provides replacement commitments and auto-upgrade paths on model retirement, dampening operational dependency [61]. The broader enterprise pattern is decisively multi-model: a16z’s 2025 survey of 100 enterprise CIOs [46] reports that 37% of enterprises run five or more models in production (up from 29% a year earlier), and its January 2026 survey of 100 Global 2000 executives [6] finds that 81% use three or more model families in testing or production (up from 68% within a year), primarily to match models to use cases and to avoid lock-in. Notably, however, open-weight self-hosting has not grown commensurately and may have declined to around 13% of workloads, as support, security and compliance considerations favour managed providers [50], evidence that diversification is largely a hedge among the same few commercial providers rather than a migration toward provider-independence.
>
> 3) Infrastructure and middleware (provider-agnostic by design)
>
> The middleware layer is the explicit institutional response to model-provider lock-in. Model gateways and routers, LiteLLM (open-source and self-hostable), OpenRouter (a managed router across hundreds of models with automatic failover), and Portkey (an enterprise gateway with semantic caching), let teams change providers without rewriting application code and fail over when a provider degrades [62], [63], [64], [65]. Their existence lowers the technical sub-index for products that adopt them. The irony is that the gateway then becomes a tier-0 dependency in its own right: an outage of the abstraction layer can disable every AI feature that flows through it [62]. Dependency is thus not eliminated but relocated, from a single model provider to a (more substitutable, but still single) routing layer, a nuance the AIPDI captures by scoring the gateway itself as provider-agnostic yet systemically critical (Figures 4–5).
>
> 4) Recent-vintage firms and SMEs (where AI-centrality is highest)
>
> A vintage lens sharpens the picture. The catalogue is dominated by firms founded during the past decade, and especially since the 2022 LLM inflection (Figure 7); most are AI-native, and many are early-stage SMEs for which the model is not a feature but the entire product. For these firms the commercial sub-index is structurally high: the share of product value attributable to AI approaches unity, so even prudent multi-model engineering cannot push commercial dependency below the floor set by AI-centrality itself. The result is a characteristic split, low technical lock-in to any single provider (most route across several), yet high commercial dependency on the continued availability, capability and affordability of the model layer as a whole. Recency compounds this in two ways. First, young firms have had less time to accumulate the proprietary data, workflow integration and distribution that constitute a moat, leaving them more exposed to commoditization and to “Sherlocking” (Section II-E). Second, building at the frontier ties them to the fastest-moving part of the stack: best-model migration, price re-cards and aggressive deprecation (Section V-D) impose recurring switching costs on precisely the firms least able to absorb them. The practical implication, developed in Section VII, is that for recent AI-native SMEs the binding question is rarely “which provider?” but “how exposed is our economic model to the model layer at large?”, which is what the AIPDI commercial sub-index is designed to surface.

### Section VII as it stood before condensation (verbatim)

> VII. Managerial and policy implications
>
> A. For product builders
>
> We suggest a staged programme keyed to the AIPDI. Immediately, builders should run the substitution and withdrawal tests, compute their single-supplier share, and produce a first-pass index. Within a quarter, they should introduce a model-abstraction layer so that no provider name appears in business logic, stand up at least one fallback provider, and evaluate an open-weight option for the highest-volume or most-sensitive workloads. Over subsequent quarters, the strategic priority is to convert technical optionality into a commercial moat, proprietary data flywheels, workflow embedding and distribution, since these, not the model, are what the commercial sub-index rewards. Escalation triggers include a provider deprecating a relied-upon model, shipping a competing first-party feature, or a single-supplier share exceeding roughly 70%. A step-by-step self-assessment guide, from the substitution and withdrawal tests to a computed score and a prioritized mitigation list, accompanies the companion code (see Code and data availability). The same diagnostic reads in reverse for investors: a product’s AIPDI prices the platform risk of the asset, separating ventures that are AI-enabled from those that are existentially AI-dependent.
>
> B. For enterprise buyers
>
> Enterprises should treat foundation-model providers as critical third parties and govern them accordingly: maintain a provider registry, select models by data sensitivity and use case, review the portfolio on a regular cadence, and require tested exit paths for material workloads, in effect, an internal analogue of the operational-resilience regimes already applied to cloud. The multi-model norm documented here [46] is a necessary but insufficient condition for resilience; without exercised fallback and exit testing, optionality is theoretical.
>
> C. For policymakers
>
> At the system level, the combination of natural-oligopoly economics, a high HHI, and pervasive downstream deployment is the signature of a concentration risk worth monitoring. The DORA precedent [19] offers a concrete template: designation of systemically important model providers, mandatory incident reporting, and, most consequentially for contestability, interoperability and portability standards for prompts and embeddings that would lower switching costs and reduce lock-in at its technical root. Such measures would address the dependency this paper measures without presuming to slow the underlying technology.

## 2026-07-05: 15-page trim, round two (archetype figures; Appendix compression)

Two further illustrative figures were relocated to the supplement (color
originals and captions already in [figures/](figures/) as
fig4_matrix.png and fig5_aipdi_segments.png, captions quoted in
figures.md): the two-axis archetype plane (submission Fig. 3, preprint
Fig. 4) and the illustrative segment bands (submission Fig. 4, preprint
Fig. 5). Their content is carried in the submission by Table III (bands)
and by the measured case chart (now Fig. 4 of the submission; preprint
Fig. 9). The Appendix coding-notes paragraph was compressed to posture
codes, dagger rule, and the repository pointer; the full legend remains
verbatim in [table_V_full_catalogue.md](table_V_full_catalogue.md).
Reference-list font reduced to 8 pt; equation images reduced 12 percent.

## 2026-07-05: 15-page trim, round three (Section III-B, III-C, III-D, III-E tail; IX)

Condensed in the submission copy; preserved verbatim below as they stood
before this round. Citations resolve via
[paper_references.md](paper_references.md); all citation numbers remain
cited in the condensed text.

### Section III-A through III-E as it stood before condensation (verbatim)

> III. Conceptualizing AI-provider dependency
>
> A. Definition
>
> We define AI-provider dependency as the degree to which a product’s continued delivery of value is contingent on continued access, on current terms, to one or more third-party foundation-model providers. The intuition can be sharpened by two thought experiments. The substitution test asks how much value the product would lose, and at what cost and delay, if it had to switch its primary model to the best available alternative. The withdrawal test (a stress case) asks what remains if the primary provider’s access were revoked outright today. A thin wrapper fails both; a product in which AI is an additive convenience passes both with little degradation. Most products lie between.
>
> B. The technical and operational dimension
>
> The first dimension concerns how tightly a product is wired, in engineering terms, to a specific provider. Its indicators include: the number of providers in production use and whether a model-abstraction layer insulates business logic from any one of them; the portability of prompts and tool-calling schemas, which rarely transfer cleanly between providers; provider-specific fine-tuning, whose weights are non-portable and whose availability is tied to a base model’s lifecycle [37]; the lock-in created by embeddings, since a corpus vectorized with one provider’s model is not interoperable with another’s vector space without costly re-embedding [38]; reliance on the provider’s availability and service levels; and the existence of a credible open-weight, self-hostable fallback. That switching is genuinely costly is visible in behaviour: Menlo Ventures [5] finds that only about 11% of teams changed model providers in the prior year, with most instead upgrading within their existing vendor.
>
> C. The commercial and strategic dimension
>
> The second dimension concerns how much of the product’s economic value and defensibility rests on the model. Its indicators include: the share of the product’s value proposition attributable to the AI feature (if “we use a frontier model” is the whole pitch, dependency is near-total); the strength of moats independent of the model, proprietary data, network effects, workflow embedding, brand and switching costs; exposure of margins to provider price changes, given that AI carries real per-token costs rather than the near-zero marginal cost of classical software; platform and Sherlocking exposure, i.e. the probability and impact of the provider entering the product’s category; and contractual or compliance lock-in (data-residency commitments, zero-retention terms, certification dependencies).
>
> D. Overlap between the dimensions
>
> The two dimensions are correlated but separable, and they interact. An outage (technical) becomes lost revenue and churn (commercial); a provider’s decision to ship a competing feature (commercial platform risk) is enabled by, and may be foreshadowed within, the same API relationship (technical). A product can be technically diversified yet commercially fragile (multi-model, but no moat and easily Sherlocked), or technically locked-in yet commercially robust (deep fine-tuning, but defended by proprietary data and workflow). The most dangerous position is high on both axes simultaneously. Table I lays out the indicators; the overlaps are noted explicitly in the final column.
>
> Table I. Indicators of AI-provider dependency along the technical and operational and commercial and strategic dimensions, with explicit overlaps.
>
> E. The AI-Provider Dependency Index (AIPDI)
>
> We operationalize the framework as a transparent, additive index. Each dimension contributes a sub-index scored on 0–50; their sum is the AIPDI on 0–100, with higher values denoting greater dependency. Formally, the technical sub-index is T = 50 · Σᵢ wᵢ tᵢ and the commercial sub-index is C = 50 · Σⱼ vⱼ cⱼ, where each indicator tᵢ, cⱼ is rated on a normalized 0–1 scale against published anchors and the weights wᵢ, vⱼ each sum to one. The composite is AIPDI = T + C. The index is paired with two provider-side measures: the market-level Herfindahl–Hirschman Index (HHI), and a firm-level single-supplier share S, the fraction of a product’s model calls routed to its largest provider, which captures concentration that an aggregate score can mask. Table II sets out the indicators and the weights we propose; we stress that the weights are a starting point requiring empirical calibration (Section VIII). Section III-F states the index formally and gives it a reliability interpretation.
>
> Table II. Proposed AIPDI scoring rubric. Each indicator is rated 0–1 against published anchors; weights within each sub-index sum to one and scale to a 0–50 contribution. Weights are author-proposed and await empirical calibration.
>
> The technical and operational sub-index deliberately mirrors the criteria by which financial regulators designate critical third parties under the EU Digital Operational Resilience Act: the systemic impact of a provider’s failure, the importance of the entities relying on it, the degree and concentration of that reliance, and the substitutability of the provider [19]. Our single-provider-concentration, availability and SLA-criticality, and open-weight-fallback indicators operationalize concentration and substitutability at the level of an individual product, making the AIPDI a firm-level counterpart to a regime that today operates only at the sector level.

### Section IX as it stood before condensation (verbatim)

> IX. Conclusion
>
> The generative-AI application economy is being built atop a small, highly concentrated set of model providers. We have argued that the resulting dependency is neither uniform nor binary but a measurable spectrum spanning two correlated dimensions, technical and operational and commercial and strategic, and we have offered the AIPDI, grounded in the lock-in, switching-cost, concentration and operational-resilience literatures, as a transparent way to score it. Applied across AI-native applications, embedding incumbents and infrastructure, the framework shows that the existential danger zone is narrow and specific, that mitigation relocates rather than abolishes dependency, and that firm-level diversification has done little to reduce the sector’s collective reliance on a few firms. Documented incidents confirm the risk is live. For builders, the path out of dependency runs through model-agnostic architecture and, decisively, through moats the model cannot supply; for enterprises, through governing providers as critical third parties; and for policymakers, through portability standards and resilience oversight modelled on regimes already applied to cloud. Measuring dependency is the first step toward managing it.

## 2026-07-06: Declarations removed; availability statement shortened

The CRediT, competing-interest, and funding declarations (Elsevier-style
conventions, not IEEE ones) were removed from the submission copy, and the
Code and data availability statement was shortened to a single sentence;
the repository README carries the full description. Removed or replaced
text, verbatim:

> CRediT author statement. Mohammadamin Keshtkar: Conceptualization, Methodology, Software, Formal analysis, Data curation, Validation, Writing – original draft, Writing – review & editing.
>
> Declaration of competing interest. The authors declare no competing financial or personal interests.
>
> Funding. This research received no specific grant from funding agencies in the public, commercial, or not-for-profit sectors.
>
> Code and data availability. The complete named-entity catalogue (all 398 entities, machine-readable) and an open-source Python implementation of the AIPDI are released at https://github.com/skycit/aipdi (to be archived at Zenodo with a DOI upon acceptance). The repository reproduces every score, figure, and sensitivity result in this paper: it contains the normalization, sub-index, and aggregation functions of Section III-F (additive and geometric variants), the alternative weighting schemes and the variance-based Sobol’ sensitivity routine of Section IV-C, the firm catalogue as catalogue.csv, and a worked example. The repository’s supplement folder preserves the paper’s supplementary material, including the complete Table V coding sheet (all 398 entities with the Indic. AIPDI column), full-color versions of all figures, including the value-chain, funding, and sample-composition charts relocated from this manuscript for space, with the machine-readable data underlying the data-bearing figures, a practitioner self-assessment guide, a structured comparison of adjacent dependency instruments, and any material condensed from this manuscript to meet the page limit.

<!-- Subsequent trims are appended below, newest last. -->
