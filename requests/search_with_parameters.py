
import requests

# Search scientific articles on PubMed:
url = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
param_dict = {'db':'pubmed', 'term':'escherichia', 'rettype':'uilist'}

r = requests.get(url, params=param_dict)
print(r.text)
