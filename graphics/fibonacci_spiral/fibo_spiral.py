
import turtle

a = 1
b = 1

depth = 0
maxdepth = 15

while depth < maxdepth:
    turtle.circle(a, 90)
    a, b = b, a + b
    depth += 1

input()
