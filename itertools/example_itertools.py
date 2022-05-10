
import itertools

# concatenate lists
ch = itertools.chain([1, 2], [3, 4])
print(list(ch))

# repeat lists
print(list(itertools.repeat([1, 2], 3)))


# Permutations and combinations of list elements:
p = itertools.permutations([1, 2, 3])
print(list(p))

c = itertools.combinations([1, 2, 3], 2)
print(list(c))


# Pairwise combinations
pr = itertools.product([1, 2, 3], [4, 5])
print(list(pr))
