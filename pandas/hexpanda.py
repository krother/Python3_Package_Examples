
# create a hex-binned plot from randomly sampled panda pixels

import pandas as pd
import pylab as plt
from scipy.misc import imread


panda = imread('panda.png')
panda = panda[:,:,:3].mean(axis=2)  # aggregate color channels

pixels = pd.DataFrame(255 - panda)

# extract dark pixels
pixels = pixels.unstack()
pixels = pixels[pixels > 0]

n_points = pixels.shape[0] // 10   # 10% of pixels

sample = pixels.sample(n_points)

coords = sample.index.to_frame().values

df = pd.DataFrame({'x': coords[:,0], 'y': -coords[:,1], 'n': sample.values})

df.plot.hexbin(x='x', y='y', gridsize=24, cmap=plt.get_cmap('Greys'))

plt.savefig('hexpanda.png')
