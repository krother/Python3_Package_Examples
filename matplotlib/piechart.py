
from matplotlib import pyplot as plt

nucleotides = 'G', 'C', 'A', 'U'
count = [1024, 759, 606, 398]
explode = [0.0, 0.0, 0.05, 0.05]

colors = ["#f0f0f0", "#dddddd", "#bbbbbb", "#999999"]

def get_percent(value):
    '''Formats float values in pie slices to percent.'''
    return "%4.1f%%" % (value)

plt.figure(1)
plt.title('nucleotides in 23S RNA from T.thermophilus')

plt.pie(count, explode=explode, labels=nucleotides, shadow=True,
    colors=colors, autopct=get_percent)

plt.savefig('piechart.png', dpi=150)
