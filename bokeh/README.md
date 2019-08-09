
# Bokeh

### What it is good for?

Creating diagrams for the web.

Bokeh creates interactive and non-interactive diagrams that can be displayed as web pages (or parts thereof). Of course, plots can also be saved as images. Compared to `matplotlib`, Bokeh is not as mature yet, but shows many interesting features already

### Installed with Python by default

no

### Installed with Anaconda

no

### How to install it?

    pip install bokeh

### Example

Plot a simple line plot, write it to a HTML file:

    >>> from bokeh.plotting import figure, output_file, show

    >>> x = [1, 2, 3, 4, 5]
    >>> y = [6, 7, 2, 4, 5]

    >>> output_file("lines.html", title="line plot example")

    >>> p = figure(title="simple line example", x_axis_label='x', y_axis_label='y')
    >>> p.line(x, y, legend="Temp.", line_width=2)

Display the results in a web browser:

    >>> show(p)

### Where to learn more?

[http://bokeh.pydata.org](http://bokeh.pydata.org)
