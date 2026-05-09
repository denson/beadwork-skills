# Beat scripts — beadwork-as-memory walkthrough

Source of truth for what each beat says. HTML carries visuals; this file carries words.

Structure: 4 linear beats. Total ~3-4 minutes.

---

## Beat 1 — Hook: a few specific things have to survive

### Chat (3-4 sentences)

Most of what your AI needs across sessions isn't the whole chat history — it's a few specific things that have to survive: the decision you reached, the constraint you hit, the blocker you noted, the half-finished plan. Chat-only AI assistants lose those things every time the session ends, the chat gets compacted, or the machine changes. `bw` (beadwork) gives your AI a place to write those few specific things down — durably, in your repo, in a format the next session can read. The shape of the interaction doesn't change: you talk to your agent; your agent writes the durable parts to `bw`; tomorrow's session reads them.

### AskUserQuestion

> Want to see how memory actually works in bw?

Options:
- **Yes — show me the mechanism** — proceed to Beat 2.
- **Tell me what kinds of things people store** — proceed to Beat 3 first (scenarios), then circle back to Beat 2 if curious.
- **I have a specific question** — invite the user to ask, answer, then proceed to Beat 2.

### Image

`walkthrough_html/images/beat1-hook.jpg` — A stylized horizontal timeline showing two sessions separated by a gap. LEFT session: an AI assistant figure at a laptop, with thought bubbles and a small ticket card emerging from the AI ("decision: Auth0 with PKCE", "constraint: budget <$50/mo", "blocker: vendor API down until Wed"). The session ends with a "session ended" mark. CENTER (the gap): the same ticket card persists, anchored by a small icon labeled "bw — your repo." RIGHT session: a fresh session opening; the same AI figure (or a new one) reads the ticket card, with a thought bubble reading "right — picking up where we left off." Caption: *"Memory isn't the chat. Memory is the few things you wrote down."*

### Tone notes

- Direct. Doesn't re-explain compaction (overview did that); just names the few-specific-things property.
- Cite jallum + bw is implicit; no need to re-link if user came from overview.

---

## Beat 2 — How memory works in bw

### Chat (3-4 sentences)

`bw` stores everything as ticket-shaped records on a special git branch (the orphan branch — never merged into your code, just there in your repo's git database). Each ticket has a title, a description, fields like priority and status, and a thread of comments. Each comment records who wrote it (your AI signs as itself, or as a role you've configured) and when. Months later, your AI runs `bw show <ticket-id>` and gets the full thread back — title, description, every comment in order, every author, every timestamp. Because it's git-backed, you can also see the *diff history* of edits — the past doesn't get retroactively rewritten; you see the timeline of how you got here.

### AskUserQuestion

> Want to see scenarios where this matters?

Options:
- **Yes — show me where memory pays off** — proceed to Beat 3.
- **Tell me about the orphan-branch trick first** — short detour: the orphan branch has no shared history with `master`/`main`, so its commits never appear in your code's git log; your project's git log stays clean. Then proceed to Beat 3.

### Image

`walkthrough_html/images/beat2-mechanism.jpg` — A simplified diagram of one ticket card with a column of comment bubbles, each labeled with a date stamp and an author (e.g., "claude · 2026-05-08", "user · 2026-05-09", "claude · 2026-05-12"). Above the ticket: a small bar showing "title / description / fields (priority, status, type)." Off to the side, an AI assistant figure with an arrow into the ticket labeled "`bw show <id>` returns the full thread." Caption: *"Title + comments + author + timestamp = reconstruction substrate."*

### Tone notes

- Schema-light explainer. Don't get lost in fields; emphasize the reconstruction property.
- "Past doesn't get retroactively rewritten" matters — distinguishes from many "AI memory" tools that overwrite state.

---

## Beat 3 — Memory in three shapes

### Chat (5-6 sentences)

