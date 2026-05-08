---
name: beadwork-install
description: "Install and configure beadwork (bw — github.com/jallum/beadwork) in a git repo. Adapts to bw release state: uses install.sh if a release containing PR #117 is available, builds from source on main otherwise. Handles Go toolchain prerequisite. Surfaces platform security prompts (UAC, sudo, Gatekeeper) before they fire so non-technical users aren't surprised. Drives storage-mode choice (local-only / private cloud solo / team cloud / public) with explicit warning about public-repo exposure and accurate GitHub pricing context. Triggers: install bw, install beadwork, set up beadwork, set up bw, configure bw, initialize beadwork, add bw to this project, get beadwork running."
---

# beadwork-install — Drive the install end-to-end

Use this skill when the user wants `bw` (beadwork — github.com/jallum/beadwork) installed and configured in a git repo. **Agent-execution shape**: Claude Code reads this skill and drives the install on the user's behalf. The user makes a few yes/no choices; Claude does the rest.

This skill has two modes:

- **AI agent mode** (default): structured commands for autonomous execution. Terse.
- **Human mode**: step-by-step with explanations, asking before each significant choice.

---

## Banner — install path adapts to bw release state

`bw` is in active development. As of this skill's authoring (2026-05-08), the latest tagged release is **v0.12.3** (2026-04-12) and contains a real bug with the go-git library that bites users running bw in repos where `git worktree` has been used. **PR #117** (merged to bw `main` 2026-04-17) fixes it, but no tagged release contains the fix yet.

This skill **adapts based on bw release state at runtime**:

