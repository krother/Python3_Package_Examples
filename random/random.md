
# random

### What it is good for?

Generate random numbers.

`random` contains generators for the most common distributions.

### Installed with Python by default

yes

## Example

### Creating random integers

One most wanted function is to create random integers in a given range:

    dice = random.randint(1,6)

### Creating random floats

The `random()` functin generates float numbers between 0 and 1:

    import random
    print random.random()

### Generate random numbers from a few distributions.

    import random

    random.randint(1,6)

    random.random()

    random.gauss(0.0, 1.0)

### Shuffle a list

    data = [1, 2, 3, 4]
    random.shuffle(data)

### Creating random lists

Random combinations of elements with repetition:

    from random import choice

    bases = ['A','C','G','T']
    dna = [choice(bases) for i in range(20)]
    print ''.join(dna)

When elements are to be picked without repetition, you would use, the `sample` function:

    from random import sample
    
    flavors = ['vanilla','banana','mint']
    icecream = sample(flavors, 2)


### Where to learn more?

[https://docs.python.org/3/library/random.html](https://docs.python.org/3/library/random.html)


