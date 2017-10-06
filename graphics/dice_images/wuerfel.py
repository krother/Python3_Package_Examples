"""
Generiert Bilder von Wuerfelseiten
"""

from PIL import Image
from PIL import ImageDraw

w = Image.new('RGB', (64,64), '#80b940')

blank = w.copy()
blank.save('blank.png')

d = ImageDraw.Draw(w)

d.ellipse(((26, 26), (38, 38)), '#ffffff')
eins = w.copy()
eins.save('eins.png')

d.ellipse(((10, 10), (22, 22)), '#ffffff')
d.ellipse(((42, 42), (54, 54)), '#ffffff')
drei = w.copy()
drei.save('drei.png')

d.ellipse(((10, 42), (22, 54)), '#ffffff')
d.ellipse(((42, 10), (54, 22)), '#ffffff')
fuenf = w.copy()
fuenf.save('fuenf.png')

d.ellipse(((26, 26), (38, 38)), '#80b940')
vier = w.copy()
vier.save('vier.png')

d.ellipse(((10, 42), (22, 54)), '#80b940')
d.ellipse(((42, 10), (54, 22)), '#80b940')
zwei = w.copy()
zwei.save('zwei.png')

d.ellipse(((10, 42), (22, 54)), '#ffffff')
d.ellipse(((42, 10), (54, 22)), '#ffffff')
d.ellipse(((26, 10), (38, 22)), '#ffffff')
d.ellipse(((26, 42), (38, 54)), '#ffffff')
sechs = w.copy()
sechs.save('sechs.png')

w = Image.new('RGB', (64*6,64), '#80b940')
w.paste(eins, box=(64 * 0, 0))
w.paste(zwei, box=(64 * 1, 0))
w.paste(drei, box=(64 * 2, 0))
w.paste(vier, box=(64 * 3, 0))
w.paste(fuenf, box=(64 * 4, 0))
w.paste(sechs, box=(64 * 5, 0))
w.save('wuerfel.png')
