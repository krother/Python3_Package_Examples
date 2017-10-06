
# generate a random sequence with weighted probabilities

import random
import time

weights = [
    ('A',4.0),
    ('U',4.0),
    ('G',1.0),
    ('C',1.0)
    ]

def random_char():
    # calculate cumulative weights
    cumul_sum = 0.0
    cweights = []
    for char,w in weights:
        cumul_sum += w
        cweights.append((char,cumul_sum))
    # create a number
    rand = random.random()*cumul_sum
    for char, cweight in cweights:
        if rand < cweight:
            return char

def random_char_gen():
    # calculate cumulative weights
    cumul_sum = 0.0
    cweights = []
    for char,w in weights:
        cumul_sum += w
        cweights.append((char,cumul_sum))
    # generate numbers
    while True:
        rand = random.random()*cumul_sum
        for char, cweight in cweights:
            if rand < cweight:
                yield char


bef = time.time()
num = [random_char() for i in range(5000000)]
print time.time()-bef

bef = time.time()
gen = random_char_gen()
num = [gen.next() for i in range(5000000)]
print time.time()-bef


