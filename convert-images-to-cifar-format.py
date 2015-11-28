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

	    ###########################
	    #get image into byte array#
	    ###########################

	    # create array of bytes to hold stuff

	    #first append the class_name byte
	    data.append(class_name)

	    #then write the rows
	    #Extract RGB from pixels and append
	    #note: first we get red channel, then green then blue
	    #note: no delimeters, just append for all images in the set
	    for color in range(0,3):
		for x in range(0,32):
		    for y in range(0,32):
			data.append(pix[x,y][color])


############################################
#write all to binary, all set for cifar10!!#
############################################

output_file = open('cifar10-ready.bin', 'wb')
data.tofile(output_file)
output_file.close()


