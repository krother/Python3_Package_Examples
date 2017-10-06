import re

pattern = ' s.*? s'
text = "The sixth sick sheikh's sixth sheep's sick."

matches = re.findall(pattern, text)
print(matches)
