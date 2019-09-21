

# Define a square function; create noisy X/Y data using `numpy`:

def func(x, a, b):
    return a * x**2 + b

import numpy as np 

x = np.linspace(-10, 10, 100)
y = func(x, 1, 5)
ynoise = y + 20 * np.random.laplace(size=len(x))


# Fit the parameters of the function with noisy data:

from scipy.optimize import curve_fit

params, pcov = curve_fit(func, x , ynoise)
yfit = func(x, params[0], params[1])


# Plot the outcome:

import matplotlib.pyplot as plt

fig = plt.figure
plt.plot(x, yfit, "k-")
plt.plot(x, ynoise, "bx")
plt.savefig('fit.png')
