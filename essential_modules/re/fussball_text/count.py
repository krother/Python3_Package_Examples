"""
Das Modul re erlaubt in Strings auch nach komplexen Mustern zu suchen.

Das Muster unten ist definiert als:
- ein oder mehrere Buchstaben 
- gefolgt von einem Zeichen, welches kein Buchstabe ist 
- gib die laengsten gefundenen Buchstabenfolgen aus (runde Klammer)
- ignoriere Gross-/Kleinschreibung
"""
import re

text = open('deutschland_wm.txt').read()

wort = re.compile('([a-z]+)[^a-z]', re.IGNORECASE + re.UNICODE)

matches = wort.findall(text)
print (matches[:50])

print ("\nDer Text enthaelt %5i Woerter.\n"%(len(matches)))


