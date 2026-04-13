# AgentWarehouse

My repository of reusable GitHub Copilot custom-agent profile files.
Agent definitions live under `.github/agents/` as `*.agent.md` files.

## Agents

![Agent summary table](assets/agent-table.png)

## Agent Overviews

### BUILDER
BUILDER implements functional requirements minimally and accurately, verifying execution before declaring any task complete. Correctness takes priority over breadth. Output is working code.

### DOCUMENTER
DOCUMENTER identifies gaps between the README and the actual codebase and corrects them directly. It preserves information density without adding noise.

### FUNCTIONALIST
FUNCTIONALIST translates architecture proposals into technical requirements that are clear, minimal, and encapsulated. It operates as a translation layer between strategic vision and implementation, not a decision-maker.

### IDEATOR
IDEATOR sets project vision and architecture at the strategic level, naming and framing concepts with precision. It remains deliberately above implementation detail. Output is conceptual, not executable.

### IDLER_LITE
IDLER_LITE is a minimal placeholder agent. It is intentionally inert, occupying a structural slot without performing any active function.

### NARRATER
NARRATER improves narrative flow and information density in documentation using consultant-level structure and zero emotional language. Its domain is communication clarity and style, not content generation.

### OPTIMIZER
OPTIMIZER optimises existing code for speed by first cleaning and reducing, then ranking further strategies by impact and complexity. It seeks user approval before acting on ranked strategies, distinguishing it from agents that act autonomously.

### RESEARCHER_QUANT
RESEARCHER_QUANT solves narrow, deep quantitative problems by deriving theory first and validating results through targeted code simulations. It is suited to precise, bounded analytical questions, not broad survey work.

### RESEARCHER_WIDE
RESEARCHER_WIDE answers broad research questions by weighing source credibility, forming and testing hypotheses, and delivering concise conclusions with honest caveats. Its strength is synthesis across wide scope, not deep precision on a single point.

### VALIDATOR
VALIDATOR adversarially audits code and logic by assuming mistakes exist and systematically searching for them, then proposes concrete resolutions. Its adversarial posture distinguishes it from neutral review agents.

### VISUALISER
VISUALISER designs and generates Python data visualisations, working sequentially from data selection through to artefact quality. It ensures outputs are stored and referenced correctly within the visualisation pipeline.

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

