#!/usr/bin/env python3
import os
import shutil

# Directory with the renamed web fonts
WEB_FONTS_DIR = '/Users/seanivore/Development/voice-mkt-sfa/assets/web-fonts'

# Process each OTF file in the web-fonts directory
for file in os.listdir(WEB_FONTS_DIR):
    if file.endswith('.otf'):
        otf_path = os.path.join(WEB_FONTS_DIR, file)
        ttf_path = os.path.join(WEB_FONTS_DIR, file.replace('.otf', '.ttf'))
        
        # Create a copy with .ttf extension
        shutil.copy2(otf_path, ttf_path)
        print(f"Created TTF copy: {os.path.basename(ttf_path)}")

print("Done creating TTF versions (note: these are just copies with .ttf extension)")
EOF 
