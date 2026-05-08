# Beat scripts — beadwork-overview walkthrough

This is the **working-doc source of truth** for what each beat says. The HTML pages in `walkthrough_html/` carry the visual presentation; this file carries the words. Chat text in CCD is a 2-4 sentence summary that bridges from the HTML into the AskUserQuestion — write it in your own voice, but use the prose here as the spec.

Structure: 5 beats + a hub fork on Beat 3 with 4 deeper-dive paths (Technical / Operations / Professional / All-Seven). Beat 5 closes. Total ~5-6 beats per traversal.

---

## Beat 1 — Hook: agents forget; bw fixes that

### Chat (3-4 sentences)

Your AI assistant forgets. Chat ends, sessions compact, machines change — the thread your AI was on is gone, and tomorrow's session starts blank. There's a small tool called [`bw`](https://github.com/jallum/beadwork) (beadwork — written by [jallum](https://github.com/jallum)) that gives your AI durable memory and a shared communication channel with other AIs. It works across every kind of work — engineering, science, operations, customer support, legal, solo business — and across every AI vendor. The interaction is simple: you talk to your agent; the agent uses `bw`; you don't have to know it's there.

### AskUserQuestion

> Recognize the problem?

Options:
- **Yes — show me what bw does** — proceed to Beat 2 (the trust story).
- **Tell me about where the data lives first** — short detour: explain that bw stores everything in your repo's git database (a special branch, never merged into your code), then proceed to Beat 2.
- **Not really — explain compaction first** — short detour: explain how Claude (and other AIs) summarize long sessions when context fills, dropping detail in favor of a summary, then proceed to Beat 2.

### Image

`walkthrough_html/images/beat1-hook.jpg` — A two-panel split scene. LEFT panel: a generic AI assistant figure (no specific vendor branding) looking confused, with a thought bubble reading *"wait — what was I doing?"* Around the figure: scattered fragments representing forgotten context (a half-finished list, a question mark, a dimmed conversation bubble drifting away). RIGHT panel: the same AI assistant figure looking calm and resumed, reading from a small ticket card sitting on a desk; a thought bubble reads *"right — yesterday we decided X, the next step is Y."* A small label at the bottom of the right panel reads "context restored from `bw show`."

Caption: *"Sessions end. Context shouldn't."*

Style: editorial illustration, flat design, simple shapes, light warm-gray background. Generic agent figure (NOT branded as our four-role pipeline; no Pliny/Ada/Vera/Cato). Clean and approachable.

### Tone + length notes

- Punchy, conversational. The reader hasn't read anything else yet.
- 3-4 sentences in the chat copy; lean toward the shorter end.
- The "talk to your agent" framing must land here. It threads through every subsequent beat.
- Cite jallum + bw with a link upfront. Credit the source.
- DO NOT mention "the four-role agent pipeline" or any agent-team specifics. Generic AI assistant only.

---

## Beat 2 — What bw is (the trust story)

### Chat (4-5 sentences)

Five structural things make bw different from the SaaS alternatives most AI-memory tools take. **It lives in your repo** — your disk, your git, your remote of choice. Not on jallum's servers. Not on any vendor's servers. **It's free** — no signup, no quotas, single binary. **It's cross-AI portable** — Claude, Gemini, OpenAI, anything that can run `bw show` reads the same store, so your AI's memory follows you across vendors. **It's open source** — jallum's project, MIT-licensed, plain JSON in a git branch. **And the killer feature: it survives compaction.** Sessions die, machines change, the years pass — the tickets and comments don't.

### AskUserQuestion

> Want to see who uses it?

Options:
- **Yes — show me the breadth** — proceed to Beat 3 (the seven personas + hub fork).
- **One question first** — invite the user to ask, answer briefly, then proceed to Beat 3.

### Image

`walkthrough_html/images/beat2-trust.jpg` — A stylized diagram of a developer's repository, shown as a folder labeled "your repo / your disk." Inside the folder: project files visible at the top (a generic source-code icon, a README file, a config file), and a separate compartment at the bottom labeled "beadwork (orphan branch)" containing several ticket cards. Multiple AI assistant icons (different colors / different vendor styles — generic representations of Claude, Gemini, OpenAI, an unspecified fourth) are arrayed around the folder, each with arrows reading and writing into the beadwork compartment. A large arrow points outside the diagram with the label "no SaaS, no vendor servers, no signup."

Caption: *"Lives where your code lives."*

Style: technical-but-friendly diagram. Same flat editorial vocabulary as Beat 1.

### Tone + length notes

- Matter-of-fact. List the structural advantages over SaaS alternatives.
- 4-5 sentences plus the question.
- "Cross-AI portable" is the under-told story — emphasize. Most "AI memory" tools today are vendor-locked.
- "Survives compaction" is jallum's headline feature — call it the killer feature.

---

## Beat 3 — Seven roles, one interaction pattern (HUB)

### Chat (5-7 sentences)

Seven kinds of people use bw, all the same way. **Software engineers** — debugging, architecture decisions, multi-agent code review. **Data scientists** — long-running investigations, multi-agent analysis pipelines, reproducibility for stakeholder defense. **Logistics analysts** — performance analytics, vendor scorecards, model iteration. **Warehouse managers** — incident logs, vendor coordination across organizations, supervisor handoffs across shifts. **Customer support managers** — escalation tracking, cross-team coordination with engineering, SLA pattern detection. **Lawyers and paralegals** — case files, multi-agent document review, privilege logs, court-defensible audit. **Solo entrepreneurs and small agency owners** — personal-OS for the business, vendor management, lessons across engagements. The interaction is identical in every case: **you talk to your agent; your agent uses `bw`.** What differs is what each role is tracking, not how they interact with the tool.

### AskUserQuestion (this is the HUB)

> Which sounds closest to your work?

Options:
- **(A) Technical roles** — engineer, data scientist, logistics analyst. Theme: bw as audit substrate.
- **(B) Operations & customer-facing** — warehouse manager, customer support manager. Theme: bw as durable async channel.
- **(C) Independent / professional services** — lawyer, solo entrepreneur. Theme: bw as personal-OS.
- **(D) Show me all 7 quickly** — the unification pitch (same interaction across every persona).

(After the chosen path, proceed to Beat 5 — no further fork.)

### Image

`walkthrough_html/images/beat3-personas.jpg` — A grid of seven illustrated cards, arranged in a 4-3 layout. Each card has a persona icon, a role name, and a one-line use:

1. **Software engineer** — a developer at a laptop, label *"debugging, decisions, code review."*
2. **Data scientist** — a figure with charts and a notebook, label *"investigations, pipelines, reproducibility."*
3. **Logistics analyst** — a figure with route maps and graphs, label *"analytics, scorecards, model iteration."*
4. **Warehouse manager** — a figure on a warehouse floor with a clipboard, label *"incidents, vendor coordination, shift handoffs."*
5. **Customer support manager** — a figure at a headset, label *"escalations, cross-team coordination."*
6. **Lawyer / paralegal** — a figure with a case file, label *"cases, document review, audit."*
7. **Solo entrepreneur** — a figure at a small desk juggling many hats, label *"personal-OS, lessons across engagements."*

Below the grid: a horizontal banner with the text "**all seven: talk to your agent. agent uses bw.**"

Caption: *"Seven roles. Same interaction."*

Style: clean grid layout, editorial illustration. Each persona icon distinct but stylistically consistent.

### Tone + length notes

- 5-7 sentences (longer than other beats because there are 7 personas to brief).
- Each persona gets one phrase — no longer.
- The unification line ("**you talk to your agent; your agent uses bw**") is the load-bearing claim. Make it land.
- The hub fork at the end is mandatory — this is the only branching point in the walkthrough.

---

## Beat 4 — HUB (no own content; just the fork from Beat 3)

The hub itself is just the AskUserQuestion at the end of Beat 3. No new content lives at Beat 4 directly; the user enters one of the four dynamic paths below.

---

### Path A — Technical roles (engineer, data scientist, logistics analyst)

#### Chat (5-6 sentences)

Engineers, data scientists, and logistics analysts share one thing: their work has to be correct and defensible — to senior reviewers, to stakeholders, to regulators, or to their future selves six months later. **Engineer:** a debugging session spans three days; today's Claude reads yesterday's `bw show` and resumes. On PR submission, three review agents (security, style, test-coverage) write structured verdicts to a shared ticket; a fourth "conflict-finder" agent reads all three and flags contradictions. **Data scientist:** an investigation into a metric anomaly spans a week; an analysis pipeline of three agents (cleaner → tester → visualizer) all write to bw; a methodology-auditor agent reviews the chain. Six months later, leadership asks *"why did you conclude X?"* — the answer is `bw show`. **Logistics analyst:** vendor scorecard updates weekly; same data feeds the operations team via shared bw; route-model iterations logged so abandoned approaches are explainable. **Common thread:** bw as audit substrate — defensible by construction.

#### AskUserQuestion

> Which deeper-dive skill resonates?

Options:
- **Memory across sessions** (`beadwork-as-memory`) — the long-running-investigation flavor.
- **Agent-to-agent communication** (`beadwork-as-bus`) — the multi-agent-pipeline flavor.
- **Meta-analysis** (`beadwork-for-meta-analysis`) — running an agent over OTHER agents' bw work.
- **Decision log / audit trail** (`beadwork-for-decisions`) — the *"future-X reads `bw show`"* flavor.
- **Show me all of them** — proceed to Beat 5 (the closing list).

#### Image

`walkthrough_html/images/dynamic-technical.jpg` — Three vertical lanes, each showing a scenario.

LEFT lane (Engineer): a developer at a laptop with three small AI assistant figures around them. Arrows from each AI converge on a single ticket card labeled "PR-42 review" with three structured-verdict comments visible (one from "security agent," one from "style agent," one from "test-coverage agent"). A fourth AI figure labeled "conflict-finder" stands separately, reading all three verdicts.

MIDDLE lane (Data Scientist): a figure with a notebook. An analysis pipeline of three AI agents arrayed horizontally (data cleaner → statistical tester → visualizer) with arrows between them. A fourth AI figure labeled "methodology auditor" stands above the pipeline, reading the chain.

RIGHT lane (Logistics Analyst): a figure with a dashboard. A vendor scorecard ticket card in the middle. Two AI figures (different colors) on either side of the ticket — one labeled "analyst's AI," one labeled "operations AI" — both reading the same ticket.

Caption: *"Correctness + validation across three roles."*

Style: technical-illustration, three clean lanes, same flat editorial vocabulary.

#### Tone + length notes

- 5-6 sentences in the chat copy.
- Concrete scenarios, real-feeling. No specific ticket IDs from any actual project (use generic placeholders like "PR-42" or "Q2-anomaly").
- The "**common thread: bw as audit substrate**" line is the load-bearing claim for this path.
- Acknowledge SWE/CLI residual without dwelling — *"engineers sometimes still dip into the CLI directly, but that's trending agent-mediated."*

---

### Path B — Operations & customer-facing (warehouse manager, customer support manager)

#### Chat (5-6 sentences)

Warehouse managers and customer support managers share another shape: coordination across teams, shifts, and organizations, with record-keeping that has to hold up to compliance audits or SLA disputes. **Warehouse manager:** the day-shift supervisor's AI logs exceptions to bw; the night-shift supervisor's AI reads them on session start and briefs the night supervisor. Vendor agents at logistics partners coordinate pickups asynchronously through shared bw — two organizations' AIs writing back and forth without a common chat thread. OSHA inspector arrives; AI runs `bw show` over safety incidents, formats for the inspector. **Customer support manager:** an escalated complaint opens a bw ticket; engineering's AI reads it, posts findings + fix ETA; manager AI reads engineering's update, drafts customer reply. Pattern detection across hundreds of conversations: *"top 5 pain points this quarter?"* runs `bw list`, synthesizes themes, feeds the product roadmap. **Common thread:** bw as durable async channel — coordination data IS the audit trail, no extra tooling needed.

#### AskUserQuestion

> Which deeper-dive skill resonates?

(Same options as Path A: memory / bus / meta-analysis / decisions / all-of-them. All lead to Beat 5.)

#### Image

`walkthrough_html/images/dynamic-operations.jpg` — A composition with two horizontal scenes.

TOP scene (Warehouse Manager): a warehouse cross-section showing day-shift activity on the left fading into night-shift activity on the right. Both shifts have AI assistant figures; an arrow connects them through a central bw ticket card labeled "shift handoff log." Two separate organization buildings off to the side, with two more AI figures (vendor coordination), arrows between them through another bw ticket card.

BOTTOM scene (Support Manager): a customer service interface on the left; an engineering team workspace on the right. Three AI figures (CS, engineering, manager) all reading and writing to a central ticket card labeled "escalation 2026-Q2-acme." A small inspector/auditor figure on the side with a clipboard, reading from a stack of ticket cards.

Caption: *"Coordination IS record-keeping."*

Style: same flat editorial vocabulary. Two clearly demarcated scenes.

#### Tone + length notes

- 5-6 sentences.
- These personas never see the CLI — emphasize that the AI is the entire interface.
- The "two organizations' AIs writing back and forth without a common chat thread" point is novel and worth landing.

---

### Path C — Independent / professional services (lawyer, solo entrepreneur)

#### Chat (5-6 sentences)

Lawyers and solo entrepreneurs share a third shape: small team or solo, audit-critical, no admin overhead to set up. **Lawyer:** each case is a ticket epic; child tickets per phase (discovery, deposition prep, filing, settlement). A new associate joining the case reads `bw show` for the full history. A discovery dump of 10,000 documents partitioned across review agents; an audit agent reads the chain to verify inter-agent consistency — bar standing rides on review accuracy, the audit agent is professional insurance. Privilege log preserved with timestamp + drafter + rationale; opposing counsel challenges a redaction six months later — `bw show` produces court-defensible reasoning. **Privacy is non-negotiable** — bw stays local-only or in a strictly-private repo. **Solo entrepreneur:** every domain (sales, ops, finance, knowledge) gets a bw epic. AI logs activity, decisions, vendor notes across all of them. *"You tried this with Acme; didn't work because X. Want a different approach?"* — personal knowledge graph that survives every chat compaction. Tax-time defense: AI runs `bw show` on the year's expense decisions. **Common thread:** bw as personal-OS substrate — durable, auditable, low admin overhead, privacy-respecting.

#### AskUserQuestion

> Which deeper-dive skill resonates?

(Same options as Path A.)

#### Image

`walkthrough_html/images/dynamic-professional.jpg` — A composition with two horizontal scenes.

TOP scene (Lawyer): a small law office. A stack of case-file ticket cards each labeled with a generic case name. Multiple AI assistant figures partitioning a tall stack representing 10,000 documents. A separate AI figure labeled "audit agent" reads the chain. A privilege log card off to the side with a date stamp and a "court-defensible" label. Lock icons around the scene emphasizing privacy.

BOTTOM scene (Solo Entrepreneur): a single figure at a desk surrounded by labels for many domains (sales, ops, finance, marketing, knowledge). A single AI assistant figure beside them with a notebook ticket card labeled "all domains." Arrows showing the AI logging activity across each labeled domain. A small sub-scene showing "lessons learned" tickets being surfaced for a new engagement.

Caption: *"Personal-OS, audit-grade, low overhead."*

Style: same flat editorial vocabulary. Two demarcated scenes; lock icons in the top scene reinforcing privacy.

#### Tone + length notes

- 5-6 sentences.
- The privacy story for the lawyer is non-negotiable — say so explicitly.
- "Personal-OS substrate" is the load-bearing claim for this path.

---

### Path D — Show me all 7 quickly

#### Chat (5-6 sentences)

The most striking thing about all seven personas is how similar their interaction with bw is. The **engineer** asks Claude *"why did we decide on Auth0?"* — Claude reads `bw show`. The **data scientist** asks *"what was the methodology in March's churn investigation?"* — Claude reads `bw show`. The **warehouse manager** asks *"what incidents this month?"* — AI runs `bw list`. The **support manager** asks *"top 5 pain points?"* — AI runs `bw list`. The **lawyer** asks *"what's the privilege reasoning on document 4789?"* — AI reads `bw show`. The **logistics analyst** asks *"vendor scorecard for Q2?"* — AI reads the bw ticket. The **solo entrepreneur** asks *"what worked with Acme?"* — AI surfaces lessons from bw. **Same pattern, seven roles, seven kinds of work.** The user talks; the agent uses bw; the data persists; the next session resumes where the last one left off. The user almost never types `bw` themselves — and that's the point.

#### AskUserQuestion

> Which deeper-dive skill resonates?

(Same options as Path A.)

#### Image

`walkthrough_html/images/dynamic-all.jpg` — A grid of seven small panels, one per persona, arranged in a 4-3 layout. Each panel shows the same simple shape:

- Persona figure on the left
- Speech bubble in the middle showing what they ask their agent
- AI assistant figure on the right
- bw ticket card emerging from or being read by the AI

The seven panels:
1. Engineer: speech bubble *"why did we decide on Auth0?"* AI figure reading `bw show`.
2. Data scientist: *"what was March's churn methodology?"* AI reading `bw show`.
3. Warehouse manager: *"incidents this month?"* AI running `bw list`.
4. Support manager: *"top 5 pain points?"* AI running `bw list`.
5. Lawyer: *"privilege reasoning on doc 4789?"* AI reading `bw show`.
6. Logistics analyst: *"Q2 vendor scorecard?"* AI reading the bw ticket.
7. Solo entrepreneur: *"what worked with Acme?"* AI surfacing bw lessons.

Across the bottom: a single banner reading *"one pattern. seven roles. seven kinds of work."*

Caption: *"One pattern. Seven roles."*

Style: small repeated-pattern panels; same flat editorial vocabulary; visually emphasizes the **sameness** across roles.

#### Tone + length notes

- 5-6 sentences.
- The pattern of "user asks; AI runs `bw show` / `bw list`" repeated across all 7 IS the unification pitch. Don't break it with variation.
- The closing claim — *"the user almost never types bw themselves — and that's the point"* — is the punchline.

---

## Beat 5 — Close: pointers to deeper-dive skills

### Chat (4-5 sentences)

Where to go from here. Five companion skills go deeper on specific use-case angles. **`beadwork-as-memory`** — bw as durable agent memory across long-running work. **`beadwork-as-bus`** — multi-agent pipelines and cross-team / cross-organization coordination. **`beadwork-for-meta-analysis`** — running an agent over the bw history of *other agents* to audit, check methodology, or synthesize. **`beadwork-for-decisions`** — bw as decision log / ADR / compliance audit trail. **`beadwork-install`** — drive the install end-to-end (Claude can run it for you; the only choice you make is the storage mode). All open source. All authored by Denson Smith. `bw` itself is jallum's project at [github.com/jallum/beadwork](https://github.com/jallum/beadwork).

### AskUserQuestion

**None.** Beat 5 is the terminus. End with the message above and stop.

### Image

`walkthrough_html/images/beat5-close.jpg` — A "where to next" card.

Center top: a small bw ticket icon with a checkmark. Below it, five labeled cards arranged in a 3-2 grid representing the five companion skills:

Top row:
1. Memory icon (a clock + brain shape) labeled "**beadwork-as-memory**"
2. Network icon (multiple agents connected through a central node) labeled "**beadwork-as-bus**"
3. Magnifying glass over a stack of tickets, labeled "**beadwork-for-meta-analysis**"

Bottom row:
4. Decision-tree icon labeled "**beadwork-for-decisions**"
5. Wrench icon labeled "**beadwork-install**"

Below the grid: a small caption reading "open source. authored by Denson Smith. `bw` itself by jallum (github.com/jallum/beadwork)."

Caption: *"Five companion skills."*

Style: clean grid card; same flat editorial vocabulary.

### Tone + length notes

- Wrap-up. Forward-pointing.
- 4-5 sentences plus the skill list.
- No `AskUserQuestion`.
- The closing attribution (Denson Smith for the skills; jallum for bw) lands here verbatim. Don't paraphrase.
