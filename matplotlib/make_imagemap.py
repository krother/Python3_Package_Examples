
from matplotlib import pyplot as plt
import sys
import random

plt.figure()

name = 'imap'

# make some fake data
xs = range(15)
ys = [random.choice(xs) for i in range(len(xs))]

# create a plot
fig, = plt.plot(xs, ys, 'ro-')
dpi = fig.figure.get_dpi()
height = fig.figure.get_figheight() * dpi

# save figure
plt.savefig(name + '.png', dpi=dpi) # dpi is needed!

# convert the x,y coords into image coords.
xys = list(zip(xs, ys))
transform = fig.get_transform()
icoords = transform.transform(xys)
i

# Create a HTML image map
template = """
<html><head></head><body>
<img src="%s.png" usemap="#points" border="0">
<map name="points">%s</map>
</body></html>"""

# change this as needed, e.g. if not plotting points.
fmt = "<area shape='circle' coords='%i,%i,5' href='http://example.com/%i/%i' >"

fmts = []
for (ix, iy), (x, y) in zip(icoords, xys):
    fmts.append(fmt % (ix, height-iy, x, y) )
image_map = "\n".join(fmts)

html_page = template%(name, image_map)


# save HTML file
outfile = open(name + ".html", 'w')
outfile.write(html_page)
