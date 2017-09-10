
from PIL import Image, ImageDraw, ImageChops

carrot = Image.open('carrot.png')
brain = Image.open('brain.png')

carrot = carrot.resize((250, 250))

arrow = Image.new('RGBA', (250, 250), "white")
draw = ImageDraw.Draw(arrow)
draw.rectangle((0, 50, 100, 100), fill="black")
draw.polygon((100, 25, 100, 125, 150, 75), fill="black")

gradient = Image.new('RGBA', (250, 250), "white")
draw = ImageDraw.Draw(gradient)
for x in range(250):
    box = (x, 0, x+1, 250)
    color = (255, (255-x), 0)
    draw.rectangle(box, fill=color)

f1 = ImageChops.multiply(brain, carrot)
f1.save('filter1.png')

f2 = ImageChops.blend(brain, carrot, 0.2)
f2.save('filter2.png')

f3 = ImageChops.screen(carrot, gradient)
f3.save('filter3.png')
