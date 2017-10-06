
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random


NPIECES = 25  # 16
EDGEWIDTH = 16  # 25
VEC_GROWTH = 1.020  # 1.03
PHASE1_FRAMES = 250
PHASE2_FRAMES = 100


def create_pieces(filename):
    """
    Takes a picture and dissects it into NPIECES**2
    smaller images
    """
    flower = Image.open(filename, 'r')
    flower = flower.resize((NPIECES * EDGEWIDTH, NPIECES * EDGEWIDTH))

    pieces = []
    positions = []
    for x in range(NPIECES):
        for y in range(NPIECES):
            copy = flower.copy()
            piece = copy.crop((x * EDGEWIDTH, y * EDGEWIDTH,
                              (x + 1) * EDGEWIDTH, (y + 1) * EDGEWIDTH))
            pieces.append(piece)
            positions.append((x * EDGEWIDTH, y * EDGEWIDTH))
    return pieces, positions


def increment():
    """Returns a random number from +-0.1 .. 1.1"""
    inc = random.random() + 0.1
    if random.random() > 0.5:
        return -inc
    return inc


def randvec():
    """Returns a random (x, y) vector"""
    return increment(), increment()


def create_image(pieces, positions):
    """Assembles all small pieces to a big image"""
    img = Image.new("RGB", (NPIECES * EDGEWIDTH, NPIECES * EDGEWIDTH))
    for pc, pos in zip(pieces, positions):
        img.paste(pc, pos)
    return img


def move_pieces(positions, vectors):
    """modifies positions of images"""
    new_pos = []
    for pos, vec in zip(positions, vectors):
        new_pos.append((pos[0] + int(vec[0]), pos[1] + int(vec[1])))
    return new_pos
    # TODO: this would be much easier with pandas!!!


def increase_vectors(vectors):
    """accelerate so that pieces move faster in earlier frames"""
    new_vecs = []
    for vec in vectors:
        new_vecs.append((vec[0]*VEC_GROWTH, vec[1]*VEC_GROWTH))
    return new_vecs


if __name__ == '__main__':
    pcs, pos = create_pieces('flower.jpg')
    vecs = [randvec() for i in pos]

    # writing standstill frames at the end.
    img = create_image(pcs, pos)
    for iframe in range(PHASE1_FRAMES, PHASE1_FRAMES + PHASE2_FRAMES):
        img.save('out/frame_{:04d}.png'.format(iframe))

    # writing gradually dissipating frames
    for iframe in range(PHASE1_FRAMES, 0, -1):
        img = create_image(pcs, pos)
        img.save('out/frame_{:04d}.png'.format(iframe))
        pos = move_pieces(pos, vecs)
        vecs = increase_vectors(vecs)
