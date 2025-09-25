---
layout: default
title: Crypto & Web3
---

# ₿ Crypto & Web3 Episodes

<div class="category-description">
  <p>Latest episodes covering cryptocurrency, blockchain technology, DeFi, and Web3 developments.</p>
</div>

<div class="episodes-grid">
{% assign crypto_episodes = site.episodes | where_exp: "episode", "episode.tags contains 'crypto' or episode.tags contains 'bitcoin' or episode.tags contains 'blockchain' or episode.tags contains 'web3'" | sort: 'date' | reverse %}
{% for episode in crypto_episodes %}
  <div class="episode-card">
    <h3><a href="{{ episode.url }}">{{ episode.title }}</a></h3>
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

    {% if episode.companies and episode.companies.size > 0 %}
      <div class="featured-companies">
        <strong>Projects/Companies:</strong>
        {% for company in episode.companies limit:4 %}
          <span class="company">{{ company.name }}</span>{% unless forloop.last %}, {% endunless %}
        {% endfor %}
      </div>
    {% endif %}
  </div>
{% endfor %}
</div>

{% if crypto_episodes.size == 0 %}
<div class="no-episodes">
  <p>No crypto episodes found yet. Check back soon!</p>
</div>
{% endif %}

<style>
.category-description {
  background: #fff8e1;
  padding: 1rem;
  border-radius: 0.5rem;
  margin-bottom: 2rem;
  border-left: 4px solid #ff9800;
}

.episodes-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1.5rem;
  padding: 1rem 0;
}

.episode-card {
  background: white;
  border: 1px solid #dee2e6;
  border-radius: 0.5rem;
  padding: 1.5rem;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.episode-card h3 {
  margin-bottom: 0.75rem;
}

.episode-card h3 a {
  color: #2c3e50;
  text-decoration: none;
}

.episode-meta {
  display: flex;
  gap: 0.75rem;
  margin-bottom: 1rem;
  flex-wrap: wrap;
}

.episode-meta span {
  background: #fff3e0;
  color: #f57c00;
  padding: 0.25rem 0.5rem;
  border-radius: 0.25rem;
  font-size: 0.8rem;
}

.episode-excerpt {
  color: #6c757d;
  margin-bottom: 1rem;
  line-height: 1.4;
}

.featured-companies {
  font-size: 0.9rem;
  color: #495057;
}

.company {
  background: #fff3e0;
  padding: 0.2rem 0.4rem;
  border-radius: 0.25rem;
  font-weight: 500;
  color: #f57c00;
}

.no-episodes {
  text-align: center;
  padding: 3rem 1rem;
  color: #6c757d;
}

@media (max-width: 768px) {
  .episodes-grid {
    grid-template-columns: 1fr;
    gap: 1rem;
    padding: 0;
  }

  .episode-card {
    padding: 1rem;
  }
}
</style>