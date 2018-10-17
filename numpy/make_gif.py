
import imageio

PATH = 'vortex/'
images = []

for i in range(15):
    images.append(imageio.imread(PATH + 'vortex_0.png'))

for i in range(0, 361, 3):
    filename = 'vortex_{}.png'.format(i)
    images.append(imageio.imread(PATH + filename))

imageio.mimsave('vortex.gif', images, fps=20)
