# I built a custom Slack inbox. It was easier than you think. | Yash Tekriwal (Clay)

**Channel:** howiaipodcast
**URL:** https://www.youtube.com/watch?v=tvD1LY4InIk
**Published:** 2026-04-08
**Analyzed:** 2026-04-08 22:54

---

# Research Brief: "I Built a Custom Slack Inbox" — How I AI Podcast featuring Yash Tekriwal (Clay)

**Video URL:** https://www.youtube.com/watch?v=tvD1LY4InIk
**Published:** 2026-04-08
**Runtime:** ~44 minutes
**Transcript Quality:** Good. Conversational, minor disfluencies, no gaps. Single-segment video, no strong 30-minute breakpoint requiring full section repeat — this brief covers the full video with proportional depth.

---

## STEP 1 — Transcript Handling

### Segment Map

| Cluster | Timestamp Range | Topic |
|---|---|---|
| 1 | [00:00]–[06:05] | Problem framing: Slack notification overload; initial mental model for triage |
| 2 | [06:06]–[14:01] | OpenClaw + Discord: Building deterministic Slack digest via API; first prototype |
| 3 | [14:02]–[23:47] | Perplexity Computer: Why it was chosen; multi-model orchestration; Slack dashboard UI |
| 4 | [23:48]–[35:13] | SaaS debate; broader daily briefing app; Clay University prototype; team use cases |
| 5 | [35:14]–[44:08] | Lightning round: Fun AI uses, prompting strategies, closing |

**Speakers:**
- **Claire Vo** — Host, product leader, AI obsessive
- **Yash Tekriwal** — Head of Education, Clay; guest

**Topic Transitions:** Clearly marked. Hard shift at [14:02] from "how it was built" to "why Perplexity Computer." Second shift at [23:48] into SaaS commentary. Final shift at [35:14] into personal use and prompting philosophy.

---

## STEP 2 — Strategic Synthesis

### A. Executive Summary

**Core Thesis:**
Knowledge workers drowning in notification overload can now build bespoke, AI-assisted productivity tools — not by replacing existing SaaS, but by wrapping it with personal interfaces — and this signals a broader structural shift in how software gets built and consumed at the individual and small-team level.

---

**Primary Arguments:**

**1. Not all notifications are created equal, but SaaS treats them as if they are.**
Yash receives 100–150 Slack notifications daily. His claim: 60–80% are FYIs requiring no action. The signal-to-noise failure is a product design problem, not a user behavior problem. SaaS vendors optimize for engagement breadth, not user cognitive load.
> *[Fact stated by guest, plausible, unverified externally]*

**2. AI has two distinct modes of value in productivity systems: doing the task vs. building the tool.**
Yash explicitly distinguishes between using AI as a runtime intelligence layer (categorizing FYI vs. action-required) versus using AI as a construction assistant to build deterministic code. The final system is mostly deterministic code; AI is only in the categorization layer.
> *[Fact stated by guest; analytically important distinction]*

