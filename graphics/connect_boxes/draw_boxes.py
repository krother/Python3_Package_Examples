
from PIL import Image, ImageDraw


pics = [
    "gold_box.png",
    "green_box.png",
    "green_box.png",
    "purple_box.png",
    "gold_box.png"
    ]

# Create an empty image
graph = Image.new('RGB', (700, 200), (255,255,255))

draw_tool = ImageDraw.Draw(graph)

x = 50
for filename in pics:
    print(filename)
    box = Image.open(filename, 'r')
    graph.paste(box, (x, 50))
    x = x + box.size[0]

draw_tool.line(((50, 100),(650, 100)), fill=(0,0,0),width=3)

# Write the image to disk
graph.save('graph.png')
