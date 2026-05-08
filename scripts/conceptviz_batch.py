#!/usr/bin/env python3
"""
ConceptViz batch runner for beadwork-skills marketplace.

Generates 24 images across 5 walkthrough skills:
  - beadwork-overview        (8 images: hook, trust, personas, 4 dynamic-paths, close)
  - beadwork-as-memory       (4 images: hook, mechanism, scenarios, close)
  - beadwork-as-bus          (4 images: hook, mechanism, scenarios, close)
  - beadwork-for-meta-analysis  (4 images: hook, mechanism, scenarios, close)
  - beadwork-for-decisions   (4 images: hook, mechanism, scenarios, close)

(beadwork-install has no images — agent-execution shape, no preview panel.)

Submits up to 5 in-flight, polls all to completion, then submits the next
wave. Mirrors each downloaded image to BOTH:
  - skills/<skill>/assets/images/<name>.<ext>             (source-of-truth)
  - skills/<skill>/walkthrough_html/images/<name>.<ext>   (server mirror)

Sidecar .task.json written next to source-of-truth copy only.

PREREQUISITES:
  - 1Password Desktop running and signed in (CLI auth-bridge).
  - `op item get ConceptViz --vault Private` returns the item.
  - `requests` library installed: pip install requests

USAGE:
  python scripts/conceptviz_batch.py            # real run
  python scripts/conceptviz_batch.py --dry-run  # plan only, no API

API CONSTRAINT (read before running):
  ConceptViz accepts max 5 in-flight submissions per account. Submitted tasks
  must reach terminal state before more can be submitted. Script respects this
  via MAX_CONCURRENT_SUBMISSIONS = 5.

Cost estimate: 24 images × 1 credit each (2k quality) = 24 credits.
"""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

try:
    import requests
except ImportError:
    print("ERROR: requests library not installed. Run: pip install requests", file=sys.stderr)
    sys.exit(1)


OP_REFERENCE = "op://Private/ConceptViz/credential"
API_BASE = "https://conceptviz.app/api/v1"
POLL_INTERVAL_S = 6
POLL_TIMEOUT_S = 600
MAX_CONCURRENT_SUBMISSIONS = 5

REPO_ROOT = Path(__file__).parent.parent


@dataclass
class PromptSpec:
    name: str
    skill: str
    aspect_ratio: str
    quality: str
    prompt_body: str


# =============================================================================
# Style — every prompt gets the common style baseline + the per-skill subject
# context appended at submit time.
# =============================================================================

COMMON_STYLE = (
    "Colorblind-friendly, no hex codes. Style: flat design, editorial "
    "illustration, simple shapes, bold colors on a light warm-gray background. "
    "Think 'product strategy deck illustration,' not whiteboard sketch. Generic "
    "AI-assistant figures (NOT vendor-branded; do not include any specific "
    "agent names like Pliny, Vera, Cato, Ada, or any company logo)."
)

SKILL_CONTEXT: dict[str, str] = {
    "beadwork-overview": (
        "These images are for the beadwork-overview presenter skill — a tour of "
        "how seven kinds of users (software engineers, data scientists, logistics "
        "analysts, warehouse managers, customer support managers, lawyers, solo "
        "entrepreneurs) use beadwork (bw — github.com/jallum/beadwork) through "
        "their AI assistants for durable agent memory and agent-to-agent "
        "communication. The unifying interaction: 'you talk to your agent; your "
        "agent uses bw.'"
    ),
    "beadwork-as-memory": (
        "These images are for the beadwork-as-memory presenter skill — a deep-dive "
        "on bw (beadwork — github.com/jallum/beadwork) as durable agent memory "
        "across sessions, restarts, and time. Concrete personas in the scenarios: "
        "data scientist, lawyer, solo entrepreneur."
    ),
    "beadwork-as-bus": (
        "These images are for the beadwork-as-bus presenter skill — a deep-dive "
        "on bw (beadwork — github.com/jallum/beadwork) as agent-to-agent "
        "communication across multiple agents, teams, organizations, and AI "
        "vendors. Concrete personas in the scenarios: engineer, data scientist, "
        "support manager, warehouse manager."
    ),
    "beadwork-for-meta-analysis": (
        "These images are for the beadwork-for-meta-analysis presenter skill — a "
        "deep-dive on running an agent over the bw (beadwork — "
        "github.com/jallum/beadwork) history of OTHER agents to audit, check "
        "methodology, or synthesize. Concrete personas in the scenarios: engineer "
        "(multi-agent code review with conflict-finder), data scientist (analysis "
        "pipeline with methodology auditor), lawyer (cross-case consistency check)."
    ),
    "beadwork-for-decisions": (
        "These images are for the beadwork-for-decisions presenter skill — a "
        "deep-dive on bw (beadwork — github.com/jallum/beadwork) as decision "
        "log / ADR / audit trail substrate. Concrete personas in the scenarios: "
        "engineer (architecture decision record), lawyer (privilege log), solo "
        "entrepreneur (tax-time decision defense)."
    ),
}


def assemble_full_prompt(spec: PromptSpec) -> str:
    context = SKILL_CONTEXT.get(spec.skill)
    if context is None:
        raise ValueError(f"no context for skill: {spec.skill}")
    return f"{spec.prompt_body}\n\n{context}\n\n{COMMON_STYLE}"


# =============================================================================
# Prompts — 24 total
# =============================================================================

