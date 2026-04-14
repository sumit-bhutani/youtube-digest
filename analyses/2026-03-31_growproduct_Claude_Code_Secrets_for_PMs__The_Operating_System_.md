# Claude Code Secrets for PMs: The Operating System, Skills, and Data Viz

**Channel:** growproduct
**URL:** https://www.youtube.com/watch?v=Eqh2iwSl570
**Published:** 2026-03-30
**Analyzed:** 2026-03-31 00:30

---

# Claude Code: The Operating System Layer — Research Brief

**Video:** "Claude Code Secrets for PMs: The Operating System, Skills, and Data Viz"
**Channel:** growproduct | **Published:** 2025-03-30
**Duration:** ~66 minutes | **Transcript Quality:** Good — minor editing artifacts, no critical gaps

---

## STEP 1 — TRANSCRIPT CLUSTERS

| Cluster | Timestamp Range | Topic |
|---|---|---|
| 1 | 00:00–06:25 | Framing: Claude Code vs. co-work/OpenClaw; episode scope |
| 2 | 06:26–23:50 | Context management: status line, sub agents, escape/rollback, context rot |
| 3 | 23:51–32:10 | Skills system: ask-user-questions, front-end design plugin, skill architecture |
| 4 | 32:11–41:55 | Tools and integrations: MCPs vs. CLIs, web research skill, Tavily + Firecrawl |
| 5 | 41:56–55:30 | Auto-invocation via hooks; make-slides skill with Puppeteer; builder-validator pattern |
| 6 | 55:31–66:01 | OS layer: folder structure, data analysis in Jupyter, standup skill, CLAUDE.md |

**Speakers:** Host (unnamed, product-focused interviewer) + Carl Vatti (guest expert, cloud code practitioner/educator)

---

---

# STEP 2A — EXECUTIVE SUMMARY

## Core Thesis

Claude Code is not a chatbot. It is an extensible runtime environment — an operating system — and users who treat it like a chatbot are leaving the majority of its power unused. The strategic unlock is moving from *prompting* Claude to *engineering the environment in which Claude operates*: controlling what enters the context window, what tools are available, how work is delegated, and how outputs are verified.

## Primary Arguments (3–5)

**1. Context is the primary resource to manage, not prompts.**
The shift from "prompt engineering" to "context engineering" is presented as the governing principle of advanced Claude Code usage. Context rot — measurable degradation of output quality as context fills — is a real phenomenon. Sub agents are the primary technical lever for preserving main-session context by offloading tool-heavy work (web searches, file reads) to isolated clones that return only the summary.

**2. Skills are the mechanism for encoding role-specific expertise into Claude.**
Skills are prompt files (with optional code/tools attached) that Claude can invoke. The thesis is that Claude is not generically bad at design, research, or slides — it lacks the structured constraints that human roles provide. Skills supply those constraints. The front-end design plugin (Anthropic-official) is offered as evidence: same model, dramatically better output.

**3. CLIs are superior to MCPs for tool integration.**
Strongly argued (with Andrej Karpathy cited as external validator): MCPs consume context tokens by existing in the session, even before use. CLIs are installed at the machine level and invoked by the agent on demand, consuming zero passive context. Hierarchy stated as: MCP < API < CLI. GitHub CLI and Vercel CLI cited as near-mandatory for vibe coding workflows.

**4. Verifiable analysis requires a reproducible artifact layer (Jupyter notebooks).**
Trust in AI data outputs is the central blocker for PMs using AI for analysis. The proposed solution is forcing Claude to produce Jupyter notebooks — self-documenting, reproducible, renderable natively in VS Code/Cursor — so that the chain of computation is visible and auditable, not just the conclusion.

**5. An OS-layer folder structure compounds value over time.**
The operating system framing culminates in a specific folder architecture: `/knowledge`, `/projects`, `/data`, `/tasks`, `/tools`, `/skills`, and `CLAUDE.md`. This is not organizational hygiene — it is described as the mechanism by which context becomes cumulative and cross-session, transforming Claude from a stateless assistant into a context-rich collaborator.

## Quantitative Insights

