
from PIL import Image, ImageDraw

def angle(base_pos):
    return base_pos * 360 / 4361

TET = angle(88), angle(1276)
AMP = angle(3293), angle(4153)
ORI = angle(2519), angle(3133)

pBR322 = Image.new('RGB', (500,500), 'white')
BOX_OUTER = (50, 50, 450, 450)
BOX_INNER = (80, 80, 420, 420)
d = ImageDraw.Draw(pBR322)

d.pieslice(BOX_OUTER, 0, 360, fill='gray')
d.arc(BOX_OUTER, 0, 360, fill='black')

d.pieslice(BOX_OUTER, TET[0], TET[1], fill='lightblue', outline='blue')
d.pieslice(BOX_OUTER, AMP[0], AMP[1], fill='yellow', outline='orange')
d.pieslice(BOX_OUTER, ORI[0], ORI[1], fill='magenta', outline='darkmagenta')

d.pieslice(BOX_INNER, 0, 360, fill='white')

d.arc(BOX_INNER, 0, 360, fill='black')
d.arc(BOX_INNER, TET[0], TET[1], fill='blue')
d.arc(BOX_INNER, AMP[0], AMP[1], fill='orange')
d.arc(BOX_INNER, ORI[0], ORI[1], fill='darkmagenta')

pBR322.save('plasmid_pBR322.png')

# adding a restriction site
import math

def coord(angle, center, radius):
    rad = math.radians(angle) 
    x = int(center[0] + math.cos(rad) * radius)
    y = int(center[1] + math.sin(rad) * radius)
    return x, y

ECOR1 = angle(4359)
point1 = coord(ECOR1, (250, 250), 170)
point2 = coord(ECOR1, (250, 250), 200)
d.line((point1, point2), fill='black',width=3)

pBR322.save('plasmid_pBR322_rest.png')

# text
#arial16 = ImageFont.truetype('arial.ttf',16)
d.text((90,155),"gold", fill=(0,0,0)) #,font=arial16)
pBR322.save('plasmid_pBR322_text.png')

# arrow tips
point1 = coord(TET[1]+10, (250, 250), 185)
point2 = coord(TET[1], (250, 250), 160)
point3 = coord(TET[1], (250, 250), 210)
d.polygon((point1, point2, point3), fill='lightblue', outline='blue')

point1 = coord(AMP[0]-10, (250, 250), 185)
point2 = coord(AMP[0], (250, 250), 160)
point3 = coord(AMP[0], (250, 250), 210)
d.polygon((point1, point2, point3), fill='yellow', outline='orange')

point1 = coord(ORI[0]-10, (250, 250), 185)
point2 = coord(ORI[0], (250, 250), 160)
point3 = coord(ORI[0], (250, 250), 210)
d.polygon((point1, point2, point3), fill='magenta', outline='darkmagenta')

pBR322.save('plasmid_pBR322_arrows.png')
