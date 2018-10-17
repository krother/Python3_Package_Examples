import re

text = "7 apples, 24 bananas, 14 carrots, and oranges are fruit"

# replace one word by another
result = re.sub('','',text)
assert result == "7 apples, 24 bananas, 14 pears, and oranges are fruit"

# remove all numbers
result = re.sub('','',text)
assert result == "apples, bananas, carrots, and oranges are fruit"