- Claude Code: $2.5B annualized revenue, achieved in 9 months — described as fastest B2B software product ramp in history *(stated as fact by host, unverified source)*
- Starting context usage at session open with MCPs + tools enabled: ~16% consumed before any user message
- Sub agent for web research task: reduced context consumption from ~25% to ~16.5% (saved ~8.5 percentage points per research task)
- Sub agent ran 10 tool uses, consumed ~30,000 tokens — all absorbed inside the sub agent session, not the main context
- Anthropic official plugin library: 56 plugins available
- Survey dataset used in demo: 23 rows, multiple numeric columns

## Key Examples

- **Status line customization** via `/statusline` command — visual context gauge (green/orange/red)
- **Context guard skill** — auto-evaluates whether a task should run in main session or sub agent
- **Ask-user-questions tool** — generates dynamic UI-based question flows inside the CLI; one user reportedly received 67 questions
- **Make-slides skill** with Puppeteer — self-iterating visual design with screenshot-based validation, must iterate 3 times minimum
- **Web research skill** using Tavily (high-quality search) + Firecrawl CLI (clean markdown scraping)
- **Correlation heatmap** from survey data — enterprise interest correlated with security and team management, not pricing
- **Standup skill** aggregating GitHub, Linear, tasks, calendar into a single morning briefing

## Strategic Implications

- For **PMs**: Claude Code is becoming a personal data analyst, meeting preparer, slide designer, and research engine — but only if the OS layer is configured. Without it, you're getting 20% of the value.
- For **AI builders**: The CLI-over-MCP insight is immediately actionable and reduces latent context bloat in any agent system.
- For **founders**: The skills marketplace (Vercel-backed) and prompt injection risks in third-party skills are early signals of an emerging security/trust layer problem in AI tooling.
- For **strategy leaders**: The $2.5B / 9-month ramp claim, if directionally accurate, indicates enterprise adoption of AI coding tools is not slowing — it is compounding.

## What Changed vs. Conventional Wisdom

| Conventional Wisdom | What This Video Argues |
|---|---|
| Add more MCPs to extend Claude's capabilities | MCPs bloat context; prefer CLIs |
| Skills auto-invoke when you mention keywords | Auto-invocation is unreliable; use hooks with keyword-matching scripts |
| AI is just bad at design/slides/research | AI lacks role constraints; skills supply those constraints |
| Context limit is a nuisance, auto-compact handles it | Context rot degrades quality before the limit; proactive management is required |
| Use co-work or OpenClaw for the best experience | Claude Code CLI is the most powerful layer; others build on top of it with constraints |

## Fact / Opinion / Interpretation Separation

**Facts stated:**
- `/statusline` and `/context` are real Claude Code slash commands
- Sub agents in Claude Code are spawned via `Task` tool and run in isolated context
- Escape key stops execution; double-escape shows message history for rollback
- CLAUDE.md is always in context across all messages
- Puppeteer is a real front-end automation tool for screenshot capture
- Jupyter notebooks render natively in VS Code and Cursor

**Speaker opinion:**
- CLIs are becoming the preferred integration method over MCPs
- Context management is "the golden rule" of advanced AI usage
- The ask-user-questions tool is the "absolute favorite" feature of Claude Code
- Co-work is good for its use cases but "constrained" relative to raw Claude Code

**Analyst interpretation:**
- The OS-layer framing is strategically significant: it repositions Claude Code as infrastructure, not a product — with compounding moats for power users
- The skills-as-role-encoding concept maps directly onto enterprise AI deployment patterns (role-specific AI personas)
- Prompt injection risk in third-party skill marketplaces is underweighted in the discussion relative to how seriously it should be treated

---

## STEP 2B — KEY INSIGHTS EXPANSION (10–15 Bullets)

**1. Context is not just a technical constraint — it's a quality signal.**
`[10:18–10:40]` | The host introduces "context rot" as a measured phenomenon — quality degrades proportionally as context fills. This reframes context management from a performance optimization to an output quality imperative.
*Why it matters:* PMs presenting AI-generated analysis to leadership are unknowingly degrading output quality by running long sessions.
*Implication:* Establish session length norms and context checkpoints as part of any AI workflow standard.

**2. Sub agents are context firewalls, not just parallelization tools.**
`[14:40–16:42]` | A sub agent absorbs all intermediate tool calls (10 calls, ~30K tokens) and returns only the final summary to the main session. Main context cost: 0.5% vs. ~9% without.
*Why it matters:* This is the single highest-ROI context management technique in the video. It changes how you architect any multi-step task.
*Implication:* Any task involving web search, file reading, or multi-tool orchestration should default to sub agent delegation.

