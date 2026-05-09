---
name: beadwork-overview
description: "Interactive overview of beadwork (bw — github.com/jallum/beadwork). Universal elevator pitch (AI assistants forget; here's a tool that helps before you get locked into a SaaS memory vendor), then the plain-English explanation of git + the four storage modes (local-only free; cloud backup paid; team cloud paid; public free) + what the user authorizes. Defaults to plain-English; software-engineer audiences can opt in to the technical version. Triggers: what is beadwork, what is bw, beadwork overview, why bw, why beadwork, who uses bw, beadwork tour, explain beadwork, walk me through beadwork, do I need beadwork."
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

1. **Navigate the preview panel:** `preview_eval` → `window.location.href = 'http://localhost:8910/beadwork-overview/walkthrough_html/<page>.html?v=' + Date.now()` (the cache-bust query string ensures the user sees fresh content after edits).
2. **Write 2-4 sentences of conversational context in chat.** Not a copy of the HTML. Add color, respond to what the user said, bridge from the visual to the question.
3. **Ask ONE question via `AskUserQuestion`** with 2-4 options. **Each option must map to a specific page or destination — never deflect a question with a different question.**
4. **STOP. Wait for the user to respond before proceeding.**

Never deliver two beats without a user response between them.

## The beat structure

This walkthrough has **4 beats** (5 if the user opts into the developer-flavored Beat 2 sibling).

