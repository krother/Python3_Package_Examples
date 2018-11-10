import numpy as np
import matplotlib.pyplot as plt
from skimage.transform import PiecewiseAffineTransform, warp
from imageio import imread, imsave

image = imread('datascience_course_planning/logos/bayesian_basil.png')

rows, cols = image.shape[0], image.shape[1]

src_cols = np.linspace(0, cols, 20)
src_rows = np.linspace(0, rows, 10)
src_rows, src_cols = np.meshgrid(src_rows, src_cols)
src = np.dstack([src_cols.flat, src_rows.flat])[0]

# add sinusoidal oscillation to row coordinates
FRAMES = 50
for i in range(0, FRAMES):
    ofs = i/FRAMES * 2 * np.pi

    dst_rows = src[:, 1] - np.sin(np.linspace(ofs + 0, ofs+3 * np.pi, src.shape[0])) * 50
    dst_cols = src[:, 0]
    dst_rows *= 1.5
    dst_rows -= 1.5 * 50
    dst = np.vstack([dst_cols, dst_rows]).T

    tform = PiecewiseAffineTransform()
    tform.estimate(src, dst)

    out_rows = image.shape[0] - 1.5 * 50
    out_cols = cols
    out = warp(image, tform, output_shape=(out_rows, out_cols))

    imsave(f'wave/out{i}.png', out)



import imageio
import os

f = []
for fn in os.listdir('wave'):
    fn = 'wave/' + fn
    f.append(imageio.imread(fn))

imageio.mimsave('output.gif', f, fps=20)
