
# itertools

### What it is good for?

Functions to work with lists and iterators.

Most functions in this module return *iterators*, so you can use their result once or convert it to a list.

### Installed with Python by default

yes

### Example

Concatenate a list:

    >>> import itertools
    >>> ch = itertools.chain([1,2],[3,4])
    >>> list(ch)
    [1, 2, 3, 4]

    >>> list(itertools.repeat([1,2], 3))
    [[1, 2], [1, 2], [1, 2]]

Permutations and combinations of list elements:

    >>> p = itertools.permutations([1,2,3])
    >>> list(p)
    [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

    >>> c = itertools.combinations([1,2,3], 2)
    >>> list(c)
    [(1, 2), (1, 3), (2, 3)]

### Where to learn more?

[https://docs.python.org/3/library/itertools.html](https://docs.python.org/3/library/itertools.html)
