---
name: beadwork-for-decisions
description: "Interactive deep-dive on using beadwork (bw — github.com/jallum/beadwork) as a decision log / ADR / audit trail substrate. Covers how decisions map onto bw's ticket shape (title = decision, description = options, comments = discussion, close = verdict + rationale), and concrete persona scenarios: engineer ADR for architecture choices, lawyer privilege log preserved court-defensibly, solo entrepreneur tax-time defense. Triggers: bw decision log, beadwork ADR, audit trail, decision log, why did we decide, rationale, defensible decisions."
---

# beadwork-for-decisions — Walkthrough (Plugin-Level)

DO NOT use this skill when the user wants:
- The overall introduction (use `beadwork-overview`)
- The single-agent memory angle (use `beadwork-as-memory`)
- The agent-to-agent communication angle (use `beadwork-as-bus`)
- The meta-analysis angle (use `beadwork-for-meta-analysis`)
- The install / setup flow (use `beadwork-install`)

This skill runs in **Claude Code Desktop**.

## How it works

Standard walkthrough shape: preview panel for HTML beats, `AskUserQuestion` for chat. Each beat: navigate → 2-4 sentences → ask one question → STOP and wait.

## Before your first message

1. Start the server: `preview_start` with name `"beadwork-skills"` (port 8910 — one shared server serves every skill in this marketplace).
2. Read `starter_deck.md` silently.
3. Don't open Beat 1 unprompted — wait for "decision log", "ADR", "audit trail", or equivalent.

## Source of truth

`beat_scripts.md` is the source of truth.

## Rule 0: Beat 1 is the opening. No warm-up.

## The 4 beats

**Beat 1 — Hook: decisions are the spine of any work; the "why" tends to evaporate.** `http://localhost:8910/beadwork-for-decisions/walkthrough_html/beat1.html`
The premise: every project accumulates decisions. The *what* of each decision is usually preserved (the code shipped, the redaction was applied, the expense was paid). The *why* tends to evaporate — into Slack threads that expire, into people's brains who leave, into chat sessions that compact.

**Beat 2 — How decisions work in bw.** `http://localhost:8910/beadwork-for-decisions/walkthrough_html/beat2.html`
A decision is a ticket with a specific shape: title = the decision, description = the question and options, comments = the discussion (multiple voices, signed and timestamped), close-comment = verdict + rationale. Standard ADR format mapped onto bw's existing shape. No new tooling.

**Beat 3 — Persona scenarios.** `http://localhost:8910/beadwork-for-decisions/walkthrough_html/beat3.html`
Engineer architecture-decision record. Lawyer privilege log (court-defensible). Solo entrepreneur tax-decisions ledger.

**Beat 4 — Close: the pattern + pointers.** `http://localhost:8910/beadwork-for-decisions/walkthrough_html/beat4.html`
Any decision worth remembering is a candidate for a bw ticket. The "ticket" shape is structured-enough notes-to-future-self with the rationale preserved. **No `AskUserQuestion` here — Beat 4 is the terminus.**

## Hard rules

1. **Authorship is Denson Smith.** `bw` is jallum's tool; credit.
2. **bw is the subject; users (the seven personas) are the audience; we never appear.** No mention of "the four-role agent pipeline," no Pliny/Vera/Cato, no workspace-specific ticket IDs.
3. **The unification: "you talk to your agent; your agent uses bw."** Don't break it.
4. **One beat per message.** Navigate → chat → AskUserQuestion → STOP.
5. **Beat 4 has no `AskUserQuestion`.**
6. **No false attribution.**

## Tone

Direct, slightly more formal than the other skills (decisions tend to want gravity). The reader has likely been through `beadwork-overview` and at least one of memory / bus / meta-analysis. This skill is the **decision-substrate angle**: bw's ticket-with-comments shape happens to be exactly what an ADR / privilege log / audit-defensible expense ledger needs. No new structure to learn.