PROMPTS: list[PromptSpec] = [

    # --------------------------------------------------------------------------
    # beadwork-overview (8 images)
    # --------------------------------------------------------------------------

    PromptSpec(
        name="beat1-hook",
        skill="beadwork-overview",
        aspect_ratio="16:9", quality="2k",
        prompt_body=(
            "A two-panel split scene divided vertically by a thin line.\n\n"
            "LEFT PANEL (warm red-pink tint, labeled at the top \"Without bw\"): "
            "a generic AI-assistant figure in the center looking confused, with "
            "a thought bubble reading \"wait — what was I doing?\" Around the "
            "figure: scattered fragments representing forgotten context — a "
            "half-finished checklist, a stack-trace card with stylized error "
            "lines, a question mark, a dimmed conversation bubble drifting away.\n\n"
            "RIGHT PANEL (cool teal tint, labeled at the top \"With bw\"): the "
            "same generic AI-assistant figure standing calm and resumed, reading "
            "from a small ticket card sitting on a small desk in front of it. "
            "The ticket card has a clean header (TITLE bar) and three small "
            "comment-bubbles attached labeled with date stamps. A clear thought "
            "bubble reads \"right — yesterday we decided X, the next step is Y.\" "
            "A small label at the bottom of the right panel reads \"context "
            "restored from `bw show`.\"\n\n"
            "Caption at the bottom of the full image: \"Sessions end. Context "
            "shouldn't.\""
        ),
    ),

    PromptSpec(
        name="beat2-trust",
        skill="beadwork-overview",
        aspect_ratio="16:9", quality="2k",
        prompt_body=(
            "A stylized diagram of a developer's repository, shown as a folder "
            "labeled \"your repo / your disk.\" Inside the folder, two "
            "compartments visible:\n\n"
            "TOP COMPARTMENT (labeled \"project files — visible\"): three "
            "rounded-rectangle file icons — one labeled README.md, one labeled "
            "src/, one labeled docs/.\n\n"
            "BOTTOM COMPARTMENT (separated by a dashed line labeled "
            "\"orphan-branch boundary\", with a soft warm-amber tint to set it "
            "apart): three small ticket cards labeled with abbreviated "
            "ticket-IDs (e.g. \"auth.7\", \"design.4\", \"deploy.2\").\n\n"
            "Around the folder: four AI-assistant icons in different colors "
            "(generic, representing different vendors — NO logos, just colored "
            "stylized assistant figures), each with arrows pointing INTO and OUT "
            "OF the bottom compartment. A label between the four assistants "
            "reads \"Claude / Gemini / OpenAI / others — same store.\"\n\n"
            "A large arrow points outside the folder to empty space, with a "
            "prominent label: \"no SaaS, no vendor servers, no signup.\"\n\n"
            "Caption: \"Lives where your code lives.\""
        ),
    ),

    PromptSpec(
        name="beat3-personas",
        skill="beadwork-overview",
        aspect_ratio="16:9", quality="2k",
        prompt_body=(
            "A grid of seven illustrated cards arranged in a 4-3 layout. Each "
            "card has a stylized persona icon at the top, a role-name label in "
            "bold below the icon, and a one-line use description below the role "
            "name.\n\n"
            "TOP ROW (4 cards, left to right):\n"
            "1. Software engineer — a developer at a laptop. Label: \"Software "
            "Engineer.\" Use: \"debugging, decisions, code review.\"\n"
            "2. Data scientist — a figure with charts and a notebook. Label: "
            "\"Data Scientist.\" Use: \"investigations, pipelines, "
            "reproducibility.\"\n"
            "3. Logistics analyst — a figure with route maps and a graph. "
            "Label: \"Logistics Analyst.\" Use: \"analytics, scorecards, model "
            "iteration.\"\n"
            "4. Warehouse manager — a figure on a warehouse floor with a "
            "clipboard. Label: \"Warehouse Manager.\" Use: \"incidents, vendor "
            "coordination, shift handoffs.\"\n\n"
            "BOTTOM ROW (3 cards, left to right):\n"
            "5. Customer support manager — a figure at a headset. Label: "
            "\"Customer Support Manager.\" Use: \"escalations, cross-team "
            "coordination.\"\n"
            "6. Lawyer / paralegal — a figure with a case file and gavel icon. "
            "Label: \"Lawyer.\" Use: \"cases, document review, audit.\"\n"
            "7. Solo entrepreneur — a figure at a small desk juggling many "
            "small icons (a laptop, a calendar, a coffee, a phone). Label: "
            "\"Solo Entrepreneur.\" Use: \"personal-OS, lessons across "
            "engagements.\"\n\n"
            "Below the grid: a horizontal banner with the bold text "
            "\"all seven: talk to your agent. agent uses bw.\"\n\n"
            "Caption: \"Seven roles. Same interaction.\""
        ),
    ),

    PromptSpec(
        name="dynamic-technical",
        skill="beadwork-overview",
        aspect_ratio="16:9", quality="2k",
        prompt_body=(
            "Three vertical lanes, each showing a technical-role scenario.\n\n"
            "LEFT LANE (cool blue tint, header \"Engineer\"): a developer figure "
            "at a laptop with three small AI-assistant figures around them. "
            "Arrows from each AI converge on a central ticket card labeled "
            "\"PR-42 review\" with three structured-verdict comments below "
            "(\"security agent: pass\", \"style agent: needs-revisions\", "
            "\"test-coverage agent: pass\"). A fourth AI figure off to the side "
            "labeled \"conflict-finder\" reads all three.\n\n"
            "MIDDLE LANE (warm amber tint, header \"Data Scientist\"): a figure "
            "with a notebook and pen. An analysis pipeline of three AI agents "
            "arranged horizontally with arrows between them: \"cleaner\" → "
            "\"tester\" → \"visualizer.\" A fourth AI figure stands above the "
            "pipeline labeled \"methodology auditor\" reading the chain.\n\n"
            "RIGHT LANE (cool teal tint, header \"Logistics Analyst\"): a "
            "figure with a dashboard. A vendor-scorecard ticket card labeled "
            "\"Q2 vendor scorecard\" in the middle. Two AI figures in different "
            "colors on either side of the ticket — one labeled \"analyst's AI,\" "
            "one labeled \"warehouse manager's AI\" — both reading the same "
            "ticket.\n\n"
            "Caption: \"Correctness + validation across three roles.\""
        ),
    ),

    PromptSpec(
        name="dynamic-operations",
        skill="beadwork-overview",
        aspect_ratio="16:9", quality="2k",
        prompt_body=(
            "A composition with two horizontal scenes stacked vertically.\n\n"
            "TOP SCENE (Warehouse Manager): a warehouse cross-section with "
            "day-shift activity on the left (forklift, pallets) fading into "
            "night-shift activity on the right (lower lighting). Both shifts "
            "have AI-assistant figures. An arrow connects them through a "
            "central ticket card labeled \"shift handoff log.\" Off to the "
            "right side: two separate small organization buildings labeled "
            "\"warehouse\" and \"logistics partner,\" each with an AI-assistant "
            "figure, with arrows between them through another ticket card "
            "labeled \"vendor coordination.\"\n\n"
            "BOTTOM SCENE (Customer Support Manager): a customer service "
            "interface on the left (a chat-bubble + headset icon); an "
            "engineering team workspace on the right (a code-screen icon). "
            "Three AI figures arrayed (one near customer service, one near "
            "engineering, one in the middle labeled \"manager's AI\") all "
            "reading and writing to a central ticket card labeled \"escalation "
            "2026-Q2-acme.\" A small inspector figure with a clipboard sits "
            "off to the side, reading from a stack of ticket cards.\n\n"
            "Caption: \"Coordination IS record-keeping.\""
        ),
    ),

    PromptSpec(
        name="dynamic-professional",
        skill="beadwork-overview",
        aspect_ratio="16:9", quality="2k",
        prompt_body=(
            "A composition with two horizontal scenes stacked vertically.\n\n"
            "TOP SCENE (Lawyer): a small law office. A stack of three "
            "case-file ticket cards labeled with generic case names (\"case-1,\" "
            "\"case-2,\" \"case-3\"). Multiple AI-assistant figures partitioning "
            "a tall stack of small document-icons (representing 10,000 documents). "
            "A separate AI figure off to the side labeled \"audit agent\" reads "
            "the chain. A privilege-log ticket card with a date stamp and the "
            "label \"court-defensible.\" Several lock icons around the scene "
            "emphasizing privacy.\n\n"
            "BOTTOM SCENE (Solo Entrepreneur): a single figure at a small desk "
            "surrounded by small floating labels for many domains: \"sales,\" "
            "\"ops,\" \"finance,\" \"marketing,\" \"knowledge.\" A single "
            "AI-assistant figure beside them, reading a notebook ticket card "
            "labeled \"all domains.\" Arrows from the AI to each domain label, "
            "showing the AI logging activity across all of them. A small "
            "sub-scene at the bottom-right showing a \"lessons learned\" ticket "
            "being surfaced for a new engagement.\n\n"
            "Caption: \"Personal-OS, audit-grade, low overhead.\""
        ),
    ),

    PromptSpec(
        name="dynamic-all",
        skill="beadwork-overview",
        aspect_ratio="16:9", quality="2k",
        prompt_body=(
            "A grid of seven small panels, one per persona, arranged in a 4-3 "
            "layout. Each panel shows the same simple shape: persona figure on "
            "the left, a small speech bubble in the middle showing what they "
            "ask their agent, an AI-assistant figure on the right, and a bw "
            "ticket card emerging from or being read by the AI.\n\n"
            "TOP ROW:\n"
            "1. Engineer — speech bubble \"why did we decide on Auth0?\" — AI "
            "reading bw show.\n"
            "2. Data scientist — speech bubble \"what was March's churn "
            "methodology?\" — AI reading bw show.\n"
            "3. Warehouse manager — speech bubble \"incidents this month?\" — "
            "AI running bw list.\n"
            "4. Support manager — speech bubble \"top 5 pain points?\" — AI "
            "running bw list.\n\n"
            "BOTTOM ROW:\n"
            "5. Lawyer — speech bubble \"privilege reasoning on doc 4789?\" — "
            "AI reading bw show.\n"
            "6. Logistics analyst — speech bubble \"Q2 vendor scorecard?\" — "
            "AI reading the bw ticket.\n"
            "7. Solo entrepreneur — speech bubble \"what worked with Acme?\" — "
            "AI surfacing bw lessons.\n\n"
            "Across the bottom of the full image: a single banner reading "
            "\"one pattern. seven roles. seven kinds of work.\"\n\n"
            "Caption: \"One pattern. Seven roles.\""
        ),
    ),

    PromptSpec(
        name="beat5-close",
        skill="beadwork-overview",
        aspect_ratio="16:9", quality="2k",
        prompt_body=(
            "A clean closing card. At the top center: a small bw ticket icon "
            "with a checkmark inside.\n\n"
            "Below the ticket icon: five labeled cards arranged in a 3-2 grid "
            "representing the five companion skills, each card with a "
            "representative icon and a name label:\n\n"
            "TOP ROW (3 cards):\n"
            "1. A clock + brain icon — label \"beadwork-as-memory.\"\n"
            "2. A network icon (multiple agents connected through a central "
            "node) — label \"beadwork-as-bus.\"\n"
            "3. A magnifying-glass icon over a stack of tickets — label "
            "\"beadwork-for-meta-analysis.\"\n\n"
            "BOTTOM ROW (2 cards):\n"
            "4. A decision-tree icon — label \"beadwork-for-decisions.\"\n"
            "5. A wrench icon — label \"beadwork-install.\"\n\n"
            "Below the grid: a small caption in italic reading \"open source. "
            "authored by Denson Smith. bw itself by jallum (github.com/jallum/"
            "beadwork).\"\n\n"
            "Caption: \"Five companion skills.\""
        ),
    ),

    # --------------------------------------------------------------------------
    # beadwork-as-memory (4 images)
    # --------------------------------------------------------------------------

    PromptSpec(
        name="beat1-hook",
        skill="beadwork-as-memory",
        aspect_ratio="16:9", quality="2k",
        prompt_body=(
            "A stylized horizontal timeline showing two sessions separated by "
            "a gap.\n\n"
            "LEFT SESSION (warm tint): a generic AI-assistant figure at a "
            "laptop, with thought bubbles and a small ticket card emerging from "
            "the AI. The ticket card has three short comments visible: "
            "\"decision: Auth0 with PKCE\", \"constraint: budget < $50/mo\", "
            "\"blocker: vendor API down until Wed.\" The session ends with a "
            "\"session ended\" mark on the timeline.\n\n"
            "CENTER (the gap, neutral background): the same ticket card "
            "persists prominently, anchored by a small icon labeled \"bw — "
            "your repo.\" The ticket card looks unchanged; comments still "
            "visible.\n\n"
            "RIGHT SESSION (cool tint): a fresh session opening. The same "
            "AI-assistant figure (or a new one of the same style) reads the "
            "ticket card, with a thought bubble reading \"right — picking up "
            "where we left off.\" The session timeline starts fresh on the "
            "right.\n\n"
            "Caption: \"Memory isn't the chat. Memory is the few things you "
            "wrote down.\""
        ),
    ),

    PromptSpec(
        name="beat2-mechanism",
        skill="beadwork-as-memory",
        aspect_ratio="16:9", quality="2k",
        prompt_body=(
            "A diagram of one ticket card, rendered in detail, with a "
            "structured layout.\n\n"
            "TOP BAR of the ticket: TITLE \"Auth0 migration plan\" plus three "
            "small chip-tags: \"priority:1\", \"status:open\", \"type:task.\"\n\n"
            "BODY: a column of comment bubbles, each with a date-stamp on the "
            "left and an author label, vertically stacked:\n"
            "- \"claude · 2026-05-01\" — \"investigated three providers; "
            "Auth0, Clerk, in-house.\"\n"
            "- \"user · 2026-05-02\" — \"Auth0 it is. Pricing concern at "
            "scale; revisit at 50K MAU.\"\n"
            "- \"claude · 2026-05-12\" — \"PKCE flow scaffolded. Test JWT "
            "issued. Working.\"\n\n"
            "OFF TO THE SIDE: a small AI-assistant figure with an arrow "
            "pointing into the ticket, labeled \"`bw show <id>` returns the "
            "full thread.\"\n\n"
            "Caption: \"Title + comments + author + timestamp = "
            "reconstruction substrate.\""
        ),
    ),

    PromptSpec(
        name="beat3-scenarios",
        skill="beadwork-as-memory",
        aspect_ratio="16:9", quality="2k",
        prompt_body=(
            "Three vertical lanes, each showing a memory scenario across a "
            "different time horizon.\n\n"
            "LEFT LANE (Data Scientist, cool blue tint): a multi-day timeline "
            "labeled \"Day 1 → Day 7\" with daily comment-cards stacking up "
            "vertically on a central ticket card labeled \"Q3-churn-"
            "investigation.\" On Day 7, an AI-assistant figure reads the full "
            "stack and emerges with a doc icon labeled \"executive memo.\"\n\n"
            "MIDDLE LANE (Lawyer, warm amber tint): a long horizontal "
            "case-file ticket labeled \"case-smith-v-jones\" with many "
            "comment-cards spanning months (timeline labeled \"March → "
            "November\"). A \"new paralegal\" figure appears at the September "
            "mark on the timeline, with an AI-assistant figure beside them "
            "reading the ticket from the start.\n\n"
            "RIGHT LANE (Solo Entrepreneur, warm rose tint): two engagement "
            "ticket cards labeled \"April client\" and \"October client,\" "
            "connected by a curving \"lessons\" arrow from the first to the "
            "second. A solo-entrepreneur figure with their AI-assistant figure "
            "beside them, reading the connecting lesson.\n\n"
            "Caption: \"Same mechanism, three shapes of memory.\""
        ),
    ),

    PromptSpec(
        name="beat4-close",
        skill="beadwork-as-memory",
        aspect_ratio="16:9", quality="2k",
        prompt_body=(
            "A simple closing card. Across the top: a row of failure-mode "
            "icons in small chip-cards: \"session ended,\" \"/clear,\" \"agent "
            "restart,\" \"machine swap,\" \"vendor swap,\" \"+ time passes.\" "
            "Each chip has a small downward arrow.\n\n"
            "All six arrows converge on a single durable ticket card centered "
            "below the chips. The ticket is bold, unbroken, with a green "
            "checkmark in its corner.\n\n"
            "Below the ticket: four small pointer-card icons arranged "
            "horizontally for the companion skills, each with name and "
            "representative icon: \"beadwork-overview\" (compass icon), "
            "\"beadwork-as-bus\" (network icon), \"beadwork-for-meta-analysis\" "
            "(magnifying-glass icon), \"beadwork-for-decisions\" "
            "(decision-tree icon).\n\n"
            "Caption: \"Memory survives. Pick what to read next.\""
        ),
    ),

    # --------------------------------------------------------------------------
    # beadwork-as-bus (4 images)
    # --------------------------------------------------------------------------

    PromptSpec(
        name="beat1-hook",
        skill="beadwork-as-bus",
        aspect_ratio="16:9", quality="2k",
        prompt_body=(
            "A composition showing several AI-assistant figures arranged in a "
            "loose ring around a central ticket card. Each AI figure is "
            "rendered slightly differently in different colors representing "
            "different vendors (NO logos — generic stylized AI assistants in "
            "different colors). Arrows from each AI both INTO and OUT OF the "
            "central ticket card — both reading and writing.\n\n"
            "The central ticket card has a stack of comment bubbles inside, "
            "each one labeled with a different author and timestamp, showing "
            "the conversation across agents. Visible authors include a mix of "
            "agent-style names and human-like names: \"agent-A · 2026-05-01,\" "
            "\"alice · 2026-05-02,\" \"agent-B · 2026-05-03.\" A small label "
            "on the ticket reads \"shared bw store.\"\n\n"
            "Caption: \"Many agents. One ticket. Asynchronous, signed, "
            "durable.\""
        ),
    ),

    PromptSpec(
        name="beat2-mechanism",
        skill="beadwork-as-bus",
        aspect_ratio="16:9", quality="2k",
        prompt_body=(
            "A diagram showing two ticket cards side by side, each with "
            "several comment bubbles inside.\n\n"
            "LEFT TICKET (\"ticket-1\") with three comments labeled with "
            "different author + timestamp combinations.\n\n"
            "RIGHT TICKET (\"ticket-2\") with three different comments, also "
            "labeled with author + timestamp.\n\n"
            "ABOVE THE TWO TICKETS: two AI-assistant figures (different colors "
            "to suggest different agents). Agent A on the left has an arrow "
            "pointing to ticket-1; Agent B on the right has an arrow pointing "
            "to ticket-2. Both agents writing simultaneously. The arrows do "
            "NOT cross or overlap.\n\n"
            "BELOW THE TWO TICKETS: a \"merged view\" shown as both tickets "
            "coexisting in a single bw-store box, with a small label \"same "
            "store, different files. no collision.\"\n\n"
            "Caption: \"Different tickets, different files. No collision.\""
        ),
    ),

    PromptSpec(
        name="beat3-scenarios",
        skill="beadwork-as-bus",
        aspect_ratio="16:9", quality="2k",
        prompt_body=(
            "Four small panels arranged in a 2×2 grid, each showing one "
            "agent-to-agent communication scenario.\n\n"
            "TOP-LEFT (Engineer): a PR-42 review ticket card with three "
            "structured-verdict comments visible (\"security agent\", \"style "
            "agent\", \"test-coverage agent\"). An engineer's AI-assistant "
            "figure stands beside the ticket synthesizing the responses.\n\n"
            "TOP-RIGHT (Data Scientist): three day-stamped tickets connected "
            "horizontally by arrows showing the analysis pipeline: cleaner "
            "(Monday) → tester (Tuesday) → visualizer (Wednesday). A small AI-"
            "assistant figure beside each ticket.\n\n"
            "BOTTOM-LEFT (Support Manager): three columns (Customer Support, "
            "Engineering, Manager) each with an AI-assistant figure, all "
            "writing to a central escalation ticket card in the middle.\n\n"
            "BOTTOM-RIGHT (Warehouse Manager): two organization-building icons "
            "(labeled \"warehouse\" and \"logistics partner\"), each with an "
            "AI-assistant figure, both writing to a shared pickup-schedule "
            "ticket between them.\n\n"
            "Caption: \"Within a job, across days, across teams, across "
            "organizations.\""
        ),
    ),

    PromptSpec(
        name="beat4-close",
        skill="beadwork-as-bus",
        aspect_ratio="16:9", quality="2k",
        prompt_body=(
            "A composition emphasizing cross-vendor portability. Across the "
            "top: four AI-assistant figures in different colors arranged "
            "horizontally, each labeled generically with vendor styles "
            "(\"Claude-style,\" \"Gemini-style,\" \"OpenAI-style,\" "
            "\"other\"). NO logos.\n\n"
            "All four AI figures have arrows pointing downward to a single "
            "centered bw-store box labeled \"your repo / your bw store.\" "
            "Inside the box, several ticket cards visible.\n\n"
            "BELOW THE STORE: a small caption \"swap vendors freely. The "
            "store stays.\" Below that: four small companion-skill icons "
            "arranged horizontally with names: \"beadwork-overview,\" "
            "\"beadwork-as-memory,\" \"beadwork-for-meta-analysis,\" "
            "\"beadwork-for-decisions,\" plus \"beadwork-install.\"\n\n"
            "Caption: \"Swap vendors freely. The store stays.\""
        ),
    ),

    # --------------------------------------------------------------------------
    # beadwork-for-meta-analysis (4 images)
    # --------------------------------------------------------------------------

    PromptSpec(
        name="beat1-hook",
        skill="beadwork-for-meta-analysis",
        aspect_ratio="16:9", quality="2k",
        prompt_body=(
            "A two-panel split scene divided vertically.\n\n"
            "LEFT PANEL (warm pink-red tint, header \"Chat history — can't "
            "audit this\"): a tangled, noisy conversation thread rendered as "
            "a long stream of speech bubbles in many colors, overlapping and "
            "crowded together, no clear order. An audit-agent figure (a "
            "stylized AI with a magnifying-glass icon attached) tries to read "
            "it, with a confused thought bubble reading \"who said what? "
            "when? what did they decide?\" Some bubbles are blurred or fading.\n\n"
            "RIGHT PANEL (cool blue tint, header \"bw history — can audit "
            "this\"): the same content but rendered as a clean stack of "
            "structured ticket cards. Each card has TITLE plus several "
            "comments with clearly visible author + timestamp stamps. The "
            "audit-agent figure stands in front, with a clear thought bubble "
            "reading \"agent A on day 1: <decision>. agent B on day 4: "
            "<verdict>. they agree on X but conflict on Y.\"\n\n"
            "Caption: \"Same work. Different substrate. Only one is "
            "auditable.\""
        ),
    ),

    PromptSpec(
        name="beat2-mechanism",
        skill="beadwork-for-meta-analysis",
        aspect_ratio="16:9", quality="2k",
        prompt_body=(
            "A diagram with a stack of structured ticket cards on the LEFT "
            "side. Each ticket shows TITLE plus several signed-and-timestamped "
            "comments in a clean column layout. Three to four tickets stacked "
            "vertically.\n\n"
            "On the RIGHT side: a single audit-agent figure (rendered "
            "distinctly with a magnifying-glass icon) reading the stack. "
            "Above the audit agent, four thought-bubble questions arranged in "
            "a small cluster:\n"
            "- \"consistency?\"\n"
            "- \"drift?\"\n"
            "- \"contradictions?\"\n"
            "- \"missing steps?\"\n\n"
            "BETWEEN the tickets and the audit agent: a small label \"`bw "
            "show / bw list / bw history`.\"\n\n"
            "BELOW the diagram: a footnote reading \"all author stamps. all "
            "timestamps. all structure. = analyzable.\"\n\n"
            "Caption: \"Read the work, not the chat.\""
        ),
    ),

    PromptSpec(
        name="beat3-scenarios",
        skill="beadwork-for-meta-analysis",
        aspect_ratio="16:9", quality="2k",
        prompt_body=(
            "Three vertical lanes, each showing a meta-analysis scenario.\n\n"
            "LEFT LANE (Engineer): a PR-42 review ticket card with three "
            "structured-verdict comments visible: \"security agent: require "
            "strict CORS,\" \"style agent: strip those headers,\" \"test-"
            "coverage agent: OK.\" A fourth AI-assistant figure labeled "
            "\"conflict-finder\" stands beside the ticket, with a flag-icon "
            "thought bubble reading \"contradiction: security vs style on "
            "CORS.\"\n\n"
            "MIDDLE LANE (Data Scientist): a horizontal pipeline of three "
            "day-stamped ticket cards with arrows: \"cleaner (filtered to "
            "active users)\" → \"tester (ran t-test on full population)\" → "
            "\"visualizer.\" A \"methodology auditor\" AI-assistant figure "
            "stands above the pipeline reading all three; thought bubble: "
            "\"tester used 'full population'; cleaner had filtered to 'active "
            "users' — gap.\"\n\n"
            "RIGHT LANE (Lawyer): a stack of twelve case-file ticket cards "
            "(rendered compactly) each with several review-comment cards "
            "visible. An \"audit agent\" AI-assistant figure stands in front "
            "of the stack, with a thought bubble reading \"case-3 and case-9 "
            "both ruled work-product privilege — different agents, same "
            "criterion applied? checking…\"\n\n"
            "Caption: \"Three roles. Three flavors of audit. One substrate.\""
        ),
    ),

    PromptSpec(
        name="beat4-close",
        skill="beadwork-for-meta-analysis",
        aspect_ratio="16:9", quality="2k",
        prompt_body=(
            "A clean closing card.\n\n"
            "CENTER TOP: a stylized structured ticket card (with the now-"
            "familiar TITLE plus comments-with-author-and-timestamp shape) "
            "being read by a magnifying-glass icon labeled \"any agent can "
            "read this.\"\n\n"
            "BELOW the ticket: a horizontal label/banner reading \"signed + "
            "timestamped + structured = analyzable.\"\n\n"
            "BELOW THE BANNER: five small companion-skill icons arranged "
            "horizontally with their names underneath:\n"
            "1. compass icon — \"beadwork-overview\"\n"
            "2. clock + brain icon — \"beadwork-as-memory\"\n"
            "3. network icon — \"beadwork-as-bus\"\n"
            "4. decision-tree icon — \"beadwork-for-decisions\"\n"
            "5. wrench icon — \"beadwork-install\"\n\n"
            "BOTTOM: a small caption in italic \"open source. Denson Smith. "
            "bw itself by jallum.\"\n\n"
            "Caption: \"Meta-analysis is just another agent reading the "
            "substrate.\""
        ),
    ),

    # --------------------------------------------------------------------------
    # beadwork-for-decisions (4 images)
    # --------------------------------------------------------------------------

    PromptSpec(
        name="beat1-hook",
        skill="beadwork-for-decisions",
        aspect_ratio="16:9", quality="2k",
        prompt_body=(
            "A two-panel scene divided vertically.\n\n"
            "LEFT PANEL (warm tint, header \"Without a decision log\"): a "
            "calendar showing months passing horizontally — labels Jan, Feb, "
            "Mar, ..., Aug. At Jan: a small group of three figures with "
            "thought bubbles having a discussion — speech bubbles full of "
            "detail. By August (right side of calendar): the same scene but "
            "the figures have left and the speech bubbles have faded to "
            "outlines or fragments. A new person stands at the August mark "
            "with a confused thought bubble: \"why did we decide on this?\"\n\n"
            "RIGHT PANEL (cool tint, header \"With bw decision tickets\"): "
            "the same calendar layout. At the Jan position there's a ticket "
            "card with TITLE \"Auth: Auth0 vs in-house OAuth\", a description "
            "(\"options: Auth0, in-house OAuth, Firebase\"), and a stack of "
            "comment-bubbles labeled with author + date. The ticket card "
            "extends visually to the August position, unchanged. The new "
            "person at August reads the ticket with a clear thought bubble: "
            "\"now I understand the rationale.\"\n\n"
            "Caption: \"What decisions look like in six months.\""
        ),
    ),

    PromptSpec(
        name="beat2-mechanism",
        skill="beadwork-for-decisions",
        aspect_ratio="16:9", quality="2k",
        prompt_body=(
            "A single ticket card rendered cleanly with each part labeled.\n\n"
            "TITLE BAR at top: \"Auth: Auth0 vs in-house OAuth\" with a small "
            "label-tag chip reading \"decision\" and a status chip reading "
            "\"closed.\"\n\n"
            "DESCRIPTION BLOCK below the title, in a slightly muted "
            "background: \"Question: how do we authenticate users? Options "
            "considered: (1) Auth0 SaaS, (2) roll our own OAuth, (3) Firebase "
            "Auth.\"\n\n"
            "COMMENTS section, three comment-bubbles stacked vertically, each "
            "with author + date stamps:\n"
            "- \"alice · 2026-04-12\" — \"Auth0 wins on time-to-ship; rolling "
            "our own is at least 6 weeks of dev.\"\n"
            "- \"bob · 2026-04-13\" — \"concerned about per-user pricing as "
            "we scale; need to model.\"\n"
            "- \"alice · 2026-04-14\" — \"modeled, breakeven is at 50K MAU; "
            "we're at 2K.\"\n\n"
            "CLOSE-COMMENT at the bottom with a special highlighted border "
            "(thicker, distinct color):\n"
            "- \"closed: 2026-04-15 by alice — Decision: Auth0. Rationale: "
            "time-to-ship dominates at our scale; revisit if we cross 50K "
            "MAU.\"\n\n"
            "Caption: \"Decision = ticket. ADR shape, bw substrate.\""
        ),
    ),

    PromptSpec(
        name="beat3-scenarios",
        skill="beadwork-for-decisions",
        aspect_ratio="16:9", quality="2k",
        prompt_body=(
            "Three vertical lanes, each showing a decision-log scenario in a "
            "different professional setting.\n\n"
            "LEFT LANE (Engineer): a ticket card titled \"Architecture: REST "
            "vs gRPC for orders service\" with multiple comments showing "
            "trade-off analysis (latency, tooling, team familiarity). Below "
            "the ticket: a small \"6 months later\" arrow pointing to a "
            "new-engineer figure reading the ticket, with a thought bubble "
            "\"now I understand why.\"\n\n"
            "MIDDLE LANE (Lawyer): a privilege-log ticket card titled \"Doc "
            "4789: work-product privilege\" with a structured comment showing "
            "the legal reasoning (cited rule, reasoning chain, signed by an "
            "attorney name, dated). Below: a \"9 months later\" arrow "
            "pointing to an opposing-counsel figure reading the ticket, with "
            "a thought bubble \"reasoning preserved → court-defensible.\" A "
            "small gavel icon in the corner of the lane.\n\n"
            "RIGHT LANE (Solo Entrepreneur): a stack of three small "
            "expense-decision ticket cards titled \"MailerLite: vs "
            "ConvertKit,\" \"Hetzner: vs DigitalOcean,\" \"Notion Pro: vs "
            "free tier,\" each with a brief rationale-comment visible. "
            "Below: a \"tax time\" arrow pointing to an accountant figure "
            "with a tablet, reading the bw export, thought bubble \"every "
            "expense documented + reasoned.\"\n\n"
            "Caption: \"Three roles. Three flavors of decision log. Same "
            "ticket shape.\""
        ),
    ),

    PromptSpec(
        name="beat4-close",
        skill="beadwork-for-decisions",
        aspect_ratio="16:9", quality="2k",
        prompt_body=(
            "A clean closing card.\n\n"
            "CENTER: a stylized ticket card with the parts clearly labeled "
            "and visible: title, description block, three comments with "
            "author+timestamp, and a highlighted close-comment-with-rationale "
            "at the bottom.\n\n"
            "BELOW the ticket: a horizontal banner with the bold text \"any "
            "decision worth remembering = a bw ticket.\"\n\n"
            "BELOW THE BANNER: five small companion-skill icons arranged "
            "horizontally with their names:\n"
            "1. compass icon — \"beadwork-overview\"\n"
            "2. clock + brain icon — \"beadwork-as-memory\"\n"
            "3. network icon — \"beadwork-as-bus\"\n"
            "4. magnifying-glass icon — \"beadwork-for-meta-analysis\"\n"
            "5. wrench icon — \"beadwork-install\"\n\n"
            "BOTTOM: a small caption in italic \"open source. Denson Smith. "
            "bw itself by jallum.\"\n\n"
            "Caption: \"Any decision worth remembering is a ticket.\""
        ),
    ),
]


