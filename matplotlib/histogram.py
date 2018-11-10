
from matplotlib import pyplot as plt
from random import gauss

data = [gauss(100, 20) for i in range(1000)]

plt.figure()
plt.hist(data, 20, normed=1.0, histtype='bar', \
         facecolor='green', alpha=0.75)
plt.title('Histogram')
plt.xlabel('value')
plt.ylabel('frequency')
plt.grid(True)
plt.savefig('histogram.png')
