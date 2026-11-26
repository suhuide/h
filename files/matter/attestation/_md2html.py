# -*- coding: utf-8 -*-
"""Convert matter-security.md to a standalone matter-security.html (offline-friendly)."""
import html, re, io, sys

SRC = r"D:\hrf\h\files\matter\attestation\attestation.md"
DST = r"D:\hrf\h\files\matter\attestation\attestation.html"

def slug(t):
    t = t.strip().lower()
    t = re.sub(r"[^\w\u4e00-\u9fff\- ]", "", t)  # drop punctuation, keep CJK/word/hyphen/space
    t = t.replace(" ", "-")
    return t

def inline(s):
    s = html.escape(s, quote=False)
    codes = []
    def stash(m):
        codes.append("<code>%s</code>" % m.group(1))
        return "\x00%d\x00" % (len(codes) - 1)
    s = re.sub(r"`([^`]+)`", stash, s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"\[([^\]]+)\]\(#([^)]+)\)",
               r'<a href="#\2">\1</a>', s)
    s = re.sub(r"\x00(\d+)\x00", lambda m: codes[int(m.group(1))], s)
    return s

def join_para(lines):
    out = ""
    for ln in lines:
        ln = ln.strip()
        if not out:
            out = ln
        elif re.match(r".*[\u4e00-\u9fff，。；：）】]$", out) and re.match(r"^[\u4e00-\u9fff（【]", ln):
            out += ln          # CJK 换行不加空格
        else:
            out += " " + ln
    return out

def split_row(line):
    line = line.strip()
    if line.startswith("|"): line = line[1:]
    if line.endswith("|"): line = line[:-1]
    return [c.strip() for c in line.split("|")]

def render_table(block):
    def cell(c):
        # 含 HTML 的单元格(彩色代码块)原样放行, 其余走 inline 转义
        if re.search(r"<(?:pre|code|br)\b", c):
            return c.strip()
        return inline(c)
    rows = [b for b in block if b.strip()]
    if len(rows) < 2 or not re.match(r"^\s*\|?\s*:?-+:?\s*(\|\s*:?-+:?\s*)+\|?\s*$", rows[1]):
        return None
    head = split_row(rows[0])
    out = ["<table>", "<thead><tr>", "".join("<th>%s</th>" % cell(c) for c in head), "</tr></thead>", "<tbody>"]
    for r in rows[2:]:
        cells = split_row(r)
        cells += [""] * (len(head) - len(cells))
        out.append("<tr>" + "".join("<td>%s</td>" % cell(c) for c in cells[:len(head)]) + "</tr>")
    out += ["</tbody>", "</table>"]
    return "\n".join(out)

def render_list(block, ordered):
    tag = "ol" if ordered else "ul"
    items, cur = [], None
    pat = re.compile(r"^\s*(\d+\.|-)\s+(.*)$")
    for ln in block:
        m = pat.match(ln)
        if m:
            if cur is not None: items.append(cur)
            cur = [m.group(2)]
        elif cur is not None and ln.startswith(("   ", "    ", "\t")):
            cur.append(ln.strip())
        elif cur is not None:
            cur.append(ln.strip())
    if cur is not None: items.append(cur)
    out = ["<%s>" % tag]
    for it in items:
        out.append("<li>%s</li>" % inline(join_para(it)))
    out.append("</%s>" % tag)
    return "\n".join(out)

def render_quote(block):
    inner = []
    for ln in block:
        inner.append(re.sub(r"^>\s?", "", ln))
    # 引用块内可能是多行段落
    return "<blockquote><p>%s</p></blockquote>" % "<br/>\n".join(inline(l.strip()) for l in inner if l.strip())

# ---- 分块：按空行切，但围栏代码块整体保护 ----
lines = io.open(SRC, encoding="utf-8").read().split("\n")
blocks, buf, in_fence, fence_lang = [], [], False, ""
for ln in lines:
    m = re.match(r"^```(\w*)\s*$", ln)
    if m and not in_fence:
        if buf: blocks.append(("text", buf)); buf = []
        in_fence, fence_lang = True, m.group(1)
        buf = []
        continue
    if in_fence:
        if re.match(r"^```\s*$", ln):
            blocks.append(("fence", (fence_lang, buf)))
            in_fence = False
            buf = []          # 关键: 断开与已存块的共享引用
        else:
            buf.append(ln)
        continue
    if ln.strip() == "":
        if buf: blocks.append(("text", buf)); buf = []
        continue
    if ln.startswith("#") and buf:      # 标题行独立成块, 不吞并后面的表格/段落
        blocks.append(("text", buf)); buf = []
    buf.append(ln)
    if ln.startswith("#"):
        blocks.append(("text", buf)); buf = []
if buf: blocks.append(("text", buf))