**3. Skills are not macros — they are encoded role expertise.**
`[29:51–31:04]` | The front-end design skill contains no new capabilities — it is "just a really good prompt" with design heuristics. The output quality improvement is entirely from constraint and framing, not new model access.
*Why it matters:* This democratizes skill creation. Any PM can encode their domain knowledge into a skill without engineering support.
*Implication:* Build a skill library that maps to the roles you collaborate with (designer, analyst, researcher, writer) before reaching for external tools.

**4. The MCP-to-CLI migration is already underway — and Karpathy validated it.**
`[36:41–37:51]` | Andrej Karpathy is cited as recommending CLI preference over MCP. The hierarchy: MCP (context-expensive, unreliable) < API < CLI (machine-level, zero passive context cost).
*Why it matters:* Teams building MCP-heavy agent stacks are accumulating technical debt in the form of latent context consumption.
*Implication:* Audit your MCP stack. Replace with CLIs wherever available (GitHub CLI, Vercel CLI, Google Workspace CLI cited as ready alternatives).

**5. Hooks enable deterministic skill invocation — solving Claude Code's biggest UX failure.**
`[43:44–46:45]` | Skills auto-invocation is described as "really finicky" and unreliable. The fix: a `PreToolUse` hook running a keyword-matching script that fires before every message, bypassing LLM routing entirely.
*Why it matters:* Every user of Claude Code who has built skills has encountered this failure. The hook solution is non-obvious and practically eliminates the problem.
*Implication:* Any production Claude Code workflow with skills should implement keyword-matching hooks as table stakes.

**6. The "ask user questions" tool flips the input/output dynamic.**
`[24:06–27:30]` | Rather than engineering a perfect prompt upfront, this tool has Claude generate structured question UI in-session, dynamically identifying its own knowledge gaps. One user received 67 questions.
*Why it matters:* This reduces the cognitive burden of prompt engineering and improves output quality by surfacing assumptions Claude is making.
*Implication:* Use this as a standard step before any high-stakes output (PRD, analysis, presentation) rather than iterating on bad outputs.

**7. The builder-validator pattern dramatically improves visual output quality.**
`[42:35–43:30]` | Requiring 3 self-iterations with screenshot validation before presenting output (make-slides skill) improves quality more than any single-pass prompt refinement. A Google paper on prompt repetition is cited as supporting evidence.
*Why it matters:* The pattern is generalizable: build → validate against original spec → rebuild. This applies to any output type, not just slides.
*Implication:* Encode "validate against your original instructions" as a mandatory final step in all production skills.

**8. Jupyter notebooks solve the AI data trust problem by making computation auditable.**
`[47:55–55:00]` | The core PM objection to AI data analysis is not accuracy — it is traceability. Jupyter notebooks expose every query, every transformation, every result in a reproducible, shareable format.
*Why it matters:* This converts AI analysis from a black box into a peer-reviewable artifact, which is the bar required for executive-level decision-making.
*Implication:* Mandate Jupyter notebook output for any data analysis task in a PM workflow. Never accept raw text summaries of data.

**9. The people folder is an underutilized relationship intelligence layer.**
`[56:27–58:14]` | Maintaining a per-person dossier (communication preferences, stated priorities, meeting notes via Granola MCP) in a `/knowledge/people` folder creates compounding context quality for every stakeholder communication.
*Why it matters:* This operationalizes relationship context in a way that no CRM has successfully done for individual contributors.
*Implication:* Build a skill that auto-updates people files after every meeting transcript.

**10. CLAUDE.md is a persistent system prompt — the highest-leverage configuration file.**
`[63:54–64:53]` | Unlike other files, CLAUDE.md is in context for every message in every session. It functions as a standing instruction set — persona, company context, working style preferences.
*Why it matters:* Most users treat CLAUDE.md as a one-time setup. It should be treated as a living document iterated weekly.
*Implication:* Add a standing prompt at the end of every CLAUDE.md: "After every session, suggest one update to this file based on what you learned."

**11. Control+B backgrounding enables true async multi-agent workflows.**
`[23:06–23:39]` | Sub agents can be sent to the background (Ctrl+B) while the main session continues. The result injects automatically when complete.
*Why it matters:* This enables parallelism that most users don't realize is available, dramatically compressing total task time.
*Implication:* For any workflow with independent parallel tasks (research + drafting, analysis + visualization), use background agents as default.

