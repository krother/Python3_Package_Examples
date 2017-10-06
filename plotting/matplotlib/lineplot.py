from pylab import *
from random import random

x_data = [x for x in range(50)]
y_data = [x + 10 for x in x_data]
noisy_y_data = [x + random()*10+5 for x in x_data]

figure()
curve1 = plot(x_data, y_data, 'k-',  label = 'without noise')
curve2 = plot(x_data, noisy_y_data, 'r--',  label = 'with noise')
# also try: 'k:', 'bs' , 'ro', 'g^', 'gv'

title('Noise on a linear function')
xlabel('x values')
ylabel('linear function')
legend(loc='lower right')
axis([10,40,0,60])
# print help(xlabel) for more information

savefig('lineplot.png')

