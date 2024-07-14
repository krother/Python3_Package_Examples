#
# more examples that transform the Python logo
#

import numpy as np
from PIL import Image


def imsave(filename, a):
    Image.fromarray(a).convert('RGB').save(filename)

im = Image.open('python_logo.png')
a = np.array(im)


# reduce brightness
d = a // 2
imsave('dim.png', d)

# flip over
b = a[:,::-1,:]
imsave('flip.png', b)

# remove color channel
g = np.array(a)
g[:,:,1] = 0
imsave('purple.png', g)

# rolling displacement
roll = np.array(a)
roll[:,:,2] = np.roll(roll[:,:,2], 25)
roll[:,:,1] = np.roll(roll[:,:,1], 50)
imsave('roll.png', roll)
