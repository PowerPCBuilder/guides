import re
from pathlib import Path
from PIL import Image
import requests
from io import BytesIO
import os

def extract_first_image(markdown_content):
    """Extract the first image URL from markdown content."""
    # Match both ![]() and <img> syntax
    pattern = r'!\[.*?\]\((.*?)\)|<img.*?src=[\'\"](.*?)[\'\"]'
    matches = re.findall(pattern, markdown_content)
    
    # Flatten and filter empty matches
    urls = [url for match in matches for url in match if url]
    return urls[0] if urls else None

def process_image(image_path):
    """Process image to 200x200 maintaining aspect ratio from center."""
    try:
        # Open the image
        if image_path.startswith(('http://', 'https://')):
            response = requests.get(image_path)
            img = Image.open(BytesIO(response.content))
        else:
            img = Image.open(image_path)
            
        # Convert to RGB if necessary
        if img.mode in ('RGBA', 'P'):
            img = img.convert('RGB')
            
        # Calculate dimensions
        original_width, original_height = img.size
        target_size = 200
        
        # Calculate scaling factor based on height
        scale = target_size / original_height
        new_width = int(original_width * scale)
        
        # Resize image maintaining aspect ratio
        img = img.resize((new_width, target_size), Image.Resampling.LANCZOS)
        
        # If width is larger than target_size, crop from center
        if new_width > target_size:
            left = (new_width - target_size) // 2
            img = img.crop((left, 0, left + target_size, target_size))
            
        return img
        
    except Exception as e:
        print(f"Error processing image: {str(e)}")
        return None

def process_markdown_files():
    """Process all markdown files in the nas folder."""
    nas_path = Path('nas')
    
    if not nas_path.exists():
        print("Error: 'nas' folder not found")
        return
        
    # Find all markdown files
    for markdown_file in nas_path.rglob('*.md'):
        try:
            # Read markdown content
            content = markdown_file.read_text(encoding='utf-8')
            
            # Extract first image
            image_url = extract_first_image(content)
            if not image_url:
                print(f"No image found in {markdown_file}")
                continue
                
            # Convert relative paths to absolute
            if not image_url.startswith(('http://', 'https://')):
                image_url = str(markdown_file.parent / image_url)
            
            # Process the image
            processed_image = process_image(image_url.lstrip('\\').replace("\\", "/"))
            if not processed_image:
                continue
                
            # Generate output filename
            original_name = os.path.splitext(image_url.split('/')[-1])[0]
            output_path = markdown_file.parent / f"{original_name}_200.png"
            # Save the processed image
            processed_image.save(output_path, 'PNG')
            print(f"Processed image saved: {output_path}")
            
        except Exception as e:
            print(f"Error processing {markdown_file}: {str(e)}")

def main():
    print("Starting image processing...")
    process_markdown_files()
    print("Processing completed!")

if __name__ == "__main__":
    main()
