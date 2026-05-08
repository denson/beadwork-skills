---
name: beadwork-as-memory
description: "Interactive deep-dive on beadwork (bw — github.com/jallum/beadwork) as durable agent memory. Covers how the orphan-branch storage works, what survives across sessions / restarts / machines / years, and concrete persona scenarios (data scientist long-running investigation, lawyer case file resumption, solo entrepreneur lessons-across-engagements). Triggers: bw memory, beadwork memory, agent memory, durable AI memory, how does bw remember things, bw across sessions."
---

# beadwork-as-memory — Walkthrough (Plugin-Level)

DO NOT use this skill when the user wants:
- The overall introduction (use `beadwork-overview`)
- The agent-to-agent communication angle (use `beadwork-as-bus`)
- The meta-analysis angle (use `beadwork-for-meta-analysis`)
- The decision log / audit trail angle (use `beadwork-for-decisions`)
- The install / setup flow (use `beadwork-install`)

This skill runs in **Claude Code Desktop**.

## How it works

Standard walkthrough shape: preview panel for HTML beats, `AskUserQuestion` for chat. Each beat: navigate → 2-4 sentences → ask one question → STOP and wait.

## Before your first message

1. Start the server: `preview_start` with name `"beadwork-as-memory"` (port 8911).
2. Read `starter_deck.md` silently.
3. Don't open Beat 1 unprompted — wait for "memory in bw" or equivalent.

## Source of truth

`beat_scripts.md` is the source of truth.

## Rule 0: Beat 1 is the opening. No warm-up.

## The 4 beats

**Beat 1 — Hook: most of what your AI needs isn't a whole chat history; it's a few specific things that have to survive.** `http://localhost:8911/beat1.html`

**Beat 2 — How memory works in bw.** `http://localhost:8911/beat2.html`
The orphan-branch storage; ticket comments record speaker + timestamp; reconstruction via `bw show` and `bw history`.

**Beat 3 — Persona scenarios: memory in three shapes.** `http://localhost:8911/beat3.html`
Data scientist multi-day investigation; lawyer multi-month case; solo entrepreneur cross-engagement lessons.

**Beat 4 — Close: pointers + what survives.** `http://localhost:8911/beat4.html`
The full survival story (sessions, /clear, agents, machines, vendors, time) plus pointers to companion skills. **No `AskUserQuestion` here — Beat 4 is the terminus.**

## Hard rules

1. **Authorship: Denson Smith.** `bw` is jallum's tool; credit explicitly.
2. **bw is the subject; users (the seven personas) are the audience; we never appear.** No mention of "the four-role agent pipeline," no Pliny/Vera/Cato, no workspace-specific ticket IDs.
3. **The unification: "you talk to your agent; your agent uses bw."** Don't break it.
4. **One beat per message.** Navigate → chat (2-4 sentences) → AskUserQuestion → STOP.
5. **Beat 4 has no `AskUserQuestion`.** Four beats end the walkthrough.
6. **No false attribution.**

## Tone

Direct, concrete. The reader has likely come from `beadwork-overview` and already knows what bw is. This skill goes deeper on the memory angle without re-explaining the basics.
