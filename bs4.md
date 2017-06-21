
# BeautifulSoup

### What it is good for?

Parsing HTML pages.

Beautiful soup is much, much easier to use than the default HTML parser installed with Python.

### Installed with Python by default

no

### Installed with Anaconda

no

### How to install it?

    pip install bs4

### Example

Parsing list items out of a HTML document:

    from bs4 import BeautifulSoup

    html = """<html><head></head><body>
    <h1>Hamlet</h1>
    <ul class="cast"> 
      <li>Hamlet</li>
      <li>Polonius</li>
      <li>Ophelia</li>
      <li>Claudius</li>
    </ul>
    </body></html"""

    soup = BeautifulSoup(html, "lxml")

    for ul in soup.find_all('ul'):
        if "cast" in ul.get('class', []):
            for item in ul.find_all('li'):
                print(item.get_text(), end=", ")


### Where to learn more?

[http://www.crummy.com/software/BeautifulSoup/bs4/doc/](http://www.crummy.com/software/BeautifulSoup/bs4/doc/)
