
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np 


def func(x, a, b):
    """parabolic function"""
    return a * x**2 + b


# create noisy X/Y data
x = np.linspace(-10, 10, 100)
y = func(x, 1, 5)
ynoise = y + 20 * np.random.laplace(size=len(x))

# fit the parameters of the function with noisy data:
params, pcov = curve_fit(func, x , ynoise)
yfit = func(x, params[0], params[1])

# plot the outcome:
fig = plt.figure
plt.plot(x, yfit, "k-")
plt.plot(x, ynoise, "bx")
plt.savefig('fit.png')
