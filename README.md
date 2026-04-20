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

Cold outreach is one of the most misunderstood growth channels in B2B SaaS.

Most teams approach it as a volume problem — sending more emails, automating more sequences, and hoping something works.

In reality, effective outbound is a system problem:
- Who you target
- What you say
- When you reach out
- How you follow up

This project is focused on understanding how top operators actually build outbound pipelines that convert — not just send messages.


---

## Expert Selection Criteria

I chose experts who meet at least two of the following:

1. Have personally sent (or built systems that sent) millions of outbound messages
2. Have built a business — agency, SaaS product, or client roster — on the back of cold outreach
3. Share tactical, data-backed content with real campaign numbers (not just frameworks)
4. Are actively posting in 2024–2025 (not just legacy voices)

This avoids generic “growth advice” and focuses on **what actually works in the field**.

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
## Key Patterns Observed

After reviewing the content, a few consistent patterns emerged:

### 1. ICP clarity > personalization
Most teams over-index on personalization tactics.

Top operators focus first on:
- defining a sharp ICP
- identifying real pain points
- understanding buying triggers

Without that, personalization doesn’t matter.

---

### 2. Messaging beats tools
Tools (automation, sequencing, scraping) are widely available.

The real differentiator is:
- how clearly the problem is articulated
- how relevant the message feels to the recipient

Strong messaging consistently outperforms complex tooling.

---

### 3. Timing is underrated
Outbound works best when:
- the problem already exists
- the company is in a buying window

Reaching the right person at the wrong time fails — even with good messaging.
### 4. Multi-touch systems win
Single-channel outreach is weak.

High-performing systems combine:
- LinkedIn
- Email
- Content
- Warm touchpoints

Consistency across channels increases response rates significantly.

---

### 5. Founder-led outreach is high leverage (early stage)
In early-stage companies:
- founder-led outbound performs better than generic SDR outreach
- credibility + context = higher trust

---

## Early Hypothesis

> Cold outreach is not primarily a messaging problem.  
> It is an ICP selection and timing problem.

Most outreach fails because:
- it targets the wrong people
- at the wrong time
- with generic positioning

Fix those, and messaging becomes much easier.

---

## What this leads to

This research is a foundation to build a **repeatable outbound playbook**, including:

- ICP definition frameworks
- Messaging structures based on pain and triggers
- Multi-channel outreach systems
- Feedback loops between outreach → response → refinement

---

  ## What's Inside

The research phase is complete and has been synthesized into a full Playbook / SOP:

📄 [Cold Outreach Playbook — View Here](./playbook/cold-outreach-sop.md)

The playbook covers:
- ICP definition and tiered account model
- Infrastructure setup (domains, warm-up, inbox rotation, authentication)
- List building and trigger-based targeting
- Copy frameworks and AI personalization workflow
- 21-day multi-channel sequence architecture
- Reply management and nurture systems
- Measurement, A/B testing, and iteration protocol
- Where experts disagree — and which side I take
- What I rejected and why
- One original idea not found in any source
- Honest weaknesses of the playbook
- Who I would not recommend following and why

---

*This project is part of a portfolio process with 100Hires. All research and synthesis is original work.*
