---
name: beadwork-as-bus
description: "Interactive deep-dive on beadwork (bw — github.com/jallum/beadwork) as agent-to-agent communication. Covers how multiple agent sessions read and write the same store to act as a team of specialist agents (most often sessions of one lab's model — multiple Claude sessions or multiple Gemini sessions — each playing a role like designer, implementer, reviewer; cross-lab interop is real but secondary), conflict-free concurrent writes, cross-team and cross-organization coordination, and concrete persona scenarios (engineer multi-agent code review, scientist analysis pipeline, support manager cross-team escalation, warehouse manager cross-org vendor coordination). Triggers: bw bus, beadwork as message bus, multi-agent communication, agent-to-agent communication, team of specialist agents, multi-agent pipeline, cross-team coordination."
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

1. Start the server: `preview_start` with name `"beadwork-skills"` (port 8910 — one shared server serves every skill in this marketplace).
2. Read `starter_deck.md` silently.
3. Don't open Beat 1 unprompted — wait for "agents talking through bw" or "team of agents" or equivalent.

## Source of truth

`beat_scripts.md` is the source of truth.

## Rule 0: Beat 1 is the opening. No warm-up.

## The 4 beats

**Beat 1 — Hook: a team of specialist agents, sharing one workspace.** `http://localhost:8910/beadwork-as-bus/walkthrough_html/beat1.html`
Multi-session same-lab is the headline (a designer agent, an implementer agent, a reviewer agent — usually all Claude or all Gemini, in different roles). Cross-lab interop is mentioned in passing only.

**Beat 2 — How communication works in bw.** `http://localhost:8910/beadwork-as-bus/walkthrough_html/beat2.html`
Multiple agents read and write the same store. Comments record speaker. Conflict-free by construction (different tickets = different files; no merge driver needed). Cross-lab interop sits in a parenthetical inside the "substrate is just shell" callout — not as a headline.

**Beat 3 — Multi-agent + cross-team scenarios.** `http://localhost:8910/beadwork-as-bus/walkthrough_html/beat3.html`
Four shapes: engineer review pipeline (within-job multi-agent), scientist analysis chain (across-days multi-agent), support manager ↔ engineering (cross-team), warehouse manager ↔ vendor org (cross-org).

**Beat 4 — Close: you have a team.** `http://localhost:8910/beadwork-as-bus/walkthrough_html/beat4.html`
The take-away: with bw, your AI isn't one amnesiac generalist — it's one member of a team of specialists from your lab. Two bonuses listed second: humans-on-a-team can join the same workspace; cross-lab works too. **AskUserQuestion has 2 options + auto Other:** *"Back to overview"* and *"Next: beadwork-for-meta-analysis"*. Other handles install / specific-skill jumps / stop.

## Hard rules

1. **Metadata authorship is Denson Smith (immutable).** Do NOT credit Denson Smith in user-facing walkthrough prose. The prose attributes only `bw` itself to jallum; self-credit is dropped from the closing attribution.
2. **bw is the subject; users (the seven personas) are the audience; we never appear.** No mention of "the four-role agent pipeline," no Pliny/Vera/Cato.
3. **The unification: "you talk to your agent; your agent uses bw."** Don't break it.
4. **Lead with same-lab multi-session as the headline.** A team of specialist agents from one lab (design + implementation + review) is what most users will actually run. **Cross-lab interop (Claude + Gemini sharing one store) is a real but secondary case** — mention it as "and the same mechanism works across labs too," not as the lead. Most users live in one ecosystem.
5. **Don't claim bw "fixes" anything.** It "helps" / "lets you" / "addresses." Same tone rule as `beadwork-overview`.
6. **One beat per message.** Navigate → chat → AskUserQuestion → STOP.
7. **Beat 4 ends with a simple 2-option `AskUserQuestion`** — *"Back to overview"* + *"Next: beadwork-for-meta-analysis"* (the canonical-tour next step). Auto "Other" handles install jumps, specific-skill picks, or stop. **Canonical next-order:** `overview → memory → bus → meta-analysis → decisions → install`.
8. **No false attribution.**

## Tone

Direct, concrete. The reader has likely come from `beadwork-overview` or `beadwork-as-memory`. This skill is the multi-agent angle — coordination across agent sessions of the same model (the common case), and the related properties (cross-team coordination, cross-org coordination, and as a bonus, cross-lab interop).