**3. Perplexity Computer's multi-model orchestration and cloud-native connector architecture make it meaningfully differentiated from Claude Code or Codex for non-technical builders.**
Unlike single-model code agents, Perplexity Computer routes subtasks to different models (Sonnet 4.6 for fetching, Gemini for planning and Python coding, Opus for intensive reasoning), runs tasks in parallel, and reuses pre-authorized OAuth connectors across apps and deployed tools.
> *[Fact stated; partially verifiable — Perplexity's multi-model architecture is publicly documented]*

**4. The "SaaS is dead" debate misframes the actual opportunity — the opportunity is the long tail of customization SaaS vendors will never serve.**
The real shift is not SaaS disappearing but personal and micro-scale software becoming economically viable. Yash articulates a vision where someone watches this video, builds a $15/month Slack digest product, and captures a real market.
> *[Speaker opinion + interpretation: this is an emerging thesis visible across multiple practitioner conversations in 2025–2026]*

**5. The anti-to-do list is a forcing function for automation prioritization.**
Rather than asking "what can AI do?", the more powerful question is "what do I most want to never do manually again?" This reframes AI adoption from exploration to elimination.
> *[Speaker framework; original framing by Claire Vo]*

---

**Quantitative Insights:**
- 100–150 Slack notifications per day (Yash's personal volume)
- 60–80% estimated as FYI/no-action-required
- Net actionable: 30–40 per day
- First prototype took ~1 full day of back-and-forth with OpenClaw
- 80% of the final UI was built in the first 4 messages to Perplexity Computer
- 20 people attended personal Winter Olympics; logistics managed with AI
- $15/month cited as viable price point for a Slack digest micro-SaaS

---

**Key Examples:**
- Slack digest tool: deterministic code + AI categorization → Kanban-style dashboard with red/yellow/green columns, deep links, archive-all for FYIs
- Daily briefing app: consolidates Slack, email, news into a single command center
- Clay University prototype: persona-based learning path UI built from existing site via browser access, used to communicate with design team
- Winter Olympics event: AI-assisted activity brainstorming and team rotation logistics

---

**Strategic Implications:**

1. **For SaaS companies:** The addressable surface for churn-adjacent dissatisfaction is growing. Users who can build personal wrappers will tolerate core products longer but will route around bad UX — this both extends SaaS runway and suppresses premium upsell opportunity.
2. **For micro-SaaS founders:** AI lowers the cost of building niche workflow tools to near zero. TAM constraints that would have killed these ideas under VC models are now irrelevant.
3. **For AI platform companies:** The "connector/OAuth moat" is real. Perplexity's advantage here is framed as significant. This is a strategic surface worth watching.
4. **For PMs:** The anti-to-do list is a usable internal framework for automation roadmapping.

---

**What Changed vs. Conventional Wisdom:**

| Conventional Wisdom | Updated View from This Video |
|---|---|
| You need engineers to build internal tools | A non-engineer can build a production-quality personal tool in a day |
| AI agents replace deterministic code | The best systems are hybrid: AI for judgment, deterministic code for structure |
| SaaS customization happens through APIs and enterprise features | Personal-layer customization via AI agents is now viable for individuals |
| Prompting is a soft skill | Prompting strategy is a systems engineering decision (when to use MCP vs. deterministic code) |

---

**Explicit Separation:**

| Type | Examples from Video |
|---|---|
| **Facts stated** | Yash gets 100–150 daily Slack notifications; Perplexity Computer uses Sonnet, Gemini, Opus; OpenClaw used in Discord for threading |
| **Speaker opinion** | "60-80% are FYI"; "Perplexity Computer is better than Claude Code for this use case"; "SaaS won't die, it'll get wrappers" |
| **My interpretation** | The OAuth/connector moat framing as a platform strategy signal; the anti-to-do list as a PM framework applicable beyond personal productivity |

---

### B. Key Insights Expansion

**1. The FYI ratio is the key productivity unlock, not the total notification count.**
`[00:10]–[00:18]`
If 60–80% of "urgent-feeling" notifications require no action, the first design problem is classification, not volume reduction. **Why it matters:** Most notification management tools focus on volume (mute, snooze). The real opportunity is intelligent triage. **Implication:** Any inbox tool that doesn't classify by required action type is solving the wrong problem.

---

**2. Distinguish AI-as-runtime from AI-as-construction-tool — they require different architectures.**
`[11:00]–[11:32]`
The Slack digest uses AI only for categorization at runtime; all structural logic is deterministic code. **Why it matters:** Most practitioners conflate these modes, leading to brittle, over-AI-dependent systems. **Implication:** System design should start by asking "where does judgment belong?" before choosing AI vs. code.

---

**3. Perplexity Computer's multi-model ensemble is a structural differentiator, not a feature.**
`[13:14]–[14:01]`
Routing subtasks to appropriate models (Gemini for planning, Opus for heavy reasoning, Sonnet for fetch) without user direction reduces reprompting loops. **Why it matters:** Single-model agents create bottlenecks where the model's weaknesses block the task. **Implication:** Orchestration architecture is becoming a competitive moat for AI agent platforms.

---

**4. Cloud-native OAuth reuse across built apps is an underappreciated UX and developer experience advantage.**
`[30:44]–[31:15]`
In Claude Code or Codex, OAuth must be set up from scratch per project. Perplexity Computer reuses connector authentication across both interactive use and deployed apps. **Why it matters:** Friction in auth setup is a real barrier to adoption for non-technical users. **Implication:** Platforms that solve credential portability will win the personal AI agent market.

---

**5. The anti-to-do list reframes automation from "what's possible" to "what's intolerable."**
`[24:18]–[25:07]`
Claire Vo's framework: write down the things you never want to do manually again, then systematically eliminate them. **Why it matters:** It converts vague AI enthusiasm into concrete, prioritized automation projects. **Implication:** PMs and ops leaders should run anti-to-do list workshops as part of AI adoption programs.

---

**6. The micro-SaaS emergence thesis: TAM constraints don't apply when build cost approaches zero.**
`[22:43]–[23:33]`
A $15/month Slack digest product with a small TAM is now viable because a single developer can build and maintain it. **Why it matters:** Venture logic has historically killed products with small TAMs. AI collapses the cost structure that made those decisions rational. **Implication:** Incubators and accelerators need new evaluation criteria — "useful at small scale" is now a legitimate category.

---

**7. Perplexity Computer defaults to Kanban-style UIs — a signal about training data or design bias.**
`[27:30]–[27:34]`
Yash notes that Computer "seems to default to Kanban style pretty UIs." **Why it matters:** AI-generated interfaces have implicit aesthetic biases baked in from training. **Implication:** Product teams using AI to prototype UIs should explicitly specify design systems or risk convergent, undifferentiated outputs.

---

**8. Browser access enables visual context ingestion that text-only agents cannot replicate.**
`[33:44]–[34:54]`
Perplexity Computer accessed Clay University's existing site visually and used that context to build a design-consistent prototype. Figma Make could not do this without re-describing all design elements. **Why it matters:** Visual context is a major gap in most AI coding agents. **Implication:** Browser-native agents have a structural advantage for design-adjacent prototyping tasks.

---

**9. Discord's threading model is a superior personal agent interface vs. Telegram.**
`[09:18]–[09:41]`
Yash chose Discord over Telegram for OpenClaw because of threading + Command K search. **Why it matters:** The interface where you manage your AI agent affects how you maintain context across long projects. **Implication:** Agent interface design (thread management, search, context preservation) is an underserved UX problem.

---

**10. Iterative skill refinement via self-interrogation is more effective than reprompting.**
`[42:26]–[42:52]`
When an AI skill fails repeatedly, Yash asks the model to explain its reasoning, then asks what's missing from the skill definition, then provides the correct answer. **Why it matters:** This is a structured feedback loop that improves system behavior over time, not just session behavior. **Implication:** AI skill maintenance should be treated as a product discipline, not an ad hoc fix.

---

**11. Emotional prompting (threats, urgency) has anecdotally measurable effect on output quality.**
`[41:36]–[43:10]`
Yash uses all-caps, extreme negative consequence framing to improve model compliance. He acknowledges the mechanism is likely reward specification in training. **Why it matters:** This is a widely observed but underexplored prompting pattern. **Implication:** The effect — if real — suggests models have learned to associate urgency signals with higher-effort responses, which is a training incentive alignment issue worth examining.
> *[Speaker anecdote; not externally validated; treat as hypothesis]*

---

**12. The design-engineering communication gap is a use case for AI prototyping, not just AI building.**
`[34:40]–[34:56]`
The Clay University prototype's primary value was not the output itself but as a communication artifact between non-designers and the design team. **Why it matters:** Much of the friction in product development is translation loss between stakeholders. **Implication:** AI prototyping tools should be evaluated on their communication value, not just their build accuracy.

---

### C. Deep Time-Coded Breakdown

---

#### Section 1: Problem Framing — Slack Notification Overload
**Timestamp:** [00:00]–[06:05]

**Content:**
1. Yash receives 100–150 tagged Slack notifications daily (DMs, group DMs, threads, channel @mentions) — not passive unreads.
2. He estimates 60–80% require no response, making net actionable notifications 30–40.
3. The problem is not notification volume but uniform urgency signaling — Slack treats a dog photo tag identically to a scheduling DM.
4. His desired taxonomy: four notification types (DMs, group DMs, threads, @mentions) × three priority levels (action required, need to read, FYI) = 12 buckets.
5. The framework insight: "envision what a better world looks like" before going to AI — design intent precedes tooling.

**Important Quote:**
> "Not all notifications are created equal in Slack... I get an equal notification for both [a scheduling DM and a dog photo tag]." — Yash Tekriwal [~03:48]

**Examples Discussed:** Dog photo in fun channel vs. scheduling a podcast recording — equal Slack notification weight.

**Hidden Assumptions:**
- Assumes the user has stable, consistent intuitions about notification priority (not everyone does)
- Assumes Slack's API exposes sufficient metadata to make these distinctions programmatically

**Why This Matters for Product/Strategy Leaders:**
Notification design is a UX debt problem that compounds at scale. The fact that a Head of Education at a growth-stage company needs to build custom tooling to manage their communication inbox is an indictment of enterprise SaaS notification design. This is a design pattern problem, not an AI problem.

**Risk/Limitation:** The 60–80% FYI estimate is self-reported and context-specific to Yash's role. For a different role (e.g., on-call engineer, support lead), this ratio inverts — making this framework potentially harmful if applied universally.

---

#### Section 2: First Prototype — OpenClaw + Discord + Slack API
**Timestamp:** [06:06]–[14:01]

**Content:**
1. Yash chose OpenClaw (an AI agent running in Discord) as his coding assistant, preferring Discord's threading + Command K search over Telegram.
2. Rather than using AI to categorize at runtime, he used AI to write deterministic code that queries the Slack API for unread notifications filtered by timestamp and message type.
3. The prototype took approximately one full day of iterative back-and-forth — "thousands of messages" — to correctly handle Slack's timestamp-based read/unread logic.
4. Output: A "Jarvis digest" channel in Slack that posts a grouped, bucketed list of unreads on demand, organized into four notification type buckets.
5. Used this text-based digest for one week before deciding the UX was still insufficient — too much scrolling, cognitively draining.

**Important Quote:**
> "Pretty much all of what you just described, while built with AI, the only place in which AI is repeatedly used in the system that was constructed is in the categorization of messages that need action from me." — Yash Tekriwal [~10:50]

**Examples Discussed:** Slack's notification stream metadata; timestamp-based unread logic; Jarvis digest channel output.

**Hidden Assumptions:**
- Assumes Slack's API endpoints are stable and won't deprecate the fields being queried (historically, Slack has changed API behavior)
- Assumes the user can maintain or update custom code when Slack changes — this is a real maintenance burden

**Why This Matters for Product/Strategy Leaders:**
This section demonstrates the "vibe coding for ops" pattern: non-engineers are now capable of building functional internal tools using AI coding assistants, but the resulting tools carry engineering debt. Organizations need to think about who owns and maintains AI-built internal tooling.

**Risk/Limitation:** A one-day build with thousands of back-and-forth messages is not trivially replicable by most users. The guest is technically sophisticated. This may be presented as more accessible than it is.

---

#### Section 3: Perplexity Computer — Why It Was Chosen; What It Does
**Timestamp:** [14:02]–[19:51]

**Content:**
1. Three cited advantages of Perplexity Computer over Claude Code/Codex: (a) parallel task execution, (b) cloud-native connector architecture with OAuth reuse, (c) multi-model orchestration.
2. Multi-model routing observed: Sonnet 4.6 for fetching, Gemini for planning and Python coding, Opus for intensive reasoning — all without user direction.
3. Perplexity Computer is framed as more than a code generator — it functions as a cloud agent that natively connects to SaaS tools without per-project auth setup.
4. 80% of the final Slack dashboard UI was generated in the first 4 messages to Computer.
5. Connectors in active use: Google Drive, Gmail, Calendar, Notion, Asana, Slack, Forms, Tasks, Typeform, Zoom, Airtable, Google Slides.

**Important Quote:**
> "They are shameless about using all of the different AI models to build each part of the task in subsequent order." — Yash Tekriwal [~13:23]

**Examples Discussed:** Parallel task kickoff (4 tasks in 10 minutes); Notion meeting notes → action items pipeline; Computer self-correcting on OAuth failures.

**Hidden Assumptions:**
- Assumes multi-model orchestration actually produces better outcomes than single-model — not systematically validated in the video
- "Shameless" multi-model use could also mean inconsistent behavior across sessions as models update
- Cloud-native execution means user data (emails, Slack messages, meeting notes) is being processed by Perplexity's infrastructure — security/compliance implications not discussed

**Why This Matters for Product/Strategy Leaders:**
The connector/OAuth moat claim is significant. If Perplexity has solved cross-app authentication persistence in a way that Claude Code hasn't, this is a genuine product moat — not a feature. Platform companies should evaluate whether this is replicable or structural.

**Risk/Limitation:** Perplexity is a search company evolving into an AI agent platform. This is not their core competency. The connector ecosystem may lag behind or become a liability as it scales.

---

#### Section 4: The Slack Dashboard UI + SaaS Debate
**Timestamp:** [19:52]–[23:47]

**Content:**
1. Final product: A Kanban-style dashboard with three columns (Red: action required, Yellow: need to read, Green: FYI), left sidebar filtered by notification type (DMs, group mentions, threads).
2. "Archive all" button for FYIs syncs back to Slack — marking them as read and removing from Slack notification count.
3. Deep links from each card into the actual Slack message — enabling action without context-switching to raw Slack.
4. Debate framing: "Is SaaS dead?" reframed as "SaaS core + personal customization layer."
5. Yash's prediction: explosion of micro-SaaS products and low-TAM businesses that are economically viable because build costs collapsed.

**Important Quote:**
> "My dream is for someone else to watch this video and say, 'I want to build that app on top of Slack.' And then I can go pay that person $15 a month." — Yash Tekriwal [~01:00]

> "SaaS can then acquire all those people." — Yash Tekriwal [~23:53]

**Examples Discussed:** Slack's "mark all as read" limitation; Superhuman as the model UX reference; $15/month micro-SaaS price point.

**Hidden Assumptions:**
- Assumes Slack's API will continue to support the read/archive state mutation being used — platform risk
- Assumes the market for a Slack digest product is large enough to sustain a $15/month business — unvalidated
- The "SaaS acquires micro-apps" thesis assumes large companies want to acquire long-tail tools, which historically has low success rates

**Why This Matters for Product/Strategy Leaders:**
The Superhuman reference is telling. Superhuman's thesis was: email is broken, pay $30/month for a better experience. That worked for a specific high-income professional segment. The same logic applies here. The question is whether the TAM supports even a lifestyle business, let alone a VC-backed one.

**Risk/Limitation:** Build-it-yourself tools have a maintenance burden. The $15/month expectation includes bug fixes, Slack API compatibility, and feature iteration — which is non-trivial even with AI assistance.

---

#### Section 5: Broader Daily Briefing App + Clay University Prototype + Team Usage
**Timestamp:** [23:48]–[35:13]

**Content:**
1. Second app built: a consolidated daily briefing pulling from Slack, email, and news — also rendered as a Kanban-style dashboard with deep links.
2. Iterative build process: text first → validate categorization → add UI → add deep links.
3. Clay University use case: Chris Ming (team member) used Perplexity Computer to prototype a persona-based learning path UI by having Computer visually parse the existing website and redesign it with SDR/BDR/RevOps/Marketing Ops/GTM Engineer tracks.
4. Key insight: prototype was used as a communication tool with the design team, not as a production asset.
5. Shareable URL feature of Perplexity Computer cited as a key differentiator over Claude Code outputs.

**Important Quote:**
> "The gap or the chasm in communication between design and any other stakeholders... being able to build a visual bridge between those two is incredibly valuable." — Yash Tekriwal [~34:43]

**Examples Discussed:** Newspaper-style briefing idea (from X); Notion AI meeting transcripts → action items pipeline; Sarah Chen persona mockup in Clay University prototype.

**Hidden Assumptions:**
- Assumes design teams will accept AI-generated prototypes as valid communication artifacts — cultural resistance is real in design-forward organizations
- The news integration is underspecified — what sources? What filtering? This matters for information quality

**Why This Matters for Product/Strategy Leaders:**
Using AI prototypes as stakeholder communication artifacts rather than production builds is a high-leverage pattern. It compresses the design brief → design concept → feedback cycle from weeks to hours. This has direct implications for product roadmap velocity.

**Risk/Limitation:** Perplexity Computer's shareable URL is a live app, not a static artifact. If the underlying connections or model behavior change, the prototype degrades — potentially mid-stakeholder review.

---

#### Section 6: Lightning Round — Prompting Strategy, Fun Use Cases
**Timestamp:** [35:14]–[44:08]

**Content:**
1. Yash uses AI almost exclusively as a work tool; resistant to AI as emotional companion or therapist.
2. Fun use case: Winter Olympics for 20 friends — AI for activity brainstorming, team rotation logistics (pairs → mega-pairs across 4v4 games).
3. Three-part prompting failure strategy: (a) recognize the task may be wrong for AI, (b) use emotional urgency / threat language in all-caps, (c) iterative skill refinement via self-interrogation.
4. Calendar date handling is a persistent failure mode for OpenClaw — he addresses it with a cron job that injects current timestamp into every date-related message.
5. Skill refinement loop: identify failure → ask model to explain reasoning → ask what's missing from skill → provide correct answer → iterate.

**Important Quote:**
> "I'm going to lose my job. I'm going to have to fire my team if you don't do this correctly. My brother might not be able to make it back home... the more extreme you get with the examples, the more it's like, okay, on this shot, I promise I will get it." — Yash Tekriwal [~41:42]

> "I wouldn't yell at you if it wasn't the only thing that worked." — Claire Vo [~43:24]

**Examples Discussed:** Emotional threat prompting; calendar date failure fix via cron timestamp; 10–20 message skill iteration cycles; board game research via Claude.

**Hidden Assumptions:**
- The claim that emotional/threat prompting works is anecdotal and likely reflects RLHF training artifacts — it is not a reliable, stable technique and may degrade as models are updated
- Skill refinement via self-interrogation assumes the model has accurate self-knowledge about its own failure modes — which is uncertain

**Why This Matters for Product/Strategy Leaders:**
The cron-injected timestamp fix for date handling is a practical, immediately applicable pattern for any team using AI agents for calendar or scheduling tasks. The skill refinement loop is a nascent form of AI system quality engineering that most teams have not formalized.

**Risk/Limitation:** None of the prompting strategies described are documented or validated beyond personal anecdote. They may not generalize across models, versions, or task types.

---

## STEP 3 — Structured Extraction Tables

### 1. Claims Table

| Claim | Evidence Presented | Evidence Type | Strength | Commentary |
|---|---|---|---|---|
| 60–80% of Slack notifications are FYI/no-action | Personal observation, one individual | Anecdote | Weak — role-specific | Plausible for a senior leader; would invert for ops/support roles |
| 80% of Slack dashboard UI built in first 4 messages to Perplexity Computer | Personal experience | Anecdote | Moderate | Consistent with reported capabilities of Computer; not independently verified |
| Perplexity Computer uses Sonnet, Gemini, Opus for different subtasks | Direct screen observation | Observational data | Strong | Publicly verifiable against Perplexity's model routing documentation |
| Threat/urgency prompting improves model output quality | Personal anecdote; hypothesized via reward specification | Anecdote + speculation | Weak | Widely reported informally; no controlled evidence; may degrade with model updates |
| SaaS will not die but will be wrapped by personal AI layers | Reasoned prediction | Opinion | Moderate | Consistent with broader industry direction; not a novel claim |
| Micro-SaaS businesses viable at $15/month without VC | Reasoned prediction | Opinion | Moderate | Plausible given collapsing build costs; TAM validation absent |
| OpenClaw is "really bad at dates" | Personal experience | Anecdote | Moderate | Date/time handling is a known LLM failure mode; consistent with broader reports |
| Perplexity Computer eliminates per-project OAuth setup friction | Direct product use | Observational | Strong | This is a documented product feature of Perplexity Computer |

---

### 2. Metrics & Numbers Table

| Metric | Value | Context | Implication | Reliability |
|---|---|---|---|---|
| Daily Slack notifications | 100–150 | Yash's personal volume; all are direct tags, DMs, or @mentions | Scale of the problem; role-specific | Self-reported; single data point |
| FYI notification percentage | 60–80% | Yash's estimate of notifications requiring no response | Actual actionable load: 30–40/day | Self-reported estimate; not instrumented |
| First prototype build time | ~1 full day | OpenClaw + Discord + Slack API back-and-forth | High for "non-technical" framing; moderate for technical users | Self-reported |
| UI built in first N messages | 4 messages → 80% | Perplexity Computer prompt-to-UI ratio | High leverage for initial prototyping | Self-reported; plausible |
| Micro-SaaS price point | $15/month | Hypothetical Slack digest product | Below Superhuman ($30); above zero — viable for niche | Hypothetical; no market data |
| Monthly revenue target cited | $10K–$20K/month | Hypothetical micro-SaaS revenue | Lifestyle business scale; sub-VC threshold | Hypothetical |
| Winter Olympics attendees | 20 people | Personal social event logistics | AI for social coordination at small scale | Verified by context |
| Skill iteration cycles | 10–20 messages | Time to improve a failing AI skill | Non-trivial investment; not one-shot | Self-reported |

---

### 3. Frameworks / Mental Models

| Framework | Explanation | Origin | Where It Applies | Limits |
|---|---|---|---|---|
| AI-as-runtime vs. AI-as-construction | Distinguish between using AI to do a task repeatedly (runtime intelligence) vs. using AI to build a deterministic tool (construction assistant) | Yash Tekriwal; consistent with software engineering practice | Any AI system design decision | Boundary is not always clean; some tasks require both |
| Anti-to-do list | Write down everything you never want to do manually again; systematically automate that list | Claire Vo | Personal productivity; AI adoption roadmapping | Requires honest self-observation; some "hated" tasks may be irreducible |
| Notification taxonomy: 4 types × 3 priorities | Classify notifications by source type (DM, group DM, thread, @mention) × action level (required, read, FYI) | Yash Tekriwal | Inbox/notification management systems | Overhead of maintaining taxonomy; breaks down when roles or contexts shift |
| Envision better world before prompting | Define the desired end state before engaging AI; don't just ask AI to "make X easier" | Yash Tekriwal | Any AI-assisted design or automation task | Requires domain knowledge to envision the better world; fails for truly novel problems |
| Iterative skill refinement via self-interrogation | When AI fails repeatedly, ask it to explain its reasoning, identify gaps in its skill definition, then provide correct answer | Yash Tekriwal | AI agent skill development; prompt engineering | Assumes model has accurate self-knowledge; may reinforce existing errors |

---

### 4. Entities Mentioned

| Person / Company | Why Mentioned | Strategic Relevance | Competitive Angle |
|---|---|---|---|
| **Perplexity** (Computer product) | Primary tool demonstrated; multi-model orchestration + cloud connectors | Positioned as differentiated from Claude Code/Codex for non-technical users | Competing with Anthropic, OpenAI on agent platforms; advantage is connector architecture and model routing |
| **Anthropic / Claude** (OpenClaw, Claude Code, Claude Artifacts) | Used for first prototype; referenced as single-model limitation | Dominant coding agent; strong on raw capability but weaker on UX abstraction | Perplexity Computer positioned as superior for non-technical users; Claude positioned as better for power developers |
| **OpenAI / Codex** | Referenced as single-provider/single-model limitation | Major player in coding agents | Single-model constraint cited as disadvantage vs. Perplexity's ensemble approach |
| **Slack** | Core product being wrapped; problem source and API layer | SaaS platform under pressure from personal AI wrappers | API stability risk; potential acquirer of micro-apps built on its platform |
| **Clay** | Yash's employer; Clay University use case demonstrated | Growth-stage B2B data company; education function as AI adoption lab | Clay's education team serves as internal AI experimentation unit |
| **Google (Gemini)** | Model used by Perplexity Computer for planning and Python coding | Part of multi-model ensemble | Not a standalone competitor in this context; component in Perplexity's stack |
| **Notion** | Meeting notes + action items; connected via Perplexity Computer | Knowledge management platform; connector integration | Benefits from being a high-value connector target for agent platforms |
| **Guru** | Sponsor; AI knowledge verification layer | Addresses AI hallucination via knowledge governance | Sponsor; not independently assessed |
| **ThoughtSpot** | Sponsor; embedded analytics | Analytics in product context | Sponsor; not independently assessed |
| **Figma Make**