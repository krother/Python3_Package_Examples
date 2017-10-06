
# Generate random numbers from a few distributions.

import random

print(random.randint(1,6))

print(random.random())

print(random.gauss(0.0, 1.0))


# Shuffle a list.

data = [1, 2, 3, 4]
random.shuffle(data)
print(data)
