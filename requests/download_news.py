"""
Herunterladen von Artikeln
von tagesschau.de
"""

import requests

# Schritt 1:
# RDF-Newsticker herunterladen
# (leichter maschinenlesbar als Hauptseite)
url = "http://www.tagesschau.de/newsticker.rdf"
page = requests.get(url)
text = str(page.content)
open('newsticker.rdf', 'w').write(text)

# Schritt 2:
# Aus der Liste die Titel und Links auslesen
titel = []
for artikel in text.split('<title>'):
    t = artikel.split('</title>')[0]
    titel.append(t)

links = []
for artikel in text.split('<link>'):
    t = artikel.split('</link>')[0]
    links.append(t)

# Schritt 3:
# Einzelne Artikelseiten herunterladen
import time

i = 1
for url in links[20:23]:  # nur 3 Artikel als Beispiel
    page = requests.get(url)
    text = str(page.content)
    open('artikel{}.html'.format(i), 'w').write(text)  # in Datei speichern
    i = i + 1
    time.sleep(20)  # Warten, damit der Server uns nicht blockt!


# alle Artikel als Tabelle ablegen
tabelle = []
for ti, lk in zip(titel, links):
    tabelle.append([ti, lk])
print(tabelle)
