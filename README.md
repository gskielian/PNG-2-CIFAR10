# PNG-to-CIFAR10-Format
Command line tool for converting a set of images to cifar10 binary format for training - requires imagemagick and python 2.7 PIL

# Usage

1\. place png's inside respective classes in the `classes` directory

2\. run the following to convert each of these pngs (must be in their class directory) to 32x32 pixels

`./resize-script.sh`

3\. run the python script to create one, big, cifar10 binary:

`convert-images-to-cifar10-bin.py`

4\. $$$Profit$$$