out, in_quote = [], False
def close_quote():
    global in_quote
    if in_quote:
        out.append("</blockquote>")
        in_quote = False

for kind, blk in blocks:
    if kind == "fence":
        lang, code = blk
        body = html.escape("\n".join(code), quote=False)
        if lang == "mermaid":
            out.append('<pre class="mermaid-src"><code>%s</code></pre>' % body)
        else:
            cls = " class=\"language-%s\"" % lang if lang else ""
            out.append("<pre><code%s>%s</code></pre>" % (cls, body))
        continue
    text = blk
    first = text[0]
    if first.startswith("####"):
        close_quote()
        out.append("<h4 id=\"%s\">%s</h4>" % (slug(first.lstrip("#")), inline(first.lstrip("# ").strip())))
    elif first.startswith("###"):
        close_quote()
        out.append("<h3 id=\"%s\">%s</h3>" % (slug(first.lstrip("#")), inline(first.lstrip("# ").strip())))
    elif first.startswith("##"):
        close_quote()
        out.append("<h2 id=\"%s\">%s</h2>" % (slug(first.lstrip("#")), inline(first.lstrip("# ").strip())))
    elif first.startswith("#"):
        close_quote()
        out.append("<h1>%s</h1>" % inline(first.lstrip("# ").strip()))
    elif re.match(r"^\s*---+\s*$", first):
        close_quote()
        out.append("<hr/>")
    elif first.lstrip().startswith("|"):
        close_quote()
        t = render_table(text)
        out.append(t if t else "<p>%s</p>" % "<br/>\n".join(inline(l) for l in text))
    elif first.lstrip().startswith(">"):
        if not in_quote:
            out.append("<blockquote>"); in_quote = True
        q = [re.sub(r"^>\s?", "", l) for l in text]
        out.append("<p>%s</p>" % inline(join_para(q)))
    elif re.match(r"^\s*\d+\.\s", first):
        close_quote()
        out.append(render_list(text, True))
    elif re.match(r"^\s*-\s", first):
        close_quote()
        out.append(render_list(text, False))
    else:
        close_quote()
        out.append("<p>%s</p>" % inline(join_para(text)))
close_quote()

CSS = """
body{font-family:-apple-system,"Segoe UI","Microsoft YaHei","PingFang SC",sans-serif;
     max-width:960px;margin:0 auto;padding:24px 20px 80px;line-height:1.75;color:#1f2328;background:#fff}
h1{font-size:1.9em;border-bottom:2px solid #0969da;padding-bottom:.4em}
h2{font-size:1.45em;border-bottom:1px solid #d0d7de;padding-bottom:.35em;margin-top:2em}
h3{font-size:1.18em;margin-top:1.6em}
pre{background:#f6f8fa;border:1px solid #d0d7de;border-radius:6px;padding:12px 14px;overflow:auto;
    font-family:Consolas,"Courier New",monospace;font-size:.88em;line-height:1.5}
code{font-family:Consolas,"Courier New",monospace;background:#f0f2f4;border-radius:4px;padding:.1em .35em;font-size:.92em}
pre code{background:none;padding:0;font-size:1em}
table{border-collapse:collapse;margin:1em 0;width:100%;font-size:.93em}
th,td{border:1px solid #d0d7de;padding:6px 10px;text-align:left;vertical-align:top}
th{background:#f6f8fa}
blockquote{margin:1em 0;padding:.6em 1em;border-left:4px solid #0969da;background:#f6f9ff;color:#3b434b}
blockquote p{margin:.3em 0}
hr{border:none;border-top:1px solid #d0d7de;margin:2.2em 0}
a{color:#0969da;text-decoration:none}
a:hover{text-decoration:underline}
ol,ul{padding-left:1.6em}
li{margin:.35em 0}
.mermaid-src{background:#fbfbdf;border-color:#e3dcb0}
"""

HEAD = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>Matter PAA/PAI/DAC 验签过程详解</title>
<style>%s</style>
<script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
</head>
<body>
""" % CSS

TAIL = """
<script>
(function () {
  var pres = document.querySelectorAll("pre.mermaid-src > code");
  if (!window.mermaid || pres.length === 0) return;   // 离线时保留代码展示
  mermaid.initialize({ startOnLoad: false, fontSize: 14 });
  pres.forEach(function (el) {
    var d = document.createElement("div");
    d.className = "mermaid";
    d.textContent = el.textContent;
    el.parentElement.replaceWith(d);
  });
  if (mermaid.run) mermaid.run({ querySelector: ".mermaid" });
  else if (mermaid.init) mermaid.init(undefined, ".mermaid");
})();
</script>
</body>
</html>
"""

io.open(DST, "w", encoding="utf-8").write(HEAD + "\n".join(out) + TAIL)
print("written", DST, len(out), "blocks")
