
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

seq1 = [ 15, 2, 4, 4, 6, 12, 3, 5, 7, 5, 1, 2, 0, 2, 3, 9, 6, 3, 1, 5]
seq2 = [ 23, 3, 4, 6, 7, 17, 5, 8, 4, 2, 2, 4, 2, 1, 4, 12, 8, 4, 2, 9]
seq3 = [ 9,  1, 2, 2, 1, 7, 2, 3, 4, 4, 0, 0, 1, 3, 1, 5, 7, 1, 2, 3]

fig = plt.figure()
ax = Axes3D(fig)
for c, zs, ys in zip(['r', 'g', 'b'], [3, 2, 1], [seq1, seq2, seq3]):
    xs = np.arange(20)
    ax.bar(xs, ys, zs, zdir='y', color=c, alpha=0.3)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
