"""
Run a query on http://www.genesilico.pl/rnapathwaysdb
"""
import requests


"""
Part 1: 
Fill all fields in the search form.
You find it in the page source in a 
section looking like this:

<form action="/rnapathwaysdb/search/keyword/" method="post">
  <br/><br/>
  <input name="query" size="8"/>
  <br/><br/>
  <input type="submit" value="Search" class="default"/>
</form>
"""

url = "http://www.genesilico.pl/rnapathwaysdb/search/keyword/"
form_values = {'query': 'trna'}

response = requests.post(url, form_values)
print(response)  # if you see "200", the website returned something

html = response.text  # contents of the result page
open('search_result.html', 'w').write(html)
# you can open the result in a browser now


"""
Part 2: 
parse the 'pathway' names from the html page.
Here we use string functions 
and regular expressions.
"""
import re

start = html.find('<b>Pathway</b>')
end = html.find('<b>EnzymaticComplex</b>')  # section after pathways
print(start, end)  # -1 means section not found

# isolate pathway list
pathways = html[start:end]

# extract pathway titles
results = re.findall('<a href=".+">(.+)</a><br />', pathways)

print("\npathways found:\n")
for r in results:
    print(r)
