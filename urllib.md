
# urllib

### What it is good for?

Retrieving webpages.

`urllib` sends HTTP requests to web pages and allows you to read their content similar to files. Parameters can be passed as part of the URL like in a browser if the website is using the HTTP GET protocol.
(For forms using(HTTP POST) you need something different (Python example with ~5 lines)

### Installed with Python by default

yes

### Example

Read the homepage of the author.

    >>> from urllib import request, parse
    >>> term = "hemoglobin"
    >>> url = 'http://www.academis.eu'
    >>> req = request.urlopen(url)
    >>> page = req.read()
    >>> print(len(page))


### Where to learn more?

[https://docs.python.org/3/library/zipfile.html](https://docs.python.org/3/library/zipfile.html)
