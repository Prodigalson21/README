# Cursor Setup and Extensions

## 1. Tools Installed
- Cursor IDE
- Claude Code Extension
- Codex Extension

## 2. Steps Completed
1. Installed Cursor IDE from https://cursor.com/
2. Opened Cursor and navigated to Extensions
3. Searched for and installed "Claude Code"
4. Logged into Claude Code
5. Searched for and installed "Codex"
6. Logged into Codex
7. Created a GitHub account
8. Created a new public repository
9. Opened the repository in Cursor
10. Created this README.md file

## 3. Issues Encountered and Solutions

### Issue 1: Extension not installing
- Solution: Restarted Cursor IDE and retried installation

### Issue 2: Login issues with extensions
- Solution: Ensured stable internet connection and re-authenticated

### Issue 3: GitHub push failed
- Solution: Configured Git with username and email using:
  git config --global user.name "Your Name"
  git config --global user.email "your@email.com"

## 4. Conclusion
The setup was successfully completed, and all tools are working correctly.
## Research: AI-Powered SEO Content Production

This repository contains a research corpus on **AI-powered SEO content production** – a practitioner-focused investigation into how AI is changing SEO content workflows, LLM citations, and brand strategy.

### What Was Collected

| Folder | Contents |
|--------|----------|
| `research/sources.md` | 10 expert profiles with links, collection dates, and annotations |
| `research/linkedin-posts/` | LinkedIn posts from each expert (manually collected) |
| `research/youtube-transcripts/` | Video transcripts fetched via `fetch_transcripts.py` |
| `research/other/` | Cross-expert pattern analysis and emerging signals |

### Why These 10 Experts

Experts were selected against four criteria:

1. **Practitioner status** – actively runs SEO/content campaigns, not just commentary
2. **AI-specific output** – publishes experiments, frameworks, or tools for AI content
3. **Verifiable track record** – named clients, measurable results, or open-source tools
4. **Active in 2024–2026** – current relevance, not historical

| Expert | Why Chosen |
|--------|-------------|
| Kevin Indig | Former VP SEO at Shopify, G2, Atlassian. Analyzed 7,000+ LLM citations. |
| Lily Ray | Google update authority. Created AEO framework tracking AI brand mentions. |
| Aleyda Solís | International SEO + LLM workflow automation. Practical prompt templates. |
| Chima Mmeje | Moz content strategist. Keyword clustering methodology for AI content. |
| Kyle Roof | Controlled ranking experiments with isolated test sites – empirical data. |
| Bernard Huang | Built Clearscope. Content relevance scoring and AI quality gates. |
| Ross Hudgens | Agency-side AI production at scale. "Brand-first SEO" framework. |
| Michał Suski | Surfer SEO co-founder. Tool-native AI workflows used by thousands. |
| Nathan Gotch | GEO frameworks and step-by-step AI tutorials – replicable templates. |
| AJ Ghergich | Enterprise AI content governance. Named on multiple expert lists. |

### Key Patterns Found

Across all 10 experts, six consensus themes emerged (detailed in `research/other/cross-expert-patterns.md`):

1. **AI Draft Model** – AI writes 80%, humans add E-E-A-T
2. **LLM Citation ≠ Google SEO** – Dual optimization required
3. **Brand as Infrastructure** – Brand recognition is now a search variable
4. **Reddit, YouTube, Forums as SEO Infrastructure** – LLMs cite them heavily
5. **Volume Without Quality is a Liability** – Penalties for low-E-E-A-T AI content
6. **Evergreen Declining, Experience Rising** – Original data is the moat

### How to Use This Research

1. Read `research/sources.md` to understand each expert's focus
2. Run `python fetch_transcripts.py` to download YouTube transcripts (requires `pip install yt-dlp`)
3. Study `research/other/cross-expert-patterns.md` for actionable consensus and disagreements
4. Use the patterns to build your own AI content workflow

*Research collected April 2026*
        