**12. Skill security is an unresolved trust problem in the Claude Code ecosystem.**
`[20:50–21:13]` | Third-party skill marketplaces contain documented malware and prompt injection attacks. The risk is amplified when running `--dangerously-skip-permissions`.
*Why it matters:* Enterprise adoption of Claude Code skills from public marketplaces is a live security risk, not a theoretical one.
*Implication:* Establish a skills governance policy before deploying in enterprise contexts. Source only from verified vendors or build in-house.

---

## STEP 2C — DEEP TIME-CODED BREAKDOWN

---

### Section 1: Claude Code vs. Co-work/OpenClaw — Strategic Positioning

**Timestamp:** `[00:00–06:25]`

**Content:**

1. Claude Code is framed as the foundational layer; co-work and OpenClaw are described as UIs or constrained interfaces built on top of it. Co-work adds file management UI but reduces power. OpenClaw adds always-on monitoring and heartbeat features but is not suitable for "driver's seat" work.

2. The guest has been using Claude Code 8–10 hours/day for 6–8 months. This is a practitioner's perspective, not a reviewer's. The depth of tactical knowledge presented is consistent with this claim.

3. The episode is explicitly positioned as a "mastery layer" — assuming prior completion of beginner and advanced episodes. The audience is already using Claude Code but hitting friction.

4. Four friction areas announced: context management, skill gaps (research, UI, slides), output trust (data analysis), and system cohesion.

5. The $2.5B / 9-month revenue claim is stated as fact by the host with no source attribution. This is the fastest B2B software product ramp "in history" — a strong claim that warrants scrutiny.

**Key Quote:** *"If you need the person doing the most powerful work that you can, you really have to be in Claude Code."* — Carl Vatti

**Hidden Assumption:** That "power" = CLI-level control. Users who prioritize collaboration, UX, or auditability may find co-work or similar GUI tools more appropriate. The framing conflates power-user needs with universal needs.

**Why It Matters for Strategy Leaders:** The competitive framing (Claude Code > co-work > OpenClaw) implies Anthropic is winning the developer/power-user segment by not constraining the raw interface. This is a deliberate product strategy choice with parallels to Vim vs. VS Code debates — the raw tool retains a loyal high-power segment indefinitely.

**Risk:** The guest has direct commercial interest in Claude Code adoption (course at cc4pms.com, newsletter). This creates incentive alignment bias in the competitive framing.

---

### Section 2: Context Management — Status Line, Sub Agents, Rollback

**Timestamp:** `[06:26–23:50]`

**Content:**

1. `/statusline` is a customizable UI element in Claude Code's terminal interface. It can display model name, working directory, and a color-coded context gauge. It is built by Claude itself from a natural language description via `/statusline [description]`.

2. `/context` reveals a breakdown of what is consuming context: system prompt (~2%), enabled tools/MCPs (~8%), conversation history, and loaded files. Baseline consumption before any user message was 16% in the demo — primarily from active MCPs.

3. Sub agents in Claude Code work by spawning an isolated instance of Claude (a "clone") that executes a task within its own context window, returning only the result to the parent session. This is not a separately configured service — Claude can spin one up ad hoc when instructed.

4. The demonstrated savings: research task without sub agent ~25% context; with sub agent ~16.5%. The sub agent internally consumed 10 tool uses and ~30,000 tokens — none of which appeared in the main session.

5. Double-escape rollback allows reverting the session to any prior message state, literally erasing subsequent context and tool calls. This is a destructive operation with no undo.

6. Context guard skill: dynamically evaluates whether a task should run in-session or be delegated, classifying tasks by context intensity before execution.

**Key Quote:** *"When you understand how Claude works, you can kind of tell it how to operate itself, which really just levels up and makes it feel less like you're just prompting Claude and watching it and more like you understand how it works and you're working together."*

**Example:** Research task "top 5 Claude Code tips from this week" — without sub agent fills context with 10 search calls + page reads; with sub agent, main session sees only the summary.

**Hidden Assumption:** Sub agent spawning is reliable and deterministic. In practice, Claude does not always choose to use sub agents even when prompted — the guest acknowledges this ("oftentimes it will not do it when it would be a good idea"). The `context guard` skill is a patch for non-deterministic behavior.

