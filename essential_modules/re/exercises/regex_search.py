
# Exercise: Regular expression search
#
# Find the right regular expressions that find something in the text.
#
# 1. Replace the 'regex' in the code
# 2. Run the program to see whether it works.
# 3. As soon as it does, uncomment the next example.

import re

text = """
2ow8 3.71 tRNA_Phe ribosome_(p-site)
1b23 2.60 tRNA_Cys Ef-Tu
1qrt 2.70 tRNA_Gln GlnRS
1qf6 2.90 tRNA_Thr ThrRS
1j1u 1.95 tRNA_Tyr TyrRS
2fk6 2.90 tRNA_Thr RNase_Z
2hgr 4.51 tRNA_Phe ribosome_(e_or_p-site)
"""

# find all words 'tRNA'
result = re.findall('regex',text)
assert len(result) == 7

# extract all PDB codes
#result = re.findall('regex',text)
# assert result == ['2ow8','1b23','1qrt','1qf6','1j1u','2fk6','2hgr']

# extract all aromatic amino acids
#result = re.findall('regex',text)
# assertt result == ['tRNA_Phe','tRNA_Tyr','tRNA_Phe']

# extract elements flanked by spaces on the left and right (2 middle columns)
# result = re.findall('regex',text)
# assertt len(result) == 14

# extract a whole line containing key phrase 'Ef-Tu'
# result = re.findall('regex',text)
# assertt result == ['1b23 2.60 tRNA_Cys Ef-Tu']