**Beat 1 — Elevator pitch.** `walkthrough_html/beat1.html`
Universal hook for all audiences. **Lead is a SaaS-lock-in warning:** *"AI assistants forget. A whole industry is gearing up to sell you the answer. Look at `bw` before you get locked in — it's free, open source, and might be all you need."* Followed by the three forgetting modes (session ends, second concurrent session, mid-session compaction/drift), the three-tier escalation (memory across sessions / multi-session same-lab specialist team / cross-human team), and three reassurances (don't have to learn it / can stay on your computer / free + open source).

**Beat 2 — What bw is.** Two pages, user picks at Beat 1:
- `walkthrough_html/beat2_everyone.html` — **default plain-English version.** Explains what git is from scratch, what bw does on top of git, four storage modes with honest pricing (local-only free / cloud backup ~$4/mo GitHub Pro / team cloud ~$4/person/mo GitHub Team / public free), and what the user is authorizing their AI to do (install git, install bw, create a notes folder, read/write inside it).
- `walkthrough_html/beat2_coder.html` — **opt-in developer view.** Tight SWE pitch: orphan branch storage, single Go binary, cross-AI portable, MIT-licensed, survives compaction. Three-tier escalation in dev terms.

**Beat 3 — Where it helps.** `walkthrough_html/beat3.html`
Seven persona snapshots showing the same memory + agent-coordination pattern across very different jobs (engineer, data scientist, logistics analyst, warehouse manager, support manager, lawyer, solo entrepreneur). Same interaction in every case; what differs is what each role tracks.

**Beat 4 — Close + next-skill router.** `walkthrough_html/beat4.html`
The canonical 6-skill companion list with a "← you are here" pill on **`beadwork-overview`**. CTA-style install row: *"install now; your AI does the work. Then stop re-explaining."* **AskUserQuestion at the end** routes the user to whichever next-skill they want to tour, or to install — the companion list is a real fork, not a dead-end.

## Routing rules (the only branch is at Beat 1)

After Beat 1's `AskUserQuestion`, route based on user's pick:

| User picks | Next page | Chat framing emphasis |
|---|---|---|
| "Continue — show me what bw actually is" | `beat2_everyone.html` | Standard plain-English tour |
| "What's the catch? Costs / privacy / what's required" | `beat2_everyone.html` | **Lead the chat with the storage-modes / costs / authorization-stack section** — the page is the same but the framing primes that content |
| "I'm a developer, give me the technical version" | `beat2_coder.html` | SWE-flavored framing |
| "Skip ahead — show me the install" | exit overview, switch to `beadwork-install` skill | n/a |

After Beat 2 (either variant), proceed to Beat 3 (use cases). After Beat 3, proceed to Beat 4 (close). No further branches.

If a user is mid-tour on the everyone path and says "I'm a developer, can you give me the technical version?" — navigate to `beat2_coder.html` and continue.

## Hard rules

1. **Metadata authorship is Denson Smith (immutable).** All marketplace metadata, `plugin.json`, `LICENSE`, `SKILL.md` author fields, etc. credit Denson Smith and never anyone else. **But in user-facing walkthrough prose, do NOT credit Denson Smith.** The closing attribution mentions only jallum + `bw`. Source citation (jallum) is required; self-credit in prose is dropped.
2. **bw is the subject; users (the seven personas) are the audience; we never appear.** No mention of "the four-role agent pipeline," "Pliny / Ada / Vera / Cato," our specific ticket-ID conventions (e.g. `vyo.16`, `ariadne--xft.7`), our specific friction points, or our agent-team field-report patterns. The seven personas are the lens; bw is the tool; we are nowhere in the prose.
3. **The unifying pitch is "you talk to your agent."** The user almost never types `bw` directly. Software engineers are a partial exception (some still dip into the CLI), but that's trending toward agent-mediated like everything else. Acknowledge without making it the focus.
4. **Don't claim bw "fixes" anything.** It "helps in many cases." It "addresses." It "lets you." Not "fixes" or "solves." Same goes for the deep-dive skills.
5. **The three-tier escalation is load-bearing.** Memory across time → **a team of agents coordinating (usually same-lab, multi-session)** → memory across humans-on-a-team. Hit all three early; don't bury the team angle. **Lead tier 2 with same-lab multi-session ("a team of specialists from the same lab"), not with cross-vendor interop** — most users live in one ecosystem; cross-lab is a real but secondary case.
6. **Storage-mode framing for non-coders.** The headline option is **local-only on one computer, free, no online account at all.** Surface this first and clearly — many users will stop right there. **Cloud backup (laptop-crash survival + cross-device sync) is framed as a paid GitHub plan (~$4/month for personal, ~$4/person/month for team)** — this is the simplest path for a non-coder. (Empirical footnote for the curious: free GitHub accounts technically support private repos too, but for non-coders the paid plan is the smoother setup; don't over-explain in chat.) **For coders (`beat2_coder.html`),** the empirical reality (free covers solo private cloud) is fine to state directly.
7. **Each AskUserQuestion option maps to a specific page or destination.** Never deflect "what's the catch?" by asking a different question. The user's choice should determine where the tour goes next.
8. **Default to plain English.** Don't ask the user whether they're a developer. If they are, they'll say so or pick the technical option in Beat 1. Plain English is inclusive of both audiences.
9. **One beat per message.** Navigate preview, write chat text, ask question, STOP.
10. **Keep chat text to 2-4 sentences plus the question.** The HTML carries the detail.
11. **Beat 4 ends with an `AskUserQuestion` that routes to the next skill** (or to install, or to "stop here"). The companion-list visual on the page is paired with an actionable picker in chat — the user shouldn't have to type a skill name freeform to get there.
12. **No false attribution.** `bw` is jallum's — credit explicitly in prose and metadata. This walkthrough's *metadata* attributes to Denson Smith (LICENSE, plugin.json, etc., all immutable); the *prose* drops self-credit. Never put jallum or anyone else in author/owner/copyright fields of artifacts Denson built — that is the immutable rule and the bigger safety concern.

## Resources in this skill directory

- `starter_deck.md` — beat-by-beat navigation map (read silently before Beat 1).
- `beat_scripts.md` — source-of-truth prose for every beat, image, and tone notes.
- `walkthrough_html/` — rendered HTML beats served by the local HTTP server (port 8910).
- `assets/images/` — image source files referenced from `walkthrough_html/`.

## Tone

Conversational, concrete, honest. **Describe; don't pitch.** The reader could be any of the seven personas — the framing should land regardless. The default everyone path uses plain English (explains git, repos, CLI in friendly terms). The `beat2_coder.html` opt-in uses developer vocabulary. **Cite jallum + bw with a link upfront.** The product speaks for itself once seen.
