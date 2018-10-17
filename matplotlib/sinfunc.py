
from pylab import *
import math

figure()

x = [0.01 * i for i in range(1000)]
y = [math.sin(j) for j in x]

plot(x, y, 'k-', linewidth=1)
text(5, 0, "$y = sin(x)$", horizontalalignment='center', fontsize=20)
axis([0, 3*math.pi, -1.2, 1.2])

savefig('sinfunc.png')

