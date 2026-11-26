# -*- coding: utf-8 -*-
"""Convert serial.md -> s.docx (headings, pipe tables, HTML frame tables, code blocks, blockquotes)."""
import re
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.section import WD_ORIENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

SRC = r'C:\Users\huide\Desktop\s\serial.md'
DST = r'C:\Users\huide\Desktop\s\s.docx'
CJK = '微软雅黑'
MONO = 'Consolas'
TOTAL_W = Cm(26.1)   # A4 landscape, 1.8cm margins


def set_ea(run, ea=CJK):
    rPr = run._element.get_or_add_rPr()
    rFonts = rPr.find(qn('w:rFonts'))
    if rFonts is None:
        rFonts = OxmlElement('w:rFonts')
        rPr.append(rFonts)
    rFonts.set(qn('w:eastAsia'), ea)


def add_runs(p, text, size=None, color=None, bold=False):
    text = re.sub(r'</?font[^>]*>', '', text)
    text = text.replace('&nbsp;', ' ')
    parts = re.split(r'(\*\*[^*]+\*\*|`[^`]+`)', text)
    for tok in parts:
        if not tok:
            continue
        if tok.startswith('**') and tok.endswith('**') and len(tok) > 4:
            r = p.add_run(tok[2:-2]); r.bold = True
        elif tok.startswith('`') and tok.endswith('`') and len(tok) > 2:
            r = p.add_run(tok[1:-1])
            r.font.name = MONO; set_ea(r, CJK)
        else:
            r = p.add_run(tok)
            if bold: r.bold = True
        if size: r.font.size = size
        if color: r.font.color.rgb = color


def shade_par(p, fill):
    pPr = p._p.get_or_add_pPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear'); shd.set(qn('w:color'), 'auto'); shd.set(qn('w:fill'), fill)
    pPr.append(shd)


def shade_cell(cell, fill):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear'); shd.set(qn('w:color'), 'auto'); shd.set(qn('w:fill'), fill)
    tcPr.append(shd)


def wlen(s):
    s = re.sub(r'\*\*|`', '', s)
    return sum(2 if ord(ch) > 0x2E80 else 1 for ch in s)


def strip_quote(line):
    s = line.lstrip()
    if s.startswith('>'):
        return s[1:].lstrip()
    return line


def add_paragraph(doc, text, size=None, color=None, indent_cm=None, style=None):
    p = doc.add_paragraph(style=style) if style else doc.add_paragraph()
    add_runs(p, text, size=size, color=color)
    if indent_cm is not None:
        p.paragraph_format.left_indent = Cm(indent_cm)
    p.paragraph_format.space_after = Pt(3)
    return p


def add_code_block(doc, lines):
    p = doc.add_paragraph()
    shade_par(p, 'F2F2F2')
    pf = p.paragraph_format
    pf.left_indent = Cm(0.3); pf.space_before = Pt(3); pf.space_after = Pt(6)
    for i, line in enumerate(lines):
        r = p.add_run(line)
        r.font.name = MONO; set_ea(r, CJK); r.font.size = Pt(8.5)
        if i < len(lines) - 1:
            r.add_break()


def add_md_table(doc, header, rows):
    ncol = len(header)
    t = doc.add_table(rows=len(rows) + 1, cols=ncol)
    t.style = 'Table Grid'
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = False
    data = [header] + rows
    w = [max(4, min(50, max(wlen(r[c]) if c < len(r) else 0 for r in data))) for c in range(ncol)]
    tot = sum(w)
    widths = [int(TOTAL_W * x / tot) for x in w]
    for ri, row in enumerate(data):
        for ci in range(ncol):
            cell = t.cell(ri, ci)
            cell.width = widths[ci]
            txt = row[ci] if ci < len(row) else ''
            p = cell.paragraphs[0]
            p.paragraph_format.space_after = Pt(0)
            add_runs(p, txt, size=Pt(8), bold=(ri == 0))
            if ri == 0:
                shade_cell(cell, 'D9D9D9')
    doc.add_paragraph().paragraph_format.space_after = Pt(2)


def add_html_table(doc, block):
    rows = re.findall(r'<tr[^>]*>(.*?)</tr>', block, re.S)
    grid, covered = {}, set()
    ncols = 0
    for r, row in enumerate(rows):
        c = 0
        for m in re.finditer(r'<(t[hd])([^>]*)>(.*?)</\1>', row, re.S):
            attrs, content = m.group(2), m.group(3)
            cs = int(re.search(r'colspan="(\d+)"', attrs).group(1)) if 'colspan' in attrs else 1
            rs = int(re.search(r'rowspan="(\d+)"', attrs).group(1)) if 'rowspan' in attrs else 1
            while (r, c) in covered or (r, c) in grid:
                c += 1
            text = re.sub(r'<[^>]+>', '', content)
            text = re.sub(r'\s+', ' ', text).strip()
            grid[(r, c)] = (text, rs, cs)
            for dr in range(rs):
                for dc in range(cs):
                    if dr or dc:
                        covered.add((r + dr, c + dc))
            c += cs
            ncols = max(ncols, c)
    nrows = len(rows)
    t = doc.add_table(rows=nrows, cols=ncols)
    t.style = 'Table Grid'
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = False
    widths = [int(TOTAL_W / ncols)] * ncols
    for (r, c), (text, rs, cs) in sorted(grid.items()):
        cell = t.cell(r, c)
        cell.width = widths[c]
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_after = Pt(0)
        add_runs(p, text, size=Pt(9), bold=(r == 0))
        if r == 0:
            shade_cell(cell, 'D9D9D9')
        if rs > 1 or cs > 1:
            cell.merge(t.cell(r + rs - 1, c + cs - 1))
    doc.add_paragraph().paragraph_format.space_after = Pt(2)


