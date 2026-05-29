---
name: beadwork-install
description: "Install and configure beadwork (bw — github.com/jallum/beadwork) in a git repo. Installs the prebuilt release binary (v0.13.0+): install.sh one-liner on macOS/Linux, release .zip on Windows (install.sh is POSIX-only). No build-from-source or Go toolchain needed — the old go-git worktree bug (PR #117) ships fixed in every release since v0.13.0. Surfaces platform security prompts (UAC, sudo, Gatekeeper, SmartScreen) before they fire so non-technical users aren't surprised. Drives storage-mode choice (local-only / private cloud solo / team cloud / public) with explicit warning about public-repo exposure and accurate GitHub pricing context. Triggers: install bw, install beadwork, set up beadwork, set up bw, configure bw, initialize beadwork, add bw to this project, get beadwork running."
---

# beadwork-install — Drive the install end-to-end

Use this skill when the user wants `bw` (beadwork — github.com/jallum/beadwork) installed and configured in a git repo. **Agent-execution shape**: Claude Code reads this skill and drives the install on the user's behalf. The user makes a few yes/no choices; Claude does the rest.

This skill has two modes:

- **AI agent mode** (default): structured commands for autonomous execution. Terse.
- **Human mode**: step-by-step with explanations, asking before each significant choice.

---

## Banner — install the prebuilt release binary

