"""Build the GitHub Pages site in docs/ from the update pages in updates/.

Update pages are HTML fragments (title + style + content). This wraps each in a
full document and writes an index listing them newest first.
"""
import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "updates"
OUT = ROOT / "docs"

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>body{margin:0}img{max-width:100%}</style>
"""

INDEX_STYLE = """<title>Sentience Investigation</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:wght@400;700&family=Bricolage+Grotesque:opsz,wght@12..96,700&family=IBM+Plex+Mono:wght@400&display=swap">
<style>
:root{--bg:#f5f8f7;--fg:#14211e;--muted:#51635e;--line:#c9d5d1;--accent:#0b6e63}
@media (prefers-color-scheme: dark){:root{--bg:#0f1514;--fg:#e2ebe8;--muted:#9bb0aa;--line:#2c3a37;--accent:#5fd0bf;color-scheme:dark}}
body{background:var(--bg);color:var(--fg);font-family:"Atkinson Hyperlegible","Helvetica Neue",Arial,sans-serif;font-size:1.0625rem;line-height:1.6}
.wrap{max-width:44rem;margin:0 auto;padding:2.5rem 1.25rem 4rem;display:flex;flex-direction:column;gap:2rem}
h1{font-family:"Bricolage Grotesque",system-ui,sans-serif;font-size:clamp(2rem,6vw,2.8rem);line-height:1.1;margin:0}
p{margin:0}
ol{list-style:none;margin:0;padding:0;display:flex;flex-direction:column}
li{border-top:1px solid var(--line);padding:1.1rem 0;display:flex;flex-direction:column;gap:.3rem}
.d{font-family:"IBM Plex Mono",ui-monospace,monospace;font-size:.8rem;letter-spacing:.06em;text-transform:uppercase;color:var(--muted)}
a{color:var(--accent);font-weight:700;font-size:1.2rem;text-decoration-thickness:1px;text-underline-offset:3px}
.s{color:var(--muted)}
</style>
"""


def main():
    OUT.mkdir(exist_ok=True)
    (OUT / ".nojekyll").write_text("")
    items = []
    for f in sorted(SRC.glob("*.html"), reverse=True):
        body = f.read_text()
        (OUT / f.name).write_text(
            HEAD + body.replace("<div class=\"wrap\">", "</head>\n<body>\n<div class=\"wrap\">", 1)
            + '\n<p style="text-align:center;padding:0 1rem 3rem"><a href="./">All updates</a></p>\n</body>\n</html>\n')
        h1 = re.search(r"<h1>(.*?)</h1>", body, re.S)
        eyebrow = re.search(r'class="eyebrow">(.*?)<', body, re.S)
        lede = re.search(r'class="lede">(.*?)</p>', body, re.S)
        items.append((f.name, eyebrow.group(1) if eyebrow else f.stem,
                      h1.group(1) if h1 else f.stem,
                      re.sub(r"<.*?>", "", lede.group(1)) if lede else ""))
    lis = "\n".join(
        f'<li><span class="d">{html.escape(html.unescape(e))}</span><a href="{n}">{t}</a>'
        f'<span class="s">{s}</span></li>' for n, e, t, s in items)
    (OUT / "index.html").write_text(
        HEAD + INDEX_STYLE + "</head>\n<body>\n<div class=\"wrap\">\n"
        "<h1>Where does feeling come from?</h1>\n"
        "<p>An ongoing investigation into sentience: reading the research, then testing each possible "
        "answer with simulations and calculations to see which survive. Each update is written to be "
        "read with no background.</p>\n"
        f"<ol>\n{lis}\n</ol>\n</div>\n</body>\n</html>\n")
    print(f"built {len(items)} update(s) into {OUT}")


if __name__ == "__main__":
    main()
