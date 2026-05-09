# Beat scripts — beadwork-overview walkthrough

This is the **working-doc source of truth** for what each beat says. The HTML pages in `walkthrough_html/` carry the visual presentation; this file carries the words. Chat text in CCD is a 2-4 sentence summary that bridges from the HTML into the AskUserQuestion — write it in your own voice, but use the prose here as the spec.

**Structure:** 5 beats with a single literacy fork between Beat 2 and Beat 3.

```
Beat 1 (universal hook)
   ↓
Beat 2 (literacy ASK: how do you use AI?)
   ↓
   ├── "writing code"     → Beat 3-coder
   └── anything else      → Beat 3-everyone
                              ↓
                       Beat 4 (universal use cases — both paths converge)
                              ↓
                       Beat 5 (close)
```

Tone rules across all beats:
- **Never claim bw "fixes" anything.** It "helps in many cases." Use "helps" / "addresses" / "lets you" — not "fixes" / "solves."
- **Three-tier escalation lands early:** one AI's memory across time → multiple AIs sharing notes → multi-human team coordination.
- **The non-coder doesn't have to learn anything.** Their AI does the work. Repeat this reassurance.

---

## Beat 1 — Elevator pitch (universal hook)

### Chat (3-4 sentences)

**AI assistants forget — chats end, second sessions don't know about the first, and even mid-session details get lost (Claude Code's compaction summarizes when context fills; OpenAI and Gemini models drift gradually as the chat grows).** A whole industry is gearing up to sell you the answer. **Look at [`bw`](https://github.com/jallum/beadwork) (beadwork) before you get locked in: it's free, open source, and might be all you need.** Three things it does: durable memory across sessions, multi-session coordination as a team of specialists (usually all from the same lab), and humans-plus-agents sharing one workspace. **You don't have to learn it — your AI does.**

### AskUserQuestion

> Sound interesting?

Options:
- **Yes, tell me more** — proceed to Beat 2 (the literacy fork).
- **First, what's the catch?** — short detour: it's free and open source, your data stays where you tell it to (your computer or your cloud), it's a small CLI tool that ships with instructions for your AI to install. Then proceed to Beat 2.
- **Skip ahead — show me the install** — exit overview; switch to `beadwork-install` skill.

### Image

`walkthrough_html/images/beat1-hook.jpg` — A two-panel split scene. LEFT: a generic AI assistant figure looking confused, thought bubble *"wait — what was I doing?"* RIGHT: same figure, calm, reading from a small ticket card; thought bubble *"right — yesterday we decided X, the next step is Y."* Bottom-right label: *"context restored from `bw show`."*

Caption: *"Sessions end. Context shouldn't."*

### Tone + length notes

- **The lead is a SaaS-lock-in warning, not a feature pitch.** "AI assistants forget. A whole industry is gearing up to sell you the answer. Look at bw before you get locked in — it's free, open source, and might be all you need." This is the load-bearing manifesto for the entire walkthrough; everything else is supporting evidence.
- **Three forgetting modes named explicitly:** (1) session ends → next chat starts blank, (2) second concurrent session of the same AI → doesn't know about the first, (3) mid-session forgetting (Claude Code's *compaction*; OpenAI/Gemini's gradual drift as context fills). Worth saying all three; users have hit at least one.
- **Lead callout drops "by jallum" text.** The repo link (github.com/jallum/beadwork) carries the attribution implicitly via the URL. Visible "by jallum" text reads as pitchy double-credit in the headline.
- The **three-tier escalation** lands here. Don't drop any of the three. Specifically:
  - **Tier 1 — memory across time:** one AI session reads what an earlier session wrote.
  - **Tier 2 — a team of agents coordinating.** This is **multi-session coordination, usually within the same lab** (multiple Claude sessions, or multiple Gemini sessions) acting as specialist agents — design, implementation, review. **Cross-lab interop (Claude + Gemini sharing one store) is a real but secondary case** — mention it as "and the same mechanism works across vendors too" rather than leading with it.
  - **Tier 3 — humans on a team plus their agents.** Multiple humans, each with their own AI, all reading and writing the same shared notes.
- **No "fix" or "solve" language.** "Helps in many cases."
- The reassurance trio (don't have to learn it / can stay on your computer / free + open source) is part of the elevator pitch, not an afterthought.
- 3-4 sentences in chat; lean shorter.
- Cite jallum + bw with a link upfront. Credit the source.

---

## Beat 2 — The literacy fork

### Chat (2-3 sentences)

Quick question before going deeper. The next page splits two ways: a "you're a developer, you know git" version and a plain-English version that explains everything from scratch. **Same tool, same story — just different vocabulary.**

### AskUserQuestion

> How do you mainly use AI?

Options:
- **Writing code** — software development, scripts, infra, automation. → routes to **Beat 3-coder.**
- **Writing, research, learning** — drafting, analysis, study, summaries. → routes to **Beat 3-everyone.**
- **Business or personal projects** — operations, customers, finance, legal, life admin. → routes to **Beat 3-everyone.**
- **Something else** — a mix, or none of the above. → routes to **Beat 3-everyone.**

### Image

No ConceptViz image — the HTML uses CSS-only audience cards as the visual focus. The question is the centerpiece.

### Tone + length notes

- This is a transition beat. Short. Light. The question is the focus.
- **The default for non-"writing code" answers is the everyone fork.** Don't try to be clever; if there's any ambiguity, route to everyone — it's the more inclusive starting point.

---

## Beat 3-coder — What bw is, SWE-flavored

### Chat (4-5 sentences)

Skipping the long version since you're a developer. **Storage:** orphan branch in a git repo, plain JSON files. **Install:** single Go binary, one-line curl or build from source. **Cross-AI portable:** anything that can shell out to `bw show` reads the same store. **License:** MIT, jallum's project. **And the killer feature: it survives compaction** — tickets and comments persist across session boundaries, agent restarts, machine swaps. The three-tier escalation in your terms: persistent context for one session graph → multi-agent async pipelines → push the orphan branch to a shared remote and the team's agents read/write the same store via standard PR/review workflow.

### AskUserQuestion

> Want to see where this kind of memory + coordination earns its keep?

Options:
- **Yes, show me where it helps** — proceed to Beat 4.
- **First — install path?** — short detour: bw is jallum's; install via `install.sh` from the repo or `go build` from source. Then proceed to Beat 4.

### Image

`walkthrough_html/images/beat2-trust.jpg` (reused) — folder labeled "your repo / your disk" with project files top, "beadwork (orphan branch)" compartment bottom containing tickets. Multiple AI vendor icons reading/writing into the bw compartment. Label outside: *"no SaaS, no vendor servers, no signup."*

Caption: *"Lives where your code lives."*

### Tone + length notes

- Tight. SWE knows the words. Don't over-explain.
- The cross-AI portability point is under-told in the wider market — emphasize.
- "Survives compaction" is jallum's headline feature — call it out.

---

## Beat 3-everyone — What bw is, plain-English

### Chat (4-6 sentences)

Plain-English version. **Git** is a free, very-reliable tool that's been around for nearly twenty years — programmers use it for code, but `bw` uses it because it's the most trustworthy place we have to put notes. You probably don't have it installed yet; that's fine — your AI installs it for you. **`bw` itself is a small program** that uses git to keep a "shelf" of notes in a folder you point it at. **The simplest mode is free:** notes stay on one computer, no online account at all. **If you want cloud backup that survives a laptop crash and syncs across your devices,** that's a paid GitHub plan (~$4/month for personal, or ~$4/person/month for a team). There's also a public-cloud mode (free; only for non-sensitive work). **You're authorizing your AI to install git, install bw, create a notes folder, and read/write inside it. That's all.**

### AskUserQuestion

> Storage mode preference, or skip ahead?

Options:
- **My computer only — maximum privacy, no online account** — note the preference; reassure them this is the simplest free mode; proceed to Beat 4.
- **Cloud backup so my laptop dying isn't a disaster** — note the preference; mention this is GitHub Pro (~$4/month); proceed to Beat 4.
- **Shared with my team** — note the preference; mention GitHub Team (~$4/person/month) for the polished experience; proceed to Beat 4.
- **Show me where this helps first; I'll pick later** — proceed to Beat 4 without a storage-mode commitment.

### Image

`walkthrough_html/images/beat2-trust.jpg` (reused, framed differently in chat) — same folder + bw + multiple AIs diagram; the "no SaaS" label still applies; in plain-English context, frame it as "this all lives in a folder on your computer."

Caption: *"Lives in a folder on your computer."*

### Tone + length notes

- **No assumed knowledge.** Explain "git" before assuming the reader knows what it is. Explain "repo" if you use the word.
- **Storage modes (non-coder framing — emphasize the free local-only mode first):**
  - **Local-only on one computer: free, no online account at all.** This is the headline option. Surface it first and clearly. The trade-off: if the laptop dies, the notes go with it.
  - **Cloud backup + cross-computer sync: ~$4/month** (paid GitHub Pro). This is what survives a laptop crash and lets the user pick up on another device. *(Technical footnote: free GitHub accounts also support private repos, but the paid plan is the smoother non-coder setup. Don't over-explain this in chat.)*
  - **Team cloud: ~$4/person/month** (GitHub Team) for the team-management features (CODEOWNERS, branch protection, audit log).
  - **Public: free; warn explicitly** that "anyone on the internet can read it."
- **Risk frame** is required: what is the AI authorized to do? Install git, install bw, create a folder, read/write inside it. That's it. The bw tool itself can't make purchases or send messages.
- Repeat the **"you don't have to learn anything"** reassurance at the end.

---

## Beat 4 — Where this kind of memory helps (universal use cases)

### Chat (4-6 sentences)

This is where both paths converge. The same tool works for very different jobs because the underlying need — *"my AI should remember things and my AIs should be able to share notes"* — shows up everywhere. Quick tour of seven shapes: **engineer** running multi-agent PR review with a synthesizer agent on top; **data scientist** keeping a multi-session investigation that a methodology auditor can review months later; **logistics analyst** with vendor scorecards that explain abandoned approaches; **warehouse manager** with day/night shift handoffs and cross-organization vendor coordination; **support manager** with engineering + manager AIs writing to one escalation ticket; **lawyer** with privilege determinations preserved verbatim for opposing counsel nine months later; **solo entrepreneur** with every business decision logged, ready for tax-time defense. **Same interaction in every case** — you talk to your AI, the AI uses bw on your behalf. What differs is what each role tracks, not how they interact with the tool.

### AskUserQuestion

> Want pointers to deeper-dive skills?

Options:
- **Yes — show me the companion skills** — proceed to Beat 5.
- **Just the install** — exit overview; switch to `beadwork-install` skill.

### Image

`walkthrough_html/images/beat3-personas.jpg` (reused — the seven-persona grid). Banner: *"all seven: talk to your agent. agent uses bw."*

Caption: *"Same interaction in every case."*

### Tone + length notes

- Both forks land here, so the prose can't lean too hard on either coder vocabulary or non-coder explanation. Stay neutral; rely on the personas to do the work.
- The **team angle** (warehouse manager + support manager especially) reinforces the third tier of the escalation — no need to repeat the framing, just let the examples carry it.
- **Don't oversell.** Each persona gets one phrase.

---

## Beat 5 — Where to go from here

### Chat (3-4 sentences)

This was the overview. Five companion skills go deeper on specific use-case angles, plus an install skill that drives setup end-to-end. **`beadwork-as-memory`** for the durable-agent-memory deep-dive. **`beadwork-as-bus`** for multi-agent + multi-team + multi-org communication patterns. **`beadwork-for-meta-analysis`** for running an agent over the bw history of *other agents*. **`beadwork-for-decisions`** for decision logs / audit trails. **`beadwork-install`** drives the install end-to-end — your AI runs it for you. All open source, MIT-licensed. `bw` itself is [jallum](https://github.com/jallum)'s project at [github.com/jallum/beadwork](https://github.com/jallum/beadwork).

### AskUserQuestion

**None.** Beat 5 is the terminus. End with the message above and stop.

### Image

`walkthrough_html/images/beat5-close.jpg` — five companion-skill cards in a 3-2 grid (memory, bus, meta-analysis, decisions, install). Bottom caption: *"open source, MIT-licensed. bw by jallum (github.com/jallum/beadwork)."*

Caption: *"Five companion skills."*

### Tone + length notes

- Wrap-up. Forward-pointing.
- 3-4 sentences plus the skill list.
- No `AskUserQuestion`.
- **The closing attribution credits jallum + bw only.** Do NOT credit Denson Smith in the user-facing prose. The metadata authorship (LICENSE, plugin.json, marketplace.json, etc.) stays Denson Smith — that's the immutable rule — but the walkthrough prose itself only credits jallum as the author of `bw` the tool.
- One sentence reserved for the non-coder reassurance: *"if you're not a coder, the install skill walks your AI through everything — you don't need to know git or run commands yourself."*
