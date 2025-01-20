import os
import yaml
from supabase import create_client
from pathlib import Path

# Supabase configuration
SUPABASE_URL = "https://iqoemefpfkcrhnubyknp.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imlxb2VtZWZwZmtjcmhudWJ5a25wIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzczMDI5MjUsImV4cCI6MjA1Mjg3ODkyNX0.fH-ZlaudQX-ouZ1o7FgNrVHSDM5pGVt5cVC6SPUKUc0"

# Initialize Supabase client
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def parse_markdown_frontmatter(file_path):
    """Parse front matter from markdown file."""
    content = file_path.read_text(encoding='utf-8')
    
    # Check if file has front matter
    if not content.startswith('---'):
        return None
    
    # Extract front matter
    _, front_matter, _ = content.split('---', 2)
    return yaml.safe_load(front_matter)

def get_category_from_path(file_path):
    """Extract category from file path (first folder name)."""
    parts = file_path.parts
    return parts[0] if parts else None

def sync_markdown_files():
    """Sync markdown files with Supabase table."""
    # Get all existing URLs from the table
    existing_records = supabase.table('guide').select('url').execute()
    existing_urls = {record['url'] for record in existing_records.data}
    
    # Scan for markdown files
    for markdown_file in Path('.').rglob('*.md'):
        # Skip files not in specific folders
        category = get_category_from_path(markdown_file)
        if not category or category not in ['nas']:  # Add more folders as needed
            continue
            
        # Parse front matter
        front_matter = parse_markdown_frontmatter(markdown_file)
        if not front_matter:
            continue
            
        # Prepare record data
        record = {
            'category': category,
            'phase': front_matter.get('phase'),
            'url': front_matter.get('permalink'),
            'title': front_matter.get('title'),
            'description': front_matter.get('description'),
            'tags': front_matter.get('tags')
        }
        
        # Skip if no URL
        if not record['url']:
            print(f"Skipping {markdown_file}: No URL found")
            continue
            
        try:
            if record['url'] in existing_urls:
                # Update existing record
                print(f"Updating: {record['url']}")
                supabase.table('guide').update(record).eq('url', record['url']).execute()
            else:
                # Insert new record
                print(f"Inserting: {record['url']}")
                supabase.table('guide').insert(record).execute()
        except Exception as e:
            print(f"Error processing {markdown_file}: {str(e)}")

def main():
    print("Starting markdown to Supabase sync...")
    sync_markdown_files()
    print("Sync completed!")

if __name__ == "__main__":
    main()