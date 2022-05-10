
# create a hex-binned plot from randomly sampled panda pixels

import pandas as pd
import pylab as plt
from PIL import Image
import numpy as np

# read image and convert it to a numpy array
panda = np.array(Image.open('panda.png'))
panda = panda[:,:,:3].mean(axis=2)  # aggregate each color channel separately
print(panda.shape) # rows and columns

pixels = pd.DataFrame(255 - panda)

# extract dark pixels
pixels = pixels.unstack()
pixels = pixels[pixels > 0]

# select 10% of pixels
n_points = pixels.shape[0] // 10
sample = pixels.sample(n_points)

# create new table from indices
coords = sample.index.to_frame().values
df = pd.DataFrame({'x': coords[:,0], 'y': -coords[:,1], 'n': sample.values})

df.plot.hexbin(x='x', y='y', gridsize=24, cmap=plt.get_cmap('Greys'))

plt.savefig('hexpanda.png')
