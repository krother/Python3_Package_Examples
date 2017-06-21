
import re

text = "the quick brown fox jumps over the lazy dog"


# Search for `o` and show adjacent characters:

print(re.findall(".o.", text))


# Search for three-letter words enclosed by whitespace:

print(re.findall("\s(\wo\w)\s*", text))


# Substitute any of `dflj` by a `w`:

print(re.sub("[dflj]", "w", text))

# Check if `jumps` or `swims` occurs and return details:

print(re.search('jumps|swims', text))
