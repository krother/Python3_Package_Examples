
from matplotlib import pyplot as plt
import math

plt.figure()

x = [0.01 * i for i in range(1000)]
y = [math.sin(j) for j in x]

plt.plot(x, y, 'k-', linewidth=1)
plt.text(5, 0, "$y = sin(x)$", horizontalalignment='center', fontsize=20)
plt.axis([0, 3*math.pi, -1.2, 1.2])

plt.savefig('sinfunc.png')
