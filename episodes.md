---
layout: default
title: All Episodes
---

# 📚 All Episodes

<div class="episodes-grid">
{% assign sorted_episodes = site.episodes | sort: 'date' | reverse %}
{% for episode in sorted_episodes %}
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
      <p class="episode-excerpt">{{ episode.summary | strip_html | truncate: 150 }}</p>
    {% endif %}
    <div class="episode-tags">
      {% for tag in episode.tags limit:3 %}
        <span class="tag">{{ tag }}</span>
      {% endfor %}
    </div>
  </div>
{% endfor %}
</div>

<style>
.episodes-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1.5rem;
  padding: 1rem;
}

.episode-card {
  background: white;
  border: 1px solid #dee2e6;
  border-radius: 0.5rem;
  padding: 1.5rem;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  transition: box-shadow 0.2s;
}

.episode-card:hover {
  box-shadow: 0 4px 8px rgba(0,0,0,0.15);
}

.episode-card h3 {
  margin-bottom: 0.75rem;
  line-height: 1.3;
}

.episode-card h3 a {
  color: #2c3e50;
  text-decoration: none;
}

.episode-card h3 a:hover {
  color: #007bff;
}

.episode-meta {
  display: flex;
  gap: 0.75rem;
  margin-bottom: 1rem;
  flex-wrap: wrap;
}

.episode-meta span {
  background: #f8f9fa;
  padding: 0.25rem 0.5rem;
  border-radius: 0.25rem;
  font-size: 0.8rem;
  color: #6c757d;
}

.episode-excerpt {
  color: #6c757d;
  margin-bottom: 1rem;
  line-height: 1.4;
}

.episode-tags {
  display: flex;
  gap: 0.5rem;
  flex-wrap: wrap;
}

.tag {
  background: #007bff;
  color: white;
  padding: 0.2rem 0.4rem;
  border-radius: 0.25rem;
  font-size: 0.7rem;
}

@media (max-width: 768px) {
  .episodes-grid {
    grid-template-columns: 1fr;
    gap: 1rem;
    padding: 0.5rem;
  }

  .episode-card {
    padding: 1rem;
  }
}
</style>