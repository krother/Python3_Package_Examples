
import pandas as pd
import pylab as plt
import numpy as np
import random
from PIL import Image as im
import os

panda = im.open('panda.png')
panda = panda.convert('L')

width, height = panda.size
gmap = list(panda.getdata())
gmap = np.array(gmap)
gmap = gmap.reshape((height, width))

g = gmap - 255
g = -1 * g
p = pd.DataFrame(g)

pp = p.unstack()
pp = pp[pp > 0]

# FIXME
# convert Series to DataFrame
pp.to_csv('panda.csv')
pr = pd.read_csv('panda.csv', names=['x', 'y', 'col'])
os.remove('panda.csv')
pr['y'] *= -1


def sample(val):
    ri = random.randint(1, 1024)
    return ri <= val


pandasample = pr['col'].apply(sample)
pr = pr[pandasample]

pr.plot.hexbin(x='x', y='y', gridsize=24, cmap=plt.get_cmap('Greys'))
plt.savefig('hexpanda.svg')

# to see all different gridsizes:
# for i in range(1, 50):
#     pr.plot.hexbin(x='x', y='y', gridsize=i, cmap=plt.get_cmap('Greys'))
#     plt.savefig('hexpandas/hexpanda_{}.png'.format(i))
