#!/usr/bin/env python3
import os
import subprocess
import re
import shutil
import tempfile

# Directory containing the fonts
FONT_DIR = '/Users/seanivore/Development/voice-mkt-sfa/assets/fonts'

# Directory for converted fonts
OUTPUT_DIR = '/Users/seanivore/Development/voice-mkt-sfa/assets/web-fonts'

# Create the output directory if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)

def get_font_name(font_path):
    """Extract the font name from the font file using FontForge"""
    try:
        # Create a temporary script for FontForge
        with tempfile.NamedTemporaryFile(mode='w', suffix='.pe', delete=False) as script_file:
            script_path = script_file.name
            
            script_content = f"""Open("{font_path}");
Print($fontname);
Print(" ");
Print($familyname);
Print(" ");
Print($fullname);
Quit(0);"""
            
            script_file.write(script_content)
        
        # Run FontForge with the script
        result = subprocess.run(['fontforge', '-script', script_path], 
                               capture_output=True, text=True, check=True)
        
        # Clean up the script file
        os.unlink(script_path)
        
        # Parse the output
        output = result.stdout.strip()
        if output:
            # Try to use fullname first, then familyname, then fontname
            parts = output.split(' ')
            if len(parts) >= 3 and parts[2]:  # fullname
                return parts[2]
            elif len(parts) >= 2 and parts[1]:  # familyname
                return parts[1]
            elif parts[0]:  # fontname
                return parts[0]
        
        # If we couldn't parse the name, use the original filename
        return os.path.basename(font_path)
    except subprocess.CalledProcessError as e:
        print(f"Error getting font name: {e}")
        return os.path.basename(font_path)

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

def convert_font(font_path, output_path):
    """Convert font from OTF to TTF using FontForge"""
    try:
        # Create a temporary script for FontForge
        with tempfile.NamedTemporaryFile(mode='w', suffix='.pe', delete=False) as script_file:
            script_path = script_file.name
            
            script_content = f"""Open("{font_path}");
Save("{output_path}");
Quit(0);"""
            
            script_file.write(script_content)
        
        # Run FontForge with the script
        result = subprocess.run(['fontforge', '-script', script_path], 
                              capture_output=True, text=True, check=True)
        
        # Clean up the script file
        os.unlink(script_path)
        
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error converting {font_path}: {e}")
        print(f"FontForge output: {e.stdout if hasattr(e, 'stdout') else 'No output'}")
        print(f"FontForge error: {e.stderr if hasattr(e, 'stderr') else 'No error'}")
        return False

def main():
    # Get all .otf files in the directory
    font_files = [f for f in os.listdir(FONT_DIR) if f.endswith('.otf')]
    
    # Process each font
    for font_file in font_files:
        font_path = os.path.join(FONT_DIR, font_file)
        
        # Get the proper font name
        font_name = get_font_name(font_path)
        print(f"Processing: {font_file} -> {font_name}")
        
        # Skip if font name couldn't be determined
        if not font_name or font_name == font_file:
            print(f"  Skipping {font_file}: Could not determine proper name")
            continue
            
        # Create sanitized filename
        safe_name = sanitize_filename(font_name)
        
        # If the name doesn't include a valid filename extension, add .ttf
        if not (safe_name.lower().endswith('.ttf') or safe_name.lower().endswith('.otf')):
            safe_name += '.ttf'
            
        # Ensure the name isn't empty
        if not safe_name:
            safe_name = f"font_{font_file.replace('.otf', '.ttf')}"

        # Replace .otf with .ttf if it's still there
        safe_name = safe_name.replace('.otf', '.ttf')
            
        output_path = os.path.join(OUTPUT_DIR, safe_name)
        
        # Convert the font
        print(f"  Converting to: {output_path}")
        success = convert_font(font_path, output_path)
        
        if success:
            print(f"  Successfully converted {font_file} to {safe_name}")
        else:
            print(f"  Failed to convert {font_file}")

if __name__ == "__main__":
    main()
EOF 
