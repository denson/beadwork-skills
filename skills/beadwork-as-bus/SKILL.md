---
name: beadwork-as-bus
description: "Interactive deep-dive on beadwork (bw — github.com/jallum/beadwork) as agent-to-agent communication. Covers how multiple agents read and write the same store, conflict-free concurrent writes, cross-team and cross-organization coordination, and concrete persona scenarios (engineer multi-agent code review, scientist analysis pipeline, support manager cross-team escalation, warehouse manager cross-org vendor coordination). Triggers: bw bus, beadwork as message bus, multi-agent communication, agent-to-agent communication, cross-team coordination, multi-agent pipeline."
---

# beadwork-as-bus — Walkthrough (Plugin-Level)

DO NOT use this skill when the user wants:
- The overall introduction (use `beadwork-overview`)
- The single-agent memory angle (use `beadwork-as-memory`)
- The meta-analysis angle (use `beadwork-for-meta-analysis`)
- The decision log angle (use `beadwork-for-decisions`)
- The install / setup flow (use `beadwork-install`)

This skill runs in **Claude Code Desktop**.

## How it works

Standard walkthrough shape: preview panel for HTML beats, `AskUserQuestion` for chat. Each beat: navigate → 2-4 sentences → ask one question → STOP and wait.

## Before your first message

1. Start the server: `preview_start` with name `"beadwork-as-bus"` (port 8912).
2. Read `starter_deck.md` silently.
3. Don't open Beat 1 unprompted — wait for "agents talking through bw" or equivalent.

## Source of truth

`beat_scripts.md` is the source of truth.

## Rule 0: Beat 1 is the opening. No warm-up.

## The 4 beats

**Beat 1 — Hook: agents need to talk to each other (and to you, asynchronously).** `http://localhost:8912/beat1.html`

**Beat 2 — How communication works in bw.** `http://localhost:8912/beat2.html`
Multiple agents read and write the same store. Comments record speaker. Conflict-free by construction (different tickets = different files; no merge driver needed).

**Beat 3 — Multi-agent + cross-team scenarios.** `http://localhost:8912/beat3.html`
Engineer review pipeline. Scientist analysis chain. Support manager ↔ engineering. Warehouse manager ↔ vendor org.

**Beat 4 — Close: pointers + the cross-vendor angle.** `http://localhost:8912/beat4.html`
Cross-AI portability: agents from different vendors can write to the same store. **No `AskUserQuestion` here — Beat 4 is the terminus.**

## Hard rules

1. **Authorship: Denson Smith.** `bw` is jallum's tool; credit explicitly.
2. **bw is the subject; users (the seven personas) are the audience; we never appear.** No mention of "the four-role agent pipeline," no Pliny/Vera/Cato.
3. **The unification: "you talk to your agent; your agent uses bw."** Don't break it.
4. **One beat per message.** Navigate → chat → AskUserQuestion → STOP.
5. **Beat 4 has no `AskUserQuestion`.**
6. **No false attribution.**

## Tone

Direct, concrete. The reader has likely come from `beadwork-overview` or `beadwork-as-memory`. This skill is the multi-agent angle — coordination across agents, teams, organizations, and AI vendors.
