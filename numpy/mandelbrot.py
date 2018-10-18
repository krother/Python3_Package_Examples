"""
Drawing the Mandelbrot set

based on R code by Myles Harrison
http://www.everydayanalytics.ca
"""
import numpy as np
from scipy.misc import imsave


def calculate(z, k, c):
    index = z < 2
    z[index] = z[index] ** 2 + c[index]
    k[index] = k[index] + 1
    return z, k


def draw_mandelbrot(xmin=-2, xmax=1.0, nx=500,
                    ymin=-1.5, ymax=1.5, ny=500,
                    n=100):
  x = np.linspace(xmin, xmax, nx)
  real = np.outer(x, np.ones(ny))

  y = np.linspace(ymin, ymax, ny)
  imag = 1j * np.outer(np.ones(nx), y)

  c = real + imag

  z = np.zeros((nx, ny)) * 1j
  k = np.zeros((nx, ny))
  
  for recursion in range(1, n):
      z, k = calculate(z, k, c)
  
  return k


if __name__ == '__main__':
    mtx = draw_mandelbrot()
    imsave('mandelbrot.png', mtx)
