
from pulp import *

prob = LpProblem("PULPTEST", LpMinimize)

# model variables
XCOORD = [0, 1, 2]
YCOORD = [0, 1, 2]
NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# variable is a 3 x 3 x 9 matrix of binary values
allocation = LpVariable.dicts("square", (XCOORD, YCOORD, NUMBERS), 0, 1, LpInteger)

# target function
prob += 0, "Arbitrary Objective Function"

# constraint: sum over rows
for x in XCOORD:
    prob += lpSum([n * allocation[x][y][n] for y in YCOORD for n in NUMBERS]) == 15

# constraint: sum over columns
for y in YCOORD:
    prob += lpSum([n * allocation[x][y][n] for x in XCOORD for n in NUMBERS]) == 15

# constraint: each number only once
for n in NUMBERS:
    prob += lpSum([allocation[x][y][n] for x in XCOORD for y in YCOORD]) == 1

# constraint: three numbers per column
for x in XCOORD:
    prob += lpSum([allocation[x][y][n] for y in YCOORD for n in NUMBERS]) == 3

# constraint: three numbers per row
for y in YCOORD:
    prob += lpSum([allocation[x][y][n] for x in XCOORD for n in NUMBERS]) == 3

# constraint: 9 numbers set
prob += lpSum([allocation[x][y][n] for x in XCOORD for y in YCOORD for n in NUMBERS]) == 9

# run the solver
prob.solve()

print("Status:", LpStatus[prob.status])

# print the numbers that have been found
for y in YCOORD:
    for x in XCOORD:
        for n in NUMBERS:
            if value(allocation[x][y][n]) == 1:
                print(n, end=' ')
                #print(x, y, n)
    print()
