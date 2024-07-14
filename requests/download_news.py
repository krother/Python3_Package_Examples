
import requests

# Step 1: download machine-readable RDF-feed
url = "http://www.tagesschau.de/newsticker.rdf"
page = requests.get(url)
text = str(page.content)
open('newsticker.rdf', 'w').write(text)

# Step 2: parse titles and links
titel = []
for artikel in text.split('<title>'):
    t = artikel.split('</title>')[0]
    titel.append(t)

links = []
for artikel in text.split('<link>'):
    t = artikel.split('</link>')[0]
    links.append(t)

# Step 3: read articles
import time

i = 1
for url in links[20:23]:  # 3 examples only
    page = requests.get(url)
    text = str(page.content)
    open('artikel{}.html'.format(i), 'w').write(text)
    i = i + 1
    time.sleep(5)  # to prevent server from blocking!


# print titles
print('\n'.join(titel))
