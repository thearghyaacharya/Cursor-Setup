# Cold Outreach Pipeline for B2B SaaS — Research Project

**Author:** Arghya Acharya  
**Project Type:** Portfolio Research Project  
**Status:** In Progress  
**Last Updated:** April 2026

---

## What This Is

This repository is a structured research project on building a cold outreach pipeline for B2B SaaS companies. The goal: collect, organize, and synthesize high-signal content from 10 practitioners who have actually built, run, or scaled outbound systems — not just written about them.

The research is organized to support a future playbook. Everything in this repo is raw material toward that output.

---

## Why Cold Outreach Pipeline for B2B SaaS

Cold outreach is the backbone of most B2B SaaS growth at early and mid-stage. It's one of the few channels that is fully controllable, measurable, and doesn't depend on algorithm changes, ad budgets, or existing brand equity. For a company like 100Hires — whose product exists to help B2B teams hire and whose revenue engine runs on outbound — understanding what makes cold outreach work isn't peripheral. It's the core.

Beyond the relevance to this project, I chose this topic because I have first-hand exposure to outbound. At Shorter Loop (B2B SaaS), I ran cold outreach sequences and achieved reply rates significantly above industry benchmarks. I can evaluate these experts with a practitioner's eye, not just a student's.

---

## Expert Selection Criteria

I chose experts who meet at least two of the following:

1. Have personally sent (or built systems that sent) millions of outbound messages
2. Have built a business — agency, SaaS product, or client roster — on the back of cold outreach
3. Share tactical, data-backed content with real campaign numbers (not just frameworks)
4. Are actively posting in 2024–2025 (not just legacy voices)

I deliberately excluded experts who are primarily educators or consultants without operational proof points. The question I kept asking: *does this person have skin in the game?*

---

## The 10 Experts

| # | Expert | Role | Primary Platform |
|---|--------|------|-----------------|
| 1 | Jack Reamer | CEO, SalesBread | LinkedIn + YouTube + Podcast |
| 2 | Will Allred | Co-founder, Lavender.ai | LinkedIn |
| 3 | Nick Abraham | Founder, Leadbird + Scrubby | LinkedIn + X |
| 4 | Jeremy Chatelaine | Founder, QuickMail | LinkedIn + YouTube |
| 5 | Jay Feldman | Founder, Enzo Agency | YouTube + LinkedIn |
| 6 | Patrick Spychalski | Founder, The Kiln | LinkedIn |
| 7 | Alex Hormozi | Managing Partner, Acquisition.com | YouTube + LinkedIn |
| 8 | Alex Berman | Founder, X27 Marketing | YouTube + LinkedIn |
| 9 | Vin Matano | Ex-Demandbase SDR, Outbound Coach | LinkedIn + YouTube |
| 10 | Morgan J Ingram | Founder, AMP; 4x LinkedIn Top Sales Voice | LinkedIn + YouTube |

Full annotations, links, and content collection status for each expert are in [`/research/sources.md`](./research/sources.md).

---

## Repository Structure

```
cold-outreach-b2b-saas/
├── README.md                          ← You are here
├── research/
│   ├── sources.md                     ← All 10 experts with annotations and links
│   ├── linkedin-posts/                ← Posts organized by author
│   │   ├── will-allred/
│   │   ├── nick-abraham/
│   │   ├── patrick-spychalski/
│   │   ├── vin-matano/
│   │   └── morgan-j-ingram/
│   ├── youtube-transcripts/           ← Transcripts organized by creator
│   │   ├── jack-reamer/
│   │   ├── alex-hormozi/
│   │   ├── jay-feldman/
│   │   └── jeremy-chatelaine/
│   └── other/                         ← Podcast notes, benchmark reports, misc
│       └── podcast-notes.md
```

---

## Tools Used

### YouTube Transcript Collection
- **yt-dlp** — open source tool for downloading YouTube video metadata and subtitles
- **Supadata API** — for structured transcript extraction where yt-dlp subtitles are unavailable
- Scripts stored in `/scripts/` folder

### LinkedIn Post Collection
- Manual collection (LinkedIn scraping is legally grey; manual is cleaner for a portfolio project and produces better-annotated data)
- Posts saved as `.md` files, organized by author, with date and URL metadata

### Repository and Code
- **Cursor IDE** — primary development environment
- **Claude Code** (Cursor extension) — used for script writing, folder structuring, and content organization
- **Git + GitHub** — version control and public hosting

---

## Commit Log Philosophy

Commits are made incrementally as content is collected — not in one giant push at the end. Each commit represents a meaningful unit of work: a folder populated, a transcript processed, a set of posts annotated.

---

## What Comes Next

Once the research phase is complete, the collected material will be synthesized into a cold outreach playbook covering:

- ICP definition and list building
- Sending infrastructure setup (domains, warm-up, deliverability)
- Copy frameworks and personalization systems
- Sequence design and follow-up logic
- Tool stack recommendations
- Measurement: what to track and what benchmarks to aim for

---

## Setup Completed (Step 1)

*For reference: this project builds on the environment setup from Step 1.*

- Cursor IDE installed
- Claude Code extension installed and authenticated
- Codex extension installed and authenticated
- GitHub repository created and connected
- README.md committed and pushed

---

*This project is part of a portfolio process with 100Hires. All research and synthesis is original work.*
