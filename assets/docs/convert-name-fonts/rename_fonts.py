#!/usr/bin/env python3
import os
import subprocess
import re
import shutil
import tempfile

# Directory containing the fonts
FONT_DIR = '/Users/seanivore/Development/voice-mkt-sfa/assets/fonts'

# Directory for renamed fonts
OUTPUT_DIR = '/Users/seanivore/Development/voice-mkt-sfa/assets/renamed-fonts'

# Create the output directory if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)

def get_font_info(font_path):
    """Extract comprehensive font info from the font file using FontForge"""
    try:
        # Create a temporary script for FontForge
        with tempfile.NamedTemporaryFile(mode='w', suffix='.pe', delete=False) as script_file:
            script_path = script_file.name
            
            script_content = f"""Open("{font_path}");
Print("FONTNAME: " + $fontname);
Print("FAMILY: " + $familyname);
Print("FULLNAME: " + $fullname);
Print("WEIGHT: " + $weight);
Print("STYLE: " + $fontstyle);
Quit(0);"""
            
            script_file.write(script_content)
        
        # Run FontForge with the script
        result = subprocess.run(['fontforge', '-script', script_path], 
                               capture_output=True, text=True, check=True)
        
        # Clean up the script file
        os.unlink(script_path)
        
        # Parse the output
        output = result.stdout.strip()
        
        # Extract font information
        info = {}
        for line in output.split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                info[key.strip()] = value.strip()
        
        return info
    except subprocess.CalledProcessError as e:
        print(f"Error getting font info: {e}")
        return {}

def sanitize_filename(name):
    """Make the font name suitable for a filename"""
    # Replace spaces with hyphens and remove any characters that aren't allowed in filenames
    name = re.sub(r'[\\/*?:"<>|]', '', name)
    name = name.replace(' ', '-')
    # Remove any leading or trailing whitespace
    name = name.strip()
    # Remove any non-printable characters
    name = ''.join(c for c in name if c.isprintable())
    return name

def create_font_name(info):
    """Create a good font name from the font info"""
    family = info.get('FAMILY', '')
    fullname = info.get('FULLNAME', '')
    weight = info.get('WEIGHT', '')
    style = info.get('STYLE', '')
    
    # Use fullname if available, as it's usually the most complete
    if fullname:
        return fullname

    # Try to assemble a name from family and style/weight
    if family:
        if weight and weight.lower() != 'regular' and weight.lower() != 'normal':
            return f"{family}-{weight}"
        elif style and style.lower() != 'regular' and style.lower() != 'normal':
            return f"{family}-{style}"
        else:
            return family
    
    # Last resort: just use fontname
    return info.get('FONTNAME', 'unknown')

def main():
    # Get all .otf files in the directory
    font_files = [f for f in os.listdir(FONT_DIR) if f.endswith('.otf')]
    
    # Track processed font names to handle duplicates
    processed_names = set()
    
    # Process each font
    for i, font_file in enumerate(font_files, 1):
        font_path = os.path.join(FONT_DIR, font_file)
        
        print(f"[{i}/{len(font_files)}] Processing: {font_file}")
        
        # Get the font info
        font_info = get_font_info(font_path)
        
        if not font_info:
            print(f"  Skipping {font_file}: Could not determine font info")
            continue
        
        # Print the font info for debugging
        print(f"  Found font information:")
        for key, value in font_info.items():
            print(f"    {key}: {value}")
        
        # Create a good font name
        font_name = create_font_name(font_info)
        print(f"  Suggested name: {font_name}")
        
        # Create sanitized filename
        safe_name = sanitize_filename(font_name)
        
        # Ensure the extension is .otf
        if not safe_name.lower().endswith('.otf'):
            safe_name += '.otf'
            
        # Handle duplicates by adding a number
        original_safe_name = safe_name
        counter = 1
        while safe_name in processed_names:
            name_parts = original_safe_name.rsplit('.', 1)
            safe_name = f"{name_parts[0]}-{counter}.{name_parts[1]}"
            counter += 1
        
        processed_names.add(safe_name)
            
        output_path = os.path.join(OUTPUT_DIR, safe_name)
        
        # Copy the font file
        print(f"  Copying to: {output_path}")
        try:
            shutil.copy2(font_path, output_path)
            print(f"  Successfully renamed {font_file} to {safe_name}")
        except Exception as e:
            print(f"  Failed to copy {font_file}: {e}")

if __name__ == "__main__":
    main()
EOFMARKER 
