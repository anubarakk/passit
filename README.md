# PassIt ✅

> **Type your topic. Get your reviewer. Pass your exam.**

PassIt is an AI agent on the **OKX.AI Agent Marketplace** (category: **Lifestyle**) that turns any topic into a clear, organized **reviewer** — ready-to-study material in minutes.

## How it works (3 steps)

1. **Type your topic.** Example: "Photosynthesis" or "U.S Nursing Board — Pharmacology basics".
2. **(Optional)** Attach your own notes, PDF, book pages, or photos of handwritten notes — if you want the reviewer to match your class material exactly.
3. **Get your reviewer in minutes** — organized, simple to follow, and ready to study.

That's it. No files needed. Just a topic.

## Services & Prices

| # | Service | Job | Price |
|---|---------|-----|-------|
| 1 | **Quick Reviewer** | 📖 Learn | 0.1 USDT |
| 2 | **Full Reviewer** | 📖 Learn | 0.5 USDT |
| 3 | **Mock Exam** | 📝 Prove | 0.3 USDT |
| 4 | **Explain This** | 🆘 Fix | 0.1 USDT |
| 5 | **Exam Pack** | 🏆 All | 1.0 USDT |

See [docs/02-services-and-pricing.md](docs/02-services-and-pricing.md) for full marketplace listings.

## Documentation

| Doc | Contents |
|-----|----------|
| [01-overview.md](docs/01-overview.md) | What PassIt is, the problem, the solution, target buyers, why we win |
| [02-services-and-pricing.md](docs/02-services-and-pricing.md) | The 5 services, prices, and professional A2A marketplace listings |
| [03-reviewer-structure.md](docs/03-reviewer-structure.md) | The standard reviewer structure + a full sample |
| [04-rules.md](docs/04-rules.md) | Product rules and listing disclaimer |
| [05-price-ladder.md](docs/05-price-ladder.md) | How buyers move up the price ladder |
| [06-launch-checklist.md](docs/06-launch-checklist.md) | Launch checklist & marketing plan |
| [07-roadmap.md](docs/07-roadmap.md) | Future ideas (v2) |

## Agent Skills

The agent is built from **5 selling skills + 1 internal helper**, written as platform-independent instructions in the OpenClaw `SKILL.md` format:

```
skills/
  passit-quick-reviewer/SKILL.md
  passit-full-reviewer/SKILL.md
  passit-mock-exam/SKILL.md
  passit-explain-this/SKILL.md
  passit-exam-pack/SKILL.md
  passit-pdf-maker/
    SKILL.md
    scripts/make_pdf.py
```

Setup instructions live in [skills/README.md](skills/README.md).

## Rules & Disclaimer

PassIt is a **study aid**. It is not for use during exams and does not guarantee results. See [docs/04-rules.md](docs/04-rules.md).