# =============================================================================
# Path computation per skill
# =============================================================================

def asset_path(spec: PromptSpec) -> Path:
    return REPO_ROOT / "skills" / spec.skill / "assets" / "images"


def html_mirror_path(spec: PromptSpec) -> Path:
    return REPO_ROOT / "skills" / spec.skill / "walkthrough_html" / "images"


# =============================================================================
# API key loading
# =============================================================================

def load_api_key() -> str:
    if shutil.which("op") is None:
        print("ERROR: 1Password CLI (`op`) not found on PATH.", file=sys.stderr)
        sys.exit(1)
    completed = subprocess.run(
        ["op", "read", OP_REFERENCE],
        capture_output=True, text=True, timeout=60, check=False,
    )
    if completed.returncode != 0:
        print(f"ERROR: `op read {OP_REFERENCE}` failed (exit {completed.returncode}).", file=sys.stderr)
        if completed.stderr.strip():
            print(f"op stderr: {completed.stderr.strip()}", file=sys.stderr)
        print(
            "Hint: 1Password Desktop must be running and signed in. "
            "Run `op account list` to verify.",
            file=sys.stderr,
        )
        sys.exit(1)
    value = completed.stdout.strip()
    if not value:
        print("ERROR: op read returned empty value.", file=sys.stderr)
        sys.exit(1)
    return value


