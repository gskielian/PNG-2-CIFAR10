#!/bin/bash

#simple script for resizing images in all class directories
#also reformats everything from whatever to png
for file in classes/*/*.png; do
  convert "$file" -resize 28x28\! "${file%.*}png"
  file "$file" #uncomment for testing
done

