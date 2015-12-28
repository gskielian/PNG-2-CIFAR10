#python script for converting 32x32 pngs to format

from PIL import Image
import os
from array import *

data = array('B')

for dirname, dirnames, filenames in os.walk('./classes'):
    for filename in filenames:
        if filename.endswith('.png'):

            ################
            #grab the image#
            ################

            im = Image.open(os.path.join(dirname, filename))
            pix = im.load()
            #print(os.path.join(dirname, filename))

            #store the class name from look at path
            class_name = int(os.path.join(dirname).split('/')[-1])
            #print class_name




            ###############################
            #        MNIST Fork           #
            #getting image into byte array#
            ###############################

            # create array of bytes to hold stuff
            data.append(0x0803) # magic number for training images
            data.append(0x0002) # two images
            data.append(0x001C) # number of rows 28
            data.append(0x001C) # number of columnns 28

            # create array of bytes to hold stuff
            data.append(0x0801) # magic number for training labels
            data.append(0x0002) # two images
            data.append(0x001C) # number of rows 28
            data.append(0x001C) # number of columnns 28

            #first append the class_name byte
            data.append(class_name)

            #then write the rows

            #Pixels are organized row-wise. Pixel values are 0 to 255. 0 means background (white), 255 means foreground (black).

            #note: rows then columns
            #note: no delimters, just grayscale images left right, top down
            #note: each pixel is one byte each
            #note: each label is also one byte each
            for color in range(0,3):
                for x in range(0,28):
                    for y in range(0,28):
                        data.append(pix[x,y][color])


############################################
#write all to binary, all set for cifar10!!#
############################################

output_file = open('cifar10-ready.bin', 'wb')
data.tofile(output_file)
output_file.close()


