#!/bin/bash

#simple script for resizing images in all class directories
for file in classes/*/*.png; do
  convert "$file" -resize 32x32\! "$file"
  file "$file" #uncomment for testing
done

