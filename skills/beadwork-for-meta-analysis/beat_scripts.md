# Beat scripts — beadwork-for-meta-analysis walkthrough

Source of truth for what each beat says. HTML carries visuals; this file carries words.

Structure: 4 linear beats. Total ~3-4 minutes.

---

## Beat 1 — Hook: agents make mistakes; chat history can't help you find them

### Chat (3-4 sentences)

In any non-trivial agent workflow, agents make mistakes — they drift on a convention they were supposed to follow, they apply different criteria across what should be similar tasks, they miss things their peer just flagged. The cheap way to catch those mistakes is **another agent reading the work** — not the chat that produced it, but the actual decisions and verdicts. Chat history doesn't work for that: it's unstructured stream-of-consciousness, the speaker is implicit, the timing is muddied, and most of it is noise. `bw` (beadwork) is structured: every comment records who wrote it, when, on which ticket, in what shape. **An audit agent reading `bw show` gets the substrate it needs to actually find the mistakes.**

### AskUserQuestion

> Recognize the problem?

Options:
- **Yes — show me how meta-analysis works** — proceed to Beat 2.
- **Tell me about a concrete scenario first** — proceed to Beat 3 (scenarios), circle back to Beat 2 if curious.
- **I have a specific question** — invite the user to ask, answer briefly, then proceed to Beat 2.

### Image

`walkthrough_html/images/beat1-hook.jpg` — A two-panel split scene.

LEFT panel ("Chat history — can't audit this"): a tangled, noisy conversation thread rendered as a long stream of speech bubbles in different colors, overlapping and crowded together. An audit-agent figure tries to read it, with a confused thought bubble reading *"who said what? when? what did they decide?"* Bits of the chat are blurred or fading.

RIGHT panel ("bw history — can audit this"): the same content but rendered as a clean stack of structured ticket cards, each card showing TITLE / multiple comments with **author** + **timestamp** stamps clearly visible / structured fields (status, priority, type). The audit-agent figure stands in front, with a clear thought bubble reading *"agent A on day 1: <decision>. agent B on day 4: <verdict>. they agree on X but conflict on Y."*

Caption: *"Same work. Different substrate. Only one is auditable."*

### Tone notes

- Direct. The premise — "agents make mistakes; you need a way to audit" — should land in one sentence.
- The "structured, signed, timestamped" property is the load-bearing claim. Make it land.
- Don't oversell — describe what the substrate makes possible.

---

## Beat 2 — How meta-analysis works in bw

### Chat (3-4 sentences)

A meta-analysis agent doesn't watch agents work. It reads what they wrote afterward. `bw show <ticket>` returns the full thread for one ticket — title, description, every comment in order, every author, every timestamp. `bw list` returns ranges of tickets matching filters (status, type, label, date range). The audit agent feeds those into its prompt and asks questions a single agent can't answer alone: *"did agents A and B apply the same criteria across these 12 reviews?"*, *"is there drift on naming convention over the last quarter?"*, *"agent C said X; agent D's comment two days later contradicts it — flag for human review."* Same git-backed substrate as memory and the bus; new analysis layer on top.

### AskUserQuestion

> Want to see scenarios where this pays off?

Options:
- **Yes — show me concrete examples** — proceed to Beat 3.
- **Tell me about access to bw history first** — short detour: explain that `bw history <id>` returns the diff history of edits (so you can see how a ticket evolved, not just its current state). Then proceed to Beat 3.

### Image

`walkthrough_html/images/beat2-mechanism.jpg` — A diagram with a stack of structured tickets on the left side (each ticket showing TITLE + multiple signed/timestamped comments in a clean column layout). On the right, a single audit-agent figure (rendered slightly differently — perhaps with a magnifying-glass icon) reading the stack. Above the audit agent: thought bubbles representing the questions it can ask: *"consistency?"*, *"drift?"*, *"contradictions?"*, *"missing steps?"* A small label between the tickets and the audit agent reads `bw show / bw list`. A note off to the side: *"all author stamps. all timestamps. all structure. = analyzable."*

Caption: *"Read the work, not the chat."*

### Tone notes

- Schema-light. Don't get lost in field names.
- The "questions a single agent can't answer alone" framing is the load-bearing point — meta-analysis is meaningful precisely because it's *cross-agent* analysis.

---

## Beat 3 — Persona scenarios

### Chat (5-6 sentences)

