
# matplotlib

### What it is good for?

Plotting diagrams.

`matplotlib` is capable of producing static images of all common types of diagrams in print quality: line plots, scatter plots, bar charts, pie charts, histograms, heat maps etc. 

### Installed with Anaconda

yes

### How to install it:

    pip install matplotlib

### Example

Plot a square function:

    >>> from pylab import *

    >>> x = list(range(-10, 10))
    >>> y = [xval**2 for xval in x]
    >>> figure()
    >>> plot(x, y, 'bo') # blue circles
    >>> title('square function')
    >>> xlabel('x')
    >>> ylabel('$x^2$')
    >>> savefig('plot.png')

![output from matplotlib](matplotlib_output.png)

### Where to learn more?

[http://matplotlib.org/](http://matplotlib.org/)
