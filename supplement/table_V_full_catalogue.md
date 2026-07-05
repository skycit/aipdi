# Table V: full named-entity catalogue (N = 398)

Supplementary material for the paper "AI-Dependent or AI-Enabled? A Reliability-Oriented Index for Measuring Downstream Reliance on Foundation-Model Providers" (IEEE Transactions on Reliability, under review). This file is the full coding sheet behind the paper's Table V; the submission manuscript carries a short excerpt and points here for the complete table.

Generated from the packaged catalogue via `aipdi.catalogue.load_catalogue()`, which attaches the computed `indic_aipdi` column (the deterministic segment x posture band of `aipdi.catalogue.indicative_band`). Verified cell-by-cell against the manuscript's Table V. A machine-readable copy is in [`table_V_full_catalogue.csv`](table_V_full_catalogue.csv); the `paper_ref` column gives the reference number used in the paper for each source. Reference numbers follow the 38-page preprint; in the trimmed submission manuscript, four related-index references were inserted as [33]-[36], so preprint references numbered 33 and above appear there as n+4.

## Caption (as in the paper)

> Table V. Full named-entity catalogue (N = 398), with disclosed model posture, indicative (rule-based) AIPDI, and an indicative source. † = posture coded at segment-typical value absent a firm-specific public disclosure; Indic. AIPDI is a deterministic function of segment × posture, not a firm-level measurement (Sections IV-C, VIII). The full coding sheet is available from the corresponding author.

## Legend and coding notes (Appendix text, as in the paper)

> Table V lists all 398 entities in the named-entity catalogue, each coded by segment, vertical and role and disclosed model posture, with an indicative dependency score and a source. Posture codes: S = high single-provider dependency; M = multi-model or diversified; O = owns or self-hosts model(s). Posture reflects public disclosures at the time of writing and will change; entries without a firm-specific public disclosure are coded at their segment-typical posture and marked †. The Source column is indicative: it gives a primary disclosure where one exists and otherwise the landscape directory in which the entity is catalogued (entities were compiled from Andreessen Horowitz, 2023, 2025; CB Insights, 2025; Northflank, 2026; Wellows, 2026; Bloomberg, 2025; and primary disclosures). The Indic. AIPDI column is a deterministic function of segment and posture, not a firm-specific measurement, provided only to locate each entity on the index’s 0–100 scale (Section III-E): thin single-provider AI-native products ≈ 90, diversified AI-native products ≈ 55, model-owners ≈ 45, embedding incumbents ≈ 26–42, infrastructure and middleware ≈ 28–60 (wide, reflecting low lock-in to any one model provider but high systemic criticality), and foundation-model providers ≈ 10. Firm-specific scoring requires the evidence and calibration discussed in Sections IV-C and VIII.

## Segment counts

| Segment | Entities |
|---|---|
| Provider | 24 |
| Infrastructure | 121 |
| AI-native | 201 |
| Incumbent | 52 |
| Total | 398 |

## Full catalogue

