"""
simpe matplotlib-examples

Installation on OSX/Linux:

    sudo pip install matplotlib

On Windows:
    install Anaconda
"""

import pylab as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 22, 3]

plt.figure()
plt.plot(x, y, 'bo')
plt.savefig('plot.png', dpi=150)
plt.show()
