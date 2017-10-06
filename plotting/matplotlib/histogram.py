
from pylab import figure, title, xlabel, ylabel, \
                  hist, grid, savefig
from random import gauss

def make_histo(data, n_bins, fn):
    figure()
    num, bins, patches = hist(data, n_bins, normed=1.0, histtype='bar', \
                              facecolor='green', alpha=0.75)
    title('Histogram')
    xlabel('value')
    ylabel('frequency')
    grid(True)
    savefig(fn)


data = [gauss(100, 20) for i in range(1000)]

make_histo(data, 20, 'histogram.png')
