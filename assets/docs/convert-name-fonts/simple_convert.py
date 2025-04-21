#!/usr/bin/env python3
import os
import subprocess
import shutil

# Directory containing the fonts
FONT_DIR = '/Users/seanivore/Development/voice-mkt-sfa/assets/fonts'

# Directory for web-ready fonts
OUTPUT_DIR = '/Users/seanivore/Development/voice-mkt-sfa/assets/web-fonts'

# Create the output directory if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Define common font types based on font numbers
FONT_TYPES = {
    # Sans serif fonts
    '17': 'Sans',
    '40': 'Sans',
    # Display fonts
    '46': 'Display',
    # Narrow fonts
    '49': 'Narrow', 
    # Pro fonts
    '25': 'Pro',
    '44': 'Pro',
    # Bifur fonts
    '51': 'Bifur',
    # Text fonts
    '30': 'Text',
    # Script fonts
    '50': 'Script',
    # Misc fonts
    '29': 'Tall',
    '37': 'Donne',
    '41': 'Solid',
    '43': 'Auster',
    '27': 'Antiquarian',
}

def main():
    # Get all .otf files in the directory
    font_files = [f for f in os.listdir(FONT_DIR) if f.endswith('.otf')]
    
    # Track processed font names to handle duplicates
    processed_names = set()
    
    # Process each font
    for i, font_file in enumerate(font_files, 1):
        font_path = os.path.join(FONT_DIR, font_file)
        
        print(f"[{i}/{len(font_files)}] Processing: {font_file}")
        
        # Determine a font name from the file number
        file_number = font_file.lstrip('.').split('.')[0]
        prefix = file_number[:2] if len(file_number) >= 2 else file_number
        
        font_name = FONT_TYPES.get(prefix, 'Font')
        safe_name = f"{font_name}-{file_number}.ttf"
            
        # Handle duplicates by adding a counter
        original_safe_name = safe_name
        counter = 1
        while safe_name in processed_names:
            name_parts = original_safe_name.rsplit('.', 1)
            safe_name = f"{name_parts[0]}-{counter}.{name_parts[1]}"
            counter += 1
        
        processed_names.add(safe_name)
        output_path = os.path.join(OUTPUT_DIR, safe_name)
        
        # Convert from .otf to .ttf using FontForge's command line interface
        cmd = ['fontforge', '-c', f'Open("{font_path}"); Generate("{output_path}"); Close();']
        
        try:
            subprocess.run(cmd, check=True, capture_output=True, text=True)
            print(f"  Successfully converted {font_file} to {safe_name}")
        except subprocess.CalledProcessError as e:
            print(f"  Failed to convert {font_file}: {e}")
            print(f"  Error details: {e.stderr}")

if __name__ == "__main__":
    main()
EOF 
