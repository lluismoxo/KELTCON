#!/usr/bin/env python3
"""Localize ALL Google Fonts across the site/ pages.
- find every fonts.googleapis.com/css?family=... URL in the HTML files
- download each CSS (browser UA -> woff2), download referenced woff2 (deduped)
- rewrite CSS to point at local woff2
- rewrite each HTML to point at the local CSS
Local layout: site/_gfonts/<md5>.css  and  site/_gfonts/woff2/<name>.woff2
"""
import os, re, hashlib, glob, html as htmlmod, urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.join(ROOT, "site")
GF = os.path.join(SITE, "_gfonts")
WOFF = os.path.join(GF, "woff2")
os.makedirs(WOFF, exist_ok=True)

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0 Safari/537.36")

def fetch(url, binary=False):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        data = r.read()
    return data if binary else data.decode("utf-8")

html_files = glob.glob(os.path.join(SITE, "**", "index.html"), recursive=True)

# 1. collect unique google css URLs (raw, as they appear, entity-decoded for fetching)
url_re = re.compile(r'https://fonts\.googleapis\.com/css\?family=[^"\'\s>]+')
raw_urls = set()
for f in html_files:
    txt = open(f, encoding="utf-8").read()
    for m in url_re.findall(txt):
        raw_urls.add(m)

print(f"distinct google css URLs in HTML: {len(raw_urls)}")

# map: raw_url_as_in_html -> local css relative path (from site root)
url_to_local = {}
woff_seen = {}  # gstatic url -> local filename

for raw in sorted(raw_urls):
    fetch_url = htmlmod.unescape(raw)  # &#038; / &amp; -> &
    css = fetch(fetch_url)
    # download woff2 referenced
    for gs in set(re.findall(r'https://fonts\.gstatic\.com/[^)\'"]+\.woff2', css)):
        name = gs.split("/")[-1]
        if name not in woff_seen:
            open(os.path.join(WOFF, name), "wb").write(fetch(gs, binary=True))
            woff_seen[name] = name
        css = css.replace(gs, f"woff2/{name}")
    h = hashlib.md5(raw.encode()).hexdigest()[:12]
    cssname = f"{h}.css"
    open(os.path.join(GF, cssname), "w", encoding="utf-8").write(css)
    url_to_local[raw] = f"/_gfonts/{cssname}"

print(f"woff2 downloaded (unique): {len(woff_seen)}")
print(f"local css written: {len(url_to_local)}")

# 2. rewrite HTML: replace each raw google url with local /_gfonts/<hash>.css
for f in html_files:
    txt = open(f, encoding="utf-8").read()
    n = 0
    for raw, local in url_to_local.items():
        if raw in txt:
            txt = txt.replace(raw, local)
            n += 1
    open(f, "w", encoding="utf-8").write(txt)

print("html files rewritten for gfonts:", len(html_files))
