
# adapted from Cookbook 8.3

import random


# random set with repeats
ALPHABET = ["A","G","C","U"]
random_bases = [random.choice(ALPHABET) for i in range(50)]
random_seq = ''.join(random_bases)
print random_seq


# random set without repeats (Cookbook 8.4)
NUMBERS = range(1,101)
print random.sample(NUMBERS, 10)

    
