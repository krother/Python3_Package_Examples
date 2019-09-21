# requires pip install array2gif

from scipy.ndimage import imread, rotate
from scipy.misc import imsave
import numpy as np

a = imread('python_logo.png', mode='RGB')

# circles containing the squared distance to the (100, 100) point
xx, yy = np.mgrid[:200, :200]
circle = (xx - 100) ** 2 + (yy - 100) ** 2


# create masks
bounds = [0, 800, 2000, 3200, 5000, 6500, 9000, 10500, 13000, 16000, 40000]
masks = [None]
for i in range(1, 10):
    donut = np.logical_and(circle < bounds[i], circle >= bounds[i - 1])
    masks.append(donut.astype(np.int64))

# calculate 360 frames
for iframe in range(361):
    vortex = np.zeros_like(a, np.int64)
    for i in range(1, 10):
        rot = rotate(a, i * iframe, reshape=False)
        g = np.array(rot, np.int64)
        g[:, :, 0] *= masks[i]
        g[:, :, 1] *= masks[i]
        g[:, :, 2] *= masks[i]
        vortex += g

    vortex[vortex == 0] = 255  # cover black dots
    imsave('vortex/vortex_{}.png'.format(iframe), vortex)

#
# create an animated GIF
#
import imageio

PATH = 'vortex/'
images = []

for i in range(15):
    images.append(imageio.imread(PATH + 'vortex_0.png'))

for i in range(0, 361, 3):
    filename = 'vortex_{}.png'.format(i)
    images.append(imageio.imread(PATH + filename))

imageio.mimsave('vortex.gif', images, fps=20)
