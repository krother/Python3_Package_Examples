
# random weighted choice
# based on cookbook 4.21

#TODO: compare with KRs implementation

import random

elements = ["A","G","C","U"]
odds = [3,3,1,1]

def picker(ele, odds):
    table = [z for x,y in zip(ele,odds) for z in [x]*y]
    while True:
        yield random.choice(table)
        #DOES NOT WORK FOR NON-INTEGER ODDS!

rna = picker(elements, odds)
print ''.join([rna.next() for i in range(50)])