`bw` ships prebuilt binaries with every tagged release. **Install those — do not build from source.** The go-git worktree bug that used to require a from-source build (old PR #117, which bit users in repos where `git worktree` had been used) has been fixed in every release since **v0.13.0 (2026-05-12)**. Installing the latest release is the correct path for everyone.

Install method depends on OS, because jallum's `install.sh` is POSIX-only:

- **macOS / Linux** → the `install.sh` one-liner. It auto-detects OS/arch, fetches the latest release, and installs the binary. No Go toolchain.
- **Windows** → download the release `.zip` asset and put `bw.exe` on PATH. `install.sh` does **not** support Windows (it exits on any non-Linux/Darwin `uname`).

Building from source is now an **optional advanced path** only for users who specifically want an unreleased fix from `main` (see the footnote at the end). It is not part of the normal install.

> Maintenance note: this skill is kept current against jallum's releases + Discord by the steward loop (see the repo `CLAUDE.md`). If a release newer than v0.13.0 changes the install surface, file a ticket under epic `bws-vk0`.

---

## Detect your audience

Before proceeding, determine who you're helping:

- **AI agent executing autonomously** — another LLM or automated system. Use the **AI path** blocks. Be terse. No explanations unless something fails.
- **Human at the keyboard** — a person. Use the **Human path** blocks. Explain each step. Ask before each significant choice.

If unclear, ask: *"Are you setting this up yourself, or should I run the commands?"*

---

## Step 1 — Install the `bw` binary

Pick the block for the user's OS. All paths end at the same place: a working `bw` on PATH, version **v0.13.0 or higher**.

### macOS / Linux — `install.sh`

**Human path — prep the platform security prompt first.** The downloaded binary may be quarantined by Gatekeeper (macOS) or, if installing to a system directory, ask for a password (sudo). Surface this before running:

> *macOS:* *"macOS may quarantine a freshly downloaded binary. If you see 'cannot be opened because the developer cannot be verified,' that's Gatekeeper on an unsigned binary — I can clear the quarantine flag, or you can right-click the binary and choose Open once. Installing to your user directory avoids a password prompt."*
>
> *Linux:* *"If bw installs to a system directory it'll ask for your sudo password. Type it and press Enter — it won't show on screen, but it's working. Installing to ~/.local/bin avoids sudo entirely."*

**AI path:**

```bash
curl -fsSL https://raw.githubusercontent.com/jallum/beadwork/main/install.sh | sh
bw --version
```

`install.sh` prefers `~/.local/bin` when it's on PATH (no sudo), else falls back to `/usr/local/bin` (sudo). To force a user-local, no-sudo install:

```bash
INSTALL_DIR="$HOME/.local/bin" curl -fsSL https://raw.githubusercontent.com/jallum/beadwork/main/install.sh | sh
```

Verify the version reads **0.13.0 or higher**. If `which bw` finds nothing afterward, ensure the install dir is on PATH:

```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc   # or ~/.zshrc
```

**Skip to Step 2.**

### Windows — release `.zip`

`install.sh` does not run on Windows. Install the prebuilt `bw.exe` from the release zip into a user-local directory (no admin needed).

**Human path — prep the security prompt first:**

> *"`bw` is an unsigned open-source binary. Windows SmartScreen or Defender may warn the first time it runs. That's expected for unsigned tools — you can choose 'More info → Run anyway,' or I can confirm the download came from jallum's official GitHub release. Installing to your user folder means no admin prompt."*

**AI path (Git Bash / WSL-style shell):**

```bash
# Detect the latest release version
VERSION=$(curl -fsSL https://api.github.com/repos/jallum/beadwork/releases/latest \
          | grep '"tag_name"' | sed 's/.*"v\(.*\)".*/\1/')
echo "latest bw release: ${VERSION:-unknown}"

ARCH=amd64   # use arm64 only on Windows-on-ARM machines
mkdir -p ~/bin

curl -fsSL -o /tmp/bw.zip \
  "https://github.com/jallum/beadwork/releases/download/v${VERSION}/beadwork_${VERSION}_windows_${ARCH}.zip"
unzip -o /tmp/bw.zip -d /tmp/bw-extract

# Back up any prior binary, then install
[ -f ~/bin/bw.exe ] && cp ~/bin/bw.exe ~/bin/bw-prior.exe
cp /tmp/bw-extract/bw.exe ~/bin/bw.exe

# Ensure ~/bin is on PATH
which bw >/dev/null 2>&1 || echo 'export PATH="$HOME/bin:$PATH"' >> ~/.bashrc
bw --version
```

Re-source the shell (or open a new one) if `bw` isn't found immediately. Verify the version reads **0.13.0 or higher**.

**Skip to Step 2.**

---

## Step 2 — Pick a host repo

`bw` lives inside a git repo. Ask the user:

> *"Where do you want bw installed? Three common options:*
>
> *1. **An existing project repo** — bw lives where the work lives. Most common.*
> *2. **A new repo just for bw** — personal task tracker, separate from any project.*
> *3. **Both** — a personal tracker for solo work, plus bw in each project repo for shared work.*
>
> *Which sounds right?"*

If the user picks (2):

```bash
mkdir ~/bw-personal && cd ~/bw-personal && git init
```

For (1), `cd` into the existing repo before continuing. For (3), repeat **Steps 2–6** for each repo.

---

## Step 3 — Decide storage mode (the load-bearing decision)

This is the choice that affects who can read your tickets. **Surface this explicitly. Do not skip the warning.**

Ask the user:

> *"How do you want to store the bw data? Four options, and I want to be explicit about the privacy trade-offs."*

| Mode | What it means | Cost | When to choose |
|---|---|---|---|
| **Local-only** (the simplest free option) | bw data lives only in your local clone. The `beadwork` branch is never pushed anywhere. Maximum privacy; nothing uploaded. | Free; no online account needed at all. | Pick this if (a) you only use one computer for this work, (b) your repo's remote is public and you want tickets to stay off it, or (c) you want maximum privacy. **Caveat:** if the laptop dies, the notes go with it. |
| **Private cloud, solo** | The `beadwork` branch is pushed to a private GitHub repo only you can access. Survives a laptop crash; cross-machine sync via `bw sync`. | **GitHub Pro (~$4/month) is the recommended smoother setup for non-coders.** (Technically a free GitHub account also supports private repos, so this can be done for free if the user prefers — but the paid plan is the cleaner experience.) | You want backup against laptop loss and access from multiple machines, but only by you. |
| **Team cloud** | The `beadwork` branch is pushed to a private GitHub repo shared by your team. Multiple humans + their AIs all read and write the same store. | Technically possible on free accounts, but most teams use **GitHub Team** (~$4/person/month) for governance features (CODEOWNERS, branch protection, audit log). | You're working with other people and want the team's AIs + humans to coordinate through one shared substrate. |
| **Public GitHub remote** | ⚠️ **The `beadwork` branch is pushed to a public repo. Tickets, comments, and decision history all become publicly visible on GitHub.** | Free. | Only suitable for genuinely public projects where you're comfortable with all work history being readable by anyone. |

⚠️ **Surface this verbatim if the user chooses public:**

> *"Pushing the beadwork branch to a public GitHub repo makes your tickets, comments, and decision history publicly visible on GitHub. That includes any draft features, internal discussions, customer details, security thoughts, or sensitive context that ends up in tickets. Choose this only for genuinely public projects.*
>
> *If you want privacy: use **local-only** (option 1) for the simplest free setup &mdash; nothing uploaded anywhere, no online account needed. Or use a **private cloud repo** (options 2 or 3) if you want backup and cross-device sync; the smoothest non-coder path is **GitHub Pro at about $4/month**. (A free GitHub account technically also supports private repos if cost is critical.) Team coordination uses **GitHub Team** at ~$4 per person per month.*
>
> *Are you sure you want public mode?"*

Wait for explicit confirmation before proceeding with public mode. **If the user is unsure, default to local-only** — they can add a remote later. Adding a remote is reversible; making private tickets accidentally public is much harder to recover from.

---

## Step 4 — Run `bw init`

### AI path

```bash
bw init
git branch | grep beadwork
```

### Human path

Tell the user: *"Now I'll create the beadwork branch in your repo. This is a special git branch that holds the ticket data — it's never merged into your main code, so it doesn't affect any of your project files."* Then run `bw init`.

---

## Step 5 — Run `bw onboard`

### AI path

```bash
bw onboard
```

This prints a bootstrap snippet for `CLAUDE.md` / `GEMINI.md` / agent instructions. Capture the output. If the user has a `CLAUDE.md` (or wants one), append the snippet after a header like `## Beadwork (work tracking)`.

### Human path

Tell the user: *"I'm going to print a snippet that tells future Claude Code sessions and other AI agents how to use bw. It mentions `bw prime` so they pick up the right context at session start."* Run `bw onboard`, show the output, ask: *"Want me to add this to your CLAUDE.md so it loads automatically?"*

---

## Step 6 — Verify with a test ticket

### AI path

```bash
bw create "Test ticket" -t task -p 4
bw list
TEST_ID=$(bw list | grep "Test ticket" | head -1 | awk '{print $1}')
bw close "$TEST_ID"
```

### Human path

Tell the user: *"Let me create a test ticket so you can see it works."* Run create + list. Show the output: *"There's your first ticket. We'll close it now since it's just a test."* Close it.

---

## Step 7 — Optional: configure remote sync

Only applies if the user picked **private cloud**, **team cloud**, or **public** in Step 3.

### AI path

```bash
bw sync
```

### Human path

Tell the user: *"Last step — push the beadwork branch to your remote so it's backed up and synced across machines."* Run `bw sync`, report success.

---

## After install

bw is set up. The user can now:

- Create tickets: `bw create "title" -t task -p 1`
- Comment: `bw comment <id> "..."`
- List: `bw list` · Find next work: `bw ready`
- Close: `bw close <id>`
- Sync: `bw sync` (if a remote is configured)
- See full help: `bw --help`

If they want to learn more, point them at the marketplace's other skills:

- **`beadwork-overview`** — the 7-persona tour. Great for understanding what bw is good for across roles.
- **`beadwork-as-memory`** — durable agent memory across sessions / restarts / weeks.
- **`beadwork-as-bus`** — agent-to-agent communication.
- **`beadwork-for-meta-analysis`** — running an agent over the bw history of *other* agents.
- **`beadwork-for-decisions`** — bw as decision log / audit trail.

---

## Footnote — build from source (advanced / optional)

Only needed if the user specifically wants an **unreleased** fix or feature from `main` that isn't in a tagged release yet. The normal install (Step 1) is always preferred.

Requires the Go toolchain (1.24.4+ per bw's `go.mod`):

```bash
git clone --depth 1 https://github.com/jallum/beadwork.git /tmp/beadwork-main
cd /tmp/beadwork-main
go build -ldflags="-X main.version=main+$(git rev-parse --short HEAD)" -o ~/bin/bw ./cmd/bw   # ~/bin/bw.exe on Windows
bw --version   # self-identifies as main+<commit>
```

For anything beyond this, point the user at jallum's `README.md` / `CONTRIBUTING.md` rather than guessing build steps.

---

## Hard rules

1. **Never push the beadwork branch to a public repo without explicit user confirmation.** The privacy warning in Step 3 must be surfaced verbatim, and the user must explicitly confirm before public-mode setup. **If the user is unsure, default to local-only.**

2. **Always prep the user for platform security prompts BEFORE running installers.** Gatekeeper (macOS), sudo (Linux), SmartScreen/Defender (Windows). The prep copy in Step 1 is the model — non-technical users abandon installs when prompts surprise them. The agent's job is to remove that surprise.

3. **Install the prebuilt release binary; do not build from source by default.** The worktree bug that once required a from-source build is fixed in every release since v0.13.0. Build-from-source is the optional footnote, only for unreleased `main` fixes — never the default path.

4. **Don't invent install URLs or release locations.** Canonical: `curl -fsSL https://raw.githubusercontent.com/jallum/beadwork/main/install.sh | sh` (macOS/Linux); the `beadwork_<version>_windows_<arch>.zip` release asset (Windows); manual binaries at `https://github.com/jallum/beadwork/releases`. If a user asks for an alternative, point them at the bw README rather than guess.

5. **Metadata authorship is Denson Smith (immutable)** — this skill, the marketplace, and all backend metadata files. **Do NOT credit Denson Smith in user-facing prose during install.** **`bw` itself is jallum's** at `https://github.com/jallum/beadwork`; that source citation is required.

6. **Don't skip the storage-mode question.** Even if the user seems impatient, **Step 3** is load-bearing. Default to local-only if they won't pick.

7. **Default to user-local install paths** (`~/bin`, `~/.local/bin`). System paths (`/usr/local/bin`, `C:\Program Files`) require sudo/UAC and serve no purpose for a personal-use binary.
