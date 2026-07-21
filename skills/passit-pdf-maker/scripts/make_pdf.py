#!/usr/bin/env python3
"""PassIt PDF maker — converts a Markdown deliverable into a clean,
branded, printable PDF.

Usage:
    python make_pdf.py input.md output.pdf --title "Quick Reviewer: Photosynthesis"

Requires:
    pip install markdown weasyprint
"""

import argparse
import datetime
import sys

try:
    import markdown
    from weasyprint import HTML
except ImportError:
    sys.exit("Missing dependency. Run: pip install markdown weasyprint")

CSS = """
@page {
    size: A4;
    margin: 2cm;
    @bottom-center {
        content: "PassIt — Type your topic. Get your reviewer. Pass your exam.  ·  Page " counter(page);
        font-size: 8pt;
        color: #666;
    }
}
body { font-family: Helvetica, Arial, sans-serif; font-size: 11pt; color: #111; line-height: 1.5; }
h1 { color: #14532d; border-bottom: 2px solid #22c55e; padding-bottom: 4px; }
h2 { color: #14532d; margin-top: 18px; }
table { border-collapse: collapse; width: 100%; margin: 10px 0; }
th, td { border: 1px solid #bbb; padding: 6px 8px; text-align: left; font-size: 10pt; }
th { background: #f0fdf4; }
.title-page { text-align: center; margin-top: 200px; page-break-after: always; }
.title-page h1 { border: none; font-size: 26pt; }
.title-page p { color: #444; }
"""


def build_html(md_text: str, title: str) -> str:
    body = markdown.markdown(md_text, extensions=["tables", "fenced_code"])
    today = datetime.date.today().strftime("%B %d, %Y")
    return f"""<html><head><meta charset='utf-8'><style>{CSS}</style></head><body>
<div class='title-page'>
  <h1>{title}</h1>
  <p>Made by PassIt</p>
  <p>{today}</p>
</div>
{body}
</body></html>"""


def main() -> None:
    parser = argparse.ArgumentParser(description="PassIt Markdown -> PDF")
    parser.add_argument("input")
    parser.add_argument("output")
    parser.add_argument("--title", default="PassIt Reviewer")
    args = parser.parse_args()

    with open(args.input, encoding="utf-8") as f:
        md_text = f.read()

    HTML(string=build_html(md_text, args.title)).write_pdf(args.output)
    print(f"PDF created: {args.output}")


if __name__ == "__main__":
    main()
