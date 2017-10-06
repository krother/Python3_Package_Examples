
# Example: browse files.

"""
The program goes through all directories
and finds all cards with numbers dividable by 5.

"""

import os

for dirname in os.listdir('.'):
    if os.path.isdir(dirname):
        for fn in os.listdir(dirname):
            # read the file
            filename = dirname + os.sep + fn
            color, card, number = open(filename).read().strip().split()
            if int(number)%5 == 0:
                print color,card