def main():
    lines = open(SRC, encoding='utf-8').read().split('\n')
    doc = Document()

    sec = doc.sections[0]
    sec.orientation = WD_ORIENT.LANDSCAPE
    sec.page_width = Cm(29.7); sec.page_height = Cm(21.0)
    sec.left_margin = Cm(1.8); sec.right_margin = Cm(1.8)
    sec.top_margin = Cm(1.6); sec.bottom_margin = Cm(1.6)

    st = doc.styles['Normal']
    st.font.name = 'Calibri'; st.font.size = Pt(10.5)
    st.element.rPr.rFonts.set(qn('w:eastAsia'), CJK)
    for name, size in (('Heading 1', 15), ('Heading 2', 12.5), ('Heading 3', 11)):
        hs = doc.styles[name]
        hs.font.size = Pt(size); hs.font.bold = True
        hs.font.color.rgb = RGBColor(0, 0, 0)
        hs.font.name = 'Calibri'
        hs.element.rPr.rFonts.set(qn('w:eastAsia'), CJK)

    i, n = 0, len(lines)
    while i < n:
        line = lines[i].rstrip()
        stripped = line.strip()

        if stripped.startswith('```'):
            i += 1
            buf = []
            while i < n and not lines[i].strip().startswith('```'):
                buf.append(lines[i]); i += 1
            i += 1
            add_code_block(doc, buf)
            continue

        if stripped.startswith('<div') or stripped.startswith('<table'):
            buf = []
            while i < n and '</div>' not in lines[i] and '</table>' not in lines[i]:
                buf.append(lines[i]); i += 1
            if i < n:
                buf.append(lines[i]); i += 1
            block = '\n'.join(buf)
            if '<table' in block:
                add_html_table(doc, block)
            continue

        if re.match(r'^-{3,}\s*$', stripped):
            i += 1
            continue

        first = strip_quote(line).strip()
        if first.startswith('|'):
            nxt = strip_quote(lines[i + 1]).strip() if i + 1 < n else ''
            if re.match(r'^\|?\s*:?-{2,}', nxt):
                header = [c.strip() for c in first.strip('|').split('|')]
                i += 2
                rows = []
                while i < n:
                    rowline = strip_quote(lines[i]).strip()
                    if not rowline.startswith('|'):
                        break
                    rows.append([c.strip() for c in rowline.strip('|').split('|')])
                    i += 1
                add_md_table(doc, header, rows)
                continue

        m = re.match(r'^(#{1,3})\s+(.*)$', stripped)
        if m:
            hashes = len(m.group(1))
            text = m.group(2).strip()
            if hashes == 1:
                p = doc.add_paragraph()
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                add_runs(p, text, size=Pt(20), bold=True)
                p.paragraph_format.space_before = Pt(6)
                p.paragraph_format.space_after = Pt(12)
            else:
                num = re.match(r'^(\d+(?:\.\d+)*)', text)
                level = min(max((1 + num.group(1).count('.')) if num else (hashes - 1), 1), 3)
                p = doc.add_paragraph(style='Heading %d' % level)
                add_runs(p, text)
            i += 1
            continue

        if line.lstrip().startswith('>'):
            add_paragraph(doc, strip_quote(line).strip(), size=Pt(9.5),
                          color=RGBColor(0x59, 0x59, 0x59), indent_cm=0.5)
            i += 1
            continue

        m = re.match(r'^(\s*)([-*])\s+(.*)$', line)
        if m:
            level = len(m.group(1)) // 4
            style = 'List Bullet' if level == 0 else 'List Bullet %d' % min(level + 1, 3)
            try:
                p = doc.add_paragraph(style=style)
                add_runs(p, m.group(3), size=Pt(10.5))
            except KeyError:
                add_paragraph(doc, '• ' + m.group(3), indent_cm=0.5 + level * 0.5)
            i += 1
            continue

        m = re.match(r'^(\s*)(\d+)\.\s+(.*)$', line)
        if m:
            level = len(m.group(1)) // 4
            add_paragraph(doc, '%s. %s' % (m.group(2), m.group(3)), indent_cm=0.5 + level * 0.5)
            i += 1
            continue

        if not stripped:
            i += 1
            continue

        add_paragraph(doc, stripped, size=Pt(10.5))
        i += 1

    doc.core_properties.title = 'Matter 通用串口协议'
    for z in doc.settings.element.findall(qn('w:zoom')):
        z.set(qn('w:percent'), '100')
        if qn('w:val') in z.attrib:
            del z.attrib[qn('w:val')]
    doc.save(DST)
    print('saved:', DST)


if __name__ == '__main__':
    main()
