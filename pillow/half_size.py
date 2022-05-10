
# Convert all `.png` images in the directory to half their size
from PIL import Image
import os

for filename in os.listdir('.'):
    if filename.endswith('.png'):
        im = Image.open(filename)
        x = im.size[0] // 2
        y = im.size[1] // 2
        small = im.resize((x, y))
        small.save('sm_' + filename)
