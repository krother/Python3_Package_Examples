"""
Beispiel fuer das Lesen von Informationen aus einer HTML-Tabelle
mit Regular Expressions.

Das Programm hat noch verschiedene Optimierungsmoeglichkeiten
- letzte Ausgabezeile ignorieren
- Umlaute werden ignoriert
- Tore ebenfalls einlesen
"""

import re

text = open('spiele.html').read()

anfang = text.find('Spiel 1')
text = text[anfang:]

spiele = text.split('class="mu result"')
for spiel in spiele:
    nationen = re.findall('\<span class\=\"t\-nText "\>([a-z\-\s]+)\<\/span\>', spiel, re.IGNORECASE + re.UNICODE)
    print (nationen)





