#python script for converting 32x32 pngs to format
from PIL import Image
import os

im = Image.open("output.png") #Can be many different formats.
pix = im.load()
print im.size #Get the width and hight of the image for iterating over
print pix[0,0] #Get the RGBA Value of the a pixel of an image
print pix[0,1] #Get the RGBA Value of the a pixel of an image
print pix[0,2] #Get the RGBA Value of the a pixel of an image
print pix[0,3] #Get the RGBA Value of the a pixel of an image

for fn in os.listdir('./classes/1/'):
     if os.path.isfile(fn):
        print (fn)

with open ('test.png', 'wb') as f:
    f.write(b'Hi There')
    f.write(b'Hi There')