**Why It Matters:** Context budget management is the primary lever for session longevity and output quality. Any team deploying Claude Code for extended workflows without sub agent architecture is running a degrading session.

**Risk:** Rolling back context is a destructive operation. In team or shared environments, accidental rollbacks could erase significant work with no recovery path.

---

### Section 3: Skills Architecture — Ask-User-Questions, Front-End Design, Skill Creation

**Timestamp:** `[23:51–32:10]`

**Content:**

1. Skills in Claude Code are markdown files with a defined structure: name, description, trigger keywords, and instructions. They live in a `/skills` directory and are either project-level (in repo) or computer-level (installed from marketplace).

2. Creating a skill is done in natural language: "Please make a new skill that helps me tell you when you should use dedicated sub agents instead of the main session." Claude creates the file, names it, and it is immediately available without restart (recent Anthropic update).

3. The `ask user questions` tool generates a structured multi-choice or open-ended question UI directly inside the Claude Code terminal. Claude dynamically generates the questions based on context gaps. This is not a user-configured template — it is Claude predicting what it needs to know.

4. The front-end design plugin (Anthropic official, one of 56 official plugins) improves output quality not through new capabilities but through a well-structured design heuristics prompt. Side-by-side comparison: generic AI purple-gradient page vs. clean, personality-driven page.

5. Skills installed from marketplace go to a computer-level directory (outside the repo), reducing portability but enabling cross-project reuse.

**Key Quote:** *"What I think is so amazing about this skill is that it actually doesn't give Claude Code any specific new abilities. All it is is just a really good prompt."*

**Example:** Front-end design skill output for "Claude Code School" landing page — before skill: generic AI aesthetic; after skill: clean, branded, differentiated.

**Hidden Assumption:** "A really good prompt" is transferable and generalizable. In practice, design heuristics are subjective and context-dependent. The front-end design skill will not produce universally "better" output — it will produce output that aligns with whoever wrote the skill's aesthetic preferences.

**Why It Matters for Product Leaders:** The skills architecture is the mechanism for encoding institutional knowledge into Claude. A PM who builds skills for their domain expertise is building a compounding asset. A PM who doesn't is permanently dependent on generic model behavior.

**Risk:** Skills created by different team members may conflict or overlap, creating inconsistent behavior. No skill governance framework is discussed.

---

### Section 4: Tool Integration — MCPs vs. CLIs, Web Research Skill

**Timestamp:** `[32:11–41:55]`

**Content:**

1. MCPs (Model Context Protocol servers) consume context tokens passively — just by being enabled, they occupy space in the context window. Demonstrated: Tavily MCP consumes "a couple thousand tokens just by existing."

2. CLIs (Command Line Interfaces) are installed at the machine level and invoked by the agent only when needed. Zero passive context cost. Claude is described as "aggressively competent" at CLI usage.

3. Andrej Karpathy cited as endorsing CLI preference. Hierarchy: MCP (bottom, high passive context cost) → API → CLI (top, zero passive context cost, machine-native).

4. CLIs cited as available for: GitHub, Vercel, Google Workspace (alternative to the notoriously difficult Google Workspace MCP). Prediction: CLI tools will proliferate over the next year as AI adoption grows.

5. Web research skill combines Tavily (high-quality semantic search, generous free tier) + Firecrawl (clean markdown scraping, installed as CLI to avoid context bloat). The combination addresses the core weakness of Claude's default web search: low-quality SEO content from first-page Google results.

**Key Quote:** *"If you just say, 'Hey Claude, does a CLI for this exist?' More often than you'd probably guess, the answer is yes."*

**Hidden Assumption:** CLIs are always preferable. This ignores cases where MCPs provide richer bidirectional integration (e.g., live database writes, webhook subscriptions) that CLIs cannot replicate. The preference for CLIs is primarily driven by context efficiency, not capability superiority.

**Why It Matters for AI Builders:** Any agent architecture that uses MCPs for tool access should benchmark context consumption against CLI equivalents. The passive context cost of MCPs may be the hidden driver of quality degradation in production agentic systems.

**Risk:** CLIs typically have less error handling, less documentation, and less community support than MCP integrations. In enterprise environments, CLI dependency management adds DevOps complexity.

---

### Section 5: Auto-Invocation via Hooks; Make-Slides Skill; Builder-Validator Pattern

