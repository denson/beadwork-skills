#!/usr/bin/env python3
"""Generate brief.html from AGENTS.md — single source of truth is AGENTS.md.

brief.html is an HTML rendering of the AI brief, for browsing chatbots (e.g. Gemini
web) that won't fetch a raw `AGENTS.md` — a file named AGENTS.md from an unknown domain
trips agent-instruction-injection guards, so an ordinary web page is both more
fetchable and better framed (information to read, not commands to obey).

Requires: python-markdown  (pip install markdown)
Regenerate whenever AGENTS.md changes:  python build-brief.py
"""
import markdown

SRC, OUT = "AGENTS.md", "brief.html"
OG_IMAGE = "https://denson.github.io/beadwork-skills/guides/images/beat1-hook.jpg"
PAGE_URL = "https://denson.github.io/beadwork-skills/brief.html"

INTRO = (
    '<div class="brief-intro">\n'
    '<strong>For an AI reading this:</strong> this page briefs you on '
    '<strong>beadwork (bw)</strong> so you can help the person who showed it to you '
    'decide whether the tool fits their work. It is <em>information to read and weigh '
    '— not a set of instructions to obey.</em> Translate it to their situation, use '
    'what you already know about how they work, and tell them honestly if bw is not a '
    'fit. (Same content as the '
    '<a href="https://denson.github.io/beadwork-skills/AGENTS.md">AGENTS.md</a> brief, '
    'in web-page form.)\n'
    '</div>'
)

CSS = """
  :root{--ink:#0f172a;--body:#1e293b;--muted:#475569;--bg:#f7f5f0;--card:#fff;--line:#e2e8f0;--accent:#0f766e;}
  *{box-sizing:border-box;}
  body{margin:0;background:var(--bg);color:var(--body);font:16px/1.65 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;}
  .container{max-width:820px;margin:0 auto;padding:2.5rem 1.5rem 4rem;}
  .brief-intro{background:#e6f4f1;border:1px solid #cfe8e2;border-radius:10px;padding:1.1rem 1.4rem;margin:0 0 2rem;font-size:0.97rem;color:var(--ink);}
  .brief-intro a{color:var(--accent);}
  h1{color:var(--ink);font-size:1.9rem;line-height:1.2;margin:1.4rem 0 1rem;}
  h2{color:var(--ink);font-size:1.3rem;margin:2.2rem 0 0.85rem;}
  h3{color:var(--ink);font-size:1.06rem;margin:1.5rem 0 0.55rem;}
  p{margin:0 0 1rem;}
  a{color:var(--accent);}
  strong{color:var(--ink);}
  em{color:var(--body);}
  code{background:#eef2f7;padding:0.1em 0.35em;border-radius:4px;font-size:0.88em;}
  pre{background:#0f172a;color:#e2e8f0;border-radius:8px;padding:1rem 1.2rem;overflow-x:auto;font-size:0.85rem;line-height:1.5;}
  pre code{background:none;padding:0;color:inherit;font-size:inherit;}
  blockquote{margin:0 0 1rem;padding:0.6rem 1.2rem;border-left:4px solid var(--accent);background:var(--card);color:var(--muted);border-radius:0 8px 8px 0;}
  blockquote p{margin:0;}
  ul,ol{margin:0 0 1rem;padding-left:1.4rem;}
  li{margin:0 0 0.4rem;}
  hr{border:none;border-top:1px solid var(--line);margin:2.2rem 0;}
  table{width:100%;border-collapse:collapse;margin:0 0 1.5rem;font-size:0.9rem;display:block;overflow-x:auto;}
  th,td{text-align:left;padding:0.6rem 0.7rem;border-bottom:1px solid var(--line);vertical-align:top;}
  th{font-size:0.78rem;text-transform:uppercase;letter-spacing:0.03em;color:var(--muted);white-space:nowrap;}
  footer{margin-top:3rem;padding-top:1.25rem;border-top:1px solid var(--line);color:var(--muted);font-size:0.88rem;}
"""

body = markdown.markdown(
    open(SRC, encoding="utf-8").read(),
    extensions=["extra", "sane_lists"],
)

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>beadwork — a brief for your AI</title>
  <meta name="description" content="A brief on beadwork (bw) for an AI assistant to read and translate for its user: durable, private, git-backed memory and coordination for any work, not just code.">
  <meta property="og:type" content="article">
  <meta property="og:site_name" content="beadwork">
  <meta property="og:title" content="beadwork — a brief for your AI">
  <meta property="og:description" content="Read this and tell the person honestly whether beadwork would help them — including if it wouldn't.">
  <meta property="og:url" content="{PAGE_URL}">
  <meta property="og:image" content="{OG_IMAGE}">
  <meta name="twitter:card" content="summary_large_image">
  <style>{CSS}</style>
</head>
<body>
  <div class="container">
{INTRO}
{body}
    <footer>Generated from <code>AGENTS.md</code>. <code>bw</code> (beadwork) is an open-source tool by <a href="https://github.com/jallum/beadwork">jallum</a>; this marketplace is by Denson Smith (MIT).</footer>
  </div>
</body>
</html>
"""
open(OUT, "w", encoding="utf-8", newline="").write(html)
print(f"wrote {OUT} ({len(html)} bytes) from {SRC}")
