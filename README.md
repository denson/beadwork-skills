# beadwork-skills

A Claude Code marketplace for [**beadwork**](https://github.com/jallum/beadwork) (`bw`) — git-native AI memory and agent-to-agent coordination, written by [**jallum**](https://github.com/jallum).

> **AI assistants forget.** A whole industry is gearing up to sell you the answer.
> Look at `bw` before you get locked in — it's free, open source, and might be all you need.

---

## Two ways to start

### (1) If you have a daily-driver AI you trust — *one-liner*

Copy-paste this into your usual AI (Claude, ChatGPT, Gemini, Cursor, etc.):

> **Read this and tell me whether `bw` matters for me, given how you've been working with me:**
> `https://raw.githubusercontent.com/denson/beadwork-skills/main/AGENTS.md`

Your AI fetches the brief, translates it into your context, and tells you whether bw would actually help in your work — based on what it already knows about you. **You pay with attention; your AI does the cognitive work.**

(Why this works: the brief is the deck; your AI is the influencer who knows you. See [`AGENTS.md`](./AGENTS.md) for the deck itself.)

### (2) If you want a guided visual tour — *Claude Code Desktop*

Paste these three commands in Claude Code Desktop:

```
/plugin marketplace add denson/beadwork-skills
/plugin install beadwork@beadwork-skills
/beadwork-skills:beadwork-overview
```

The third command runs the overview walkthrough — six rich HTML beats with images and clickable choices. About 5 minutes.

---

## What's in the marketplace

Six skills under the `beadwork-skills` plugin. The first five are walkthroughs (HTML beats + AskUserQuestion); the install skill is agent-execution.

| Skill | What it covers |
|---|---|
| `beadwork-overview` | Seven-persona tour. SaaS-lock-in lead, three forgetting modes, four storage modes with honest pricing, the install pointer. ~5 minutes. |
| `beadwork-as-memory` | Durable memory deep-dive. How tickets + comments + authors + timestamps reconstruct context months later. Three time-horizons (week / year / cross-engagement). |
| `beadwork-as-bus` | Multi-session same-lab specialist-team coordination. Within-job, across-days, cross-team, cross-organization scenarios. Cross-lab interop is a secondary property. |
| `beadwork-for-meta-analysis` | Running an agent over the bw history of *other agents* to audit, check methodology, or synthesize. |
| `beadwork-for-decisions` | bw as decision log / ADR / audit trail. The "why did we decide X?" answer six months later. |
| `beadwork-install` | Drives setup end-to-end. Adapts to bw release state; surfaces platform security prompts; presents storage-mode choice with explicit warnings. |

After installing the marketplace, all six skills are available as `/beadwork-skills:<skill-name>` in Claude Code Desktop, or trigger automatically on phrases like *"what is beadwork"* / *"install bw"*.

---

## About bw

`bw` is [**beadwork**](https://github.com/jallum/beadwork), an orphan-branch ticket store. It stores tickets, comments, and decision history on a dedicated git branch — never checked out, never merged into product code, just there in the repo's git database. Free, no auth, no server, no signup, single binary.

The killer feature: **survives compaction.** Tickets and comments persist across Claude Code session boundaries, agent restarts, machine swaps, AI vendor swaps, and time. Any AI that can shell out to `bw show` reads the same store.

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

The marketplace was developed and tested in **Claude Code Desktop**, but `bw` and the [`AGENTS.md`](./AGENTS.md) brief are deliberately model-agnostic. The HTML walkthroughs are the only Claude-Code-Desktop-specific piece — and they're optional. Other labs' tools (GPT, Gemini, Cursor, etc.) can read [`AGENTS.md`](./AGENTS.md) and pitch bw to you in your context, no marketplace install required.