Three places where memory matters in different ways. **Data scientist:** an investigation into a metric anomaly spans a week. Each day's session adds comments — which queries were run, what results came back, what hypothesis is being tested next. On day seven, when the analysis is ready for stakeholders, the AI generates the executive memo by reading its own bw history — grounded in the actual investigation arc, not from scratch. **Lawyer:** case opened in March, settled in November. New paralegal joins in September; their AI reads `bw show case-smith-v-jones` and gets the entire case history — discovery, depositions, key decisions. The associate is up to speed in an hour, not three weeks. **Solo entrepreneur:** consulting engagement with one client in April, similar-shaped engagement in October — the AI surfaces relevant prior lessons: *"you tried this with the April client; here's what worked, here's what didn't."* Different kinds of memory, same mechanism: agent reads `bw show`, picks up where the past left off.

### AskUserQuestion

> Want to see the full list of what survives?

Options:
- **Yes — show me what survives** — proceed to Beat 4.
- **Skip ahead to the closing pointers** — proceed to Beat 4 (which closes anyway).

### Image

`walkthrough_html/images/beat3-scenarios.jpg` — Three vertical lanes, each showing a memory scenario.

LEFT lane (Data Scientist): a multi-day timeline (Day 1 → Day 7) with daily comment cards stacking up on a central ticket card labeled "Q3-churn-investigation." On Day 7, an AI figure reads the full stack and emerges with a doc icon labeled "executive memo."

MIDDLE lane (Lawyer): a long horizontal case-file ticket labeled "case-smith-v-jones" with many comments spanning months (March → November). A "new paralegal" icon appears in September, with an AI assistant beside them reading the ticket from the start.

RIGHT lane (Solo Entrepreneur): two engagement tickets labeled "April client" and "October client," connected by a curving "lessons" arrow from the first to the second. A solo entrepreneur figure with their AI assistant beside them.

Caption: *"Same mechanism, three shapes of memory."*

### Tone notes

- Three concrete scenarios. Different time horizons (week, year, multi-engagement) and different "what's being remembered" (investigation arc, case history, lessons-across-engagements).
- The "same mechanism" closing line is the unification.

---

## Beat 4 — Close: what survives + pointers

### Chat (4-5 sentences)

What `bw` memory survives, in full: sessions ending. `/clear` calls. Agent restarts. Container restarts. Switching machines. Switching between AI vendors (Claude this month, Gemini next month — same `bw` data). Time. The most underrated one is the last: most "AI memory" tools accumulate state but don't preserve the *evolution* — you see the current state of the notebook, not the path you took to get there. `bw`'s git-history-as-storage means you can always reconstruct the path. **Companion skills:** `beadwork-as-bus` (multiple agents through bw), `beadwork-for-meta-analysis` (running an agent over bw history), `beadwork-for-decisions` (decision log / audit), `beadwork-install` (drive setup). All of them are ways memory pays off.

### AskUserQuestion

> Where to next?

Options (2 + auto "Other"):
- **Back to overview** → switch to `beadwork-overview`.
- **Next: beadwork-as-bus** → continue the canonical tour to the multi-agent communication deep-dive.

The auto "Other" option lets the user say *"install now,"* *"jump to decisions,"* *"stop,"* or any specific skill. The companion list on the page shows all six.

### Image (optional — Beat 4 may run without an image)

If included: `walkthrough_html/images/beat4-close.jpg` — A simple pointer card. Top: a row of failure-mode icons (session ended, /clear, restart, machine swap, vendor swap, clock) with arrows all pointing down to a single durable ticket card that's clearly unbroken. Below the ticket: four pointer-card icons for the companion skills. Caption: *"Memory survives. Pick what to read next."*

In practice, Beat 4 may render as HTML-only (text + styled pointer card via CSS). Image is optional, generated only if budget allows.

### Tone notes

- Wrap-up. Forward-pointing.
- The "evolution preserved" framing is non-obvious and worth the closing position.
- **`AskUserQuestion` at the end** routes to next skill — make the companion list actionable, not a dead-end.
