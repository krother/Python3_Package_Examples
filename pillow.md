
# PILLOW

### What it is good for?

Image manipulation.

`PILLOW` is the inofficial successor to the **Python Imaging Library (`PIL`)**. It facilitates creating, cutting and applying various filters to pixel-based images.

### Installed with Python by default

no

### Installed with Anaconda

yes

### How to install it?

    pip install pillow

### Example

Convert all `.png` images in the directory to half their size.

    >>> from PIL import Image
    >>> import os

    >>> for filename in os.listdir('.'):
    ...     if filename.endswith('.png'):
    ...         im = Image.open(filename)
    ...         x = im.size[0] // 2
    ...         y = im.size[1] // 2
    ...         small = im.resize((x, y))
    ...         small.save('sm_' + filename)


### Where to learn more?

[https://pillow.readthedocs.org](https://pillow.readthedocs.org)
