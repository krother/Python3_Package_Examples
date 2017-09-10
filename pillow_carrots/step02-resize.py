
from PIL import Image

img = Image.new('RGBA', (800, 500), "white")

carrot = Image.open('carrot.png')
brain = Image.open('brain.png')

carrot = carrot.resize((250, 250))

img.paste(carrot, (100, 80))
img.paste(brain, (500, 100))

img.save('step02.png')

