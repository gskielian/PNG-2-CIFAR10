# PNG-to-CIFAR10-Format
Command line tool for converting a set of images to cifar10 binary format for training - requires imagemagick and libpng

# Usage

1. place png's inside respective classes in the `classes` directory
2. run the `resize-script.sh` to convert each of these pngs to 32x32 pixels

`./resize-script.sh`

3. run the python script to create a cifar10 binary:

`convert-images-to-cifar10-bin.py`

4. Profit$$$
