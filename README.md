# AgentWarehouse

My repository of reusable GitHub Copilot custom-agent profile files.
Agent definitions live under `.github/agents/` as `*.agent.md` files.

## Agents

![Agent summary table](assets/agent-table.png)

## Agent Overviews

### BUILDER
BUILDER implements functional requirements minimally and accurately. It verifies execution before declaring any task complete, prioritising correctness over breadth. Its scope is narrow and its output is working code.

### DOCUMENTER
DOCUMENTER keeps the README accurate and complete by finding gaps between documentation and the actual codebase. It corrects those gaps directly without adding noise. It protects information density and readability.

### FUNCTIONALIST
FUNCTIONALIST translates architecture proposals into technical requirements that are clear, minimal, and encapsulated. Its output is ready for implementation, positioning it between strategic vision and hands-on coding. It operates as a translation layer, not a decision-maker.

### IDEATOR
IDEATOR sets project vision and architecture at the strategic level. It names and frames concepts with precision while staying deliberately above implementation detail. Its scope is broad and its output is conceptual rather than executable.

### IDLER_LITE
IDLER_LITE is a minimal placeholder agent. It is intentionally inert and produces no output. Its purpose is structural — occupying a slot without performing any active function.

### NARRATER
NARRATER improves narrative flow and information density in documentation. It applies consultant-level structure and uses zero emotional language. Its domain is documentation style and communication clarity, not content generation.

### OPTIMIZER
OPTIMIZER optimises existing code for speed. It first cleans and reduces, then ranks further optimisation strategies by impact and complexity, and seeks user approval before acting on them. This staged, approval-gated approach distinguishes it from agents that act autonomously.

### RESEARCHER_QUANT
RESEARCHER_QUANT solves narrow, deep quantitative problems. It derives theory first, then validates results through targeted code simulations. It is suited to precise, bounded analytical questions rather than broad survey work.

### RESEARCHER_WIDE
RESEARCHER_WIDE answers broad research questions by weighing source credibility, forming and testing hypotheses, and delivering concise conclusions with honest caveats. Its strength is coverage and synthesis across a wide scope, not deep precision on a single point.

### VALIDATOR
VALIDATOR adversarially audits code and logic by assuming mistakes exist and systematically searching for them. It then proposes concrete resolutions for what it finds. Its adversarial posture distinguishes it from neutral or passive review agents.

### VISUALISER
VISUALISER designs and generates Python data visualisations. It works sequentially from data selection through to artefact quality, and ensures outputs are stored and referenced correctly. Its scope is bounded to the visualisation pipeline.

## Personality Vectors

| Agent | Domain | Primary Mode | Scope | Posture | Precision | Seeks Approval | Output Type |
|---|---|---|---|---|---|---|---|
| BUILDER | 💻 Code | ⚙️ Action | 🎯 Narrow | 🛡️ Conservative | ●●● | · | Working code |
| OPTIMIZER | 💻 Code | 🔀 Mixed | 🎯 Narrow | ⚠️ Cautious | ●●● | ✅ | Optimised code |
| VALIDATOR | 💻 Code | 🔍 Analysis | 🎯 Narrow | ⚔️ Adversarial | ●●● | · | Audit / Resolutions |
| DOCUMENTER | 📝 Docs | ⚙️ Action | ▣ Bounded | · Neutral | ●●● | · | Documentation |
| NARRATER | 📝 Docs | ⚙️ Action | ▣ Bounded | · Neutral | ●●● | · | Revised documentation |
| IDEATOR | 🗺️ Strategy | 🔍 Analysis | ◈ Strategic | · Neutral | ●●● | · | Vision / Architecture |
| FUNCTIONALIST | 🗺️→💻 Strategy → Code | 🔍 Analysis | ▣ Bounded | · Neutral | ●●● | · | Requirements |
| RESEARCHER_QUANT | 🔬 Research | 🔍 Analysis | 🎯 Narrow | · Neutral | ●●● | · | Analysis / Simulations |
| RESEARCHER_WIDE | 🔬 Research | 🔍 Analysis | 🌐 Broad | · Neutral | ●●○ | · | Research summary |
| VISUALISER | 📊 Data | ⚙️ Action | 🎯 Narrow | · Neutral | ●●● | · | Python visualisations |
| IDLER_LITE | — | 💤 Inert | — | 💤 Inert | — | · | None |

