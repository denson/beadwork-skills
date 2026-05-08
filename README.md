# beadwork-skills

A Claude Code skills marketplace for [**beadwork**](https://github.com/jallum/beadwork) (`bw`) — git-native work management for AI coding agents, written by [**jallum**](https://github.com/jallum).

The skills here are about what bw is and how seven different kinds of users — engineers, data scientists, warehouse managers, customer support managers, logistics analysts, lawyers, and solo entrepreneurs — use it through their AI assistants for **agent memory** and **agent-to-agent communication**.

The user pattern is the same across all seven: **you talk to your agent, and your agent uses bw to remember things and to communicate with other agents.** bw stays invisible.

## What's in this marketplace

| Skill | What it covers |
|---|---|
| `beadwork-overview` | What bw is + the seven personas + the trust story (git-native, no SaaS, free, cross-AI portable, open source). 5-6 minute walkthrough with a fork to dive deeper into one of three persona buckets — or the unified "show me all 7 quickly" path. |
| `beadwork-as-memory` | bw as durable agent memory across sessions, restarts, weeks. Persona examples woven in. |
| `beadwork-as-bus` | Multi-agent pipelines and cross-team / cross-organization coordination through bw as a shared store. |
| `beadwork-for-meta-analysis` | Running an agent over the bw history of *other agents* to audit, check methodology, or synthesize across many earlier sessions. The structural advantage over chat history. |
| `beadwork-for-decisions` | bw as decision log / ADR / audit trail / compliance record. |
| `beadwork-install` | Drive the install end-to-end (agent-execution shape — no preview panel). Storage-mode choice with explicit public-repo warning. |

Each skill is a self-contained directory under `skills/`.

The five presenter walkthroughs each run in Claude Code Desktop's preview panel on their own port (configured in `.claude/launch.json`). The install skill is read by the AI assistant directly — no preview panel, no port.

## About bw

`bw` is [**beadwork**](https://github.com/jallum/beadwork), an orphan-branch ticket store. It stores tickets, comments, and decision history on a dedicated git branch — never checked out, never merged into product code, just there in the repo's git database. Free, no auth, no server, no signup, single binary. The killer feature: **survives compaction.** Tickets and comments persist across Claude Code session boundaries, agent restarts, and crashes — and across machines, AI vendors, and time.

We didn't write `bw`; we built skills on top of it. This marketplace is what we made for sharing the patterns.

## Status

Under development. Skills are being authored from scratch (no carryover from the prior abandoned `bw-skills` repo).

## License

[MIT](LICENSE), copyright (c) 2026 Denson Smith.
