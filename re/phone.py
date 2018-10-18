"""
Recognize phone numbers in Germany
"""

import re

phone = re.compile("(00|0 0|\+)\s*4\s*9[0-9 ]+")

examples = [
"0049 190 34 57 90",
"+49 190 34 57 90",
"00 00 00 49 190 34 57 90 33",
"00 49 190 34 57 90",
"0049190345790",
"+48 60 60 606 9",
"+41 55 55 55 55"
]

for e in examples:
    if phone.match(e):
        print(e, "is a German phone number")
    else:
        print(e, "is some other number")
