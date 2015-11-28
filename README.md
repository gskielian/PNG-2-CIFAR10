# PNG-to-CIFAR10-Format

Command line tool for converting a set of images to cifar10 binary format for training - requires imagemagick and python 2.7 PIL


1. Copy-pasta your png images into one of the class folders (e.g. dogs -> 0, cats -> 1, ... giraffes->9)
2. Change the appropriate labels in `batches.meta.txt`
3. then use: `resize-script.sh` which converts all png's to standard 32x32pixel size
4. lastly, do `python convert-images-to-cifar-format.py` to fold all the pics and categories into a single cifar-10-compatible binary, which will appear as `cifar10-ready.bin`


Use the batches.meta.txt and cifar10-ready.bin files in place of the conventional data in any standard cifar10 tutorial (reminder you may need to adjust number of categories, size of dataset, etc.)


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

