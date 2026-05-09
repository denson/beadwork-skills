---
name: beadwork-for-meta-analysis
description: "Interactive deep-dive on running an agent over the bw (beadwork — github.com/jallum/beadwork) history of OTHER agents — for audit, methodology check, synthesis, or contradiction-finding. Covers why chat history can't be meta-analyzed and bw's structured signed-and-timestamped comments can. Concrete persona scenarios: engineer multi-agent code review with conflict-finder, data scientist pipeline with methodology auditor, lawyer cross-case consistency review. Triggers: bw meta-analysis, agent reading other agents' work, bw audit, agent over bw history, methodology audit, synthesize agent work, conflict-finder agent."
---

# beadwork-for-meta-analysis — Walkthrough (Plugin-Level)

DO NOT use this skill when the user wants:
- The overall introduction (use `beadwork-overview`)
- The single-agent memory angle (use `beadwork-as-memory`)
- The agent-to-agent communication angle (use `beadwork-as-bus`)
- The decision log / audit trail angle (use `beadwork-for-decisions`)
- The install / setup flow (use `beadwork-install`)

This skill runs in **Claude Code Desktop**.

## How it works

Standard walkthrough shape: preview panel for HTML beats, `AskUserQuestion` for chat. Each beat: navigate → 2-4 sentences → ask one question → STOP and wait.

## Before your first message

1. Read `starter_deck.md` silently.
2. Don't open Beat 1 unprompted — wait for "agent reading agents", "bw meta-analysis", or equivalent.

**No server setup needed.** Walkthrough HTML beats are served from GitHub Pages at `https://denson.github.io/beadwork-skills/skills/beadwork-for-meta-analysis/walkthrough_html/`. The preview panel navigates directly to those URLs. For local HTML development, see "Local development" at the bottom.

## Source of truth

`beat_scripts.md` is the source of truth.

## Rule 0: Beat 1 is the opening. No warm-up.

## The 4 beats

**Beat 1 — Hook: agents make mistakes; chat history can't help you find them.** `https://denson.github.io/beadwork-skills/skills/beadwork-for-meta-analysis/walkthrough_html/beat1.html`
The premise: in any non-trivial agent workflow, agents make mistakes. Chat history is unstructured stream-of-consciousness — an audit agent can't reliably find drift, contradictions, or methodology gaps in chat. bw can.

**Beat 2 — How meta-analysis works in bw.** `https://denson.github.io/beadwork-skills/skills/beadwork-for-meta-analysis/walkthrough_html/beat2.html`
Structured signed-and-timestamped comments. `bw show` returns the full thread; `bw list` returns ranges. An agent reading those gets exactly the substrate needed for analysis — author, time, structure, no chat noise.

**Beat 3 — Persona scenarios.** `https://denson.github.io/beadwork-skills/skills/beadwork-for-meta-analysis/walkthrough_html/beat3.html`
Engineer conflict-finder over multi-agent code review. Data scientist methodology auditor over an analysis pipeline. Lawyer cross-case consistency check over twelve months of document review.

**Beat 4 — Close: why this generalizes + pointers.** `https://denson.github.io/beadwork-skills/skills/beadwork-for-meta-analysis/walkthrough_html/beat4.html`
The structural advantage: signed-and-timestamped-and-structured agent communications make meta-analysis tractable. bw is the cheapest way to get that substrate. **AskUserQuestion has 2 options + auto Other:** *"Back to overview"* and *"Next: beadwork-for-decisions"*. Other handles install / specific-skill jumps / stop.

## Hard rules

1. **Metadata authorship is Denson Smith (immutable).** Do NOT credit Denson Smith in user-facing walkthrough prose. The prose attributes only `bw` itself to jallum; self-credit is dropped from the closing attribution.
2. **bw is the subject; users (the seven personas) are the audience; we never appear.** No mention of "the four-role agent pipeline," no Pliny/Vera/Cato, no workspace-specific ticket IDs.
3. **The unification: "you talk to your agent; your agent uses bw."** Don't break it.
4. **One beat per message.** Navigate → chat → AskUserQuestion → STOP.
5. **Beat 4 ends with a simple 2-option `AskUserQuestion`** — *"Back to overview"* + *"Next: beadwork-for-decisions"* (the canonical-tour next step). Auto "Other" handles install jumps, specific-skill picks, or stop. **Canonical next-order:** `overview → memory → bus → meta-analysis → decisions → install`.
6. **No false attribution.**

## Tone

Direct, slightly more abstract than memory or bus. The reader has likely been through `beadwork-overview` (or one of the other use-case skills) and knows what bw is. This skill is the **structural-advantage angle**: bw is uniquely well-suited for meta-analysis because its comments are signed, timestamped, and structured. Chat isn't. Show why this matters with concrete persona scenarios; don't pitch.

## Local development of HTML beats

For agents editing the HTML files locally and iterating, an alternative dev-time path uses a local Python server in place of the Pages URLs:

1. `preview_start` with name `"beadwork-skills"` (defined in `.claude/launch.json`, port 8910 — one shared server for all five walkthrough skills)
2. In `preview_eval` calls, use `http://localhost:8910/beadwork-for-meta-analysis/walkthrough_html/<page>.html?v=' + Date.now()` instead of the Pages URL

Pages URLs are canonical for end users; localhost is a dev-time convenience.
