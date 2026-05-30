/* beadwork guides — shared top navigation.
   Single source of the page order. Add / reorder guides in SEQ only;
   every page picks up Back / Home / Next because each page includes this script. */
(function () {
  // Reading order. Back/Next walk this list; Home is the first entry.
  var SEQ = [
    { f: "g1-is-bw-for-you.html",         t: "Is beadwork for you?" },
    { f: "g2-you-talk-your-ai.html",      t: "You talk to your AI" },
    { f: "g3-what-it-can-do.html",        t: "What it can do" },
    { f: "g11-memory.html",               t: "Durable memory" },
    { f: "g12-coordination.html",         t: "Coordination (a team)" },
    { f: "g13-decisions.html",            t: "Decisions" },
    { f: "g10-meta-analysis.html",        t: "Meta-analysis" },
    { f: "g4-where-your-data-lives.html", t: "Where your data lives" },
    { f: "g5-why-git-matters.html",       t: "Why it's just git" },
    { f: "g6-no-ceremony.html",           t: "No ceremony (solo)" },
    { f: "g8-getting-set-up.html",        t: "Getting set up" },
    { f: "g7-first-session-glossary.html", t: "First session + glossary" },
    { f: "g9-three-ways.html",            t: "The same tool, three ways" },
  ];

  var CSS = [
    ".bw-nav{position:sticky;top:0;z-index:50;display:flex;align-items:center;justify-content:space-between;gap:0.75rem;",
    "  background:#fff;border-bottom:1px solid #e2e8f0;padding:0.6rem 1rem;",
    "  font:600 0.92rem/1 -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;}",
    ".bw-nav a,.bw-nav span{display:inline-flex;align-items:center;gap:0.35rem;padding:0.45rem 0.8rem;border-radius:7px;white-space:nowrap;}",
    ".bw-nav a{color:#0f766e;text-decoration:none;border:1px solid #cfe8e2;}",
    ".bw-nav a:hover{background:#e6f4f1;}",
    ".bw-nav .bw-home{color:#0f172a;border-color:#e2e8f0;}",
    ".bw-nav .bw-home:hover{background:#f1f5f9;}",
    ".bw-nav .bw-disabled{color:#cbd5e1;border:1px solid #eef2f7;cursor:default;}",
    "@media (max-width:480px){",
    "  .bw-nav{padding:0.55rem 0.7rem;font-size:0.85rem;}",
    "  .bw-nav a,.bw-nav span{padding:0.4rem 0.55rem;}",
    "}",
  ].join("\n");

  function el(tag, cls, text, href, title) {
    var n = document.createElement(tag);
    if (cls) n.className = cls;
    if (text) n.textContent = text;
    if (href) n.href = href;
    if (title) n.title = title;
    return n;
  }

  function build() {
    var style = document.createElement("style");
    style.textContent = CSS;
    document.head.appendChild(style);

    var current = location.pathname.split("/").pop();
    var i = SEQ.map(function (s) { return s.f; }).indexOf(current);

    var nav = document.createElement("nav");
    nav.className = "bw-nav";
    nav.setAttribute("aria-label", "Guide navigation");

    // Back
    if (i > 0) {
      nav.appendChild(el("a", "bw-back", "← Back", SEQ[i - 1].f, SEQ[i - 1].t));
    } else {
      nav.appendChild(el("span", "bw-disabled", "← Back"));
    }

    // Home
    nav.appendChild(el("a", "bw-home", "Home", SEQ[0].f, SEQ[0].t));

    // Next
    if (i > -1 && i < SEQ.length - 1) {
      nav.appendChild(el("a", "bw-next", "Next →", SEQ[i + 1].f, SEQ[i + 1].t));
    } else {
      nav.appendChild(el("span", "bw-disabled", "Next →"));
    }

    document.body.insertBefore(nav, document.body.firstChild);
  }

  if (document.readyState !== "loading") build();
  else document.addEventListener("DOMContentLoaded", build);
})();
