import re

def compare(got, expected):
    """Checks if the two parameters match, and prints a message."""
    if got != expected:print "\n'%s'\nwas found instead of \n'%s'"%(str(got),str(expected))
    else:print "OK"

text = "7 apples, 24 bananas, 14 carrots, and oranges are fruit"

# replace one word by another
result = re.sub('carrots','pears',text)
compare(result,"7 apples, 24 bananas, 14 pears, and oranges are fruit")

# remove all numbers
result = re.sub('\d+\s','',text)
compare(result,"apples, bananas, carrots, and oranges are fruit")
