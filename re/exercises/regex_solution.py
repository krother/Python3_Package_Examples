
import re
from compare import compare

def substitution_examples():
    """Some examples of using regular expression substitution."""
    # example text
    text = "7 apples, 24 bananas, 14 carrots, and oranges are fruit"

    # replace one word by another
    result = re.sub('carrots','pears',text)
    compare(result,"7 apples, 24 bananas, 14 pears, and oranges are fruit")

    # remove all numbers
    result = re.sub('\d+ ','',text)
    compare(result,"apples, bananas, carrots, and oranges are fruit")



def search_examples():
    """Some examples of using regular expression search."""
    # example text body: tRNA structures from the PDB
    text = """
    2ow8 3.71 tRNA_Phe ribosome_(p-site)
    1b23 2.60 tRNA_Cys Ef-Tu
    1qrt 2.70 tRNA_Gln GlnRS
    1qf6 2.90 tRNA_Thr ThrRS
    1j1u 1.95 tRNA_Tyr TyrRS
    2fk6 2.90 tRNA_Thr RNase_Z
    2hgr 4.51 tRNA_Phe ribosome_(e_or_p-site)
    """

    # count frequency of the word 'tRNA'
    result = re.findall('tRNA',text)
    compare(len(result),7)

    # extract all PDB codes
    result = re.findall('\d\w\w\w',text)
    compare(result,['2ow8','1b23','1qrt','1qf6','1j1u','2fk6','2hgr'])

    # extract all aromatic amino acids
    result = re.findall('tRNA_Phe|tRNA_Tyr|tRNA_Trp',text)
    compare(result,['tRNA_Phe','tRNA_Tyr','tRNA_Phe'])

    # extract elements separated by spaces (2 middle columns)
    result = re.findall(' [^ ]+ ',text)
    compare(len(result),14)

    # extract a whole line containing key phrase 'Ef-Tu'
    result = re.findall('(\d.*Ef-Tu.*)\n',text)
    compare(result,['1b23 2.60 tRNA_Cys Ef-Tu'])


# run both examples
substitution_examples()
search_examples()
