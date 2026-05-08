# Starter Deck — beadwork-overview Walkthrough

**STATUS: assembled.** All HTML pages live under `walkthrough_html/`. Image references resolve to existing ConceptViz output.

This file is the **navigation map** for the walkthrough — beat IDs, URLs, image filenames, structural notes that the presenter agent reads silently before Beat 1. It is NOT the source of truth for prose; that's `beat_scripts.md` next door.

Read this silently before starting. All hard rules from `SKILL.md` apply.

---

## Flow at a glance

```
Beat 1 (universal hook)
   ↓
Beat 2 (literacy ASK)
   ↓
   ├── "writing code"     → Beat 3-coder
   └── anything else      → Beat 3-everyone
                              ↓
                       Beat 4 (use cases — converge)
                              ↓
                       Beat 5 (close — terminus)
```

Single fork. Both paths converge at Beat 4. Beat 5 has no question.

---

## Beat 1 — Elevator pitch

- **File:** `walkthrough_html/beat1.html`
- **Image:** `walkthrough_html/images/beat1-hook.jpg`
- **Navigate:** `http://localhost:8910/beadwork-overview/walkthrough_html/beat1.html`
- **Chat shape:** 3-4 sentences naming the AI-forgets pain (universal language, no "compaction" jargon), bw as a tool that helps in many cases, the three-tier escalation (memory across sessions / **team of specialist agents, usually same-lab multi-session** / cross-human team), and the three reassurances (don't have to learn it / can stay on computer / free + open source). See `beat_scripts.md` Beat 1. **Tier 2 leads with same-lab multi-session, not with cross-vendor.**
- **Question:** "Sound interesting?"

---

## Beat 2 — Literacy fork (the only branch)

- **File:** `walkthrough_html/beat2.html`
- **Image:** none (CSS-only audience cards on the page)
- **Navigate:** `http://localhost:8910/beadwork-overview/walkthrough_html/beat2.html`
- **Chat shape:** 2-3 sentences setting up the fork and explaining why we ask. See `beat_scripts.md` Beat 2.
- **Question (FORK):** "How do you mainly use AI?" — options: writing code / writing-research-learning / business-or-personal / something-else.
- **Routing:**
  - "Writing code" → `beat3_coder.html`
  - Anything else → `beat3_everyone.html`

---

## Beat 3 (coder) — What bw is, SWE version

- **File:** `walkthrough_html/beat3_coder.html`
- **Image:** `walkthrough_html/images/beat2-trust.jpg` (reused — folder + orphan branch + multi-AI)
- **Navigate:** `http://localhost:8910/beadwork-overview/walkthrough_html/beat3_coder.html`
- **Chat shape:** 4-5 sentences with developer vocabulary. Storage = orphan branch + JSON. Single Go binary. Cross-AI portable. MIT-licensed. Survives compaction. The three-tier escalation in dev terms. See `beat_scripts.md` Beat 3-coder.
- **Question:** "Want to see where this kind of memory + coordination earns its keep?"

---

## Beat 3 (everyone) — What bw is, plain-English version

- **File:** `walkthrough_html/beat3_everyone.html`
- **Image:** `walkthrough_html/images/beat2-trust.jpg` (reused — but framed in chat as "lives in a folder on your computer")
- **Navigate:** `http://localhost:8910/beadwork-overview/walkthrough_html/beat3_everyone.html`
- **Chat shape:** 4-6 sentences explaining git first, then what bw does on top of git, then the four storage modes with empirically-correct pricing, then the authorization stack. See `beat_scripts.md` Beat 3-everyone.
- **Question:** "Storage mode preference, or skip ahead?"

---

## Beat 4 — Where this kind of memory helps (converge)

- **File:** `walkthrough_html/beat4.html`
- **Image:** `walkthrough_html/images/beat3-personas.jpg` (reused — seven-persona grid)
- **Navigate:** `http://localhost:8910/beadwork-overview/walkthrough_html/beat4.html`
- **Chat shape:** 4-6 sentences walking the seven persona snapshots quickly. Stay neutral on coder/non-coder vocabulary so both forks land cleanly here. See `beat_scripts.md` Beat 4.
- **Question:** "Want pointers to deeper-dive skills?"

---

## Beat 5 — Where to go from here (terminus)

- **File:** `walkthrough_html/beat5.html`
- **Image:** `walkthrough_html/images/beat5-close.jpg`
- **Navigate:** `http://localhost:8910/beadwork-overview/walkthrough_html/beat5.html`
- **Chat shape:** 3-4 sentences listing the five companion skills + the closing attribution + the non-coder reassurance. NO `AskUserQuestion` here — Beat 5 is the terminus.

---

## Storage-mode pricing reference

### For non-coders (Beat 3-everyone) — simplified narrative

| Mode | Cost | Account needed |
|---|---|---|
| **Local-only, one computer** (the headline option) | **free** | **none** |
| Cloud backup + cross-device sync | ~$4 / month | GitHub Pro |
| Team cloud | ~$4 / person / month | GitHub Team |
| Public cloud | free | free GitHub account (warned) |

**Lead with local-only.** Many non-coder users will pick that and be done. Cloud is framed as the paid tier for the smoothest non-coder UX.

### For coders (Beat 3-coder) — empirical, more nuanced

Free GitHub accounts in 2026 actually do include unlimited private repos for individuals, so solo private cloud technically works on free. The paid plans (Pro / Team) add governance features (CODEOWNERS, branch protection, audit log, required reviewers). The coder beat can state this directly; the everyone beat keeps the simpler "free=local, paid=cloud" framing.
