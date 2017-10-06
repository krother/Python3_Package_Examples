
# random

### What it is good for?

Generate random numbers.

`random` contains generators for the most common distributions.

### Installed with Python by default

yes

### Example

Generate random numbers from a few distributions.

    import random

    print(random.randint(1,6))
    
    5

    print(random.random())

    0.9553636591673604

    print(random.gauss(0.0, 1.0))

    1.284988658685204

Shuffle a list.

    data = [1, 2, 3, 4]
    random.shuffle(data)
    print(data)

    [3, 2, 4, 1]

### Where to learn more?

[https://docs.python.org/3/library/random.html](https://docs.python.org/3/library/random.html)