# =============================================================================
# API helpers
# =============================================================================

def submit(key: str, prompt_text: str, quality: str, aspect_ratio: str) -> dict:
    headers = {
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    body = {"prompt": prompt_text, "quality": quality, "aspectRatio": aspect_ratio}
    resp = requests.post(f"{API_BASE}/generate", headers=headers, json=body, timeout=60)
    if resp.status_code >= 400:
        print(f"ERROR: POST /generate returned {resp.status_code}", file=sys.stderr)
        print(f"response: {resp.text[:2000]}", file=sys.stderr)
        sys.exit(1)
    return resp.json()


def extract_task_id(response: dict) -> str:
    for k in ("taskId", "task_id", "id", "task"):
        if k in response and response[k]:
            return str(response[k])
    data = response.get("data") or {}
    for k in ("taskId", "task_id", "id", "task"):
        if k in data and data[k]:
            return str(data[k])
    print("ERROR: could not find task id in submit response", file=sys.stderr)
    print(json.dumps(response, indent=2), file=sys.stderr)
    sys.exit(1)


def poll_one(key: str, task_id: str) -> Optional[dict]:
    headers = {"Authorization": f"Bearer {key}", "Accept": "application/json"}
    resp = requests.get(f"{API_BASE}/task/{task_id}", headers=headers, timeout=30)
    if resp.status_code >= 400:
        print(f"ERROR: GET /task/{task_id} returned {resp.status_code}", file=sys.stderr)
        print(f"response: {resp.text[:2000]}", file=sys.stderr)
        sys.exit(1)
    data = resp.json()
    status = str(data.get("status", "")).lower()
    if status in ("completed", "complete", "success", "done", "finished"):
        return data
    if status in ("failed", "error", "cancelled", "canceled"):
        print(f"ERROR: task {task_id} failed:\n{json.dumps(data, indent=2)}", file=sys.stderr)
        sys.exit(1)
    return None


def poll_until_all_done(key: str, task_ids: list[str]) -> dict[str, dict]:
    results: dict[str, dict] = {}
    pending = set(task_ids)
    start = time.monotonic()
    while pending:
        elapsed = int(time.monotonic() - start)
        if elapsed > POLL_TIMEOUT_S:
            print(f"ERROR: batch polling timed out after {POLL_TIMEOUT_S}s.", file=sys.stderr)
            print(f"  still pending: {sorted(pending)}", file=sys.stderr)
            sys.exit(1)
        for tid in list(pending):
            result = poll_one(key, tid)
            if result is not None:
                results[tid] = result
                pending.remove(tid)
                print(f"  [{elapsed:>3}s] task {tid} -> done ({len(pending)} still pending)")
        if pending:
            time.sleep(POLL_INTERVAL_S)
    return results


def extract_image_urls(result: dict) -> list[str]:
    urls: list[str] = []
    if isinstance(result.get("images"), list):
        for item in result["images"]:
            if isinstance(item, dict) and item.get("url"):
                urls.append(item["url"])
            elif isinstance(item, str):
                urls.append(item)
    if isinstance(result.get("imageUrls"), list):
        urls.extend(str(u) for u in result["imageUrls"])
    if isinstance(result.get("results"), list):
        for item in result["results"]:
            if isinstance(item, dict) and item.get("url"):
                urls.append(item["url"])
    if not urls and isinstance(result.get("data"), dict):
        urls.extend(extract_image_urls(result["data"]))
    if not urls and isinstance(result.get("url"), str):
        urls.append(result["url"])
    if not urls and isinstance(result.get("imageUrl"), str):
        urls.append(result["imageUrl"])
    seen = set()
    unique: list[str] = []
    for u in urls:
        if u not in seen:
            seen.add(u)
            unique.append(u)
    return unique


def infer_extension_from_bytes(content: bytes) -> str:
    if len(content) >= 8 and content[:8] == b"\x89PNG\r\n\x1a\n":
        return ".png"
    if len(content) >= 3 and content[:3] == b"\xff\xd8\xff":
        return ".jpg"
    if len(content) >= 12 and content[:4] == b"RIFF" and content[8:12] == b"WEBP":
        return ".webp"
    if len(content) >= 6 and content[:6] in (b"GIF87a", b"GIF89a"):
        return ".gif"
    return ".bin"


def download(url: str, dest_stem: Path) -> tuple[Path, int]:
    resp = requests.get(url, timeout=120)
    resp.raise_for_status()
    ext = infer_extension_from_bytes(resp.content)
    dest = dest_stem.with_suffix(ext)
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(resp.content)
    return dest, len(resp.content)


# =============================================================================
# Skip-existing
# =============================================================================

def already_downloaded(spec: PromptSpec) -> bool:
    base = asset_path(spec) / spec.name
    for ext in (".jpg", ".png", ".webp"):
        if base.with_suffix(ext).exists():
            return True
    return False


# =============================================================================
# Batch driver
# =============================================================================

def chunked(seq: list, n: int):
    for i in range(0, len(seq), n):
        yield seq[i:i + n]


def run_batch(prompts: list[PromptSpec], dry_run: bool) -> None:
    remaining = [p for p in prompts if not already_downloaded(p)]
    skipped = [p for p in prompts if already_downloaded(p)]

    if skipped:
        print(f"Skipping {len(skipped)} already-downloaded prompt(s):")
        for p in skipped:
            print(f"  - {p.skill}/{p.name}")
        print()

    if not remaining:
        print("Nothing to do — all prompts already have images on disk.")
        return

    if dry_run:
        print(f"DRY RUN — would submit {len(remaining)} prompts in waves of {MAX_CONCURRENT_SUBMISSIONS}:")
        for i, batch in enumerate(chunked(remaining, MAX_CONCURRENT_SUBMISSIONS), 1):
            print(f"\n  Wave {i} ({len(batch)} prompts):")
            for spec in batch:
                full = assemble_full_prompt(spec)
                print(f"    - {spec.skill}/{spec.name}  ({spec.aspect_ratio}, {spec.quality}, {len(full):,} chars)")
        return

    api_key = load_api_key()
    print(f"Loaded API key. Submitting {len(remaining)} prompts in waves of {MAX_CONCURRENT_SUBMISSIONS}.\n")

    total_credits_used = 0
    last_credits_remaining: Optional[int] = None

    for wave_idx, batch in enumerate(chunked(remaining, MAX_CONCURRENT_SUBMISSIONS), 1):
        print(f"=== Wave {wave_idx} — {len(batch)} prompts ===")

        task_id_to_spec: dict[str, PromptSpec] = {}
        for spec in batch:
            full_prompt = assemble_full_prompt(spec)
            print(f"  submitting {spec.skill}/{spec.name} ({spec.aspect_ratio}, {len(full_prompt):,} chars)")
            response = submit(api_key, full_prompt, spec.quality, spec.aspect_ratio)
            task_id = extract_task_id(response)
            print(f"    -> task {task_id}")
            credits_used = response.get("credits_used", response.get("creditsUsed"))
            credits_remaining = response.get("credits_remaining", response.get("creditsRemaining"))
            if credits_used is not None:
                total_credits_used += int(credits_used)
            if credits_remaining is not None:
                last_credits_remaining = int(credits_remaining)
            task_id_to_spec[task_id] = spec

        print(f"  polling {len(task_id_to_spec)} tasks to completion...")
        results = poll_until_all_done(api_key, list(task_id_to_spec.keys()))

        for task_id, result in results.items():
            spec = task_id_to_spec[task_id]
            urls = extract_image_urls(result)
            if not urls:
                print(f"  ERROR: task {task_id} ({spec.skill}/{spec.name}) completed but no image URLs", file=sys.stderr)
                print(json.dumps(result, indent=2), file=sys.stderr)
                continue

            saved_files: list[str] = []
            for i, url in enumerate(urls):
                suffix = "" if i == 0 else f"-v{i + 1}"

                src_stem = asset_path(spec) / f"{spec.name}{suffix}"
                src_dest, size = download(url, src_stem)
                saved_files.append(src_dest.name)

                mirror_stem = html_mirror_path(spec) / f"{spec.name}{suffix}"
                download(url, mirror_stem)

                print(f"  saved {spec.skill}/{spec.name}: {src_dest.name} ({size:,} bytes) + html mirror")

            sidecar = asset_path(spec) / f"{spec.name}.task.json"
            sidecar_payload = {
                "prompt_key": spec.name,
                "name": spec.name,
                "skill": spec.skill,
                "quality": spec.quality,
                "aspectRatio": spec.aspect_ratio,
                "task_id": task_id,
                "saved_files": saved_files,
                "result": result,
            }
            sidecar.write_text(
                json.dumps(sidecar_payload, indent=2, default=str, ensure_ascii=False),
                encoding="utf-8",
            )
            print(f"  saved sidecar {sidecar.relative_to(REPO_ROOT)}")

        print()

    print("=== Batch complete ===")
    print(f"  total credits used (this run): {total_credits_used}")
    if last_credits_remaining is not None:
        print(f"  credits remaining (last seen): {last_credits_remaining}")


def main() -> None:
    dry_run = "--dry-run" in sys.argv
    run_batch(PROMPTS, dry_run=dry_run)


if __name__ == "__main__":
    main()
