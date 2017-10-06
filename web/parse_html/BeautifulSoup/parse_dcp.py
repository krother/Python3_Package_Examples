
from bs4 import BeautifulSoup

html = open('dcp95.html').read()
soup = BeautifulSoup(html)

clubs = []
for tr in soup.find_all('tr'):
    if "\\'Grid_Top_Row" in tr.get('class', []):
        spans = tr.find_all('span')
        if len(spans) >= 2:
            club = spans[1].get_text().strip()
            clubs.append(club)

for i, c in enumerate(clubs[38:53]):
    print('%3i %30s' % (i+1, c))
print('%i records' % len(clubs))

