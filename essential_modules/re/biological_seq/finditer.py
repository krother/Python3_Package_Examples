'''

Pattern Matching - Example

The script checks if the SRC_HUMAN sequence has 
the following phosphorylation site: 'R(.)[ST][^P]' and prints 
the match, the start and end of the match and the
amino acid in the second position of the match.

'''

import re

F = open('SRC_HUMAN.fasta')
seq = ''	
for line in F:
	if line[0] != '>':
		seq = seq + line.strip()

S = 'R(.)[ST][^P]'
regexp = re.compile(S)
iter = regexp.finditer(seq)
for s in iter:
     print("match:", s.group(0))
     print("start, end", s.span())
     print("aa in second position:", s.group(1))
