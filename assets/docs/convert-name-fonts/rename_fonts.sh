#!/bin/bash

# Source and destination directories
SRC_DIR="/Users/seanivore/Development/voice-mkt-sfa/assets/fonts"
DEST_DIR="/Users/seanivore/Development/voice-mkt-sfa/assets/web-fonts"

# Create the destination directory if it doesn't exist
mkdir -p "$DEST_DIR"

# Function to determine font family from filename
get_font_family() {
  local filename="$1"
  # Extract the numeric part without the dot prefix and .otf suffix
  local num=${filename:1} # Remove the leading dot
  num=${num%.otf}        # Remove the .otf extension
  
  # Extract first two digits
  local prefix=${num:0:2}
  
  # Simple if/else instead of associative array
  if [ "$prefix" = "17" ] || [ "$prefix" = "40" ]; then
    echo "Sans"
  elif [ "$prefix" = "46" ]; then
    echo "Display"
  elif [ "$prefix" = "49" ]; then
    echo "Narrow"
  elif [ "$prefix" = "25" ] || [ "$prefix" = "44" ]; then
    echo "Pro"
  elif [ "$prefix" = "51" ]; then
    echo "Bifur"
  elif [ "$prefix" = "30" ]; then
    echo "Text"
  elif [ "$prefix" = "50" ]; then
    echo "Script"
  elif [ "$prefix" = "29" ]; then
    echo "Tall"
  elif [ "$prefix" = "37" ]; then
    echo "Donne"
  elif [ "$prefix" = "41" ]; then
    echo "Solid"
  elif [ "$prefix" = "43" ]; then
    echo "Auster"
  elif [ "$prefix" = "27" ]; then
    echo "Antiquarian"
  else
    echo "Font"
  fi
}

# Process each font file
counter=1
for font in "$SRC_DIR"/*.otf; do
  if [ -f "$font" ]; then
    filename=$(basename "$font")
    family=$(get_font_family "$filename")
    
    # Generate a new name
    new_name="${family}-${counter}.otf"
    
    # Copy to the destination
    cp "$font" "$DEST_DIR/$new_name"
    echo "Copied $filename to $new_name"
    
    # Increment counter
    counter=$((counter + 1))
  fi
done

# Generate TTF versions (using cp for now since fontforge had issues)
for font in "$DEST_DIR"/*.otf; do
  if [ -f "$font" ]; then
    ttf_name="${font%.otf}.ttf"
    cp "$font" "$ttf_name"
    echo "Created TTF (copied) version: $(basename "$ttf_name")"
  fi
done

echo "Finished processing fonts. Total copied: $((counter-1))"
EOF 
