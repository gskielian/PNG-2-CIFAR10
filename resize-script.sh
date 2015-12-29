#!/bin/bash

#simple script for resizing images in all class directories
#also reformats everything from whatever to png

if [ `ls classes/*/*.jpg 2> /dev/null | wc -l ` -gt 0 ]; then
  for file in classes/*/*.jpg; do
    convert "$file" -resize 32x32\! "${file%.*}.png"
    file "$file" #uncomment for testing
    rm "$file"
  done
fi

if [ `ls classes/*/*.png 2> /dev/null | wc -l ` -gt 0 ]; then
  for file in classes/*/*.png; do
    convert "$file" -resize 32x32\! "${file%.*}.png"
    file "$file" #uncomment for testing
  done
fi
