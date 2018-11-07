
from matplotlib import pyplot as plt
from random import random

x_data = [x for x in range(50)]
y_data = [x + 10 for x in x_data]
noisy_y_data = [x + random()*10+5 for x in x_data]

plt.figure()
curve1 = plt.plot(x_data, y_data, 'k-',  label = 'without noise')
curve2 = plt.plot(x_data, noisy_y_data, 'r--',  label = 'with noise')
# also try: 'k:', 'bs' , 'ro', 'g^', 'gv'

plt.title('Noise on a linear function')
plt.xlabel('x values')
plt.ylabel('linear function')
plt.legend(loc='lower right')
plt.axis([10,40,0,60])

plt.savefig('lineplot.png')
