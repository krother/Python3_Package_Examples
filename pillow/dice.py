# generate dice image

from PIL import Image
from PIL import ImageDraw

five = Image.new('RGB', (64,64), '#80b940')
d = ImageDraw.Draw(five)

d.ellipse(((26, 26), (38, 38)), '#ffffff')
d.ellipse(((10, 10), (22, 22)), '#ffffff')
d.ellipse(((42, 42), (54, 54)), '#ffffff')
d.ellipse(((10, 42), (22, 54)), '#ffffff')
d.ellipse(((42, 10), (54, 22)), '#ffffff')
five.save('five.png')
