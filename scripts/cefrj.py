"""Derives cefrj-1.6.tsv from the CEFR-J Wordlist's zip: each word's Headword, part of speech and
CEFR level, from the workbook's ALL sheet, and nothing else.

Usage: python3 -I scripts/cefrj.py CEFRJ_wordlist_ver1.6.zip > cefrj-1.6.tsv

Only the standard library, so the workflow installs nothing: an .xlsx is a zip of XML.
"""

import io
import sys
import xml.etree.ElementTree as ET
import zipfile

NS = {
    "m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
}
REL = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id"

# The ALL sheet's columns, as its header row names them, and the TSV's for each.
COLUMNS = {"headword": "headword", "pos": "pos", "CEFR": "level"}
LEVELS = {"A1", "A2", "B1", "B2"}


def column(ref):
    letters = "".join(c for c in ref if c.isalpha())
    n = 0
    for c in letters:
        n = n * 26 + ord(c) - ord("A") + 1
    return n - 1


def rows(book, sheet):
    workbook = ET.fromstring(book.read("xl/workbook.xml"))
    rels = ET.fromstring(book.read("xl/_rels/workbook.xml.rels"))
    target = {r.get("Id"): r.get("Target") for r in rels}
    rid = next(s.get(REL) for s in workbook.find("m:sheets", NS) if s.get("name") == sheet)
    shared = [
        "".join(t.text or "" for t in si.iter(f"{{{NS['m']}}}t"))
        for si in ET.fromstring(book.read("xl/sharedStrings.xml")).findall("m:si", NS)
    ]
    data = ET.fromstring(book.read("xl/" + target[rid].lstrip("/").removeprefix("xl/")))
    for row in data.find("m:sheetData", NS):
        cells = {}
        for c in row.findall("m:c", NS):
            v = c.find("m:v", NS)
            if c.get("t") == "s" and v is not None:
                cells[column(c.get("r"))] = shared[int(v.text)]
            elif c.get("t") == "inlineStr":
                cells[column(c.get("r"))] = "".join(t.text or "" for t in c.iter(f"{{{NS['m']}}}t"))
            elif v is not None:
                cells[column(c.get("r"))] = v.text
        yield [cells.get(i, "").strip() for i in range(max(cells, default=-1) + 1)]


def main():
    with zipfile.ZipFile(sys.argv[1]) as outer:
        (name,) = [n for n in outer.namelist() if n.endswith(".xlsx")]
        book = zipfile.ZipFile(io.BytesIO(outer.read(name)))
    lines = rows(book, "ALL")
    header = next(lines)
    try:
        at = [header.index(c) for c in COLUMNS]
    except ValueError:
        sys.exit(f"The ALL sheet's header {header} lacks one of {list(COLUMNS)}")
    out = ["\t".join(COLUMNS.values())]
    for row in lines:
        fields = [row[i] if i < len(row) else "" for i in at]
        if not any(fields):
            continue
        if not fields[0] or not fields[1] or fields[2] not in LEVELS or any("\t" in f for f in fields):
            sys.exit(f"Not a word of the ALL sheet: {row}")
        out.append("\t".join(fields))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
