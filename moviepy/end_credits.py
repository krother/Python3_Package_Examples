
import gizeh as gz
import moviepy.editor as mpy
from moviepy.editor import ImageClip, CompositeVideoClip
from faker import Factory

W, H = 1200, 1000

DURATION = 25 # seconds

LEFTCOL = 450
RIGHTCOL = 490
TEXTSIZE = 28
LINE_HEIGHT = 50

SCROLLSPEED = 130
BOTTOM_START = H * 1.2

N_NAMES = 30

# load image that does not move at all
LOGO_POS = 950, 300
LOGO_SIZE = 235, 298
LOGO = ImageClip("panda.png").resize(LOGO_SIZE).set_pos(LOGO_POS)
LOGO.duration = DURATION


# create fake text
fake = Factory.create()
text = []
while len(text) < N_NAMES:
    job = fake.job()
    name = fake.name()
    if len(job) < 25:
        text.append((job, name))


def make_frame(t):
    """Draw text elements in each frame"""
    surface = gz.Surface(W, H, bg_color=(0,0,0))
    for i, line in enumerate(text):
        job, name = line
        ypos = LINE_HEIGHT * i - int(t * SCROLLSPEED) + BOTTOM_START
        
        txt = gz.text(job, "Amiri", TEXTSIZE, fontweight='bold', \
                      h_align='right', fill=(1,1,1))
        left = gz.Group([txt]).translate((LEFTCOL, ypos))
        left.draw(surface)
        txt = gz.text(name, "Amiri", TEXTSIZE, \
                      fontweight='normal',h_align='left', fill=(1,1,1))
        right = gz.Group([txt]).translate((RIGHTCOL, ypos))
        right.draw(surface)
    return surface.get_npimage()


clip = mpy.VideoClip(make_frame, duration=DURATION)

# mix text and logo together
final = CompositeVideoClip([clip, LOGO])
final.subclip(0, DURATION).write_videofile("abspann.avi", codec="h264", fps=24) 
#final.subclip(0, DURATION).write_videofile("abspann.mp4", codec="mpeg4", fps=24) 
