#!/usr/bin/env python3
"""Rewrite all keltcon.info URLs in site/ HTML to local /KELTCON/ absolute paths.

Why absolute /KELTCON/ instead of <base>+relative:
- pages live at different depths (/, /expo/, /inicio/barcelona/). A single
  absolute prefix resolves identically from every page; relative paths would
  need per-page ../ counting. Immune to page depth, no <base> side effects.

Rules:
  https://keltcon.info/<path>   -> /KELTCON/<path>
  //keltcon.info/<path>         -> /KELTCON/<path>
  strip ?ver=... and trailing ?<digits> on asset URLs
  leave: chrome-extension://, mailto:, tel:, data:, #fragments, other domains
  external API endpoints (wp-json POST, xmlrpc, admin-ajax, oembed, feed) are
  rewritten too but those are dead in static; forms get replaced separately.
"""
import os, re, glob

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.join(ROOT, "site")
PREFIX = "/KELTCON"

html_files = glob.glob(os.path.join(SITE, "**", "index.html"), recursive=True)

# both protocol forms, both quote/paren contexts
re_https = re.compile(r'https://keltcon\.info')
re_proto = re.compile(r'(?<![a-zA-Z0-9])//keltcon\.info')

total = 0
for f in html_files:
    txt = open(f, encoding="utf-8").read()
    orig = txt
    txt = re_https.sub(PREFIX, txt)
    txt = re_proto.sub(PREFIX, txt)
    # strip ?ver=... that now sits on /KELTCON/... asset refs (in href/src/url())
    txt = re.sub(r'(/KELTCON/[^"\'\s)]+?)\?ver=[0-9A-Za-z.\-]+', r'\1', txt)
    if txt != orig:
        total += 1
    open(f, "w", encoding="utf-8").write(txt)

print(f"rewrote {total}/{len(html_files)} html files")

# report leftover absolute keltcon refs (should be 0)
left = 0
for f in html_files:
    txt = open(f, encoding="utf-8").read()
    left += len(re.findall(r'keltcon\.info', txt))
print(f"leftover 'keltcon.info' occurrences across all files: {left}")
