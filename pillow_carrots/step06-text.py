
from PIL import Image, ImageDraw, ImageChops, ImageFont

img = Image.new('RGBA', (800, 500), "white")

carrot = Image.open('carrot.png')
brain = Image.open('brain.png')

carrot = carrot.resize((250, 250))

arrow = Image.open('arrow.png')
gradient = Image.open('gradient.png')

arrow = ImageChops.screen(arrow, gradient)
    
img.paste(carrot, (100, 80))
img.paste(arrow, (325, 150))
img.paste(brain, (500, 100))

draw = ImageDraw.Draw(img)
arial = ImageFont.truetype('arial.ttf', 40)
draw.text((220, 360), "Carrots rock your brain!", fill=(0,0,0), font=arial)

img.save('step06.png')

