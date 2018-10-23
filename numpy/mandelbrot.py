"""
Drawing the Mandelbrot set
based on R code by Myles Harrison
http://www.everydayanalytics.ca
"""
import numpy as np
from scipy.misc import imshow


SIZE = 500

x = np.linspace(-2.0, 1.0, SIZE)
y = np.linspace(-1.5, 1.5, SIZE)

ones = np.ones(SIZE)

c = np.outer(x, ones) + 1j * np.outer(ones, y)

z = np.zeros((SIZE, SIZE)) * 1j
k = np.zeros((SIZE, SIZE))

for i in range(100):
    index = z < 2
    z[index] = z[index] ** 2 + c[index]
    k[index] = k[index] + 1

imshow(k)
