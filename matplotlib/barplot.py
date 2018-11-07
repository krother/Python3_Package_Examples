
from matplotlib import pyplot as plt

nucleotides = ["A", "G", "C", "U"]

counts = [
    [606, 1024, 759, 398],
    [762, 912, 639, 591],
    ]

plt.figure()

x1 = [2.0, 4.0, 6.0, 8.0]
x2 = [x - 0.5 for x in x1]

plt.xticks(x1, nucleotides)

plt.bar(x1, counts[1], width=0.5, color="#cccccc", label="E.coli 23S")
plt.bar(x2, counts[0], width=0.5, color="#808080", label="T.thermophilus 23S")

plt.legend()
plt.axis([1.0, 9.0, 0, 1200])

plt.title('RNA nucleotides in the ribosome')
plt.xlabel('RNA')
plt.ylabel('base count')
plt.savefig('barplot.png')
