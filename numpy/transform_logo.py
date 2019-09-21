#
# more examples that transform the Python logo
#

from scipy.ndimage import imread, rotate
from scipy.misc import imsave
import numpy as np


a = imread('python_logo.png', mode='RGB')

# dim
d = a // 2
imsave('dim.png', d)


b = a[:,::-1,:]
imsave('flip.png', b)

g = np.array(a)
g[:,:,1] = 0
imsave('purple.png', g)

# rotation
c = rotate(a, 30, reshape=False)
c[c == 0] = 255
imsave('rotate.png', c)

# displacement blur
blur = np.array(a, np.int32)
factor = np.array([8], np.int32)

blur[5:,:] += a[:-5,:] * factor
blur[:,5:] += a[:,:-5] * factor
blur[:-5,:] += a[5:,:] * factor
blur[:,:-5] += a[:,5:] * factor
blur //= 33
imsave('blur.png', blur)

# rolling displacement
roll = np.array(a)
roll[:,:,2] = np.roll(roll[:,:,2], 25)
roll[:,:,1] = np.roll(roll[:,:,1], 50)
imsave('roll.png', roll)


from numpy.random import randint

rr = randint(0, 10, (200, 200, 3))
rr = a * rr // 10
imsave('rand.png', rr)

spaced = np.array(a, np.int64)
spaced[::3,::3,:] *= rr[::3,::3,:]
spaced[::3,::3,:] //= 10
imsave('spaced.png', spaced)


s = np.array(a)
s[75:,75:,0] = 0
s[:125,:125,1] = 0
s[:125,75:,2] = 0
imsave('square.png', s)

# circle
xx, yy = np.mgrid[:200, :200]
imsave('meshx.png', xx)
imsave('meshy.png', yy)

# circles contains the squared distance to the (100, 100) point
circle = (xx - 100) ** 2 + (yy - 100) ** 2
imsave('circle.png', circle // 100)

# apply circle to logo
g = np.array(a, np.int64)
g[:,:,0] *= circle
g[:,:,1] *= circle
g[:,:,2] *= circle
imsave('logocircle.png', g // 20000)

# donuts contains 1's and 0's organized in a donut shape
# you apply 2 thresholds on circle to define the shape
donut = np.logical_and(circle < (4000 + 500), circle > (4000 - 500))
g = np.array(a, np.int64)
mask = 1 - donut.astype(np.int64)
imsave('mask.png', mask)

g[:,:,0] *= mask
g[:,:,1] *= mask
g[:,:,2] *= mask
imsave('masked.png', g)