- **If the latest tagged release is v0.12.4 or higher** (which will contain PR #117): the agent uses the simple `install.sh` one-curl path. Same install, no Go toolchain needed.
- **If the latest is still v0.12.3**: the agent builds bw from source on `main` to avoid the bug. Adds Go toolchain prerequisite + a few extra steps.

Both paths produce a working bw binary. **The from-source path is empirically verified** as of 2026-05-08.

The skill author monitors jallum's repo + Discord and will revise this skill to remove the from-source path once v0.12.4+ is no longer relevant. Until then, the dual-path logic below ensures the right path runs without manual intervention.

---

## Detect your audience

Before proceeding, determine who you're helping:

- **AI agent executing autonomously** — another LLM or automated system. Use the **AI path** sections. Be terse. No explanations unless something fails.
- **Human at the keyboard** — a person. Use the **Human path** sections. Explain each step. Ask before each significant choice.

If unclear, ask: *"Are you setting this up yourself, or should I run the commands?"*

---

## Step 1 — Detect bw release state

### AI path

```bash
LATEST=$(curl -fsSL https://api.github.com/repos/jallum/beadwork/releases/latest 2>/dev/null \
         | grep -m1 '"tag_name"' \
         | sed 's/.*"v\?\([^"]*\)".*/\1/')
echo "Latest bw release tag: ${LATEST:-unknown}"
```

Compare `$LATEST` against `0.12.4` (semver, basic string compare works for `0.12.x` family):

- If `$LATEST` >= `0.12.4`: proceed to **Path A** (`install.sh`).
- If `$LATEST` is `0.12.3` or unknown (API fail / no internet): proceed to **Path B** (build from source). Path B always works.

### Human path

Tell the user: *"Let me check the latest bw release."* Run the curl. If `>= 0.12.4`, say *"Good news — there's a release with the worktree fix. We'll use the simple curl install."* Otherwise: *"The latest release (v0.12.3) has a bug that affects users running bw across git worktrees. I'll build from source instead — same end result, just a couple extra steps."*

---

# Path A — install via `install.sh` (when v0.12.4+ is the latest tag)

## Step A1 — Run the install script

### AI path

```bash
curl -fsSL https://raw.githubusercontent.com/jallum/beadwork/main/install.sh | sh
bw --version
```

Verify the version reads v0.12.4 or higher.

### Human path

Tell the user: *"I'll install bw via jallum's install script. It downloads a single binary."* Run the curl, report the version.

**Skip to Step 5 — Pick a host repo.**

---

# Path B — build from source (current canonical path until v0.12.4+ ships)

## Step B1 — Install Go toolchain (prerequisite)

bw requires Go 1.24.4+ per its `go.mod`. First, check if Go is installed:

```bash
go version
```

If Go is installed and version is 1.24.4+: skip to **Step B2**.

If Go is missing: install it. **Before running the install command**, prep the user for the platform security prompt that will appear. Non-technical users abandon installs when these prompts surprise them.

### Windows (winget)

**Surface this verbatim before running the install command:**

> *"Windows will show a security prompt asking permission to install. The publisher should say 'GoLang' (or 'Microsoft' for winget itself). This is normal — Windows protects you from unsigned installers. Click 'Yes' to proceed.*
>
> *If the publisher field shows something unexpected (not 'GoLang' or 'Microsoft'), stop and tell me — that would indicate a tampered installer."*

Then run:

```bash
winget install -e --id GoLang.Go --silent --accept-package-agreements --accept-source-agreements
```

After install, current shell may not have updated PATH. Either open a new shell, or for the current shell:

```bash
export PATH="/c/Program Files/Go/bin:$PATH"
```

Verify:

```bash
go version
```

### macOS (Homebrew preferred)

**Surface this verbatim before running:**

> *"On macOS, when Homebrew installs Go, the Terminal will ask for your Mac login password. Type it and press Enter — the password won't appear on screen as you type, but it's working. This is Homebrew installing to a protected directory."*

Then run:

```bash
brew install go
```

If Homebrew isn't installed, fall back to the official installer from `https://go.dev/dl/`. Note that pkg-installed binaries trigger Gatekeeper on first run; right-click → **Open** bypasses it once.

Verify:

```bash
go version
```

### Linux (apt / dnf / pacman)

**Surface this verbatim before running:**

> *"Linux will ask for your sudo password. Type it and press Enter — the password won't appear on screen as you type, but it's working."*

Then run the appropriate one:

```bash
sudo apt install golang-go     # Debian / Ubuntu
sudo dnf install golang        # Fedora / RHEL
sudo pacman -S go              # Arch
```

If the package version is older than 1.24.4, install from `https://go.dev/dl/` tarball instead.

Verify:

```bash
go version
```

## Step B2 — Clone bw main

### AI path

```bash
rm -rf /tmp/beadwork-main
git clone --depth 1 https://github.com/jallum/beadwork.git /tmp/beadwork-main
ls /tmp/beadwork-main/internal/repo/extfilter.go
```

The presence of `internal/repo/extfilter.go` confirms PR #117's `extFilteringStorer` is in the source. If the file is missing, the clone is stale or wrong — re-clone fresh.

### Human path

Tell the user: *"I'll clone bw's main branch to a temporary directory."* Run the clone. Confirm `extfilter.go` exists.

## Step B3 — Build with version-string injection

bw's source hardcodes the version string as `0.12.3` (since main hasn't been bumped post-PR-#117). To avoid confusing the resulting binary with the released v0.12.3, inject the commit hash at build time so the binary self-identifies:

### AI path

Detect platform binary extension:

```bash
cd /tmp/beadwork-main
COMMIT=$(git rev-parse --short HEAD)

# Windows: produces .exe
# macOS / Linux: no extension
case "$OSTYPE" in
  msys*|cygwin*|win*) BIN=/tmp/bw-main.exe ;;
  *)                  BIN=/tmp/bw-main ;;
esac

go build -ldflags="-X main.version=main+${COMMIT}" -o "$BIN" ./cmd/bw
```

The first build downloads ~10 dependency packages. Allow ~30-60 seconds depending on network.

### Human path

Tell the user: *"Building bw from source. The first build takes about 30-60 seconds — Go downloads dependencies."* Run the build.

## Step B4 — Backup existing bw + install new binary

User-local install paths avoid sudo/UAC for the bw binary itself. Only the Go prereq required elevated permissions.

| OS | Path |
|---|---|
| Windows | `~/bin/bw.exe` (e.g. `/c/Users/<you>/bin/bw.exe`) |
| macOS / Linux | `~/.local/bin/bw` |

### AI path (Windows)

```bash
mkdir -p ~/bin
if [ -f ~/bin/bw.exe ]; then
  cp ~/bin/bw.exe ~/bin/bw-prior.exe
fi
cp /tmp/bw-main.exe ~/bin/bw.exe
```

### AI path (macOS / Linux)

```bash
mkdir -p ~/.local/bin
if [ -f ~/.local/bin/bw ]; then
  cp ~/.local/bin/bw ~/.local/bin/bw-prior
fi
cp /tmp/bw-main ~/.local/bin/bw
chmod +x ~/.local/bin/bw
```

Verify the user-local directory is on PATH:

```bash
which bw
```

If `which bw` returns nothing or points elsewhere, add the user-local directory to PATH:

```bash
# Windows / Git Bash:
echo 'export PATH="$HOME/bin:$PATH"' >> ~/.bashrc

# macOS / Linux:
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
```

Re-source the shell config or open a new shell.

### Human path

Same commands; explain that bw is installing to a user-local directory so no admin permission is needed.

## Step B5 — Verify

```bash
bw --version
```

Expected output: `bw main+<commit-sha>` (e.g. `bw main+dc1c4be4`) — the ldflags injection from Step B3 makes the binary self-identify as a from-source build, distinguishing it from the released v0.12.3.

If the output reads `bw 0.12.3` (no `main+` prefix), the binary is the release, not the from-source build. Re-check **Step B4** — the cp may have failed or `which bw` may be pointing at the wrong binary.

## Step B6 — Smoke test (mandatory)

This step empirically confirms the worktreeConfig fix is in the running binary. **Do not skip** — `go build` exiting 0 is necessary but not sufficient evidence that the fix works.

```bash
# Pick any git repo — empty test repo works fine
mkdir -p /tmp/bw-smoke-test
cd /tmp/bw-smoke-test
git init -q

# Introduce the broken pattern (the exact config Claude Code's worktree harness writes)
git config extensions.worktreeconfig true

# Run bw prime — should succeed under the fix
bw prime
SMOKE_EXIT=$?

# Clean up the test repo's broken pattern (irrelevant here, just hygiene)
git config --unset extensions.worktreeconfig

if [ $SMOKE_EXIT -eq 0 ]; then
  echo "SMOKE TEST PASSED — bw fix is in place."
else
  echo "SMOKE TEST FAILED — got the v0.12.3 binary somehow. Re-check Step B4 and B5."
  exit 1
fi
```

Failure here means the user has the buggy v0.12.3 binary on PATH despite the build appearing to succeed. Common cause: the user's shell PATH found a different `bw` binary first. `which bw` will reveal it.

---

# Steps 5-10: same regardless of which path was taken

## Step 5 — Pick a host repo

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

For (1), `cd` into the existing repo before continuing.

For (3), repeat **Steps 5-10** for each repo.

## Step 6 — Decide storage mode (the load-bearing decision)

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

## Step 7 — Run `bw init`

### AI path

```bash
bw init
git branch | grep beadwork
```

### Human path

Tell the user: *"Now I'll create the beadwork branch in your repo. This is a special git branch that holds the ticket data — it's never merged into your main code, so it doesn't affect any of your project files."* Then run `bw init`.

## Step 8 — Run `bw onboard`

### AI path

```bash
bw onboard
```

This prints a bootstrap snippet for `CLAUDE.md` / `GEMINI.md` / agent instructions. Capture the output.

If the user has a `CLAUDE.md` (or wants one), append the snippet to it after a section header like `## Beadwork (work tracking)`.

### Human path

Tell the user: *"I'm going to print a snippet that tells future Claude Code sessions and other AI agents how to use bw. It mentions `bw prime` so they pick up the right context at session start."* Run `bw onboard`, show the output, ask: *"Want me to add this to your CLAUDE.md so it loads automatically?"*

## Step 9 — Verify with test ticket

### AI path

```bash
bw create "Test ticket" -t task -p 4
bw list
TEST_ID=$(bw list | grep "Test ticket" | head -1 | awk '{print $1}')
bw close "$TEST_ID"
```

### Human path

Tell the user: *"Let me create a test ticket so you can see it works."* Run create + list. Show output: *"There's your first ticket. We'll close it now since it's just a test."* Close it.

## Step 10 — Optional: configure remote sync

This step only applies if the user picked **Private GitHub remote** or **Public GitHub remote** in Step 6.

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
- List: `bw list`
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

## Hard rules

1. **Never push the beadwork branch to a public repo without explicit user confirmation.** The privacy warning in Step 6 must be surfaced verbatim, and the user must explicitly confirm "yes I want this public" before proceeding with public-mode setup. **If the user is unsure, default to local-only.**

2. **Always prep the user for platform security prompts BEFORE running installers.** UAC on Windows, sudo on macOS/Linux, Gatekeeper on macOS direct downloads. The skill copy in **Step B1** is verbatim, not optional. Non-technical users abandon installs when prompts surprise them. The agent's job is to remove that surprise.

3. **The smoke test in Step B6 is mandatory.** It empirically distinguishes "I have the fix" from "I have the bug." `go build` exiting 0 is necessary but not sufficient. Don't skip; don't assume.

4. **Don't invent install URLs or release locations.** The canonical install is `curl -fsSL https://raw.githubusercontent.com/jallum/beadwork/main/install.sh | sh` for tagged releases (Path A), or build from source per **Path B** otherwise. Manual binary downloads from `https://github.com/jallum/beadwork/releases`. If a user asks for an alternative install path, point them at the bw README rather than guess.

5. **Metadata authorship is Denson Smith (immutable)** — this skill, the marketplace, and all backend metadata files. **Do NOT credit Denson Smith in user-facing prose during install** (the walkthroughs that talk to the user). **`bw` itself is jallum's** at `https://github.com/jallum/beadwork`; that source citation is required.

6. **Don't skip the storage-mode question.** Even if the user seems impatient, **Step 6** is load-bearing. Default to local-only if they really won't pick.

7. **Default to user-local install paths** (`~/bin`, `~/.local/bin`). System paths (`/usr/local/bin`, `C:\Program Files`) require sudo/UAC and serve no purpose for a personal-use binary.
