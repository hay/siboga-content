"""Zet record-embeds in een hoofdstuk om naar afbeeldingen met onderschrift.

De site toont ![[Record]] als link, niet als afbeelding. Dit script vervangt elke
regel die alleen uit ![[Record]] bestaat door een Markdown-afbeelding (uit de uri
van het record) met daaronder een onderschrift uit description_nl, gelinkt naar
het record. Opnieuw draaien werkt het onderschrift bij als description_nl wijzigt.

Gebruik: python etc/record-embeds-naar-afbeeldingen.py "chapters/Bemanning.md"
"""
import re
import sys
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EMBED = re.compile(r"^!\[\[([^\]|]+)\]\]$")
# Eerder gegenereerd blok: afbeelding + onderschrift met link naar het record.
BLOCK = re.compile(r"^!\[[^\]]*\]\(https://commons\.wikimedia\.org/wiki/Special:FilePath/[^)]*\)$")
CAPTION = re.compile(r"^\*\[\[([^\]|]+)\|.*\]\]\*$")


def frontmatter(path):
    text = path.read_text(encoding="utf-8")
    fm = text.split("---", 2)[1]
    out = {}
    for line in fm.splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            v = v.strip()
            if len(v) >= 2 and v[0] == v[-1] == '"':
                v = v[1:-1].replace('\\"', '"')
            out[k.strip()] = v
    return out


def block(name):
    fm = frontmatter(ROOT / "records" / f"{name}.md")
    uri, desc = fm["uri"], fm["description_nl"]
    if "/wiki/File:" not in uri:
        raise SystemExit(f"{name}: uri is geen Commons-bestand: {uri}")
    filename = urllib.parse.unquote(uri.split("/wiki/File:", 1)[1])
    src = "https://commons.wikimedia.org/wiki/Special:FilePath/" + urllib.parse.quote(filename, safe=",'_-.") + "?width=1200"
    alt = desc.replace("[", "(").replace("]", ")")
    return [f"![{alt}]({src})", f"*[[{name}|{alt}]]*"]


def main(chapter):
    path = ROOT / chapter
    text = path.read_text(encoding="utf-8")
    nl = "\r\n" if "\r\n" in text else "\n"
    lines = text.split(nl)
    out, i, n = [], 0, 0
    while i < len(lines):
        line = lines[i]
        m = EMBED.match(line)
        if m:
            out += block(m.group(1)); n += 1
        elif BLOCK.match(line) and i + 1 < len(lines) and CAPTION.match(lines[i + 1]):
            out += block(CAPTION.match(lines[i + 1]).group(1)); n += 1; i += 1
        else:
            out.append(line)
        i += 1
    path.write_text(nl.join(out), encoding="utf-8", newline="")
    print(f"{chapter}: {n} afbeeldingen")


if __name__ == "__main__":
    main(sys.argv[1])
