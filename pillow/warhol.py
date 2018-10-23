
# example: create Andy-Warhol like images

from PIL import Image, ImageDraw

pylogo = Image.open("python_logo.png")
print(pylogo.size)

r, g, b, a = pylogo.split()

pylogo1 = Image.merge("RGB", (b, g, r))
pylogo2 = Image.merge("RGB", (r, b, g))
pylogo3 = Image.merge("RGB", (g, b, r))
pylogo4 = Image.merge("RGB", (g, r, b))

collage = Image.new("RGBA",(600,600), "#FFFFFF")

collage.paste(pylogo1,(58,58))
collage.paste(pylogo2,(354,58))
collage.paste(pylogo3,(58,354))
collage.paste(pylogo4,(354,354))

draw_tool = ImageDraw.Draw(collage)
draw_tool.line(((5, 5),(595, 5)), fill=(0,0,0),width=5)
draw_tool.line(((595, 5),(595, 595)), fill=(0,0,0),width=5)
draw_tool.line(((5, 5),(5, 595)), fill=(0,0,0),width=5)
draw_tool.line(((5, 595),(595, 595)), fill=(0,0,0),width=5)
draw_tool.line(((300, 5),(300, 595)), fill=(0,0,0),width=5)
draw_tool.line(((5, 300),(595, 300)), fill=(0,0,0),width=5)

collage.save('pylogo_warhol.png')
collage.show()
