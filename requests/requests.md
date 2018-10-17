
# requests

### What it is good for?

Retrieving webpages.

`requests` sends HTTP requests to web pages and allows you to read their content. Most standard tasks are a lot easier compared to the standard module `urllib`. `requests` can sending data to web forms via HTTP GET and POST, submit files and manage cookies. 


### Installed with Python by default

no

### Installed with Anaconda

yes

### Example

Read the homepage of the author.

    import requests
    
    r = requests.get('http://www.academis.eu')
    print(r.text)

Search scientific articles on PubMed:

    url = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    param_dict = {'db':'pubmed', 'term':'escherichia', 'rettype':'uilist'}

    r = requests.get(url, params=param_dict)
    print(r.text)


### Where to learn more?

[http://docs.python-requests.org/en/latest/index.html](http://docs.python-requests.org/en/latest/index.html)
