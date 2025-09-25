---
layout: default
title: 🎙️ Podcast Intelligence Hub
---

# 🎙️ Podcast Intelligence Hub

<div class="hero-section">
  <p class="hero-description">AI-powered podcast summaries and insights from leading technology and business shows.</p>
</div>

## 🎯 Quick Navigation

<div class="nav-grid">
  <div class="nav-item">
    <h3><a href="{{ '/episodes.html' | relative_url }}">📚 All Episodes</a></h3>
    <p>Complete archive of analyzed podcast episodes</p>
  </div>

  <div class="nav-item">
    <h3><a href="{{ '/categories/ai.html' | relative_url }}">🤖 AI & Technology</a></h3>
    <p>Latest episodes covering artificial intelligence, machine learning, and emerging tech</p>
  </div>

  <div class="nav-item">
    <h3><a href="{{ '/categories/crypto.html' | relative_url }}">₿ Crypto & Web3</a></h3>
    <p>Cryptocurrency, blockchain technology, DeFi, and Web3 developments</p>
  </div>
</div>

## 📈 Latest Episodes

<div class="recent-episodes">
{% assign recent_episodes = site.episodes | sort: 'date' | reverse | limit: 6 %}
{% for episode in recent_episodes %}
  <div class="episode-preview">
    <h4><a href="{{ episode.url | relative_url }}">{{ episode.title }}</a></h4>
    <div class="episode-meta">
      <span class="source">{{ episode.source }}</span>
      <span class="date">{{ episode.date | date: "%b %d, %Y" }}</span>
      {% if episode.duration %}
        <span class="duration">{{ episode.duration }}m</span>
      {% endif %}
    </div>
    {% if episode.summary %}
      <p class="episode-excerpt">{{ episode.summary | strip_html | truncate: 120 }}</p>
    {% endif %}
  </div>
{% endfor %}
</div>

{% if site.episodes.size == 0 %}
<div class="no-episodes">
  <p>No episodes processed yet. The system will automatically analyze new episodes as they're published!</p>
</div>
{% endif %}

<style>
.hero-section {
  text-align: center;
  padding: 2rem 0;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border-radius: 0.5rem;
  margin-bottom: 2rem;
}

.hero-description {
  font-size: 1.2rem;
  margin: 0;
}

.nav-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
  margin: 2rem 0;
}

.nav-item {
  background: white;
  border: 1px solid #dee2e6;
  border-radius: 0.5rem;
  padding: 1.5rem;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  transition: transform 0.2s, box-shadow 0.2s;
}

.nav-item:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}

.nav-item h3 {
  margin-bottom: 0.5rem;
}

.nav-item h3 a {
  color: #2c3e50;
  text-decoration: none;
}

.nav-item h3 a:hover {
  color: #007bff;
}

.nav-item p {
  color: #6c757d;
  margin: 0;
  font-size: 0.9rem;
}

.recent-episodes {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.5rem;
  margin-top: 1rem;
}

.episode-preview {
  background: white;
  border: 1px solid #dee2e6;
  border-radius: 0.5rem;
  padding: 1.25rem;
  box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}

.episode-preview h4 {
  margin-bottom: 0.75rem;
  line-height: 1.3;
}

.episode-preview h4 a {
  color: #2c3e50;
  text-decoration: none;
}

.episode-preview h4 a:hover {
  color: #007bff;
}

.episode-meta {
  display: flex;
  gap: 0.75rem;
  margin-bottom: 0.75rem;
  flex-wrap: wrap;
}

.episode-meta span {
  background: #f8f9fa;
  padding: 0.2rem 0.4rem;
  border-radius: 0.25rem;
  font-size: 0.8rem;
  color: #6c757d;
}

.episode-excerpt {
  color: #6c757d;
  margin: 0;
  line-height: 1.4;
  font-size: 0.9rem;
}

.no-episodes {
  text-align: center;
  padding: 3rem 1rem;
  color: #6c757d;
  background: #f8f9fa;
  border-radius: 0.5rem;
}

@media (max-width: 768px) {
  .nav-grid {
    grid-template-columns: 1fr;
    gap: 1rem;
  }

  .recent-episodes {
    grid-template-columns: 1fr;
    gap: 1rem;
  }

  .nav-item, .episode-preview {
    padding: 1rem;
  }

  .hero-section {
    padding: 1.5rem 1rem;
  }

  .hero-description {
    font-size: 1.1rem;
  }
}
</style>