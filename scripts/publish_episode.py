#!/usr/bin/env python3
"""
Automated Jekyll Post Publisher for Podcast Episodes
Converts podcast analysis data to Jekyll-compatible markdown posts
"""
import os
import sys
import json
import yaml
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Any, List, Optional
from dataclasses import dataclass
import hashlib

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent.parent))

@dataclass
class EpisodeData:
    """Episode data structure for Jekyll publishing"""
    title: str
    source: str
    date: datetime
    duration: int
    original_url: str
    transcript_path: Optional[str] = None
    summary: Optional[str] = None
    companies: List[Dict[str, Any]] = None
    quotes: List[Dict[str, Any]] = None
    topics: List[Dict[str, Any]] = None
    insights: List[Dict[str, Any]] = None
    actionable_items: List[Dict[str, Any]] = None
    tags: List[str] = None
    llm_enhanced: bool = False
    processing_date: datetime = None

class JekyllPublisher:
    """Publishes podcast episodes as Jekyll posts"""

    def __init__(self, repo_path: str = "/home/mikesmalling/pods/podcast-summaries"):
        self.repo_path = Path(repo_path)
        self.episodes_dir = self.repo_path / "_episodes"
        self.episodes_dir.mkdir(exist_ok=True)

    def sanitize_filename(self, text: str) -> str:
        """Create a safe filename from episode title"""
        # Remove/replace problematic characters
        filename = re.sub(r'[<>:"/\\|?*]', '-', text)
        # Replace spaces and multiple dashes
        filename = re.sub(r'[\s\-]+', '-', filename)
        # Remove leading/trailing dashes
        filename = filename.strip('-')
        # Limit length
        return filename[:100].lower()

    def extract_episode_id(self, url: str) -> str:
        """Extract episode ID from various URL formats"""
        if 'youtube.com/watch?v=' in url:
            return url.split('v=')[1].split('&')[0]
        elif 'youtu.be/' in url:
            return url.split('/')[-1].split('?')[0]
        else:
            # Generate ID from URL hash
            return hashlib.md5(url.encode()).hexdigest()[:8]

    def determine_tags(self, analysis_data: Dict[str, Any], metadata: Dict[str, Any]) -> List[str]:
        """Determine appropriate tags for the episode"""
        tags = []

        # Source-based tags
        source = metadata.get('uploader', '').lower()
        if any(ai_term in source for ai_term in ['ai', 'artificial', 'ml', 'machine learning']):
            tags.extend(['ai', 'technology'])
        if any(crypto_term in source for crypto_term in ['crypto', 'bitcoin', 'blockchain', 'unchained']):
            tags.extend(['crypto', 'blockchain'])
        if any(vc_term in source for vc_term in ['vc', 'venture', 'a16z', 'investment']):
            tags.extend(['venture-capital', 'startup'])

        # Content-based tags from topics
        topics = analysis_data.get('topics', [])
        for topic in topics[:5]:  # Limit to top 5 topics
            topic_name = topic.get('topic', '').lower()
            if topic_name and topic_name not in tags:
                # Clean up topic name
                clean_topic = re.sub(r'[^\w\s-]', '', topic_name)
                clean_topic = re.sub(r'\s+', '-', clean_topic)
                if len(clean_topic) > 2:
                    tags.append(clean_topic)

        # Company-based tags
        companies = analysis_data.get('companies', [])
        prominent_companies = ['openai', 'anthropic', 'google', 'microsoft', 'apple', 'meta', 'nvidia']
        for company in companies:
            company_name = company.get('name', '').lower()
            if company_name in prominent_companies and company_name not in tags:
                tags.append(company_name)

        return tags[:8]  # Limit to 8 tags

    def format_duration_minutes(self, duration_seconds: int) -> int:
        """Convert duration from seconds to minutes"""
        return max(1, round(duration_seconds / 60))

    def create_episode_post(self, analysis_data: Dict[str, Any], metadata: Dict[str, Any]) -> bool:
        """Create a Jekyll post from analysis data"""
        try:
            # Extract episode information
            episode_info = analysis_data.get('episode_info', metadata)
            title = episode_info.get('title', 'Unknown Episode')
            source = episode_info.get('uploader', 'Unknown Source')
            duration_seconds = episode_info.get('duration', 0)
            original_url = episode_info.get('url') or episode_info.get('original_url', '')

            # Determine publish date
            upload_date = episode_info.get('upload_date')
            if upload_date:
                if len(upload_date) == 8:  # YYYYMMDD format
                    date = datetime.strptime(upload_date, '%Y%m%d')
                else:
                    date = datetime.fromisoformat(upload_date.replace('Z', '+00:00'))
            else:
                date = datetime.now(timezone.utc)

            # Create filename
            date_str = date.strftime('%Y-%m-%d')
            title_slug = self.sanitize_filename(title)
            filename = f"{date_str}-{title_slug}.md"
            filepath = self.episodes_dir / filename

            # Prepare episode data
            episode = EpisodeData(
                title=title,
                source=source,
                date=date,
                duration=self.format_duration_minutes(duration_seconds),
                original_url=original_url,
                summary=analysis_data.get('llm_summary', ''),
                companies=analysis_data.get('companies', []),
                quotes=analysis_data.get('quotes', []),
                topics=analysis_data.get('topics', []),
                insights=analysis_data.get('insights', []),
                actionable_items=analysis_data.get('actionable_items', []),
                tags=self.determine_tags(analysis_data, metadata),
                llm_enhanced=analysis_data.get('llm_enhanced', False),
                processing_date=datetime.now(timezone.utc)
            )

            # Generate Jekyll front matter
            front_matter = {
                'layout': 'episode',
                'title': episode.title,
                'source': episode.source,
                'date': episode.date.strftime('%Y-%m-%d %H:%M:%S %z'),
                'duration': episode.duration,
                'original_url': episode.original_url,
                'tags': episode.tags,
                'llm_enhanced': episode.llm_enhanced,
                'processing_date': episode.processing_date.strftime('%Y-%m-%d %H:%M:%S %z')
            }

            # Add optional fields if they exist
            if episode.summary:
                front_matter['summary'] = episode.summary

            if episode.companies:
                front_matter['companies'] = episode.companies

            if episode.quotes:
                front_matter['quotes'] = episode.quotes

            if episode.topics:
                front_matter['topics'] = episode.topics

            if episode.insights:
                front_matter['insights'] = episode.insights

            if episode.actionable_items:
                front_matter['actionable_items'] = episode.actionable_items

            # Generate transcript URL if available
            episode_id = self.extract_episode_id(original_url)
            front_matter['transcript_url'] = f"/transcripts/{episode_id}.html"

            # Write the Jekyll post
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write('---\n')
                yaml.dump(front_matter, f, default_flow_style=False, allow_unicode=True)
                f.write('---\n\n')

                # Add any additional content if needed
                f.write(f"<!-- Episode automatically generated from analysis data -->\n")
                f.write(f"<!-- Processing completed: {episode.processing_date.strftime('%Y-%m-%d %H:%M:%S %Z')} -->\n")

            print(f"✅ Created Jekyll post: {filename}")
            return True

        except Exception as e:
            print(f"❌ Error creating Jekyll post: {str(e)}")
            import traceback
            traceback.print_exc()
            return False

    def publish_from_database(self, db_path: str, episode_guid: str) -> bool:
        """Publish episode from database record"""
        try:
            import sqlite3

            conn = sqlite3.connect(db_path)
            conn.row_factory = sqlite3.Row

            # Get episode data
            cursor = conn.execute("""
                SELECT * FROM episodes
                WHERE guid = ? OR episode_id = ?
                ORDER BY created_at DESC
                LIMIT 1
            """, (episode_guid, episode_guid))

            row = cursor.fetchone()
            if not row:
                print(f"❌ Episode not found: {episode_guid}")
                return False

            # Parse metadata and analysis
            metadata = json.loads(row['metadata']) if row['metadata'] else {}

            # Check if analysis file exists
            analysis_file = None
            if row['transcript_file_path']:
                transcript_path = Path(row['transcript_file_path'])
                analysis_file = transcript_path.parent.parent / "analysis" / f"{transcript_path.stem}_analysis.json"

            if analysis_file and analysis_file.exists():
                with open(analysis_file, 'r') as f:
                    analysis_data = json.load(f)
            else:
                # Create minimal analysis data from database
                analysis_data = {
                    'episode_info': {
                        'title': row['title'],
                        'uploader': metadata.get('uploader', ''),
                        'duration': row['duration'],
                        'url': row['url'],
                        'upload_date': row['published_at']
                    },
                    'llm_enhanced': False,
                    'companies': [],
                    'quotes': [],
                    'topics': [],
                    'insights': [],
                    'actionable_items': []
                }

            success = self.create_episode_post(analysis_data, metadata)
            conn.close()
            return success

        except Exception as e:
            print(f"❌ Error publishing from database: {str(e)}")
            return False

    def update_index_page(self) -> bool:
        """Update the main index page with latest episodes"""
        try:
            # Get latest episodes
            episodes = list(self.episodes_dir.glob("*.md"))
            episodes.sort(key=lambda x: x.stat().st_mtime, reverse=True)

            # Update README with latest episodes
            readme_path = self.repo_path / "README.md"

            # Read current README
            with open(readme_path, 'r') as f:
                content = f.read()

            # Extract the part before "## 📊 Sources"
            if "## 📊 Sources" in content:
                header_part = content.split("## 📊 Sources")[0]
                footer_part = "## 📊 Sources" + content.split("## 📊 Sources")[1]
            else:
                header_part = content
                footer_part = ""

            # Add latest episodes section
            latest_section = "\n## 🎧 Latest Episodes\n\n"

            for episode_file in episodes[:5]:  # Show 5 latest
                # Parse front matter to get episode info
                with open(episode_file, 'r') as f:
                    file_content = f.read()

                if file_content.startswith('---'):
                    try:
                        front_matter_end = file_content.find('---', 3)
                        if front_matter_end > 0:
                            front_matter_text = file_content[3:front_matter_end]
                            episode_data = yaml.safe_load(front_matter_text)

                            title = episode_data.get('title', 'Unknown')
                            source = episode_data.get('source', 'Unknown')
                            date = episode_data.get('date', '')
                            if isinstance(date, str):
                                try:
                                    date_obj = datetime.fromisoformat(date.replace('Z', '+00:00'))
                                    date_str = date_obj.strftime('%b %d, %Y')
                                except:
                                    date_str = date
                            else:
                                date_str = str(date)

                            # Create episode link
                            episode_url = f"/episodes/{episode_file.stem}/"
                            latest_section += f"- **[{title}]({episode_url})** - {source} ({date_str})\n"
                    except:
                        continue

            # Reconstruct README
            new_content = header_part + latest_section + "\n" + footer_part

            # Write updated README
            with open(readme_path, 'w') as f:
                f.write(new_content)

            print("✅ Updated index page with latest episodes")
            return True

        except Exception as e:
            print(f"❌ Error updating index page: {str(e)}")
            return False

