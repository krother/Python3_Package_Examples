import numpy as np
import matplotlib.pyplot as plt
from skimage.transform import PiecewiseAffineTransform, warp
from imageio import imread, imsave

image = imread('python_logo.png')

rows, cols = image.shape[0], image.shape[1]

src_cols = np.linspace(0, cols, 20)
src_rows = np.linspace(0, rows, 10)
src_rows, src_cols = np.meshgrid(src_rows, src_cols)
src = np.dstack([src_cols.flat, src_rows.flat])[0]

# add sinusoidal oscillation to row coordinates
FRAMES = 20
for i in range(0, FRAMES):
    amplitude = 15
    phase = i / FRAMES * 2 * np.pi

    dst_rows = src[:, 1] - np.sin(np.linspace(phase, phase + 3 * np.pi, src.shape[0])) * amplitude
    dst_cols = src[:, 0]
    dst_rows *= 1.5
    dst_rows -= 1.5 * 50
    dst = np.vstack([dst_cols, dst_rows]).T

    tform = PiecewiseAffineTransform()
    tform.estimate(src, dst)

    out = warp(image, tform, output_shape=(rows, cols))
    imsave(f'wave/out{i:03d}.png', out)


# create animated GIF
import imageio
import os

f = []
for fn in sorted(os.listdir('wave')):
    fn = 'wave/' + fn
    f.append(imageio.imread(fn))

imageio.mimsave('output.gif', f, fps=20)
