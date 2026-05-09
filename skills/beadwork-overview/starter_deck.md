# Starter Deck — beadwork-overview Walkthrough

**STATUS: assembled.** All HTML pages live under `walkthrough_html/`. Image references resolve to existing ConceptViz output.

This file is the **navigation map** for the walkthrough — beat IDs, URLs, image filenames, structural notes that the presenter agent reads silently before Beat 1. It is NOT the source of truth for prose; that's `beat_scripts.md` next door.

Read this silently before starting. All hard rules from `SKILL.md` apply.

---

## Flow at a glance

```
Beat 1 (universal hook + ASK)
   ↓
   ├── "Continue" / "What's the catch?"  → Beat 2 (beat2_everyone.html)
   ├── "I'm a developer, technical view"  → Beat 2 (beat2_coder.html)
   └── "Skip to install"                  → exit to beadwork-install
                                              ↓
                                           Beat 3 (beat3.html — where it helps)
                                              ↓
                                           Beat 4 (beat4.html — close, terminus)
```

**Single fork at Beat 1.** Beat 2 has two sibling pages (everyone is the default; coder is opt-in). After Beat 2, both flows converge at Beat 3. Beat 4 has no question.

**Cache-bust on every preview navigation.** Always append `?v=' + Date.now()` to the navigation URL so users see fresh content immediately after edits land.

---

## Beat 1 — Elevator pitch + ASK

- **File:** `walkthrough_html/beat1.html`
- **Image:** `walkthrough_html/images/beat1-hook.jpg`
- **Navigate:** `https://denson.github.io/beadwork-skills/skills/beadwork-overview/walkthrough_html/beat1.html?v=<timestamp>`
- **Chat shape:** 3-4 sentences naming the three forgetting modes, the SaaS-lock-in warning lead, the three-tier escalation, and the three reassurances. See `beat_scripts.md` Beat 1.
- **Question:** "Sound interesting?" — 4 options that each map to a destination:
  - **Continue** → `beat2_everyone.html`
  - **What's the catch?** → `beat2_everyone.html` (different chat framing)
  - **I'm a developer** → `beat2_coder.html`
  - **My AI knows me best — give me an AGENTS.md to hand to it** → read `<marketplace-root>/AGENTS.md`, paste in chat, exit structured tour
  - (auto "Other" — for "skip to install" or any freeform)

---

## Beat 2 — What bw is

### Beat 2-everyone (default plain English)

- **File:** `walkthrough_html/beat2_everyone.html`
- **Image:** `walkthrough_html/images/beat2-trust.jpg` (reused — framed in chat as "lives in a folder on your computer")
- **Navigate:** `https://denson.github.io/beadwork-skills/skills/beadwork-overview/walkthrough_html/beat2_everyone.html?v=<timestamp>`
- **Chat shape:** 4-6 sentences explaining git first, then what bw does on top of git, then the four storage modes with empirically-correct pricing, then the authorization stack. See `beat_scripts.md` Beat 2 (everyone).
- **Question:** "Storage mode preference, or skip ahead?" — 4 options, all proceed to Beat 3.

### Beat 2-coder (opt-in developer view)

- **File:** `walkthrough_html/beat2_coder.html`
- **Image:** `walkthrough_html/images/beat2-trust.jpg` (reused)
- **Navigate:** `https://denson.github.io/beadwork-skills/skills/beadwork-overview/walkthrough_html/beat2_coder.html?v=<timestamp>`
- **Chat shape:** 4-5 sentences with developer vocabulary. Storage = orphan branch + JSON. Single Go binary. Cross-AI portable. MIT-licensed. Survives compaction. See `beat_scripts.md` Beat 2 (coder).
- **Question:** "Want to see where this kind of memory + coordination earns its keep?" — 2 options, both proceed to Beat 3.

---

## Beat 3 — Where this kind of memory helps

- **File:** `walkthrough_html/beat3.html`
- **Image:** `walkthrough_html/images/beat3-personas.jpg` (seven-persona grid — filename matches new beat numbering)
- **Navigate:** `https://denson.github.io/beadwork-skills/skills/beadwork-overview/walkthrough_html/beat3.html?v=<timestamp>`
- **Chat shape:** 4-6 sentences walking the seven persona snapshots quickly. Stay neutral on coder/non-coder vocabulary so both forks land cleanly here. See `beat_scripts.md` Beat 3.
- **Question:** "Want pointers to deeper-dive skills?" — 2 options.

---

## Beat 4 — Close (terminus)

- **File:** `walkthrough_html/beat4.html`
- **Image:** `walkthrough_html/images/beat5-close.jpg` (filename retains old "beat5" prefix; image content matches the close)
- **Navigate:** `https://denson.github.io/beadwork-skills/skills/beadwork-overview/walkthrough_html/beat4.html?v=<timestamp>`
- **Chat shape:** 3-4 sentences. The companion-skills list with "← you are here" on `beadwork-overview` lives in the HTML; the punchy install row at the bottom is the natural CTA. **`AskUserQuestion` at the end has 2 options + auto Other:** "Next: beadwork-as-memory" / "Stop" / Other (for install jump or any specific skill).

---

## Storage-mode pricing reference

### For non-coders (Beat 2-everyone) — simplified narrative

| Mode | Cost | Account needed |
|---|---|---|
| **Local-only, one computer** (the headline option) | **free** | **none** |
| Cloud backup + cross-device sync | ~$4 / month | GitHub Pro |
| Team cloud | ~$4 / person / month | GitHub Team |
| Public cloud | free | free GitHub account (warned) |

**Lead with local-only.** Many non-coder users will pick that and be done. Cloud is framed as the paid tier for the smoothest non-coder UX.

### For coders (Beat 2-coder) — empirical, more nuanced

Free GitHub accounts in 2026 actually do include unlimited private repos for individuals, so solo private cloud technically works on free. The paid plans (Pro / Team) add governance features (CODEOWNERS, branch protection, audit log, required reviewers). The coder beat can state this directly; the everyone beat keeps the simpler "free=local, paid=cloud" framing.