**Timestamp:** `[41:56–55:30]`

**Content:**

1. Skill auto-invocation via trigger keywords in skill definitions is described as "really finicky" and unreliable in practice. The root cause: Claude's LLM routing for skill selection is non-deterministic.

2. Hooks are lifecycle event handlers in Claude Code. Available hook points: user prompt submit, tool use, message return, pre/post compaction. Hooks run code (scripts) at these lifecycle points, bypassing LLM routing for deterministic behavior.

3. The fix for auto-invocation: a `PreUserPromptSubmit` hook runs a keyword-matching script on every user message. If keywords match any skill's trigger list, the skill is surfaced to the LLM with a "now is the time to use this" signal. The LLM then makes the final decision — but with explicit context, not inference.

4. Make-slides skill architecture: natural language design heuristics (similar to front-end design skill) + Puppeteer integration for screenshot capture + overflow detection script. The skill instructs Claude to: render HTML → screenshot → measure text overflow → iterate minimum 3 times.

5. Builder-validator pattern: after building, Claude re-checks its output against the original skill instructions. Google paper cited (unnamed): pasting a prompt twice improves output. Mechanism: forces re-evaluation against constraints rather than forward continuation.

**Key Quote:** *"You must iterate three times before you show me. It'll be much better than if you say, 'Oh, just go until you're done.'"*

**Hidden Assumption:** Three iterations is the right number universally. This is heuristic, not derived. The optimal iteration count likely varies by task complexity, output type, and model capability. "Iterate until done" failure mode may be a prompting issue, not an inherent model limitation.

**Why It Matters for AI Builders:** The hooks-based auto-invocation fix is a pattern applicable to any system where LLM routing of tool/skill selection is unreliable. Using deterministic code to narrow the decision space before LLM routing is a general architectural principle.

**Risk:** Hooks running scripts on every user message add latency to every interaction. For high-frequency use, this could meaningfully degrade responsiveness. No latency benchmarks discussed.

---

### Section 6: OS Layer — Folder Structure, Jupyter Analysis, Standup Skill, CLAUDE.md

**Timestamp:** `[55:31–66:01]`

**Content:**

1. Recommended OS folder structure: `/knowledge` (static reference — company info, people dossiers, research), `/projects` (active work with all related artifacts), `/data` (CSV, analysis outputs), `/tasks` (current work + backlog in markdown), `/tools` (pre-built scripts for recurring operations), `/skills` (custom skill definitions), `CLAUDE.md` (persistent system context).

2. People folder: per-person dossiers capturing communication preferences, priorities, meeting notes. Integration with Granola (meeting transcriber with MCP) enables auto-updating people files after meetings. This creates compounding relationship intelligence.

3. Jupyter notebooks: standard data science artifact. Renders natively in VS Code/Cursor. Enables traceable, reproducible analysis — every query, transformation, and visualization is documented in the notebook, not buried in conversation history.

4. Demonstrated analysis: 23-row survey dataset → distribution charts → correlation heatmap. Correlation heatmap revealed: enterprise interest correlates positively with security and team management features; negatively with pricing sensitivity. *(Demo data, not real data — treat as illustrative only.)*

5. Standup skill: aggregates GitHub activity, Linear tickets, tasks file, calendar into a single briefing. The compounding value: as more data sources are connected, the briefing improves without additional user effort.

6. CLAUDE.md as persistent standing instruction: always in context, every message. Should include: who you are, what you're working on, how you like Claude to behave, what tools are available in `/tools`.

**Key Quote:** *"When I say I'm living in Claude Code all day — once you get to a certain point, it's like, 'Oh my gosh, I do not want to have to leave Claude Code.'"*

**Hidden Assumption:** The folder structure scales to individual power users. For teams, this architecture has no stated synchronization, versioning, or access control mechanism. The "people folder" containing sensitive notes about colleagues has privacy and legal implications not discussed.

**Why It Matters:** The OS-layer framing is the most strategically significant concept in the video. It repositions Claude Code from a task tool to a personal knowledge operating system with compounding value — similar to how Notion or Obsidian became infrastructure for knowledge workers.

**Risk:** The people folder/dossier concept creates potential HR, privacy, and legal exposure if used in enterprise contexts without proper data governance. No warning is given.

---

---

