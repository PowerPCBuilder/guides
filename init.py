import os
import yaml
import re
import requests

# Directories
posts_dir = "nas"
tags_dir = "tags"
images_dir = "/assets/images/nas"

# Create necessary directories if they don't exist
os.makedirs(tags_dir, exist_ok=True)
os.makedirs(images_dir, exist_ok=True)

def clean_tags_folder(folder_path):
    """Remove all files in the tags folder to avoid dirty files."""
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(f"Removed old tag file: {file_path}")

def format_tags(tags):
    """Format tags to ensure each word's first character is uppercase, preserving the rest."""
    return [tag[0].upper() + tag[1:] if tag else tag for tag in tags]

def sanitize_filename(filename):
    # Convert to lowercase first
    filename = filename.lower()
    # Replace non-alphanumeric characters with underscores
    sanitized = re.sub(r"[^a-z0-9]", "_", filename)
    # Trim leading/trailing underscores
    sanitized = sanitized.strip('_')
    return sanitized

def download_and_replace_images(content, image_folder):
    """Download external images and replace their URLs in the markdown content."""
    def download_image(url, folder):
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            # Determine filename and extension
            filename = sanitize_filename(url.split("/")[-1])
            if not filename or '.' not in filename:
                # Get content type and infer extension if missing
                content_type = response.headers.get('Content-Type', '')
                extension = content_type.split('/')[-1] if '/' in content_type else 'jpg'
                filename = f"{filename or 'image'}.{extension}"

            local_path = os.path.join(folder, filename).lstrip('/')
            with open(local_path, 'wb') as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            return local_path
        else:
            print(f"Failed to download image: {url}")
            return None

    updated_content = content
    image_pattern = re.compile(r"!\[.*?\]\((http[s]?://.*?)\)")
    for match in image_pattern.finditer(content):
        image_url = match.group(1)
        local_image_path = download_image(image_url, image_folder)
        if local_image_path:
            # Ensure consistent formatting for relative paths
            relative_path = f"/" + os.path.relpath(local_image_path, start=os.getcwd()).replace("\\", "/").lstrip("../")
            updated_content = updated_content.replace(image_url, relative_path)
            print(f"Replaced image URL: {image_url} -> {relative_path}")

    return updated_content
def process_md_files_and_collect_tags(folder_path):
    """Process .md files: rename files, format tags, and collect all tags."""
    all_tags = set()

    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)

                # Read the content of the file
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Extract the title from the first Markdown header (#)
                title_match = re.search(r"^#\s*(.+)$", content, re.MULTILINE)
                title = title_match.group(1).strip() if title_match else "Untitled"

                # Generate a unique filename from the title
                base_filename = sanitize_filename(title)
                new_filename = f"{base_filename}.md"
                new_file_path = os.path.join(root, new_filename)
                counter = 1
                while os.path.exists(new_file_path):
                    new_filename = f"{base_filename}_{counter}.md"
                    new_file_path = os.path.join(root, new_filename)
                    counter += 1

                # Rename the file
                os.rename(file_path, new_file_path)
                print(f"Renamed: {file} -> {new_filename}")
                file_path = new_file_path  # Update file_path for further processing

                # Format tags
                front_matter_match = re.match(r"---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
                if front_matter_match:
                    front_matter = yaml.safe_load(front_matter_match.group(1))
                    if "tags" in front_matter and isinstance(front_matter["tags"], list):
                        formatted_tags = format_tags(front_matter["tags"])
                        front_matter["tags"] = formatted_tags
                        all_tags.update(formatted_tags)
                        print(f"Formatted tags for {new_filename}")

                    # Reconstruct the file content with updated front matter
                    new_front_matter = yaml.dump(front_matter, default_flow_style=False).strip()
                    content = f"---\n{new_front_matter}\n---\n" + content[front_matter_match.end():]

                # Handle external images
                content = download_and_replace_images(content, images_dir)

                # Write the updated content back to the file
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)

    return all_tags

def generate_tag_pages(tags, output_dir):
    """Generate tag pages for each unique tag."""
    clean_tags_folder(output_dir)
    for tag in tags:
        slug = tag.lower().replace(" ", "-")
        filepath = os.path.join(output_dir, f"{slug}.md")
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(f"""---
layout: default
title: "Tag: {tag}"
tag: {tag}
permalink: /tags/{slug}/
---
<h1>Pages tagged with "{tag}"</h1>
<ul>
{{% for post in site.pages %}}
  {{% if post.tags contains "{tag}" %}}
  <li><a href="{{{{ post.url }}}}">{{{{ post.title }}}}</a></li>
  {{% endif %}}
{{% endfor %}}
</ul>
""")
        print(f"Generated tag page for: {tag}")

if __name__ == "__main__":
    # Process Markdown files and collect tags
    all_tags = process_md_files_and_collect_tags(posts_dir)

    # Generate tag pages
    generate_tag_pages(all_tags, tags_dir)
