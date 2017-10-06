
from PIL import Image, ImageDraw, ImageChops, ImageFont

img = Image.new('RGBA', (800, 500), "white")

# load starting bitmaps
carrot = Image.open('carrot.png')
brain = Image.open('brain.png')

carrot = carrot.resize((250, 250))

# draw an arrow
arrow = Image.new('RGBA', (250, 250), "white")
draw = ImageDraw.Draw(arrow)
draw.rectangle((0, 50, 100, 100), fill="black")
draw.polygon((100, 25, 100, 125, 150, 75), fill="black")

# add gradient to arrow
gradient = Image.new('RGBA', (250, 250), "white")
draw = ImageDraw.Draw(gradient)
for x in range(250):
        box = (x, 0, x+1, 250)
        color = (255, (255-x), 0)
        draw.rectangle(box, fill=color)

arrow = ImageChops.screen(arrow, gradient)

# combine all component images
img.paste(carrot, (100, 80))
img.paste(arrow, (325, 150))
img.paste(brain, (500, 100))

# add text
draw = ImageDraw.Draw(img)
arial = ImageFont.truetype('arial.ttf', 40)
draw.text((220,360),"Carrots rock your brain!",fill=(0,0,0),font=arial)

img.save('step07_final.png')

