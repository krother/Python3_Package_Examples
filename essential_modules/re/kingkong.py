"""
Advanced example:
Why is humpty-dumpty not matched?
"""

import re

text = """
ping-pong
king-kong
flip-flop
hip-hop
humpty-dumpty
"""

for line in text.split():
    if re.search(r"^(\w+)i(\w+)[- ]\1o\2", line):
        print(line)
