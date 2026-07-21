---
name: passit-pdf-maker
description: Internal PassIt delivery helper. Not a marketplace service.
  Converts a finished PassIt deliverable (reviewer, mock exam, exam pack)
  written in Markdown into a clean, branded, printable PDF file using
  scripts/make_pdf.py. Use whenever a PassIt skill delivers PDF-first
  and the platform can create files and run scripts.
---

# PDF Maker — Skill Instructions

This is an internal helper. It is never listed or sold on the marketplace.

## When to use
- A PassIt selling skill has finished writing a deliverable and wants
  to deliver it as a PDF (the default for Quick Reviewer, Full Reviewer,
  Mock Exam, and Exam Pack).

## How to use
1. Save the finished deliverable as a Markdown file, e.g. output.md.
2. Run: python scripts/make_pdf.py output.md output.pdf --title "..."
3. Send output.pdf to the buyer.

## Fallback (never skip)
- If the platform cannot create files or run scripts, skip this helper:
  deliver the same content as a clean document and tell the buyer
  politely that PDF wasn't available this time.
- Never fail an order because PDF creation failed. Content comes first.

## Style (what the script produces)
- Title page: deliverable title, "Made by PassIt", date.
- Clean headings, readable body text, tables kept intact.
- Footer on every page: the PassIt tagline + page number.
- Print-friendly: black text on white, green accents only.
