
# coding: utf-8

# # Bricks
# *a linear optimization problem solved with PuLP*

# ## Problem Description
# 
# We want to place a series of colored bricks in a N x M box
# 
# ![Bricks](bricks.png)

# The bricks need to be placed according the following rules:
# 
# * all bricks with the same colour should end up in the same column
# * if this is not possible, the rightmost column of one colour should be filled up first
# * bricks of one colour should be as close to each other on the x-axis as possible
# 
# A possible solution could look like this:
# 
# ![solution](bricks_solution.png)
# 
# This notebook shows how to solve this problem using the **linear equation solver PuLP**.

# ## Preparations
# 
# First, we define the bricks and their colours in Python:

# In[1]:

bricks = ['a1', 'a2', 'a3', 'b1', 'b2', 'c1', 'c2', 'c3', 'c4', 'd1', 'd2', 'e1']


# We also define the size of the box to stack bricks in. A list of positions will help us later.

# In[2]:

XSIZE = 4
YSIZE = 3
positions = [(x,y) for x in range(XSIZE) for y in range(YSIZE)]


# ## Modeling a Linear Equation System
# To model our problem using **PuLP**, we need to perform four steps:
# 
# 1. Define the model variables
# 2. Define the optimization function
# 3. Add linear constraints
# 4. Run the solver
# 

# ### Step 1: Define the model variables
# 
# Our model variable will be a binary matrix with four dimensions. The first two dimensions are quite obvious: each space in the box has its own **x, y** position in the matrix. The third dimension are the bricks **b** themselves. We use them to specify, which brick occupies a certain space. 
# 
# The fourth dimension is probably the least obvious: It is the column **rb** in which bricks of one colour should be placed. We use it to link bricks of the same colour together.

# In[3]:

from pulp import *

v = LpVariable.dicts("bricks", (range(XSIZE), range(YSIZE), bricks, range(XSIZE)),                      lowBound = 0, upBound = 1, cat = LpInteger)


# #### Why don't we simply assign each brick a number instead of an extra dimension?
# Yes, it would be nice to cut out an extra dimension from the matrix. However, we cannot discretisize numbers in a linear equation system (e.g. say *"If x is 3 do this, if x is 4 do something else"*). I find this quite a strong limitation, and the binary matrix is the proper way to say *"I have discrete bricks a, b, c.. in my system".*.
# 
# #### I don't understand why range(XSIZE) appears twice.
# Each brick has two X values assigned: the first is the column **x** in which the brick actually is, the second is the rightmost column **rb** in which bricks of this colour should gather. We need this second value to implement the second and third rule above.

# ### Step 2: Define the Optimization Function
# 
# We first tell PuLP that we have something to minimize:

# We want to tell PuLP to minimize the distance bricks have from their colleagues to the right. For that, we need to construct a penalty matrix first. We say that any block in column *x* that ought to be in colum *rb* has a penalty of `10` for each column in between:

# In[4]:

m = LpProblem("Bricks", LpMinimize)


# In[5]:

penalties = {}
for x in range(XSIZE):
    for rb in range(XSIZE):
        penalties[(x, rb)] = 10 * abs(rb - x)
penalties


# In a linear equation system, everything needs to be composed of terms like `a*x` that are added together. This is why you will see **sum** symbols frequently. Our minimization function *m* is:
# 
# $$m(v) = \sum_{x,y,b,rb}penalties_{x,rb} * v_{x,y,n,rb}$$ 
# 
# In PuLP, this minimization function is formulated as a sum with a scary-looking list comprehension:

# In[6]:

m += lpSum([penalties[(x,rb)] * v[x][y][b][rb] for x,y in positions for b in bricks for rb in range(XSIZE)])


# ### Step 3: Adding linear constraints
# Now we specify additional rules and conditions. We need to formulate these in the linear form as well. More sums, that is.
# 
# #### Condition 1: One brick per position
# First, we want to specify that there can be only one brick per position. In math notation this is:
# 
# $$\sum_{b,rb} v_{x,y,b,rb} <= 1$$
# 
# This condition must be true for each possible **x** and **y** value.
# 
# In Python, it looks similar if you are familiar with **list comprehensions**.

# In[7]:

for x, y in positions:
        m += lpSum([v[x][y][b][rb] for b in bricks for rb in range(XSIZE)]) <= 1


# #### Condition 2: One position per brick
# Likewise, each brick can have only one position. This should be obvious, but given the binary matrix we still have to say it explicitly:

# In[8]:

for b in bricks:
    m += lpSum([v[x][y][b][rb] for x, y in positions for rb in range(XSIZE)]) == 1


# #### Condition 3: no bricks right of the rb column
# We want to implement the column **rb** (our fourth dimension) as a hard boundary. So no bricks should appear right of it. Hopefully this results in bricks stackin up in the **rb** column, and those left over left of it.
# 
# We do this by adding a constraint that certain columns need to be zero.

# In[9]:

for x in range(XSIZE):
    for rb in range(XSIZE):
        if x > rb:
            m += lpSum([v[x][y][b][rb] for y in range(YSIZE) for b in bricks]) == 0


# The art of formulating a linear problem with PuLP is to know, when to put a for loop into the sum (corresponding to an index in a sum symbol) or outside (corresponding to having multiple sums).

# #### Condition 4: bricks of same colour stick together
# This was the tough one while developing the example. We tell our equation system that any two bricks of the same colour must have the same right boundary **rb**. This way, we enforce that the same penalties in the minimization apply to one colour.
# 
# For the implementation, we need to add a separate constraint for each pair of bricks. For each pair and rb value, the corresponding values in **v** are either both 1 or both 0, which we can check by calculating their difference:

# In[10]:

pairs = [('a1', 'a2'), ('a1', 'a3'), ('a2', 'a3'), 
         ('b1', 'b2'),
         ('c1', 'c2'), ('c1', 'c3'), ('c2', 'c3'), ('c1', 'c4'), ('c2', 'c4'), ('c3', 'c4'),
         ('d1', 'd2')
        ]

for b1, b2 in pairs:
    for rb in range(XSIZE):
        m += lpSum([v[x][y][b1][rb] for x,y in positions] + [-v[x][y][b2][rb] for x,y in positions]) == 0


# #### Remark
# You might realize two things from this:
# * If you were to implement this as an algorithm, it would be **much easier**. But in a linear system it is not
# * The number of constraints explodes if you have more bricks or a bigger box. The complexity is something like $O(b^2 * x)$, which certainly is bad news.

# ### Step 4: Run the Solver
# Finally we can ask PuLP to solve the problem:

# In[11]:

m.solve()
print("Status:", LpStatus[m.status])


# ## Display the result
# Lets see whether it really worked:

# In[12]:

for y in range(YSIZE):
    row = ""
    for x in range(XSIZE):
        for b in bricks:
            for rb in range(XSIZE):
                val = value(v[x][y][b][rb])
                if val == 1:
                    row += '{}[{}]'.format(b, rb)
        row += '\t'
    print(row)


# Which is one of the possible solutions.

# In[ ]:



