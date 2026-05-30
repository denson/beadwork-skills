# beadwork-skills

A skills marketplace for [**beadwork**](https://github.com/jallum/beadwork) (`bw`) — git-native AI memory and agent-to-agent coordination, by [**jallum**](https://github.com/jallum).

> **AI assistants forget.** A whole industry is gearing up to sell you the answer.
> Look at `bw` before you get locked in — it's free, open source, and might be all you need.

---

## Hand it to your AI

You don't read the brief — *your AI does.* It maps `bw` onto what it already knows about how you work and tells you whether `bw` would actually help, **including if it wouldn't.** You pay with attention; your AI does the cognitive work. Two ways to hand it over:

- **Paste the text — works with any assistant.** Open the brief, copy it, paste it into your AI (Claude, ChatGPT, Gemini, Cursor — whatever you use) with:
  > *Based on how I work, would beadwork help me? Be honest — don't sell it.*

  Reliable whether or not your assistant can browse the web.
- **Paste a link — if your assistant browses the web.**
  - Web page (most browsing chatbots): `https://denson.github.io/beadwork-skills/brief.html`
  - Raw brief (coding agents / tools that read `AGENTS.md` by convention): `https://denson.github.io/beadwork-skills/AGENTS.md`

  If your assistant says it can't open the link, **switch to pasting the text — don't let it guess from the name.** (Some chatbots won't fetch a file named `AGENTS.md` — it looks like untrusted agent instructions — or simply can't browse arbitrary URLs. The `brief.html` page and the paste-the-text method both sidestep that.)

## What your AI does with it

- **Read & advise — any AI.** A tailored, honest read of whether `bw` fits *your* work.
- **Show you the guides — any AI that can open a web page.** A set of plain-language pages it can walk you through, link, or summarize. Start at [the guides](https://denson.github.io/beadwork-skills/guides/g1-is-bw-for-you.html).
- **Set it up — any agent that can run shell commands** (Claude Code, Cursor, etc.). Drives the install end to end, or walks you through the four manual steps.

---

## Want it permanently in Claude Code Desktop?

For ongoing access to the skills (refreshers, sharing with teammates, future sessions), three slash commands install everything:

```
/plugin marketplace add denson/beadwork-skills
/plugin install beadwork@beadwork-skills
/beadwork-skills:beadwork-overview
```

The marketplace install is **Claude-Code-Desktop-specific.** For every other environment, the brief above — `brief.html` or pasted text — gives the same content without an install.

---

## What's in the marketplace

Six skills under the `beadwork-skills` plugin. The first five are thin, **agent-agnostic playbooks** — each points your AI at the relevant plain-language [guides](https://denson.github.io/beadwork-skills/guides/g1-is-bw-for-you.html) to show, link, or explain, and adds conversation suggestions (no fixed script). The install skill drives setup.

| Skill | What it covers |
|---|---|
| `beadwork-overview` | Introduce `bw` and help someone judge fit: the hook, the four storage modes, who it's for. Default entry point. |
| `beadwork-as-memory` | Durable memory: what survives across sessions, machines, vendor swaps, and time, and how the record reconstructs context months later. |
| `beadwork-as-bus` | Multiple agents (and people) sharing one workspace — a team of specialists (usually same-lab), plus cross-team / cross-organization coordination. |
| `beadwork-for-meta-analysis` | Pointing one agent at the recorded work of *other* agents to audit, check methodology, or synthesize. |
| `beadwork-for-decisions` | `bw` as decision log / ADR / audit trail — the "why did we decide X?" answer six months later. |
| `beadwork-install` | Drives setup end to end. Adapts to `bw`'s release state; surfaces platform security prompts; presents the storage-mode choice with explicit warnings. |

After installing, all six are available as `/beadwork-skills:<skill-name>` in Claude Code Desktop, or trigger on phrases like *"what is beadwork"* / *"install bw."*

---

## About bw

`bw` is [**beadwork**](https://github.com/jallum/beadwork), an orphan-branch ticket store. It keeps tickets, comments, and decision history on a dedicated git branch — never checked out, never merged into product code, just there in the repo's git database. Free, no auth, no server, no signup, single binary.

The property that matters most: **survives compaction.** Tickets and comments persist across session boundaries, agent restarts, machine swaps, AI-vendor swaps, and time. Any AI that can shell out to `bw show` reads the same store.

This marketplace is built on top of `bw`; we didn't write `bw` itself. **Credit `bw` to jallum.**

---

## Storage modes (honest pricing, not behind a paywall)

| Mode | Cost | When to choose |
|---|---|---|
| **Local-only on one computer** | **free** (no online account at all) | Solo, single-machine, max privacy. Headline option for non-coders. |
| Cloud backup + cross-device sync | ~$4/month (GitHub Pro) | Survives laptop crash; syncs across your devices. |
| Team cloud | ~$4/person/month (GitHub Team) | Multiple humans + their AIs share one substrate. Adds team-management features. |
| Public cloud | free (free GitHub account) | **Only for non-sensitive work.** Anyone on the internet can read it. |

Many users will hear *"free, on your computer, no account"* and stop reading. That's intentional — the headline option is the simplest and the most private. The cloud modes are for users who specifically want backup or team coordination.

---

## License & attribution

[MIT](LICENSE), copyright (c) 2026 Denson Smith.

`bw` itself is also MIT, by [jallum](https://github.com/jallum).

The marketplace was developed and tested in **Claude Code Desktop**, but `bw`, the brief, the [guides](https://denson.github.io/beadwork-skills/guides/g1-is-bw-for-you.html), and the skills are deliberately model-agnostic. The marketplace *install* is the only Claude-Code-Desktop-specific piece — and it's optional. Other labs' tools (GPT, Gemini, Cursor, etc.) read the brief ([`brief.html`](https://denson.github.io/beadwork-skills/brief.html) or [`AGENTS.md`](./AGENTS.md)) and advise you in your context, no install required.
