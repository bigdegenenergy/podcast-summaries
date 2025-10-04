# 🎙️ Podcast Intelligence Hub

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live-brightgreen)](https://bigdegenenergy.github.io/podcast-summaries/)
[![Episodes](https://img.shields.io/badge/Episodes-362+-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> **AI-powered podcast summaries, transcripts, and insights.** Stay informed without listening to hours of content.

---

## 🌟 What is This?

This is an **automated podcast intelligence system** that processes, transcribes, and analyzes podcast episodes using AI. It creates searchable, mobile-friendly summaries with key insights, company mentions, and actionable takeaways.

**📊 Currently tracking:** 362+ episodes from 15+ premium podcasts  
**🔄 Update frequency:** Automatically processes new episodes as they're published  
**🎯 Categories:** AI & Technology, Crypto & Web3, Venture Capital & Startups

---

## ✨ Features

- **🎙️ Automatic Transcription** - Whisper AI generates accurate transcripts
- **🤖 AI Analysis** - Claude AI extracts insights, key quotes, and company mentions
- **📱 Mobile-Friendly** - Jekyll-powered static site optimized for all devices
- **🔍 Searchable Archive** - Browse by category, date, or search across all content
- **📊 Rich Metadata** - Duration, topics, companies, and relevance scores for each episode
- **🔗 Original Links** - Direct links to source material for full context

---

## 🚀 Quick Start

### Browsing Content

Visit the live site: **[https://bigdegenenergy.github.io/podcast-summaries/](https://bigdegenenergy.github.io/podcast-summaries/)**

- **[All Episodes](/episodes)** - Complete searchable archive
- **[AI & Technology](/categories/ai)** - AI, ML, and emerging tech
- **[Crypto & Web3](/categories/crypto)** - Blockchain and cryptocurrency

### Local Development

```bash
# Clone the repository
git clone https://github.com/bigdegenenergy/podcast-summaries.git
cd podcast-summaries

# Install dependencies
bundle install

# Run Jekyll locally
bundle exec jekyll serve

# Visit http://localhost:4000/podcast-summaries/
```

---

## 🏗️ Architecture

This project consists of several key components:

### 1. **Jekyll Static Site** (`_config.yml`, `_layouts/`, `_episodes/`)
   - Static site generator for GitHub Pages
   - Mobile-optimized theme with category navigation
   - Episode collection with custom layout and metadata

### 2. **Publishing Pipeline** (`scripts/publish_episode.py`)
   - Python script that converts analyzed podcast data to Jekyll posts
   - Automatically updates the README with latest episodes
   - Handles front matter, metadata, and file organization

### 3. **GitHub Actions** (`.github/workflows/pages.yml`)
   - Automated deployment to GitHub Pages
   - Builds and publishes on every push to main branch

### 4. **Episode Data Structure**
   Each episode markdown file includes:
   - **Front matter:** Title, date, source, duration, tags
   - **Summary:** AI-generated episode overview
   - **Key insights:** Most important takeaways
   - **Companies mentioned:** Tech companies and startups discussed
   - **Notable quotes:** Impactful statements with context
   - **Actionable items:** Tasks and recommendations from the episode

---

## 📊 Sources

### AI & Technology
- **How I AI** - Practical AI usage and tools
- **AI Chat (Audio)** - ChatGPT and AI discussions
- **No Priors: AI, ML, Tech & Startups** - AI industry insights
- **AI Explored** - Business AI applications
- **Last Week in AI** - Weekly AI news summaries
- **The AI Daily Brief** - Daily AI updates
- **Wes Roth** - AI, ML, and OpenAI coverage
- **The AI Podcast (NVIDIA)** - Deep learning and AI research
- **AI Breakdown** - AI news analysis

### Crypto & Blockchain
- **Unchained (Laura Shin)** - Crypto journalism and investigations
- **The Pomp Podcast** - Bitcoin and investment perspectives
- **Bankless** - DeFi and Ethereum ecosystem

### Venture Capital & Startups
- **a16z Podcast** - Andreessen Horowitz insights
- **The Twenty Minute VC** - Venture capital discussions

---

## 🎧 Latest Episodes

> The latest episode list is dynamically updated by the automated publishing system.

- **[AI Video Just Got WAY TOO REAL... (SORA 2)](/episodes/2025-09-30-ai-video-just-got-way-too-real...-(sora-2)/)** - Wes Roth (2025-09-30 00:00:00)
- **[Claude Sonnet 4.5 Can Code Autonomously for 30 Hours 🤯](/episodes/2025-09-30-claude-sonnet-4.5-can-code-autonomously-for-30-hours-🤯/)** - The AI Daily Brief (2025-09-30 00:00:00)
- **[Will Every Company Have Its Own Stablecoin? Yes, Says Stripe's Bridge](/episodes/2025-09-30-will-every-company-have-its-own-stablecoin-yes,-says-stripe's-bridge/)** - Unchained (2025-09-30 00:00:00)
- **[OpenAI Announces "Sora 2" New AI Video Model](/episodes/2025-09-30-openai-announces-sora-2-new-ai-video-model/)** - AI Chat (Audio) (2025-09-30 00:00:00)
- **[OpenAI Preps AI Tik-Tok App](/episodes/2025-09-30-openai-preps-ai-tik-tok-app/)** - The AI Daily Brief (2025-09-30 00:00:00)

---

## 🤝 Contributing

Contributions are welcome! If you'd like to add new podcast sources or improve the analysis pipeline:

1. **Fork this repository**
2. **Create a feature branch** (`git checkout -b feature/new-podcast-source`)
3. **Make your changes** and test locally
4. **Submit a pull request** with a clear description

### Adding New Podcast Sources

To add a new podcast to the monitoring system:
1. Add the RSS feed or YouTube channel ID to the source configuration
2. Update the "Sources" section in this README
3. Test the ingestion pipeline with a sample episode

---

## 📝 How the System Works

### Episode Processing Pipeline

1. **Monitor** - System checks RSS feeds and YouTube channels for new episodes
2. **Download** - Audio files are downloaded for processing
3. **Transcribe** - Whisper AI generates accurate transcripts
4. **Analyze** - Claude AI extracts:
   - Episode summary and key insights
   - Company and technology mentions
   - Notable quotes with context
   - Actionable takeaways
5. **Publish** - Jekyll markdown files are generated and committed
6. **Deploy** - GitHub Actions builds and deploys to GitHub Pages

### File Structure

```
podcast-summaries/
├── _episodes/          # Jekyll collection of episode markdown files
├── _layouts/           # Custom Jekyll layouts for episode pages
├── categories/         # Category index pages (AI, Crypto, etc.)
├── scripts/            # Python automation scripts
│   └── publish_episode.py  # Converts analyzed data to Jekyll posts
├── .github/
│   └── workflows/
│       └── pages.yml   # GitHub Pages deployment workflow
├── _config.yml         # Jekyll site configuration
└── README.md           # This file
```

---

## 🛠️ Technical Stack

- **Static Site Generator:** Jekyll (GitHub Pages compatible)
- **AI Transcription:** OpenAI Whisper
- **AI Analysis:** Anthropic Claude
- **Hosting:** GitHub Pages
- **CI/CD:** GitHub Actions
- **Language:** Python 3.x for automation scripts

---

## 📜 License

This project is open source and available under the MIT License.

---

## 🔗 Links

- **Live Site:** [https://bigdegenenergy.github.io/podcast-summaries/](https://bigdegenenergy.github.io/podcast-summaries/)
- **GitHub Repository:** [https://github.com/bigdegenenergy/podcast-summaries](https://github.com/bigdegenenergy/podcast-summaries)
- **Issues & Feature Requests:** [GitHub Issues](https://github.com/bigdegenenergy/podcast-summaries/issues)

---

## ⚠️ Disclaimer

This project is for educational and informational purposes. All podcast content rights belong to their respective creators. This repository provides AI-generated summaries to help users discover and understand podcast content more efficiently. Please support original creators by listening to full episodes and subscribing to their channels.

---

<p align="center">
  <strong>Last updated:</strong> Automatically every 6 hours<br>
  <strong>Powered by:</strong> Whisper AI + Claude AI + GitHub Actions + BDE
</p>
