#!/bin/bash
# Test Jekyll site locally to verify everything works before GitHub Pages deployment

echo "🧪 Testing Jekyll site locally..."
echo "================================="

cd /home/mikesmalling/pods/podcast-summaries

# Check if bundle is installed
if ! command -v bundle &> /dev/null; then
    echo "📦 Installing bundler..."
    gem install bundler
fi

# Install dependencies
echo "📦 Installing Jekyll dependencies..."
bundle install

# Build the site
echo "🏗️  Building Jekyll site..."
bundle exec jekyll build

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Jekyll build successful!"
    echo "📁 Site built in _site/ directory"
    echo "📄 Files generated:"
    ls -la _site/ | head -10
    echo ""
    echo "🌐 To test locally, run:"
    echo "   bundle exec jekyll serve"
    echo "   Then visit: http://localhost:4000/podcast-summaries/"
else
    echo "❌ Jekyll build failed"
fi