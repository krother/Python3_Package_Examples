
from PIL import Image, ImageDraw, ImageChops

img = Image.new('RGBA', (800, 500), "white")

carrot = Image.open('carrot.png')
brain = Image.open('brain.png')

carrot = carrot.resize((250, 250))

arrow = Image.new('RGBA', (250, 250), "white")
draw = ImageDraw.Draw(arrow)
draw.rectangle((0, 50, 100, 100), fill="black")
draw.polygon((100, 25, 100, 125, 150, 75), fill="black")
arrow.save('arrow.png')

gradient = Image.new('RGBA', (250, 250), "white")
draw = ImageDraw.Draw(gradient)
for x in range(250):
    box = (x, 0, x+1, 250)
    color = (255, (255-x), 0)
    draw.rectangle(box, fill=color)
gradient.save('gradient.png')

arrow = ImageChops.screen(arrow, gradient)
arrow.save('grad_arrow.png')

img.paste(carrot, (100, 80))
img.paste(arrow, (325, 150))
img.paste(brain, (500, 100))

img.save('step04.png')

