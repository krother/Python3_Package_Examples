
from pylab import plot, figure, savefig


x = range(10)
y = [xx ** 2 for xx in x]

figure()
plot (x, y)
savefig('function.png')
