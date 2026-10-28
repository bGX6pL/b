"""Download latin + latin-ext woff2 subsets from Google Fonts CSS (fetched into tmp/fontcss)
and write self-hosted @font-face rules to site/assets/fonts/fonts.css (no requests to Google at runtime)."""
import pathlib, re, urllib.request
root = pathlib.Path(__file__).resolve().parents[1]
src = root / "tmp" / "fontcss"
out = root / "site" / "assets" / "fonts"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"
rules = []
for css in sorted(src.glob("*.css")):
    text = css.read_text(encoding="utf-8")
    for subset, body in re.findall(r"/\* ([\w-]+) \*/\s*@font-face \{(.*?)\}", text, re.S):
        if subset not in ("latin", "latin-ext"):
            continue
        fam = re.search(r"font-family: '([^']+)'", body).group(1)
        weight = re.search(r"font-weight: ([\d ]+);", body).group(1).strip()
        style = re.search(r"font-style: (\w+);", body).group(1)
        url = re.search(r"url\((https://fonts\.gstatic\.com/[^)]+)\) format", body).group(1)
        urange = re.search(r"unicode-range: ([^;]+);", body).group(1)
        italic = "-italic" if style == "italic" else ""
        fname = f"{fam.lower().replace(' ', '-')}{italic}-{weight.replace(' ', '_')}-{subset}.woff2"
        dest = out / fname
        if not dest.exists():
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            dest.write_bytes(urllib.request.urlopen(req).read())
        rules.append(f"/* {fam} {weight} {subset} */\n@font-face {{ font-family: '{fam}'; font-style: {style}; font-weight: {weight}; font-display: swap; src: url('./{fname}') format('woff2'); unicode-range: {urange}; }}")
(out / "fonts.css").write_text("\n".join(rules) + "\n", encoding="utf-8")
print(len(rules), "faces")
for f in sorted(out.glob("*.woff2")):
    print(f"{f.stat().st_size/1024:6.1f} KB  {f.name}")
