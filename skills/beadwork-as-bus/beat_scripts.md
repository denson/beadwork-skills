# Beat scripts — beadwork-as-bus walkthrough

Source of truth for what each beat says.

Structure: 4 linear beats. Total ~3-4 minutes.

---

## Beat 1 — Hook: agents need to talk

### Chat (3-4 sentences)

If your AI is just one agent in one chat, memory is the whole story. But the moment you have two agents working together — or one agent today and a different agent tomorrow, or your agent and a coworker's agent, or your agent and a vendor's agent — memory alone isn't enough. They need to *talk to each other* in a way that survives. `bw` (beadwork) is the channel: multiple agents read and write the same ticket store; each comment is signed and timestamped; no two agents step on each other's writes. The interaction stays the same — you talk to your agent — but now the agent is part of a team that talks through `bw`.

### AskUserQuestion

> Want to see how that actually works?

Options:
- **Yes — show me the mechanism** — proceed to Beat 2.
- **Show me concrete scenarios first** — proceed to Beat 3 (scenarios), circle back to Beat 2 if needed.
- **I have a specific question** — invite the user to ask, answer, then proceed to Beat 2.

### Image

`walkthrough_html/images/beat1-hook.jpg` — A composition showing several AI assistant figures arranged in a loose ring around a central ticket card. Each AI figure is rendered slightly differently (different colors / vendor styles representing Claude, Gemini, OpenAI, generic). Arrows from each AI both INTO and OUT OF the central ticket — both reading and writing. The ticket card has a stack of comment bubbles inside, each one labeled with a different author and timestamp, showing the conversation across agents. A small label on the ticket reads "shared bw store." Caption: *"Many agents. One ticket. Asynchronous, signed, durable."*

### Tone notes

- Don't re-explain compaction or memory; the reader knows.
- Lead with the multi-agent reality: agents don't work alone in modern setups.

---

## Beat 2 — How communication works in bw

### Chat (3-4 sentences)

Multiple agents can read and write the same `bw` store. Each comment records who wrote it (a role name, an agent name, a timestamp) — so when Agent B reads what Agent A wrote yesterday, B knows who said it and when. Conflict-free by construction: different tickets are stored as different files, so two agents working on different tickets simultaneously never touch the same bytes. No merge drivers, no lock files, no coordination overhead — just two agents writing different files at the same time. And because `bw` is just `bw show` and `bw comment` and `bw close`, agents from different vendors (Claude, Gemini, OpenAI, anything that runs a CLI) participate the same way.

### AskUserQuestion

> Want to see scenarios?

Options:
- **Yes — show me the persona scenarios** — proceed to Beat 3.
- **Tell me about cross-vendor first** — short detour: explain that since `bw` is just shell commands, any agent that can shell out can participate. The same store works for an Anthropic-based agent on Monday and a Google-based agent on Tuesday. Then proceed to Beat 3.

### Image

`walkthrough_html/images/beat2-mechanism.jpg` — A diagram showing two ticket cards side by side, each with several comment bubbles. Two AI assistant figures: Agent A on the left writing to ticket-1; Agent B on the right writing to ticket-2 — both at the same time. Arrows show no overlap; the writes go to different files. Below: a "merged" view showing both tickets coexisting in the same `bw` store. Caption: *"Different tickets, different files. No collision."*

### Tone notes

- The conflict-free property is non-obvious to anyone who's dealt with merge conflicts. Worth making explicit.
- Cross-vendor is the load-bearing point on portability — call it out as a structural advantage.

---

## Beat 3 — Multi-agent and cross-team scenarios

### Chat (5-6 sentences)

Four shapes that come up often. **Multi-agent within one job (engineer):** PR-42 review. Three review agents (security, style, test-coverage) each post a structured verdict to the same ticket. The submitting engineer's AI reads the consolidated ticket and synthesizes the responses. **Multi-agent across days (data scientist):** Monday's data-cleaner agent writes the cleaned dataset's stats to a ticket. Tuesday's tester agent reads those stats and runs the right hypothesis tests. Wednesday's visualizer agent reads both and generates plots. The pipeline is async; each step's input is the previous step's bw comment. **Cross-team (support manager):** customer escalation opens a ticket; engineering's AI reads it, posts a fix ETA; the support manager's AI reads the update and drafts the customer reply — three departments, no Slack thread. **Cross-org (warehouse manager):** vendor agent at a logistics partner posts pickup schedules to a shared ticket; the warehouse manager's AI reads them and confirms or proposes alternatives. Two organizations' AIs coordinating asynchronously, no common chat thread, full audit trail.

### AskUserQuestion

> Ready for the close + cross-vendor angle?

Options:
- **Yes — close it out** — proceed to Beat 4.
- **One more scenario** — invite the user to ask about a specific scenario from the seven personas; answer briefly; then proceed to Beat 4.

### Image

`walkthrough_html/images/beat3-scenarios.jpg` — Four small panels arranged in a 2x2 grid, each showing one scenario.

TOP-LEFT (Engineer): a PR-42 review ticket with three structured-verdict comments (security agent, style agent, test-coverage agent), and an engineer's AI synthesizing.

TOP-RIGHT (Data Scientist): three day-stamped tickets connected by arrows showing the analysis pipeline (cleaner Monday → tester Tuesday → visualizer Wednesday).

BOTTOM-LEFT (Support Manager): three columns — CS, engineering, manager — each with an AI figure, all writing to a central escalation ticket.

BOTTOM-RIGHT (Warehouse Manager): two organization buildings (warehouse + logistics partner), each with an AI figure, both writing to a shared pickup-schedule ticket between them.

Caption: *"Within a job, across days, across teams, across organizations."*

### Tone notes

- 5-6 sentences but covers four scenarios — keep each scenario brief.
- The four-shape framing (within-job, across-days, cross-team, cross-org) is the unification.

---

## Beat 4 — Close: pointers + cross-vendor angle

### Chat (4-5 sentences)

The angle that's underrated until you live it: cross-AI portability. `bw` is just shell commands, so any agent that can run a CLI participates. Today's pipeline is Claude end-to-end; if Anthropic raises prices and you switch some agents to Gemini, the new Gemini agents read the same `bw` store the Claude agents wrote. Your multi-agent pipeline doesn't break when you swap a vendor. **Companion skills:** `beadwork-as-memory` (single-agent durability), `beadwork-for-meta-analysis` (an agent reading other agents' bw work), `beadwork-for-decisions` (decision log / audit trail), `beadwork-install` (drive setup). All of them are angles on the same substrate.

### AskUserQuestion

**None.** Beat 4 is the terminus.

### Image (optional)

If included: `walkthrough_html/images/beat4-close.jpg` — Several differently-styled AI figures (Claude, Gemini, OpenAI, generic) all converging on a single `bw` ticket store labeled "your repo." Caption: *"Swap vendors freely. The store stays."* Otherwise HTML-only with a styled pointer card.

### Tone notes

- Cross-vendor angle deserves the closing position — it's the most strategic property.
- No `AskUserQuestion`.