def main():
    """Main entry point"""
    import argparse

    parser = argparse.ArgumentParser(description='Publish podcast episode to Jekyll site')
    parser.add_argument('--analysis-file', help='Path to analysis JSON file')
    parser.add_argument('--metadata-file', help='Path to metadata JSON file')
    parser.add_argument('--db-path', help='Database path for episode lookup')
    parser.add_argument('--episode-guid', help='Episode GUID to publish from database')
    parser.add_argument('--repo-path', default='/home/mikesmalling/pods/podcast-summaries', help='Repository path')
    parser.add_argument('--update-index', action='store_true', help='Update index page')

    args = parser.parse_args()

    publisher = JekyllPublisher(args.repo_path)

    if args.update_index:
        success = publisher.update_index_page()
    elif args.db_path and args.episode_guid:
        success = publisher.publish_from_database(args.db_path, args.episode_guid)
    elif args.analysis_file:
        # Load analysis and metadata files
        try:
            with open(args.analysis_file, 'r') as f:
                analysis_data = json.load(f)

            if args.metadata_file:
                with open(args.metadata_file, 'r') as f:
                    metadata = json.load(f)
            else:
                metadata = {}

            success = publisher.create_episode_post(analysis_data, metadata)
        except Exception as e:
            print(f"❌ Error loading files: {str(e)}")
            success = False
    else:
        print("❌ No valid input provided. Use --analysis-file, --db-path + --episode-guid, or --update-index")
        success = False

    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()