
# numpy

### What it is good for?

numpy makes it easy to work with matrices in Python.

Because it is implemented in C, `numpy` accelerates many calculations. It is also type-safe - all elements of a matrix have the same type. Many of the most powerful Python libraries like `pandas`, `scikit-learn` and `PILLOW` have been built on top of numpy.

### Pre-installed on Anaconda?

yes

### How to install it?

    pip install numpy

### Example

Creating a 4 x 2 matrix and adding 10 to each element

	>>> import numpy as np
	>>> vector = np.array([[0, 1, 2, 3], [4, 5, 6, 7]])
	>>> print(vector + 10)
    [[10 11 12 13]
     [14 15 16 17]]
	>>> print(vector.shape)
    (2, 4)

### Where to learn more?

[http://www.numpy.org/](http://www.numpy.org/)

