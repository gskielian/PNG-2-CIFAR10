# PNG-to-CIFAR10

Super simple method for converting a set of images to cifar10 binary format for training (depends on imagemagick and python 2.7 PIL)

# Dependencies:

Use the following lines to install imagemagick and the python-imaging-library (PIL):

```bash
sudo apt-get update
sudo apt-get install imagemagick php5-imagick
pip install pillow
```

# Transform your images into a Cifar10 Binary:


1\. Copy-pasta your png images into one of the class folders, as seen in  (e.g. dogs -> 0, cats -> 1, ... giraffes->9)

2\. Change the appropriate labels in `batches.meta.txt`

3\. then use the following bash script which processes the images, rescaling all of the png's you placed in the folders the Cifar10 standard 32x32pixel size

`./resize-script.sh`

4\. lastly, run the following python script to fold all the pics and categories into a single cifar-10-compatible binary -- binary will appear as `cifar10-ready.bin`

`python convert-images-to-cifar-format.py`


# Victory!

You now have `batches.meta.txt` and `cifar10-ready.bin` files, and can replace the the conventional data in any standard cifar10 tutorial with your own data :D (reminder you may need to adjust number of categories, size of dataset, etc.)

Enjoy!

# Tree

example of where files will appear/where-to put png's:
```
.
├── batches.meta.txt
├── cifar10-ready.bin
├── convert-images-to-cifar-format.py
├── LICENSE
├── README.md
├── resize-script.sh
└── classes
    ├── 0
    │   ├── dog-pic-1.png
    │   └── dog-pic-2.png
    ├── 1
    │   ├── grumpy-cat-1.png
    │   └── grumpy-cat-2.png
    ├── 2
    │   └── placeholder.txt
    ├── 3
    │   └── placeholder.txt
    ├── 4
    │   └── placeholder.txt
    ├── 5
    │   └── placeholder.txt
    ├── 6
    │   └── placeholder.txt
    ├── 7
    │   └── placeholder.txt
    ├── 8
    │   └── placeholder.txt
    └── 9
        └── placeholder.txt
```

# batches.meta.txt

suppose you only have two categories (e.g. dogs and cats), in this case you would mod your batches.meta.txt file to read the following (assuming dogs are in '0' folder and cat png's are in '1'):

```txt
dog
cat

```
