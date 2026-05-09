---
name: beadwork-overview
description: "Interactive overview of beadwork (bw — github.com/jallum/beadwork). Universal elevator pitch (AI assistants forget; here's a tool that helps), then forks on user audience: a coder version (assumes git fluency) and an everyone-else version (explains git, storage modes, and what they're authorizing their AI to do, in plain English). Covers the three-tier shape: one AI's memory across sessions, multiple AI sessions coordinating as a team of specialists (usually within the same lab; cross-lab also possible), and team-of-humans-plus-AIs coordinating through a shared private repo. Triggers: what is beadwork, what is bw, beadwork overview, why bw, why beadwork, who uses bw, beadwork tour, explain beadwork, walk me through beadwork, do I need beadwork."
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
3. If the user has not yet triggered the walkthrough explicitly, **stop**. Don't open Beat 1 unprompted. Wait for "what is beadwork" or "do I need this" or equivalent.

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

## The beat structure

This walkthrough has **5 beats** with a literacy fork between Beat 2 and Beat 3.

**Beat 1 — Elevator pitch.** `walkthrough_html/beat1.html`
Universal hook for all audiences. **Lead is a SaaS-lock-in warning:** *"AI assistants forget. A whole industry is gearing up to sell you the answer. Look at `bw` before you get locked in — it's free, open source, and might be all you need."* That manifesto is the load-bearing claim for the whole walkthrough. After the lead: three things bw lets you do (escalating scope): (1) one AI remembers across sessions, (2) **multiple AI sessions coordinate as a team of specialist agents — usually sessions of the same lab's model (all Claude, all Gemini), with cross-lab interop as a secondary case**, (3) teams of humans + their AIs share notes through one substrate. Three reassurances up front: you don't have to learn it / can stay on your computer / free + open source.

**Beat 2 — Literacy fork.** `walkthrough_html/beat2.html`
The single branching question. AskUserQuestion: *"How do you mainly use AI?"* with options: writing code / writing-research-learning / business-or-personal-projects / something-else. Routing rule: **"writing code" → Beat 3 (coder); anything else → Beat 3 (everyone).** This beat's HTML is a brief transition card showing the four buckets; the question goes in chat.

**Beat 3 (coder) — What bw is, SWE-flavored.** `walkthrough_html/beat3_coder.html`
Tight technical pitch: orphan-branch storage, single Go binary, cross-AI portable, MIT-licensed, survives compaction. Restates the three layers (one-agent-time / many-agents-one-human / many-humans-many-agents) in dev terms (persistent context / async pipelines / push to shared remote).

**Beat 3 (everyone) — What bw is, plain-English.** `walkthrough_html/beat3_everyone.html`
The meaty plain-language explanation. Sections: what git is (and that they probably don't have it), what bw is doing on top of git, the four storage modes (local-only free / private-cloud free / team-cloud paid / public free) with explicit pricing, what they're authorizing their AI to do (install git, install bw, create a folder, read/write notes inside), and the standing reassurance that the AI does the work.

**Beat 4 — Where it helps.** `walkthrough_html/beat4.html`
Both paths converge here. Seven persona snapshots showing the same memory + agent-coordination pattern across very different jobs (engineer, data scientist, logistics analyst, warehouse manager, support manager, lawyer, solo entrepreneur). Closes with "same interaction in every case; what differs is what each role tracks."

**Beat 5 — Where to go from here.** `walkthrough_html/beat5.html`
Companion-skill list. **No `AskUserQuestion` here — Beat 5 is the terminus.**

## Routing rule (the only branch)

After Beat 2's `AskUserQuestion`:

| User picks | Next page |
|---|---|
| "Writing code" / "Software development" | `beat3_coder.html` |
| "Writing, research, learning" | `beat3_everyone.html` |
| "Business or personal projects" | `beat3_everyone.html` |
| "Something else" | `beat3_everyone.html` |

Both Beat 3 variants converge at Beat 4. There is no second fork.

## Hard rules

1. **Metadata authorship is Denson Smith (immutable).** All marketplace metadata, `plugin.json`, `LICENSE`, `SKILL.md` author fields, etc. credit Denson Smith and never anyone else. **But in user-facing walkthrough prose, do NOT credit Denson Smith.** The closing attribution mentions only jallum + `bw`. Source citation (jallum) is required; self-credit in prose is dropped.
2. **bw is the subject; users are the audience; we never appear.** No mention of "the four-role agent pipeline," "Pliny / Ada / Vera / Cato," our specific ticket-ID conventions (e.g. `vyo.16`, `ariadne--xft.7`), our specific friction points, or our agent-team field-report patterns. The seven personas are the lens; bw is the tool; we are nowhere in the prose.
3. **The unifying pitch is "you talk to your agent."** The user almost never types `bw` directly. Software engineers are a partial exception (some still dip into the CLI), but that's trending toward agent-mediated like everything else. Acknowledge without making it the focus.
4. **Don't claim bw "fixes" anything.** It "helps in many cases." It "addresses." It "lets you." Not "fixes" or "solves." Same goes for the deep-dive skills.
5. **The three-tier escalation is load-bearing.** Memory across time → **a team of agents coordinating (usually same-lab, multi-session)** → memory across humans-on-a-team. Hit all three early; don't bury the team angle. **Lead tier 2 with same-lab multi-session ("a team of specialists from the same lab"), not with cross-vendor interop** — most users live in one ecosystem; cross-lab is a real but secondary case.
6. **Storage-mode framing for non-coders.** The headline option is **local-only on one computer, free, no online account at all.** Surface this first and clearly — many users will stop right there. **Cloud backup (laptop-crash survival + cross-device sync) is framed as a paid GitHub plan (~$4/month for personal, ~$4/person/month for team)** — this is the simplest path for a non-coder. (Empirical footnote for the curious: free GitHub accounts technically support private repos too, but for non-coders the paid plan is the smoother setup; don't over-explain in chat.) **For coders (Beat 3-coder),** the empirical reality (free covers solo private cloud) is fine to state directly.
7. **One beat per message.** Navigate preview, write chat text, ask question, STOP.
8. **Keep chat text to 2-4 sentences plus the question.** The HTML carries the detail.
9. **Beat 5 has no `AskUserQuestion`.** Five beats end the walkthrough — don't chain. The reader either has what they came for or asks the next question themselves.
10. **No false attribution.** `bw` is jallum's — credit explicitly in prose and metadata. This walkthrough's *metadata* attributes to Denson Smith (LICENSE, plugin.json, etc., all immutable); the *prose* drops self-credit. Never put jallum or anyone else in author/owner/copyright fields of artifacts Denson built — that is the immutable rule and the bigger safety concern.

## Resources in this skill directory

- `starter_deck.md` — beat-by-beat navigation map (read silently before Beat 1).
- `beat_scripts.md` — source-of-truth prose for every beat, image, and tone notes.
- `walkthrough_html/` — rendered HTML beats served by the local HTTP server (port 8910).
- `assets/images/` — image source files referenced from `walkthrough_html/`.

## Tone

Conversational, concrete, honest. **Describe; don't pitch.** The reader could be any of the seven personas — the framing should land regardless. After Beat 2's literacy fork, the coder path uses developer vocabulary (repo, CLI, orphan branch); the everyone path explains those terms in plain English. **Cite jallum + bw with a link upfront.** The product speaks for itself once seen.
