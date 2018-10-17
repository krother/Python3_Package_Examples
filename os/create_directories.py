
# Example: create files and directories with some data

import os

cards = [str(i) for i in range(1,11)] + ["J","Q","K","A"]
colors = ["spades","hearts","clubs","diamonds"]

n = 1
for color in colors:
    # checks if the given directory does exist.
    if not os.access(color,os.F_OK) or not os.path.isdir(color):
        # create a directory.
        os.mkdir(color)
    for card in cards:
        #
        filename = color + os.sep + card + '.txt'
        # create some content for the file
        text = "%s\t%s\t%i\n"%(color,card,n)
        open(filename,'w').write(text)
        n += 1
        
        
        

