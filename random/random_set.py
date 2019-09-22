
import random

# random set with repeats
ALPHABET = list('AGCT')
random_dna = [random.choice(ALPHABET) for i in range(50)]
print(''.join(random_dna))


# random set without repeats
NUMBERS = range(1, 101)
print(random.sample(NUMBERS, 10))
