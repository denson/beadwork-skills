---
name: beadwork-overview
description: "Interactive overview of beadwork (bw — github.com/jallum/beadwork). Covers what bw is, the trust story (git-native, no SaaS, free, cross-AI portable, open source), and how seven kinds of users — engineers, data scientists, logistics analysts, warehouse managers, customer support managers, lawyers, solo entrepreneurs — use bw through their AI assistants for durable agent memory and agent-to-agent communication. Triggers: what is beadwork, what is bw, beadwork overview, why bw, why beadwork, who uses bw, beadwork tour, explain beadwork, walk me through beadwork."
---

# beadwork-overview — Walkthrough (Plugin-Level)

DO NOT use this skill when the user wants:
- The detailed memory deep-dive (use `beadwork-as-memory`)
- The agent-to-agent communication deep-dive (use `beadwork-as-bus`)
- The meta-analysis deep-dive (use `beadwork-for-meta-analysis`)
- The decision log / audit trail deep-dive (use `beadwork-for-decisions`)
- The install / setup flow (use `beadwork-install`)

This skill runs in **Claude Code Desktop**. It does not work in Cowork — the preview panel + `AskUserQuestion` shape that holds the walkthrough together isn't reliably available there.

## How it works

The walkthrough uses Claude Code Desktop's **preview panel** to display rich HTML beats (with images), while questions go in the chat via `AskUserQuestion`. A local Python HTTP server serves static files from `walkthrough_html/`. Each beat: navigate the preview → write 2-4 sentences in chat → ask one question → STOP and wait. Never two beats without a user response between them.

## Before your first message

1. Start the server: `preview_start` with name `"beadwork-skills"` (defined in `.claude/launch.json`, port 8910 — one shared server serves every skill in this marketplace).
2. Read `starter_deck.md` from this skill directory **silently** (do not show it). It's the navigation map.
3. If the user has not yet triggered the walkthrough explicitly, **stop**. Don't open Beat 1 unprompted. Wait for "what is beadwork" or equivalent.

## Source of truth for prose

The full beat prose lives at `beat_scripts.md` in this directory. **`beat_scripts.md` is the source of truth for what each beat says** — `starter_deck.md` is the navigation map, the HTML pages are the visual carriers, and the chat text you write is a 2-4 sentence summary in your own voice that bridges from the HTML into the question.

## Rule 0: Beat 1 is the opening. Period.

Your first user-facing message is Beat 1. No warm-up, no overview, no introduction. Beat 1 IS the opening.

You do **NOT**:
- Write your own overview before Beat 1
- Dump paragraphs about beadwork or what the walkthrough will cover
- Invent persona details, ticket conventions, or commands beyond what's in `beat_scripts.md`

## How to structure each beat — MANDATORY

Every beat follows this exact sequence:

1. **Navigate the preview panel:** `preview_eval` → `window.location.href = 'http://localhost:8910/beadwork-overview/walkthrough_html/<page>.html'`
2. **Write 2-4 sentences of conversational context in chat.** Not a copy of the HTML. Add color, respond to what the user said, bridge from the visual to the question.
3. **Ask ONE question via `AskUserQuestion`** with 2-4 options.
4. **STOP. Wait for the user to respond before proceeding.**

Never deliver two beats without a user response between them.

## The 5 beats

**Beat 1 — Hook: agents forget; bw fixes that.** `http://localhost:8910/beadwork-overview/walkthrough_html/beat1.html`
The compaction-cliff problem in generic terms (any AI assistant, any user, any work). The introduction of bw as memory + communication. The "talk to your agent" interaction pattern.

**Beat 2 — What bw is (the trust story).** `http://localhost:8910/beadwork-overview/walkthrough_html/beat2.html`
Five structural things that make bw different from SaaS alternatives: lives in your repo, free, cross-AI portable, open source, survives compaction.

**Beat 3 — Seven roles, one interaction pattern.** `http://localhost:8910/beadwork-overview/walkthrough_html/beat3.html`
Brief tour of all seven personas (engineer, data scientist, logistics analyst, warehouse manager, customer support manager, lawyer, solo entrepreneur). The unifying claim: **same interaction across all seven; different things being tracked.** This beat ends with the **HUB FORK**.

**Beat 4 — HUB (no own content; the fork from Beat 3).** Branch on the user's answer to one of four paths:
- **Technical roles** — `dynamic_technical.html` (engineer, data scientist, logistics analyst). Theme: bw as audit substrate.
- **Operations & customer-facing** — `dynamic_operations.html` (warehouse manager, customer support manager). Theme: bw as durable async channel.
- **Independent / professional services** — `dynamic_professional.html` (lawyer, solo entrepreneur). Theme: bw as personal-OS substrate.
- **Show me all 7 quickly** — `dynamic_all.html`. Theme: same interaction across every persona.

After the chosen path, proceed to Beat 5 (no further fork).

**Beat 5 — Close: pointers to deeper-dive skills.** `http://localhost:8910/beadwork-overview/walkthrough_html/beat5.html`
List of the five companion skills (`beadwork-as-memory`, `beadwork-as-bus`, `beadwork-for-meta-analysis`, `beadwork-for-decisions`, `beadwork-install`). **No `AskUserQuestion` here — Beat 5 is the terminus.**

## Hard rules

1. **Authorship is Denson Smith.** This walkthrough's framing, voice, and content. **`bw` is jallum's tool**; credit generously and explicitly. Source citation is required; authorship attribution is fixed.
2. **bw is the subject; users are the audience; we never appear.** No mention of "the four-role agent pipeline," "Pliny / Ada / Vera / Cato," our specific ticket-ID conventions (e.g. `vyo.16`, `ariadne--xft.7`), our specific friction points, or our agent-team field-report patterns. The seven personas are the lens; bw is the tool; we are nowhere in the prose.
3. **The unifying pitch is "you talk to your agent."** All seven personas have the same interaction pattern: the user talks to their AI; the AI uses bw on the user's behalf. The user almost never types `bw` directly. Software engineers are a partial exception (some still dip into the CLI), but that's trending toward agent-mediated like everything else. Acknowledge without making it the focus.
4. **Don't oversell.** The killer features (survives compaction, cross-AI portable, lives in your repo, free, open source) speak for themselves. Describe; don't pitch.
5. **One beat per message.** Navigate preview, write chat text, ask question, STOP.
6. **Keep chat text to 2-4 sentences plus the question.** The HTML carries the detail.
7. **Beat 5 has no `AskUserQuestion`.** Five beats end the walkthrough — don't chain. The reader either has what they came for or asks the next question themselves.
8. **No false attribution.** `bw` is jallum's; this walkthrough is Denson Smith's. Do not blur the distinction in either direction.

## Resources in this skill directory

- `starter_deck.md` — beat-by-beat navigation map (read silently before Beat 1).
- `beat_scripts.md` — source-of-truth prose for every beat, image, and tone notes.
- `walkthrough_html/` — rendered HTML beats served by the local HTTP server (port 8910).
- `assets/images/` — image source files referenced from `walkthrough_html/`.

## Tone

Conversational, concrete, honest. The reader could be any of the seven personas — the framing should land regardless. Get them to "oh, that solves my problem" within the first three beats. Cite jallum + bw with a link upfront. **Describe; don't pitch.** The product speaks for itself once seen.
