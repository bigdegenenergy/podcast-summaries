#!/bin/bash
# Setup script for GitHub Pages podcast repository

echo "🚀 Setting up Podcast Intelligence Hub repository..."

# Initialize git repository
if [ ! -d ".git" ]; then
    echo "📦 Initializing Git repository..."
    git init
    git branch -M main
fi

# Add all files
echo "📁 Adding files to repository..."
git add .

# Create initial commit
echo "💾 Creating initial commit..."
git commit -m "Initial setup: Jekyll site for AI-powered podcast summaries

✨ Features:
- Mobile-friendly Jekyll theme
- Automated episode processing
- AI-powered content analysis
- Category organization (AI/Crypto)
- GitHub Pages deployment

🤖 Generated with Claude Code
Co-Authored-By: Claude <noreply@anthropic.com>"

echo ""
echo "✅ Repository setup complete!"
echo ""
echo "🔧 Next steps:"
echo "1. Create a new GitHub repository named 'podcast-summaries'"
echo "2. Add the remote origin:"
echo "   git remote add origin https://github.com/YOUR_USERNAME/podcast-summaries.git"
echo "3. Push to GitHub:"
echo "   git push -u origin main"
echo "4. Enable GitHub Pages in repository settings"
echo "5. Update _config.yml with your GitHub username"
echo ""
echo "📱 Your podcast summaries will be available at:"
echo "   https://YOUR_USERNAME.github.io/podcast-summaries/"
echo ""
echo "🎯 To publish new episodes automatically:"
echo "   Episodes will be published automatically when the cron job processes new podcasts"
echo "   Manual publishing: python3 scripts/publish_episode.py --db-path ../data/metadata/podcasts.db --episode-guid EPISODE_GUID"