# STEP 3 — STRUCTURED EXTRACTION TABLES

## 1. Claims Table

| Claim | Evidence Presented | Evidence Type | Strength | Commentary |
|---|---|---|---|---|
| Claude Code hit $2.5B ARR in 9 months | Stated by host as fact | Assertion — no source cited | Weak | Plausible directionally (Anthropic has reported strong growth) but specific figure is unverified. Treat as directional signal, not confirmed metric. |
| Fastest B2B software product ramp in history | Stated by host | Opinion / assertion | Weak | Extraordinary claim with no comparative data. GitHub Copilot, Salesforce, Workday all had rapid ramps. Unverifiable without sourcing. |
| Sub agents reduced context from 25% to 16.5% on a web research task | Live demo | Anecdote / demonstration | Medium | Single task, single session. Not a controlled experiment. Directionally credible but not generalizable without testing. |
| MCPs consume context passively just by being enabled | Live `/context` output | Demonstration | Strong | Directly observable in the demo. Tavi MCP showed "a couple thousand tokens" passive consumption. |
| CLIs preferred over MCPs per Andrej Karpathy | Speaker attribution | Opinion (cited) | Medium | Directionally credible — Karpathy has publicly written about CLI preferences for AI tooling. Exact quote not provided. |
| Auto-invocation of skills via trigger keywords is "really finicky" | Speaker assertion + demo failure reference | Opinion + anecdote | Medium | Consistent with widely reported user experience. Not formally benchmarked. |
| Google paper shows pasting a prompt twice improves output | Speaker citation | Data (cited, unnamed) | Medium | Likely refers to real research on prompt repetition effects. Paper not named; cannot verify exact claim. |
| Skills can contain prompt injection / malware in third-party marketplaces | Speaker warning | Assertion | Medium-High | Security research community has documented this broadly. Credible warning. |
| Context rot is a measured phenomenon | Host assertion | Data (claimed, no source) | Medium | Academic research on long-context degradation exists (e.g., "Lost in the Middle" paper by Liu et al., 2023). Specific framing as "measured" is accurate. |
| Builder-validator pattern improves output quality | Speaker assertion | Opinion | Medium | Consistent with broader LLM research on self-correction and reflection prompting. Not specifically demonstrated in demo. |

---

## 2. Metrics & Numbers Table

| Metric | Value | Context | Implication | Reliability |
|---|---|---|---|---|
| Claude Code ARR | $2.5B | Annualized, 9-month ramp | Signals massive enterprise adoption; fastest B2B ramp claimed | Low — no source cited |
| Baseline context at session open | ~16% | With MCPs + tools enabled, before any user message | Significant passive context drain from tooling | Medium — single demo session |
| System prompt passive cost | ~2% | Always-on | Irreducible floor cost per session | High — structural |
| MCPs + custom agents passive cost | ~8% | At time of demo | Measurable, avoidable overhead | Medium — config-dependent |
| Context cost with sub agent (research task) | 16.5% | After full web research task | Near-zero incremental cost vs. 25% without | Medium — single task demo |
| Context cost without sub agent (research task) | ~25% | Web research in main session | ~9% per research task savings from sub agents | Medium — self-reported testing |
| Sub agent internal tool calls | 10 | For web research task | Volume of work absorbed by sub agent | High — directly logged |
| Sub agent token consumption | ~30,000 | For web research task | All isolated from main session context | High — directly logged |
| Anthropic official plugins | 56 | At time of recording | Anthropic is building a skills ecosystem | Medium — likely current at time of recording |
| Survey dataset size | 23 rows | Demo data, fictional company | Illustrative only | N/A — demo data |
| Maximum questions from ask-user-questions | 67 | Twitter report, cited by speaker | Tool scales to complex vague starting points | Low — single anecdote |

---

## 3. Frameworks / Mental Models

| Framework | Explanation | Origin | Where It Applies | Limits |
|---|---|---|---|---|
| Context Engineering > Prompt Engineering | The quality of AI output is determined more by what information is in context (and what is excluded) than by how the prompt is worded | Widely attributed in AI community; popularized by Andrej Karpathy and others | All LLM-based workflows; especially multi-step agent tasks | Does not address cases where the right context is unknown in advance |
| Context as a Budget | Context window is a finite resource to be allocated, not an infinite scratchpad. Passive costs (MCPs, system prompt) reduce available budget