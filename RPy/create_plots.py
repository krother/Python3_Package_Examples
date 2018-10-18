from rpy import r

# first plot
x = range(1,11)
y = [i**2 for i in x]

r.plot(x, y, xlab='x', ylab='y', main='My first plot',
      pch=21, col='blue', bg='lightblue', type='o') 


# second plot
x = range(1,11)
y = [i**2 for i in x]
z = [i**3 for i in x]
r.plot(x, y, main='My second plot', xlab='x', ylab='y', type='l', col='blue')
r.lines(x, z, col='red') 

# cosine function, save to file
import math
r.png('cosine.png')
x = r.seq(0,50, by=0.1)
y = [math.cos(i) for i in x]
r.plot(x, y, main='COS(X)', xlab='x', ylab='cos(x)', type='l', col='blue')
r.dev_off() 

# histogram
x = range(10) + range(3,6) + range(5,10)
r.hist(x, main='A histogram', xlab='x', col='lightblue') 

# adust plotting area
from rpy import r
x = range(1,11)
y = [i**2 for i in x]
z = [i**3 for i in x]
r.plot(x, y, main='My second plot', xlab='x', ylab='y', type='l',
       col='blue', ylim=r.range(y,z))
r.lines(x, z, col='red') 
