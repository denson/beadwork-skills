# Beat scripts — beadwork-for-decisions walkthrough

Source of truth for what each beat says. HTML carries visuals; this file carries words.

Structure: 4 linear beats. Total ~3-4 minutes.

---

## Beat 1 — Hook: decisions are the spine; the "why" evaporates

### Chat (3-4 sentences)

Every project accumulates decisions. The *what* of each decision usually survives — the code shipped, the redaction was applied, the expense was paid. The *why* tends to evaporate — into Slack threads that expire, into a teammate's brain who left the company, into a chat session that compacted last quarter. Six months later, somebody asks *"why did we choose Auth0 over rolling our own OAuth?"* and the rationale is gone. `bw` is where the why persists — every decision a ticket with a title, options considered, the discussion thread (signed + timestamped), and a close-comment recording the verdict and the rationale.

### AskUserQuestion

> Recognize the problem?

Options:
- **Yes — show me how decisions look in bw** — proceed to Beat 2.
- **Show me concrete scenarios first** — proceed to Beat 3, circle back to Beat 2 if curious.
- **I have a specific question** — invite the user, answer briefly, then proceed to Beat 2.

### Image

`walkthrough_html/images/beat1-hook.jpg` — A two-panel scene.

LEFT panel ("Without a decision log"): a calendar showing months passing (Jan → Feb → ... → Aug). On Jan, a small group of figures with thought bubbles having a discussion — speech bubbles full of detail. By August, the same scene but the figures have left and the speech bubbles have faded to outlines. A new person stands in the August scene with a confused thought bubble: *"why did we decide on this?"* No way to recover the rationale.

RIGHT panel ("With bw decision tickets"): same calendar, but at the Jan position there's a ticket card with TITLE ("Auth: Auth0 vs in-house OAuth"), description (options), and a stack of comment-bubbles labeled with author + date. By August, the ticket card is unchanged, in the same location. The new person reads `bw show` and gets the full thread — original question, the options considered, why each was rejected, the close-comment with the verdict and rationale.

Caption: *"What decisions look like in six months."*

### Tone notes

- Direct. The "why evaporates" framing is universal — every persona has felt it.
- No agent-team specifics. Generic "decisions get made; rationale gets lost."

---

## Beat 2 — How decisions work in bw

### Chat (3-4 sentences)

A decision is just a `bw` ticket with a specific shape. **Title:** the decision. **Description:** the question + the options being considered. **Comments:** the discussion — different voices, signed and timestamped as the conversation evolves over hours, days, weeks. **Close-comment:** the verdict + the rationale, written by whoever made the call. Status flips from open (still discussing) to closed (decision made). Standard ADR format mapped onto bw's existing shape — no new tooling, no new schema, no separate decision-log database. Six months later, the next person runs `bw show <ticket-id>` and gets the entire decision thread back.

### AskUserQuestion

> Want to see scenarios across roles?

Options:
- **Yes — show me persona scenarios** — proceed to Beat 3.
- **Tell me about decision tags or filters first** — short detour: explain that you can label decisions (e.g. `--label decision --label architecture`) so `bw list --label decision` shows only the decision tickets across the project. Then proceed to Beat 3.

### Image

`walkthrough_html/images/beat2-mechanism.jpg` — A single ticket card rendered cleanly with each part labeled:

- **TITLE BAR** at top: *"Auth: Auth0 vs in-house OAuth"* (with a small label tag reading "decision")
- **DESCRIPTION BLOCK** below: *"Question: how do we authenticate users? Options considered: (1) Auth0 SaaS, (2) roll our own OAuth, (3) Firebase Auth."*
- **COMMENTS** stacked below, each with author + date stamps:
  - *"alice · 2026-04-12"* — *"Auth0 wins on time-to-ship; rolling our own is at least 6 weeks of dev"*
  - *"bob · 2026-04-13"* — *"concerned about per-user pricing as we scale; need to model"*
  - *"alice · 2026-04-14"* — *"modeled, breakeven is at 50K MAU; we're at 2K"*
- **CLOSE-COMMENT** with a special border/highlight:
  - *"closed: 2026-04-15 by alice"* — *"Decision: Auth0. Rationale: time-to-ship dominates at our scale; revisit if we cross 50K MAU."*

Caption: *"Decision = ticket. ADR shape, bw substrate."*

### Tone notes

- Technical-but-accessible. Show the actual ticket shape.
- The "no new tooling" point is the load-bearing claim — bw was always this; you just use it for decisions deliberately.

---

## Beat 3 — Three persona scenarios

### Chat (5-6 sentences)

Three places where decision logs matter, in different shapes. **Engineer (ADR):** the team debates REST vs gRPC for a new service. Architecture-decision-record ticket opened, options laid out, senior engineer adds a perspective, decision: gRPC. Six months later, a new engineer joins and asks *"why gRPC?"* — `bw show <ticket>` returns the original reasoning, including which trade-offs were considered and rejected. **Lawyer (privilege log):** every redaction is a decision with documenter + rationale + timestamp. Opposing counsel challenges a specific redaction nine months later — `bw show` produces the original privilege determination with the legal reasoning preserved verbatim. Court-defensible by construction. **Solo entrepreneur (tax-time):** every business-expense decision (tools subscribed to, contractors paid, equipment bought) gets logged with rationale ("subscribed to MailerLite for newsletter — chose over ConvertKit because cheaper at our list size"). Tax audit nine months later — AI runs `bw show` on the year's expense decisions, formats for accountant. Auditable history without separate accounting software. **Common thread:** the question "why did we decide X?" always has an answer.

### AskUserQuestion

> Ready for the close?

Options:
- **Yes — close it out** — proceed to Beat 4.
- **One more scenario** — invite the user to ask about a specific persona's flavor; answer briefly; then proceed to Beat 4.

### Image

`walkthrough_html/images/beat3-scenarios.jpg` — Three vertical lanes, each showing a decision-log scenario.

LEFT lane (Engineer): a ticket card titled "Architecture: REST vs gRPC for orders service" with multiple comments showing trade-off analysis (latency, tooling, team familiarity). Below the ticket: a small "6 months later" arrow pointing to a new-engineer figure reading the ticket, thought bubble: *"now I understand why."*

MIDDLE lane (Lawyer): a privilege-log ticket card titled "Doc 4789: work-product privilege" with a structured comment showing the legal reasoning (cited rule, reasoning chain, signed by attorney, dated). Below: a "9 months later" arrow pointing to opposing counsel reading the ticket, thought bubble: *"reasoning preserved → court-defensible."* A small gavel icon in the corner.

RIGHT lane (Solo Entrepreneur): a small stack of expense-decision tickets ("MailerLite: vs ConvertKit", "Hetzner: vs DigitalOcean", "Notion Pro: vs free tier"), each with a brief rationale-comment. Below: a "tax time" arrow pointing to an accountant figure with a tablet, reading the bw export, thought bubble: *"every expense documented + reasoned."*

Caption: *"Three roles. Three flavors of decision log. Same ticket shape."*

### Tone notes

- Concrete. Real decisions of the kind each persona actually makes.
- The "common thread: the question 'why' always has an answer" line is the punchline — it generalizes across all three.

---

## Beat 4 — Close: the pattern + pointers

### Chat (4-5 sentences)

The pattern, in one sentence: **any decision worth remembering is a candidate for a `bw` ticket**. The "ticket" shape is just structured-enough notes-to-future-self with the rationale preserved. You don't need a separate decision-log tool, an ADR repository, a privilege-log app, or accounting software — `bw` was always this; you just use it for decisions deliberately. Future-you (or future-anyone) reads `bw show` and gets the why. **Companion skills:** `beadwork-overview` (the seven-persona tour), `beadwork-as-memory` (durability), `beadwork-as-bus` (multi-agent communication), `beadwork-for-meta-analysis` (an agent reading other agents' bw work), `beadwork-install` (drive setup). Each angle on the same substrate.

### AskUserQuestion

**None.** Beat 4 is the terminus.

### Image

`walkthrough_html/images/beat4-close.jpg` — A clean closing card. Center: a stylized ticket card with the parts labeled (title, description, comments, close-comment-with-rationale). Below the ticket, a banner reading: *"any decision worth remembering = a bw ticket."* Around the ticket, four small companion-skill icons arranged horizontally with names: `beadwork-overview`, `beadwork-as-memory`, `beadwork-as-bus`, `beadwork-for-meta-analysis`, plus `beadwork-install`. Bottom: small caption reading *"open source, MIT-licensed. bw by jallum (github.com/jallum/beadwork)."*

**NOTE:** The rendered image as of 2026-05-08 still shows the older caption *"open source. Denson Smith. bw itself by jallum."* — visual contradicts spec. Regenerate to match the spec when convenient (or live with the discrepancy).

Caption: *"Any decision worth remembering is a ticket."*

### Tone notes

- Wrap-up. Slightly formal close.
- The "no new tooling" framing is the strategic close — bw isn't a decision-log product; it's a general substrate that happens to do decision logs well.
- No `AskUserQuestion`.
