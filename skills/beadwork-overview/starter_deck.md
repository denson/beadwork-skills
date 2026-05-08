# Starter Deck — beadwork-overview Walkthrough

**STATUS: assembled.** All 8 HTML pages live under `walkthrough_html/`. Image generation pending — image references resolve to placeholder paths until ConceptViz output lands.

This file is the **navigation map** for the walkthrough — beat IDs, URLs, image filenames, structural notes that the presenter agent reads silently before Beat 1. It is NOT the source of truth for prose; that's `beat_scripts.md` next door.

Read this silently before starting. All hard rules from `SKILL.md` apply.

---

## Beat 1 — Hook: agents forget; bw fixes that

**File:** `walkthrough_html/beat1.html`
**Image:** `walkthrough_html/images/beat1-hook.jpg`
**Navigate:** `http://localhost:8910/beadwork-overview/walkthrough_html/beat1.html`
**Chat shape:** 3-4 sentences naming the compaction problem (generic, no agent-team specifics) and bw as the fix. The "talk to your agent" framing introduced. See `beat_scripts.md` Beat 1.
**Question:** "Recognize the problem?"

---

## Beat 2 — What bw is (the trust story)

**File:** `walkthrough_html/beat2.html`
**Image:** `walkthrough_html/images/beat2-trust.jpg`
**Navigate:** `http://localhost:8910/beadwork-overview/walkthrough_html/beat2.html`
**Chat shape:** 4-5 sentences walking the five structural advantages over SaaS alternatives. See `beat_scripts.md` Beat 2.
**Question:** "Want to see who uses it?"

---

## Beat 3 — Seven roles, one interaction pattern (HUB)

**File:** `walkthrough_html/beat3.html`
**Image:** `walkthrough_html/images/beat3-personas.jpg`
**Navigate:** `http://localhost:8910/beadwork-overview/walkthrough_html/beat3.html`
**Chat shape:** 5-7 sentences (longer than usual) briefing all seven personas. The unification claim ("you talk to your agent; your agent uses bw") lands here. See `beat_scripts.md` Beat 3.
**Question (HUB):** "Which sounds closest to your work?" — one of (A) Technical, (B) Operations, (C) Professional, (D) Show me all 7 quickly.

---

## Dynamic paths after Beat 3

The user picks one. Each path is its own short beat that proceeds directly to Beat 5 afterward (no further fork).

### Path A — Technical roles

- **File:** `walkthrough_html/dynamic_technical.html`
- **Image:** `walkthrough_html/images/dynamic-technical.jpg`
- **Personas covered:** software engineer, data scientist, logistics analyst.
- **Theme:** bw as audit substrate — work that has to be correct and defensible.

### Path B — Operations & customer-facing

- **File:** `walkthrough_html/dynamic_operations.html`
- **Image:** `walkthrough_html/images/dynamic-operations.jpg`
- **Personas covered:** warehouse manager, customer support manager.
- **Theme:** bw as durable async channel — coordination across teams, shifts, organizations, time.

### Path C — Independent / professional services

- **File:** `walkthrough_html/dynamic_professional.html`
- **Image:** `walkthrough_html/images/dynamic-professional.jpg`
- **Personas covered:** lawyer, solo entrepreneur.
- **Theme:** bw as personal-OS substrate — solo or small team, audit-critical, low admin overhead.

### Path D — Show me all 7 quickly

- **File:** `walkthrough_html/dynamic_all.html`
- **Image:** `walkthrough_html/images/dynamic-all.jpg`
- **Personas covered:** all seven, briefly.
- **Theme:** the unification pitch — same pattern, seven roles, seven kinds of work.

---

## Beat 5 — Close: pointers to deeper-dive skills

**File:** `walkthrough_html/beat5.html`
**Image:** `walkthrough_html/images/beat5-close.jpg`
**Navigate:** `http://localhost:8910/beadwork-overview/walkthrough_html/beat5.html`
**Chat shape:** 4-5 sentences listing the five companion skills + the closing attribution. NO `AskUserQuestion` here — Beat 5 is the terminus.
