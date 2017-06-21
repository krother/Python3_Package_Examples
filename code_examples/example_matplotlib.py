
# Plot a square function:

from pylab import *

x = list(range(-10, 10))
y = [xval**2 for xval in x]
figure()
plot(x, y, 'bo') # blue circles
title('square function')
xlabel('x')
ylabel('$x^2$')
savefig('plot.png')
