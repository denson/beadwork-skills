# Beat scripts — beadwork-as-bus walkthrough

Source of truth for what each beat says.

Structure: 4 linear beats. Total ~3-4 minutes.

**Tone rule across all beats:** lead with **same-lab multi-session coordination** (a team of specialist agents from one lab — design, implementation, review). Cross-vendor / cross-lab interop is real but secondary — frame it as *"and the same mechanism works across labs too"*, not as the headline. Most users live in one ecosystem.

---

## Beat 1 — Hook: a team of specialist agents

### Chat (3-4 sentences)

If your AI is one agent in one chat, memory is the whole story. But the moment you want *more than one agent working on something* — a design agent, an implementation agent, a review agent — memory alone isn't enough. **Most often these are sessions of the same model from the same lab** (multiple Claude sessions, or multiple Gemini sessions), each playing a specialist role. They need to *talk to each other* in a way that survives, and `bw` (beadwork) is the channel: multiple agents read and write the same ticket store; each comment is signed and timestamped; no two agents step on each other's writes.

### AskUserQuestion

> Want to see how that actually works?

Options:
- **Yes — show me the mechanism** — proceed to Beat 2.
- **Show me concrete scenarios first** — proceed to Beat 3 (scenarios), circle back to Beat 2 if needed.
- **I have a specific question** — invite the user to ask, answer, then proceed to Beat 2.

### Image

`walkthrough_html/images/beat1-hook.jpg` — A composition showing several AI assistant figures around a central ticket card. Arrows reading and writing into the ticket. Comment bubbles labeled with different roles (designer, coder, reviewer) and timestamps. Small label on the ticket reads "shared bw store." Caption: *"Many agents. One ticket. Asynchronous, signed, durable."*

### Tone notes

- **Lead with same-lab specialist team.** Multiple sessions of one model in different roles.
- Cross-lab interop is mentioned in passing only ("the substrate works across labs too").
- Don't re-explain compaction or memory; the reader knows.

---

## Beat 2 — How communication works in bw

### Chat (3-4 sentences)

Multiple agents can read and write the same `bw` store. Each comment records who wrote it (a role name, an agent name, a timestamp) — so when Agent B reads what Agent A wrote yesterday, B knows who said it and when. Conflict-free by construction: different tickets are stored as different files, so two agents working on different tickets simultaneously never touch the same bytes. No merge drivers, no lock files, no coordination overhead. The substrate is just shell — `bw show`, `bw comment`, `bw close` — so any agent that can shell out participates the same way (whether it's a different session of the same model, or, in rarer cases, an agent from a different lab altogether).

### AskUserQuestion

> Want to see scenarios?

Options:
- **Yes — show me the persona scenarios** — proceed to Beat 3.
- **Tell me about cross-lab interop first** — short detour: explain that since `bw` is just shell commands, an agent from a different vendor reads/writes the same store the same way. Useful if you ever swap labs but most users won't need it day to day. Then proceed to Beat 3.

### Image

`walkthrough_html/images/beat2-mechanism.jpg` — Two ticket cards side by side. Two AI figures: Agent A writing to ticket-1; Agent B writing to ticket-2 — both at the same time. No overlap; different files. Below: merged view showing both tickets in the same store. Caption: *"Different tickets, different files. No collision."*

### Tone notes

- The conflict-free property is non-obvious to anyone who's dealt with merge conflicts. Worth making explicit.
- **Cross-lab interop is a parenthetical, not the headline.** Mention it briefly inside the "substrate is just shell" callout — don't dedicate prose space to it.

---

## Beat 3 — Multi-agent and cross-team scenarios

### Chat (5-6 sentences)

Four shapes that come up often. **Multi-agent within one job (engineer):** PR-42 review. Three review agents (security, style, test-coverage) — all sessions of the same Claude/Gemini model, each in a specialist role — post structured verdicts to the same ticket. The submitting engineer's AI reads the consolidated ticket and synthesizes. **Multi-agent across days (data scientist):** Monday's data-cleaner agent writes the cleaned dataset's stats to a ticket. Tuesday's tester agent reads those stats and runs hypothesis tests. Wednesday's visualizer agent reads both and generates plots. **Cross-team (support manager):** customer escalation opens a ticket; engineering's AI reads it, posts a fix ETA; the support manager's AI reads the update and drafts the customer reply — three departments, no Slack thread. **Cross-org (warehouse manager):** vendor agent at a logistics partner posts pickup schedules to a shared ticket; the warehouse manager's AI confirms or proposes alternatives. Two organizations' AIs coordinating asynchronously, full audit trail.

### AskUserQuestion

> Ready for the close?

Options:
- **Yes — close it out** — proceed to Beat 4.
- **One more scenario** — invite the user to ask about a specific scenario; answer briefly; then proceed to Beat 4.

### Image

`walkthrough_html/images/beat3-scenarios.jpg` — Four small panels arranged in a 2x2 grid, each showing one scenario.

TOP-LEFT (Engineer): PR-42 review ticket with three structured-verdict comments and an engineer's AI synthesizing.

TOP-RIGHT (Data Scientist): three day-stamped tickets connected by arrows showing the analysis pipeline.

BOTTOM-LEFT (Support Manager): three columns — CS, engineering, manager — each with an AI figure, all writing to a central escalation ticket.

BOTTOM-RIGHT (Warehouse Manager): two organization buildings, each with an AI figure, both writing to a shared ticket between them.

Caption: *"Within a job, across days, across teams, across organizations."*

### Tone notes

- 5-6 sentences but covers four scenarios — keep each scenario brief.
- The four-shape framing (within-job, across-days, cross-team, cross-org) is the unification.
- The within-job and across-days scenarios are the heart of "team of specialist agents from one lab" — emphasize that all the agents in those scenarios are typically the same model in different roles.

---

## Beat 4 — Close: you have a team

### Chat (4-5 sentences)

Here's the shift to take away: with `bw`, your AI isn't one amnesiac generalist anymore. It's one member of a small team of specialist agents — design, implementation, review, audit — that share a durable, signed, auditable workspace. **Most of the time those agents are sessions of one lab's model** (all Claude, or all Gemini), each playing a different role. Two extras the substrate gives you for free: humans on a team can join the same workspace (push the orphan branch to a shared repo and teammates + their agents read/write the same store), and cross-lab works too (any agent that can shell out can participate). **Companion skills:** `beadwork-as-memory`, `beadwork-for-meta-analysis`, `beadwork-for-decisions`, `beadwork-install` — all angles on the same substrate.

### AskUserQuestion

> Where to next?

Options (2 + auto "Other"):
- **Back to overview** → switch to `beadwork-overview`.
- **Next: beadwork-for-meta-analysis** → continue the canonical tour to the meta-analysis deep-dive.

The auto "Other" option lets the user say *"install now,"* *"jump to decisions,"* *"stop,"* or any specific skill. The companion list on the page shows all six.

### Image (optional)

If included: `walkthrough_html/images/beat4-close.jpg` — Currently shows several differently-styled AI figures (Claude, Gemini, OpenAI, generic) converging on a single `bw` store. Visual works for the secondary cross-lab point but doesn't lead the new headline. Acceptable for now; can regenerate later if it grates.

### Tone notes

- **The headline is "you have a team of specialist agents from one lab."** Cross-lab is one of two "bonus" properties listed second.
- The other bonus property — humans-on-a-team joining via shared repo — connects this skill to the cross-human-team angle in `beadwork-overview` Beat 1's third tier.
- **`AskUserQuestion` at the end** routes to next skill — make the companion list actionable, not a dead-end.
