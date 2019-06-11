# Peter Kowalsky - 10.06.19

from markdown2 import markdown as convert

extras=["tables", "fenced-code-blocks"]

def md2html(md):
  html = convert(md, extras=extras)
  return html

def md_file2html(file):
  html = convert(file.read(), extras=extras)
  return html