Three places where meta-analysis pays off in different shapes. **Engineer (multi-agent code review):** PR-42 has three review agents — security, style, test-coverage — each posting a structured verdict to a shared ticket. A fourth "conflict-finder" agent reads all three verdicts and flags *"security wants strict CORS; style wants the same headers stripped — these contradict."* The submitting engineer sees the conflict before it ships. **Data scientist (analysis pipeline):** a pipeline of three agents — cleaner → tester → visualizer — each writes to bw. A "methodology auditor" agent reads the chain and checks *"did the tester use the same population definition the cleaner produced?"* Catches subtle gaps that don't surface in chat. **Lawyer (cross-case consistency):** an audit agent reads twelve months of bw document-review history across many cases, looks for inter-agent consistency in privilege determinations. Bar-standing-protective — uniformity matters legally, and only meta-analysis catches drift across cases. The common thread: **the auditor is just another agent, reading the substrate that all the prior agents produced.**

### AskUserQuestion

> Ready for the close?

Options:
- **Yes — close it out** — proceed to Beat 4.
- **One more scenario** — invite the user to ask about a specific persona's flavor; answer briefly; then proceed to Beat 4.

### Image

`walkthrough_html/images/beat3-scenarios.jpg` — A composition with three vertical lanes, each showing a meta-analysis scenario.

LEFT lane (Engineer): a PR-42 review ticket with three structured-verdict comments — **security agent** ("require strict CORS headers"), **style agent** ("strip those headers"), **test-coverage agent** ("OK"). A fourth agent labeled **"conflict-finder"** reads all three verdicts and emerges with a flag-icon thought bubble: *"contradiction: security vs style on CORS."*

MIDDLE lane (Data Scientist): a pipeline of three day-stamped tickets with arrows: **cleaner ticket** ("filtered to active users") → **tester ticket** ("ran t-test on full population") → **visualizer ticket**. A **"methodology auditor"** agent stands beside the chain reading all three; thought bubble: *"tester used 'full population'; cleaner had filtered to 'active users' — gap."*

RIGHT lane (Lawyer): a stack of twelve case-file tickets each with several review-comment cards. An **"audit agent"** stands in front of the stack with a thought bubble: *"case-3 and case-9 both ruled work-product privilege — different agents, same criterion applied? checking..."*

Caption: *"Three roles. Three flavors of audit. One substrate."*

### Tone notes

- Concrete. Each scenario shows the auditor reading actual prior-agent work and catching something.
- The "conflict-finder catches what single-agent review can't" line is the punchline for engineers.
- Lawyer scenario emphasizes *cross-case* — that's where bw's substrate value compounds (twelve cases worth of review data is too much for any one agent to hold in its context, but a `bw list`-driven audit can spot-check methodically).

---

## Beat 4 — Close: why this generalizes + pointers

### Chat (4-5 sentences)

The structural advantage worth naming explicitly: meta-analysis works on `bw` because `bw` produces **signed, timestamped, structured** agent communications. Chat history doesn't have that shape — speaker is implicit, timing is muddied, structure is whatever the model felt like emitting. Wherever you can produce signed-timestamped-structured agent communications, meta-analysis becomes tractable; `bw` is just the cheapest way to get that substrate. **Companion skills:** `beadwork-overview` (the seven-persona tour), `beadwork-as-memory` (durability), `beadwork-as-bus` (multi-agent communication), `beadwork-for-decisions` (decision logs), `beadwork-install` (drive setup). Each angle on the same substrate.

### AskUserQuestion

> Where to next?

Options (2 + auto "Other"):
- **Back to overview** → switch to `beadwork-overview`.
- **Next: beadwork-for-decisions** → continue the canonical tour to the decision-log deep-dive.

The auto "Other" option lets the user say *"install now,"* *"jump to memory,"* *"stop,"* or any specific skill. The companion list on the page shows all six.

### Image

`walkthrough_html/images/beat4-close.jpg` — A clean closing card. Center top: a stylized structured ticket (with the now-familiar TITLE + comments-with-author-and-timestamp shape) being read by a magnifying-glass icon labeled **"any agent can read this"**. Below the ticket, a label: *"signed + timestamped + structured = analyzable."* Around the ticket, four small companion-skill icons arranged horizontally with their names: `beadwork-overview`, `beadwork-as-memory`, `beadwork-as-bus`, `beadwork-for-decisions`, plus `beadwork-install`. Bottom: a small caption reading *"open source, MIT-licensed. bw by jallum (github.com/jallum/beadwork)."*

Caption: *"Meta-analysis is just another agent reading the substrate."*

### Tone notes

- Wrap-up. Forward-pointing.
- The "wherever you can produce signed/timestamped/structured agent comms" framing is the strategic close — bw is one implementation; the principle is broader.
- **`AskUserQuestion` at the end** routes to next skill (2 options + auto Other) — make the companion list actionable.