| # | Product or firm | Segment | Vertical and role | Posture | Indic. AIPDI | Source |
|---|---|---|---|---|---|---|
| 1 | OpenAI (GPT, o-series) | Provider | Frontier model lab | O | 10 | Northflank, 2026 [3] |
| 2 | Anthropic (Claude) | Provider | Frontier model lab | O | 10 | Northflank, 2026 [3] |
| 3 | Google DeepMind (Gemini) | Provider | Frontier model lab | O | 10 | Northflank, 2026 [3] |
| 4 | Meta (Llama) | Provider | Open-weight models | O | 10 | Bloomberg, 2025 [45] |
| 5 | Mistral AI | Provider | Open/closed models (EU) | O | 10 | Bloomberg, 2025 [45] |
| 6 | DeepSeek | Provider | Open-weight models | O | 10 | Bloomberg, 2025 [45] |
| 7 | xAI (Grok) | Provider | Frontier model lab | O | 10 | Northflank, 2026 [3] |
| 8 | Cohere | Provider | Enterprise models | O | 10 | Northflank, 2026 [3] |
| 9 | AI21 Labs (Jamba) | Provider | Enterprise models | O | 10 | CB Insights, 2025 [43] |
| 10 | Amazon (Nova / Titan) | Provider | Cloud-native models | O | 10 | Northflank, 2026 [3] |
| 11 | Microsoft (Phi) | Provider | Small/efficient models | O | 10 | CB Insights, 2025 [43] |
| 12 | Databricks (DBRX / Mosaic) | Provider | Enterprise/open models | O | 10 | CB Insights, 2025 [43] |
| 13 | Alibaba (Qwen) | Provider | Open-weight models | O | 10 | Bloomberg, 2025 [45] |
| 14 | Zhipu AI (GLM) | Provider | Open-weight models | O | 10 | Bloomberg, 2025 [45] |
| 15 | Moonshot AI (Kimi) | Provider | Frontier model lab | O | 10 | Bloomberg, 2025 [45] |
| 16 | Baidu (ERNIE) | Provider | Frontier model lab | O | 10 | Bloomberg, 2025 [45] |
| 17 | Stability AI | Provider | Open image/audio models | O | 10 | CB Insights, 2025 [43] |
| 18 | Reka AI | Provider | Multimodal models | O | 10 | CB Insights, 2025 [43] |
| 19 | Aleph Alpha | Provider | Sovereign EU models | O | 10 | Bloomberg, 2025 [45] |
| 20 | TII (Falcon) | Provider | Open-weight models | O | 10 | CB Insights, 2025 [43] |
| 21 | IBM (Granite) | Provider | Enterprise/open models | O | 10 | Northflank, 2026 [3] |
| 22 | Snowflake (Arctic) | Provider | Enterprise/open models | O | 10 | CB Insights, 2025 [43] |
| 23 | NVIDIA | Infrastructure | Compute / GPUs | O† | 28 | Northflank, 2026 [3] |
| 24 | AMD (Instinct) | Infrastructure | Compute / GPUs | O† | 28 | Northflank, 2026 [3] |
| 25 | Google (TPU) | Infrastructure | Compute / accelerators | O† | 28 | Northflank, 2026 [3] |
| 26 | AWS (Trainium / Inferentia) | Infrastructure | Compute / accelerators | M† | 35 | Northflank, 2026 [3] |
| 27 | Cerebras | Infrastructure | Compute / inference | O† | 28 | CB Insights, 2025 [43] |
| 28 | Groq | Infrastructure | Inference accelerator | M† | 35 | CB Insights, 2025 [43] |
| 29 | SambaNova | Infrastructure | Compute / inference | O† | 28 | CB Insights, 2025 [43] |
| 30 | CoreWeave | Infrastructure | GPU cloud | M† | 35 | CB Insights, 2025 [43] |
| 31 | Lambda | Infrastructure | GPU cloud | M† | 35 | CB Insights, 2025 [43] |
| 32 | Crusoe | Infrastructure | GPU cloud | M† | 35 | CB Insights, 2025 [43] |
| 33 | Together AI | Infrastructure | Open-model inference | M | 35 | Northflank, 2026 [3] |
| 34 | Fireworks AI | Infrastructure | Model inference | M | 35 | Northflank, 2026 [3] |
| 35 | Replicate | Infrastructure | Model hosting / inference | M | 35 | Merge.dev, 2025 [58] |
| 36 | Baseten | Infrastructure | Model serving | M | 35 | CB Insights, 2025 [43] |
| 37 | Modal | Infrastructure | Serverless compute | M† | 35 | CB Insights, 2025 [43] |
| 38 | Anyscale (Ray) | Infrastructure | Distributed compute | M† | 35 | CB Insights, 2025 [43] |
| 39 | OctoAI | Infrastructure | Model inference | M | 35 | Merge.dev, 2025 [58] |
| 40 | RunPod | Infrastructure | GPU cloud | M† | 35 | Northflank, 2026 [3] |
| 41 | AWS Bedrock | Infrastructure | Multi-model cloud platform | M | 35 | Harvey, 2025 [51] |
| 42 | Microsoft Azure AI Foundry | Infrastructure | Multi-model cloud platform | M | 35 | Microsoft, 2026 [57] |
| 43 | Google Vertex AI | Infrastructure | Multi-model cloud platform | M | 35 | Harvey, 2025 [51] |
| 44 | Oracle OCI Generative AI | Infrastructure | Multi-model cloud platform | M† | 35 | Northflank, 2026 [3] |
| 45 | IBM watsonx | Infrastructure | Multi-model cloud platform | M | 35 | Northflank, 2026 [3] |
| 46 | Snowflake Cortex | Infrastructure | In-warehouse multi-model AI | M | 35 | Northflank, 2026 [3] |
| 47 | Cloudflare Workers AI | Infrastructure | Edge multi-model platform | M | 35 | Merge.dev, 2025 [58] |
| 48 | LiteLLM | Infrastructure | Open-source model gateway | M | 35 | Merge.dev, 2025 [58] |
| 49 | OpenRouter | Infrastructure | Managed model router | M | 35 | Merge.dev, 2025 [58] |
| 50 | Portkey | Infrastructure | Enterprise AI gateway | M | 35 | Portkey, 2025 [61] |
| 51 | Cloudflare AI Gateway | Infrastructure | Model gateway | M | 35 | Merge.dev, 2025 [58] |
| 52 | Vercel AI Gateway / SDK | Infrastructure | Model gateway / SDK | M | 35 | altar.io, 2026 [55] |
| 53 | Kong AI Gateway | Infrastructure | API/model gateway | M† | 35 | Northflank, 2026 [3] |
| 54 | Martian | Infrastructure | Model router | M | 35 | CB Insights, 2025 [43] |
| 55 | Not Diamond | Infrastructure | Model router | M | 35 | CB Insights, 2025 [43] |
| 56 | Unify | Infrastructure | Model router | M | 35 | Merge.dev, 2025 [58] |
| 57 | TrueFoundry | Infrastructure | LLM gateway / MLOps | M | 35 | TrueFoundry, 2025 [65] |
| 58 | Eden AI | Infrastructure | Multi-provider API | M | 35 | Merge.dev, 2025 [58] |
| 59 | LangChain | Infrastructure | Orchestration framework | M | 35 | Andreessen Horowitz, 2023 [2] |
| 60 | LlamaIndex | Infrastructure | Data/orchestration framework | M | 35 | Andreessen Horowitz, 2023 [2] |
| 61 | Haystack (deepset) | Infrastructure | Orchestration framework | M† | 35 | CB Insights, 2025 [43] |
| 62 | Microsoft Semantic Kernel | Infrastructure | Orchestration SDK | M | 35 | Microsoft, 2026 [57] |
| 63 | CrewAI | Infrastructure | Multi-agent framework | M† | 35 | CB Insights, 2025 [43] |
| 64 | AutoGen (Microsoft) | Infrastructure | Multi-agent framework | M | 35 | Microsoft, 2026 [57] |
| 65 | DSPy (Stanford) | Infrastructure | Prompt/program framework | M† | 35 | Andreessen Horowitz, 2023 [2] |
| 66 | Flowise | Infrastructure | Low-code agent builder | M† | 35 | CB Insights, 2025 [43] |
| 67 | Langflow | Infrastructure | Low-code agent builder | M† | 35 | CB Insights, 2025 [43] |
| 68 | Dify | Infrastructure | LLM app platform | M | 35 | CB Insights, 2025 [43] |
| 69 | n8n | Infrastructure | Workflow automation (AI) | M | 35 | CB Insights, 2025 [43] |
| 70 | Pinecone | Infrastructure | Vector database | M† | 35 | Andreessen Horowitz, 2023 [2] |
| 71 | Weaviate | Infrastructure | Vector database | M† | 35 | Andreessen Horowitz, 2023 [2] |
| 72 | Chroma | Infrastructure | Vector database | M† | 35 | CB Insights, 2025 [43] |
| 73 | Qdrant | Infrastructure | Vector database | M† | 35 | CB Insights, 2025 [43] |
| 74 | Zilliz / Milvus | Infrastructure | Vector database | M† | 35 | CB Insights, 2025 [43] |
| 75 | Turbopuffer | Infrastructure | Vector store | M | 35 | Notion, 2025 [34] |
| 76 | LanceDB | Infrastructure | Vector database | M† | 35 | CB Insights, 2025 [43] |
| 77 | Vespa | Infrastructure | Search / retrieval engine | M† | 35 | CB Insights, 2025 [43] |
| 78 | MongoDB Atlas Vector | Infrastructure | Vector search | M† | 35 | Northflank, 2026 [3] |
| 79 | Redis (vector) | Infrastructure | Vector search | M† | 35 | Northflank, 2026 [3] |
| 80 | LangSmith | Infrastructure | LLM observability / eval | M | 35 | Andreessen Horowitz, 2023 [2] |
| 81 | Langfuse | Infrastructure | LLM observability (OSS) | M | 35 | CB Insights, 2025 [43] |
| 82 | Helicone | Infrastructure | LLM observability / gateway | M | 35 | Merge.dev, 2025 [58] |
| 83 | Braintrust | Infrastructure | Eval / observability | M | 35 | CB Insights, 2025 [43] |
| 84 | Arize (Phoenix) | Infrastructure | ML/LLM observability | M | 35 | CB Insights, 2025 [43] |
| 85 | Weights & Biases | Infrastructure | Experiment tracking / eval | M | 35 | CB Insights, 2025 [43] |
| 86 | Humanloop | Infrastructure | Prompt mgmt / eval | M | 35 | CB Insights, 2025 [43] |
| 87 | Vellum | Infrastructure | LLM dev platform | M | 35 | CB Insights, 2025 [43] |
| 88 | Galileo | Infrastructure | LLM evaluation | M | 35 | CB Insights, 2025 [43] |
| 89 | Patronus AI | Infrastructure | LLM evaluation | M | 35 | CB Insights, 2025 [43] |
| 90 | Scale AI | Infrastructure | Data labeling / RLHF | M† | 35 | CB Insights, 2025 [43] |
| 91 | Surge AI | Infrastructure | Data labeling / RLHF | M† | 35 | CB Insights, 2025 [43] |
| 92 | Labelbox | Infrastructure | Data labeling | M† | 35 | CB Insights, 2025 [43] |
| 93 | Snorkel AI | Infrastructure | Programmatic data / tuning | M† | 35 | CB Insights, 2025 [43] |
| 94 | Unstructured | Infrastructure | Document ingestion (RAG) | M† | 35 | CB Insights, 2025 [43] |
| 95 | Vectara | Infrastructure | RAG-as-a-service | M | 35 | CB Insights, 2025 [43] |
| 96 | Contextual AI | Infrastructure | Enterprise RAG platform | M | 35 | CB Insights, 2025 [43] |
| 97 | Hugging Face | Infrastructure | Open-model hub | O† | 28 | Northflank, 2026 [3] |
| 98 | Ollama | Infrastructure | Local model runtime | O† | 28 | Northflank, 2026 [3] |
| 99 | vLLM | Infrastructure | Inference serving engine | O† | 28 | CB Insights, 2025 [43] |
| 100 | Lakera | Infrastructure | LLM security / guardrails | M | 35 | CB Insights, 2025 [43] |
| 101 | Guardrails AI | Infrastructure | Output validation (OSS) | M | 35 | CB Insights, 2025 [43] |
| 102 | Protect AI | Infrastructure | AI/ML security | M† | 35 | CB Insights, 2025 [43] |
| 103 | HiddenLayer | Infrastructure | AI security | M† | 35 | CB Insights, 2025 [43] |
| 104 | Cursor (Anysphere) | AI-native | Coding assistant | M | 55 | Upstarts Media, 2025 [50] |
| 105 | Windsurf (Codeium) | AI-native | Coding assistant | S | 90 | TechCrunch, 2025 [62] |
| 106 | Replit Agent | AI-native | App builder | M | 55 | altar.io, 2026 [55] |
| 107 | Cognition (Devin) | AI-native | Autonomous coding agent | M† | 55 | TechTalks, 2025 [63] |
| 108 | Aider | AI-native | CLI coding assistant | M | 55 | altar.io, 2026 [55] |
| 109 | Continue | AI-native | Open-source coding assistant | M | 55 | altar.io, 2026 [55] |
| 110 | Cline | AI-native | Agentic coding (OSS) | M | 55 | altar.io, 2026 [55] |
| 111 | Tabnine | AI-native | Coding assistant | M | 55 | Wellows, 2026 [44] |
| 112 | Sourcegraph Cody | AI-native | Coding assistant | M | 55 | Wellows, 2026 [44] |
| 113 | Augment Code | AI-native | Coding assistant | M† | 55 | CB Insights, 2025 [43] |
| 114 | Qodo (CodiumAI) | AI-native | Code integrity / testing | M† | 55 | CB Insights, 2025 [43] |
| 115 | Magic.dev | AI-native | Code-generation models | O | 45 | CB Insights, 2025 [43] |
| 116 | Poolside | AI-native | Code-generation models | O | 45 | CB Insights, 2025 [43] |
| 117 | Factory AI | AI-native | Agentic software dev | M† | 55 | CB Insights, 2025 [43] |
| 118 | Lovable | AI-native | App builder | M† | 55 | altar.io, 2026 [55] |
| 119 | Bolt (StackBlitz) | AI-native | App builder | M† | 55 | altar.io, 2026 [55] |
| 120 | v0 (Vercel) | AI-native | App builder | M† | 55 | altar.io, 2026 [55] |
| 121 | Base44 (Wix) | AI-native | App builder | M | 55 | altar.io, 2026 [55] |
| 122 | Create.xyz | AI-native | App builder | M† | 55 | altar.io, 2026 [55] |
| 123 | Jasper | AI-native | Marketing copywriting | M | 55 | The Information, 2023 [48] |
| 124 | Copy.ai | AI-native | Marketing / GTM copy | M† | 55 | Wellows, 2026 [44] |
| 125 | Writesonic | AI-native | Marketing copywriting | M† | 55 | Wellows, 2026 [44] |
| 126 | Rytr | AI-native | Writing assistant | M† | 55 | Wellows, 2026 [44] |
| 127 | Sudowrite | AI-native | Fiction writing | M† | 55 | Wellows, 2026 [44] |
| 128 | Writer | AI-native | Enterprise writing (own models) | O | 45 | Wellows, 2026 [44] |
| 129 | Typeface | AI-native | Enterprise content | M† | 55 | CB Insights, 2025 [43] |
| 130 | Jenni AI | AI-native | Academic writing | M† | 55 | Wellows, 2026 [44] |
| 131 | Anyword | AI-native | Marketing copy | M† | 55 | Wellows, 2026 [44] |
| 132 | Perplexity | AI-native | Answer engine / search | M | 55 | Upstarts Media, 2025 [50] |
| 133 | Glean | AI-native | Enterprise search / agents | M† | 55 | Wellows, 2026 [44] |
| 134 | Hebbia | AI-native | Document intelligence (finance) | M† | 55 | CB Insights, 2025 [43] |
| 135 | You.com | AI-native | Answer engine / search | M | 55 | CB Insights, 2025 [43] |
| 136 | Dashworks | AI-native | Enterprise knowledge assistant | M† | 55 | Wellows, 2026 [44] |
| 137 | Sana AI | AI-native | Enterprise knowledge / learning | M† | 55 | CB Insights, 2025 [43] |
| 138 | Dust | AI-native | Enterprise agent platform | M | 55 | CB Insights, 2025 [43] |
| 139 | Harvey | AI-native | Legal AI | M | 55 | Harvey, 2025 [51] |
| 140 | Robin AI | AI-native | Contract AI | M† | 55 | CB Insights, 2025 [43] |
| 141 | Spellbook | AI-native | Contract drafting | M† | 55 | CB Insights, 2025 [43] |
| 142 | Luminance | AI-native | Legal document analysis | M† | 55 | CB Insights, 2025 [43] |
| 143 | EvenUp | AI-native | Personal-injury legal AI | M† | 55 | CB Insights, 2025 [43] |
| 144 | Legora | AI-native | Collaborative legal AI | M† | 55 | CB Insights, 2025 [43] |
| 145 | DraftWise | AI-native | Contract drafting | M† | 55 | CB Insights, 2025 [43] |
| 146 | Decagon | AI-native | Customer-support agents | M† | 55 | Upstarts Media, 2025 [50] |
| 147 | Sierra | AI-native | Customer-experience agents | M† | 55 | Upstarts Media, 2025 [50] |
| 148 | Ada | AI-native | Customer-support automation | M† | 55 | Wellows, 2026 [44] |
| 149 | Forethought | AI-native | Support automation | M† | 55 | CB Insights, 2025 [43] |
| 150 | Cresta | AI-native | Contact-center intelligence | M† | 55 | CB Insights, 2025 [43] |
| 151 | PolyAI | AI-native | Voice customer service | M† | 55 | CB Insights, 2025 [43] |
| 152 | Parloa | AI-native | Contact-center AI | M† | 55 | CB Insights, 2025 [43] |
| 153 | Lorikeet | AI-native | Support agents | M† | 55 | CB Insights, 2025 [43] |
| 154 | Abridge | AI-native | Clinical documentation | M† | 55 | OpenAI, 2026 [66] |
| 155 | Ambience Healthcare | AI-native | Clinical documentation | M† | 55 | OpenAI, 2026 [66] |
| 156 | Suki | AI-native | Clinical voice assistant | M† | 55 | CB Insights, 2025 [43] |
| 157 | Nabla | AI-native | Clinical documentation | M† | 55 | CB Insights, 2025 [43] |
| 158 | OpenEvidence | AI-native | Clinical decision support | M† | 55 | CB Insights, 2025 [43] |
| 159 | Hippocratic AI | AI-native | Healthcare agents (own model) | O | 45 | CB Insights, 2025 [43] |
| 160 | Heidi Health | AI-native | Clinical scribe | M† | 55 | CB Insights, 2025 [43] |
| 161 | Commure | AI-native | Healthcare operations AI | M† | 55 | CB Insights, 2025 [43] |
| 162 | Clay | AI-native | Sales / GTM data | M† | 55 | OpenAI, 2026 [66] |
| 163 | 11x | AI-native | AI sales reps | M† | 55 | CB Insights, 2025 [43] |
| 164 | Artisan | AI-native | AI sales reps | M† | 55 | CB Insights, 2025 [43] |
| 165 | AiSDR | AI-native | Sales outreach | M† | 55 | CB Insights, 2025 [43] |
| 166 | Nooks | AI-native | Sales calling platform | M† | 55 | CB Insights, 2025 [43] |
| 167 | Rogo | AI-native | Financial-analysis AI | M† | 55 | CB Insights, 2025 [43] |
| 168 | Basis | AI-native | Accounting agents | M† | 55 | CB Insights, 2025 [43] |
| 169 | Numeric | AI-native | Accounting close | M† | 55 | CB Insights, 2025 [43] |
| 170 | Granola | AI-native | AI meeting notes | M† | 55 | Fortune, 2026 [29] |
| 171 | Otter.ai | AI-native | Meeting transcription | M† | 55 | Fortune, 2026 [29] |
| 172 | Fireflies.ai | AI-native | Meeting transcription | M† | 55 | Fortune, 2026 [29] |
| 173 | Fathom | AI-native | Meeting notes | M† | 55 | Wellows, 2026 [44] |
| 174 | Read AI | AI-native | Meeting intelligence | M† | 55 | Wellows, 2026 [44] |
| 175 | Mem | AI-native | AI note-taking | M† | 55 | Wellows, 2026 [44] |
| 176 | Tana | AI-native | AI knowledge workspace | M† | 55 | Wellows, 2026 [44] |
| 177 | Midjourney | AI-native | Image generation (own models) | O | 45 | CB Insights, 2025 [43] |
| 178 | Runway | AI-native | Video generation (own models) | O | 45 | CB Insights, 2025 [43] |
| 179 | Pika | AI-native | Video generation (own models) | O | 45 | CB Insights, 2025 [43] |
| 180 | Luma AI | AI-native | Video/3D generation (own) | O | 45 | CB Insights, 2025 [43] |
| 181 | Ideogram | AI-native | Image generation (own model) | O | 45 | CB Insights, 2025 [43] |
| 182 | Leonardo.AI | AI-native | Image generation | O† | 45 | CB Insights, 2025 [43] |
| 183 | Recraft | AI-native | Design image generation | O† | 45 | CB Insights, 2025 [43] |
| 184 | Krea | AI-native | Creative image/video | M | 55 | CB Insights, 2025 [43] |
| 185 | ElevenLabs | AI-native | Voice / audio (own models) | O | 45 | CB Insights, 2025 [43] |
| 186 | Suno | AI-native | Music generation (own models) | O | 45 | CB Insights, 2025 [43] |
| 187 | Udio | AI-native | Music generation (own models) | O | 45 | CB Insights, 2025 [43] |
| 188 | Synthesia | AI-native | AI video avatars | M† | 55 | CB Insights, 2025 [43] |
| 189 | HeyGen | AI-native | AI video avatars | M† | 55 | CB Insights, 2025 [43] |
| 190 | Descript | AI-native | Audio/video editing | M† | 55 | Wellows, 2026 [44] |
| 191 | Captions | AI-native | Short-form video | M† | 55 | CB Insights, 2025 [43] |
| 192 | Photoroom | AI-native | Image editing | M† | 55 | Wellows, 2026 [44] |
| 193 | Gamma | AI-native | AI presentations | M† | 55 | Wellows, 2026 [44] |
| 194 | Galileo AI (Stitch) | AI-native | UI design generation | M† | 55 | CB Insights, 2025 [43] |
| 195 | Manus | AI-native | General autonomous agent | M† | 55 | Fast Company, 2025 [54] |
| 196 | Lindy | AI-native | Personal AI agents | M† | 55 | CB Insights, 2025 [43] |
| 197 | MultiOn | AI-native | Web-action agents | M† | 55 | CB Insights, 2025 [43] |
| 198 | Relevance AI | AI-native | Agent workforce platform | M | 55 | CB Insights, 2025 [43] |
| 199 | Genspark | AI-native | Agentic search | M† | 55 | CB Insights, 2025 [43] |
| 200 | Character.AI | AI-native | Consumer companions (own models) | O | 45 | CB Insights, 2025 [43] |
| 201 | Replika | AI-native | Consumer companion | M† | 55 | Wellows, 2026 [44] |
| 202 | Quora (Poe) | AI-native | Multi-model chat aggregator | M | 55 | Wellows, 2026 [44] |
| 203 | Khan Academy (Khanmigo) | AI-native | Education tutor | S | 90 | Wellows, 2026 [44] |
| 204 | Speak | AI-native | Language learning | M† | 55 | CB Insights, 2025 [43] |
| 205 | MagicSchool AI | AI-native | Education (teachers) | M† | 55 | CB Insights, 2025 [43] |
| 206 | Microsoft 365 Copilot | Incumbent | Office productivity | M | 30 | Microsoft, 2026 [57] |
| 207 | GitHub Copilot | Incumbent | Coding assistant | M | 30 | Microsoft, 2026 [57] |
| 208 | Microsoft Nuance DAX | Incumbent | Clinical documentation | M† | 30 | Microsoft, 2026 [57] |
| 209 | Google Workspace (Gemini) | Incumbent | Productivity | M† | 30 | Northflank, 2026 [3] |
| 210 | Salesforce (Agentforce) | Incumbent | CRM / agents | M† | 30 | Northflank, 2026 [3] |
| 211 | Notion AI | Incumbent | Productivity workspace | M | 30 | Notion, 2025 [34] |
| 212 | Atlassian (Rovo) | Incumbent | Dev / collaboration | M† | 30 | Wellows, 2026 [44] |
| 213 | ServiceNow (Now Assist) | Incumbent | ITSM / workflow | M† | 30 | Wellows, 2026 [44] |
| 214 | HubSpot (Breeze) | Incumbent | CRM / marketing | M† | 30 | Wellows, 2026 [44] |
| 215 | Adobe (Firefly / Acrobat AI) | Incumbent | Creative tools (own + partners) | O† | 26 | Wellows, 2026 [44] |
| 216 | Canva (Magic Studio) | Incumbent | Design | M† | 30 | Wellows, 2026 [44] |
| 217 | Grammarly | Incumbent | Writing assistance | M† | 30 | Wellows, 2026 [44] |
| 218 | Intercom (Fin) | Incumbent | Customer support | M† | 30 | Wellows, 2026 [44] |
| 219 | Zendesk (AI) | Incumbent | Customer support | M† | 30 | Wellows, 2026 [44] |
| 220 | Freshworks (Freddy) | Incumbent | CRM / support | M† | 30 | Wellows, 2026 [44] |
| 221 | Zoom (AI Companion) | Incumbent | Communications | M† | 30 | Wellows, 2026 [44] |
| 222 | Slack (AI) | Incumbent | Collaboration | M† | 30 | Wellows, 2026 [44] |
| 223 | SAP (Joule) | Incumbent | ERP / enterprise | M† | 30 | Northflank, 2026 [3] |
| 224 | Workday (AI) | Incumbent | HCM / finance | M† | 30 | Northflank, 2026 [3] |
| 225 | Oracle (Fusion AI) | Incumbent | ERP / database | M† | 30 | Northflank, 2026 [3] |
| 226 | Box (AI) | Incumbent | Content management | M† | 30 | Wellows, 2026 [44] |
| 227 | Dropbox (Dash) | Incumbent | File / search | M† | 30 | Wellows, 2026 [44] |
| 228 | Asana (AI) | Incumbent | Work management | M† | 30 | Wellows, 2026 [44] |
| 229 | Atlassian Jira / Confluence | Incumbent | Work management | M† | 30 | Wellows, 2026 [44] |
| 230 | Figma (AI / Make) | Incumbent | Design | M† | 30 | Wellows, 2026 [44] |
| 231 | Airtable (AI) | Incumbent | Database / apps | M† | 30 | Wellows, 2026 [44] |
| 232 | Miro (AI) | Incumbent | Whiteboarding | M† | 30 | Wellows, 2026 [44] |
| 233 | Shopify (Sidekick / Magic) | Incumbent | E-commerce | M† | 30 | Wellows, 2026 [44] |
| 234 | Stripe (AI) | Incumbent | Payments / fraud | M† | 30 | Northflank, 2026 [3] |
| 235 | Klarna (assistant) | Incumbent | Fintech support | S† | 42 | Wellows, 2026 [44] |
| 236 | Duolingo (Max) | Incumbent | Language learning | S† | 42 | Wellows, 2026 [44] |
| 237 | Quizlet (Q-Chat) | Incumbent | Education | M† | 30 | Wellows, 2026 [44] |
| 238 | Coursera (Coach) | Incumbent | Education | M† | 30 | Wellows, 2026 [44] |
| 239 | Chegg | Incumbent | Education | S† | 42 | Wellows, 2026 [44] |
| 240 | Thomson Reuters (CoCounsel) | Incumbent | Legal research | M† | 30 | CB Insights, 2025 [43] |
| 241 | LexisNexis (Lexis+ AI) | Incumbent | Legal research | M† | 30 | CB Insights, 2025 [43] |
| 242 | Bloomberg (BloombergGPT) | Incumbent | Built own LLM; off-the-shelf outperformed | O | 26 | Fast Company, 2025 [54] |
| 243 | GitLab (Duo) | Incumbent | DevOps | M† | 30 | Northflank, 2026 [3] |
| 244 | DocuSign (IAM / AI) | Incumbent | Agreements | M† | 30 | Wellows, 2026 [44] |
| 245 | Twilio (AI) | Incumbent | Communications APIs | M† | 30 | Northflank, 2026 [3] |
| 246 | ServiceTitan (AI) | Incumbent | Field-service software | M† | 30 | Wellows, 2026 [44] |
| 247 | Wendy's (FreshAI) | Incumbent | Drive-thru ordering | M† | 30 | Wellows, 2026 [44] |
| 248 | Spotify (AI DJ) | Incumbent | Consumer audio | M† | 30 | Wellows, 2026 [44] |
| 249 | Reddit (Answers) | Incumbent | Consumer social | M† | 30 | Wellows, 2026 [44] |
| 250 | Instacart (AI) | Incumbent | E-commerce / grocery | S† | 42 | Wellows, 2026 [44] |
| 251 | Expedia (assistant) | Incumbent | Travel | S† | 42 | Wellows, 2026 [44] |
| 252 | DeepL | Incumbent | Translation (own models) | O | 26 | CB Insights, 2025 [43] |
| 253 | Zed | AI-native | AI code editor | M† | 55 | CB Insights, 2025 [43] |
| 254 | Warp | AI-native | AI terminal | M† | 55 | CB Insights, 2025 [43] |
| 255 | CodeRabbit | AI-native | AI code review (SME) | M† | 55 | Y Combinator, 2026 [67] |
| 256 | Greptile | AI-native | AI code review / search (SME) | M† | 55 | Y Combinator, 2026 [67] |
| 257 | Graphite | AI-native | Code-review platform | M† | 55 | CB Insights, 2025 [43] |
| 258 | Trae (ByteDance) | AI-native | AI IDE | M† | 55 | Northflank, 2026 [3] |
| 259 | Mintlify | AI-native | AI documentation (SME) | M† | 55 | Y Combinator, 2026 [67] |
| 260 | Phind | AI-native | Developer answer engine | M† | 55 | CB Insights, 2025 [43] |
| 261 | Consensus | AI-native | Science / research search | M† | 55 | CB Insights, 2025 [43] |
| 262 | Elicit | AI-native | Research assistant | M† | 55 | CB Insights, 2025 [43] |
| 263 | SciSpace | AI-native | Research assistant (SME) | M† | 55 | Wellows, 2026 [44] |
| 264 | Eve | AI-native | Plaintiff legal AI | M† | 55 | CB Insights, 2025 [43] |
| 265 | Leya | AI-native | Legal workflow AI | M† | 55 | CB Insights, 2025 [43] |
| 266 | Garfield AI | AI-native | Legal automation (SME) | M† | 55 | CB Insights, 2025 [43] |
| 267 | Crosby | AI-native | AI contracts / legal (SME) | M† | 55 | Y Combinator, 2026 [67] |
| 268 | Freed | AI-native | Clinical scribe (SME) | M† | 55 | CB Insights, 2025 [43] |
| 269 | Tennr | AI-native | Healthcare workflow AI | M† | 55 | Y Combinator, 2026 [67] |
| 270 | Corti | AI-native | Clinical voice AI | M† | 55 | CB Insights, 2025 [43] |
| 271 | Rox | AI-native | AI sales agents | M† | 55 | CB Insights, 2025 [43] |
| 272 | Unify GTM | AI-native | GTM automation | M† | 55 | CB Insights, 2025 [43] |
| 273 | Landbase | AI-native | GTM agent platform | M† | 55 | CB Insights, 2025 [43] |
| 274 | Persana AI | AI-native | Sales prospecting (SME) | M† | 55 | Wellows, 2026 [44] |
| 275 | Tabs | AI-native | AR / billing automation (SME) | M† | 55 | Y Combinator, 2026 [67] |
| 276 | Puzzle | AI-native | AI accounting (SME) | M† | 55 | CB Insights, 2025 [43] |
| 277 | Digits | AI-native | AI accounting | M† | 55 | CB Insights, 2025 [43] |
| 278 | Rillet | AI-native | AI-native ERP / accounting (SME) | M† | 55 | Y Combinator, 2026 [67] |
| 279 | Campfire | AI-native | AI accounting / ERP (SME) | M† | 55 | Y Combinator, 2026 [67] |
| 280 | Gumloop | AI-native | No-code AI automation (SME) | M† | 55 | Y Combinator, 2026 [67] |
| 281 | Bardeen | AI-native | Workflow-automation agents | M† | 55 | CB Insights, 2025 [43] |
| 282 | Lutra | AI-native | Agentic workflows (SME) | M† | 55 | Y Combinator, 2026 [67] |
| 283 | Wordware | AI-native | Agent IDE (SME) | M† | 55 | Y Combinator, 2026 [67] |
| 284 | Cognosys | AI-native | Autonomous agents (SME) | M† | 55 | CB Insights, 2025 [43] |
| 285 | Khoj | AI-native | Personal AI assistant (OSS) | M† | 55 | Y Combinator, 2026 [67] |
| 286 | Cartesia | AI-native | Voice models (own) | O | 45 | CB Insights, 2025 [43] |
| 287 | Hume AI | AI-native | Emotion / voice models (own) | O | 45 | CB Insights, 2025 [43] |
| 288 | Vapi | AI-native | Voice-agent platform (SME) | M† | 55 | Y Combinator, 2026 [67] |
| 289 | Retell AI | AI-native | Voice-agent platform (SME) | M† | 55 | Y Combinator, 2026 [67] |
| 290 | Bland AI | AI-native | Voice-agent platform | M† | 55 | CB Insights, 2025 [43] |
| 291 | Black Forest Labs (Flux) | Provider | Open image models | O | 10 | CB Insights, 2025 [43] |
| 292 | Kuaishou (Kling) | Provider | Video models | O | 10 | Bloomberg, 2025 [45] |
| 293 | Moonvalley | AI-native | Video models (own) | O | 45 | CB Insights, 2025 [43] |
| 294 | Higgsfield | AI-native | AI video | O† | 45 | CB Insights, 2025 [43] |
| 295 | Hedra | AI-native | AI video avatars (SME) | O† | 45 | Y Combinator, 2026 [67] |
| 296 | Genmo (Mochi) | AI-native | Open video models | O | 45 | CB Insights, 2025 [43] |
| 297 | Haiper | AI-native | AI video (own models) | O | 45 | CB Insights, 2025 [43] |
| 298 | Reve | AI-native | Image generation (own model) | O | 45 | CB Insights, 2025 [43] |
| 299 | Limitless | AI-native | Wearable AI assistant | M† | 55 | CB Insights, 2025 [43] |
| 300 | Friend | AI-native | AI companion wearable (SME) | M† | 55 | CB Insights, 2025 [43] |
| 301 | Rabbit | AI-native | Consumer AI device | M† | 55 | CB Insights, 2025 [43] |
| 302 | Plaud | AI-native | AI voice recorder | M† | 55 | Wellows, 2026 [44] |
| 303 | EliseAI | AI-native | Real-estate / housing AI | M† | 55 | CB Insights, 2025 [43] |
| 304 | Buildots | AI-native | Construction computer vision | O† | 45 | CB Insights, 2025 [43] |
| 305 | Sixfold | AI-native | Insurance underwriting AI (SME) | M† | 55 | CB Insights, 2025 [43] |
| 306 | Mercor | AI-native | AI hiring / data marketplace | M† | 55 | CB Insights, 2025 [43] |
| 307 | Metaview | AI-native | Recruiting-notes AI (SME) | M† | 55 | Y Combinator, 2026 [67] |
| 308 | Listen Labs | AI-native | AI user research (SME) | M† | 55 | Y Combinator, 2026 [67] |
| 309 | Hex (Magic) | AI-native | Analytics workspace + AI | M† | 55 | CB Insights, 2025 [43] |
| 310 | Julius AI | AI-native | AI data analysis (SME) | M† | 55 | Wellows, 2026 [44] |
| 311 | AdCreative.ai | AI-native | AI ad creative (SME) | M† | 55 | Wellows, 2026 [44] |
| 312 | Creatify | AI-native | AI video ads (SME) | M† | 55 | Wellows, 2026 [44] |
| 313 | Icon | AI-native | AI ad production (SME) | M† | 55 | CB Insights, 2025 [43] |
| 314 | Browserbase | Infrastructure | Headless browser for agents | M | 35 | CB Insights, 2025 [43] |
| 315 | Browser Use | Infrastructure | Browser-agent framework (OSS) | M | 35 | Y Combinator, 2026 [67] |
| 316 | Firecrawl | Infrastructure | Web data for LLMs (SME) | M | 35 | Y Combinator, 2026 [67] |
| 317 | Skyvern | Infrastructure | Browser-automation agents (OSS) | M | 35 | Y Combinator, 2026 [67] |
| 318 | Apify | Infrastructure | Web scraping / agents | M† | 35 | Northflank, 2026 [3] |
| 319 | Mem0 | Infrastructure | Agent memory layer (SME) | M | 35 | Y Combinator, 2026 [67] |
| 320 | Zep | Infrastructure | Agent memory / context | M | 35 | CB Insights, 2025 [43] |
| 321 | Letta (MemGPT) | Infrastructure | Agent memory framework | M | 35 | CB Insights, 2025 [43] |
| 322 | LlamaCloud | Infrastructure | Parsing / RAG (LlamaIndex) | M | 35 | CB Insights, 2025 [43] |
| 323 | Reducto | Infrastructure | Document parsing (SME) | M | 35 | Y Combinator, 2026 [67] |
| 324 | Ragie | Infrastructure | RAG-as-a-service (SME) | M | 35 | Y Combinator, 2026 [67] |
| 325 | Exa | Infrastructure | Search API for AI | M | 35 | CB Insights, 2025 [43] |
| 326 | Tavily | Infrastructure | Search API for agents (SME) | M | 35 | Y Combinator, 2026 [67] |
| 327 | Predibase | Infrastructure | Fine-tuning / serving | M | 35 | CB Insights, 2025 [43] |
| 328 | OpenPipe | Infrastructure | Fine-tuning platform (SME) | M | 35 | Y Combinator, 2026 [67] |
| 329 | Ragas | Infrastructure | RAG evaluation (OSS) | M | 35 | CB Insights, 2025 [43] |
| 330 | Opik (Comet) | Infrastructure | LLM eval / observability | M | 35 | CB Insights, 2025 [43] |
| 331 | Prompt Security | Infrastructure | LLM security (SME) | M | 35 | CB Insights, 2025 [43] |
| 332 | Pillar Security | Infrastructure | AI security (SME) | M† | 35 | CB Insights, 2025 [43] |
| 333 | VAST Data | Infrastructure | AI data platform | M† | 35 | Forbes AI 50, 2025 [68] |
| 334 | Deepgram | Infrastructure | Speech-to-text models | O | 28 | CB Insights, 2025 [43] |
| 335 | AssemblyAI | Infrastructure | Speech AI models | O | 28 | CB Insights, 2025 [43] |
| 336 | LiveKit | Infrastructure | Realtime voice/video infra | M† | 35 | Northflank, 2026 [3] |
| 337 | Speechmatics | Infrastructure | Speech recognition | O | 28 | Wellows, 2026 [44] |
| 338 | Marqo | Infrastructure | Vector / multimodal search | M† | 35 | Northflank, 2026 [3] |
| 339 | Nomic AI | Infrastructure | Embeddings / data maps | O | 28 | CB Insights, 2025 [43] |
| 340 | Jina AI | Infrastructure | Embeddings / multimodal | O | 28 | Northflank, 2026 [3] |
| 341 | Voyage AI | Infrastructure | Embeddings (retrieval) | O | 28 | CB Insights, 2025 [43] |
| 342 | Cleanlab | Infrastructure | Data quality for AI | M† | 35 | Wellows, 2026 [44] |
| 343 | Encord | Infrastructure | Data labeling / eval | M† | 35 | CB Insights, 2025 [43] |
| 344 | SuperAnnotate | Infrastructure | Data labeling / RLHF | M† | 35 | Wellows, 2026 [44] |
| 345 | Fiddler AI | Infrastructure | ML / LLM observability | M† | 35 | Northflank, 2026 [3] |
| 346 | WhyLabs | Infrastructure | ML / LLM observability | M† | 35 | Wellows, 2026 [44] |
| 347 | Lamini | Infrastructure | Enterprise LLM platform | M† | 35 | CB Insights, 2025 [43] |
| 348 | Modular | Infrastructure | AI inference engine (MAX) | M† | 35 | Northflank, 2026 [3] |
| 349 | Credal | Infrastructure | Enterprise AI data security | M† | 35 | Y Combinator, 2026 [67] |
| 350 | Tracecat | Infrastructure | Security automation (AI) | M† | 35 | Y Combinator, 2026 [67] |
| 351 | Abnormal Security | Infrastructure | Email security AI | M† | 35 | CB Insights, 2025 [43] |
| 352 | Cyera | Infrastructure | Data security posture (AI) | M† | 35 | CB Insights, 2025 [43] |
| 353 | Dropzone AI | Infrastructure | SOC analyst agents | M† | 35 | Wellows, 2026 [44] |
| 354 | Maven AGI | AI-native | Customer support agents | M† | 55 | CB Insights, 2025 [43] |
| 355 | Crescendo | AI-native | Customer support AI | M† | 55 | Wellows, 2026 [44] |
| 356 | Ada | AI-native | Customer service automation | M† | 55 | Northflank, 2026 [3] |
| 357 | Gradient Labs | AI-native | Support agents (regulated) | M† | 55 | Y Combinator, 2026 [67] |
| 358 | Observe.AI | AI-native | Contact-center AI | M† | 55 | CB Insights, 2025 [43] |
| 359 | Replicant | AI-native | Voice customer service | M† | 55 | Wellows, 2026 [44] |
| 360 | Wonderful | AI-native | Customer support agents | M† | 55 | Wellows, 2026 [44] |
| 361 | Pylon | AI-native | B2B customer support | M† | 55 | Y Combinator, 2026 [67] |
| 362 | Regie.ai | AI-native | Sales content agents | M† | 55 | Wellows, 2026 [44] |
| 363 | Tektonic AI | AI-native | GTM operations agents | M† | 55 | Wellows, 2026 [44] |
| 364 | Clearbrief | AI-native | Legal writing / citations | M† | 55 | Wellows, 2026 [44] |
| 365 | Definely | AI-native | Contract drafting | M† | 55 | CB Insights, 2025 [43] |
| 366 | Wordsmith | AI-native | In-house legal AI | M† | 55 | Y Combinator, 2026 [67] |
| 367 | Augmedix | AI-native | Clinical documentation | M† | 55 | CB Insights, 2025 [43] |
| 368 | Sardine | AI-native | Fraud / risk AI | M† | 55 | CB Insights, 2025 [43] |
| 369 | Norm Ai | AI-native | Regulatory compliance agents | M† | 55 | CB Insights, 2025 [43] |
| 370 | Greenlite | AI-native | Compliance / AML agents | M† | 55 | Y Combinator, 2026 [67] |
| 371 | Sedric AI | AI-native | Compliance monitoring | M† | 55 | Wellows, 2026 [44] |
| 372 | Micro1 | AI-native | AI recruiting / vetting | M† | 55 | Wellows, 2026 [44] |
| 373 | Juicebox (PeopleGPT) | AI-native | AI talent search | M† | 55 | Wellows, 2026 [44] |
| 374 | Moonhub | AI-native | AI recruiting | M† | 55 | Y Combinator, 2026 [67] |
| 375 | Zencoder | AI-native | Coding agent | M† | 55 | Wellows, 2026 [44] |
| 376 | Sweep | AI-native | Coding / PR agent | M† | 55 | Y Combinator, 2026 [67] |
| 377 | Cosine (Genie) | AI-native | Coding agent | M† | 55 | CB Insights, 2025 [43] |
| 378 | Induced AI | AI-native | Web-action agents | M† | 55 | Y Combinator, 2026 [67] |
| 379 | Orby AI | AI-native | Enterprise automation agents | M† | 55 | CB Insights, 2025 [43] |
| 380 | Ema | AI-native | Enterprise AI-employee agents | M† | 55 | CB Insights, 2025 [43] |
| 381 | Aisera | AI-native | Agentic enterprise/IT service AI | M† | 55 | CB Insights, 2025 [43] |
| 382 | Moveworks | AI-native | Enterprise copilot | M† | 55 | CB Insights, 2025 [43] |
| 383 | Delphi | AI-native | Digital-mind / persona AI | M† | 55 | Wellows, 2026 [44] |
| 384 | Distyl AI | AI-native | Enterprise AI solutions | M† | 55 | Wellows, 2026 [44] |
| 385 | H Company | AI-native | Agentic models (Runner H) | O | 45 | Bloomberg, 2025 [45] |
| 386 | Adept | AI-native | Action / agent models | O | 45 | CB Insights, 2025 [43] |
| 387 | PlayAI | AI-native | Voice generation (own models) | O | 45 | CB Insights, 2025 [43] |
| 388 | Rime | AI-native | Voice models | O | 45 | Wellows, 2026 [44] |
| 389 | Tavus | AI-native | AI video avatars (own models) | O | 45 | CB Insights, 2025 [43] |
| 390 | Argil | AI-native | AI video avatars | M† | 55 | Wellows, 2026 [44] |
| 391 | Beautiful.ai | AI-native | AI presentations | M† | 55 | Wellows, 2026 [44] |
| 392 | Durable | AI-native | AI website builder | M† | 55 | Wellows, 2026 [44] |
| 393 | Tome | AI-native | AI presentations / storytelling | M† | 55 | CB Insights, 2025 [43] |
| 394 | Gong | Incumbent | Revenue intelligence | M† | 30 | CB Insights, 2025 [43] |
| 395 | Apollo.io | Incumbent | Sales intelligence platform | M† | 30 | Wellows, 2026 [44] |
| 396 | Clari | Incumbent | Revenue operations | M† | 30 | Northflank, 2026 [3] |
| 397 | Eightfold AI | Incumbent | Talent intelligence | M† | 30 | CB Insights, 2025 [43] |
| 398 | Innovaccer | Incumbent | Healthcare data platform | M† | 30 | CB Insights, 2025 [43] |
