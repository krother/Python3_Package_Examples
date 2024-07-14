import textract # modul zum extrahieren von text aus pdf datein
import re # reguläre ausdrücke
import operator # hilfe beim sortieren nach value

# text aus pdf extrahieren
text = textract.process("skript_101.pdf", encoding="utf-8")
# bytestring zu utf-8 dekodieren
text = text.decode('utf-8')

# zeilen am newline character "\n" splitten
lines = text.split('\n')

titleIndex = 0 # dokumententitel
authorIndex = 1 # dokumentenautorin
dropIndex = [3,4] # müll

title = lines[titleIndex]
author = lines[authorIndex]

# überschriften + unnötige lines im skript löschen
counter = 0
for i in drop_index:
    del lines[i-counter]
    counter += 1
del lines[authorIndex]
del lines[titleIndex]

# funktion um herauszufinden welcher teil vom skript einem sprecher zuzuordnen ist
def isName(str):
    if str:
        if len(str.split(' ')) == 1 and \
        str[0].isupper() and \
        str[-1:].isalpha():
            return True
    return False

# zeilen für jeden sprecher in ein dictionary einsortieren
speakerText = dict()
for i, l in enumerate(lines):
    if isName(l):
        name = l
        text = ""
        counter = 2
        # suche nach zusätzlichen zeilen
        tmp = lines[i+counter] # potentielle neue zeile
        while tmp: # tmp ist nicht leer
            if counter > 2: # neue zeile gefunden
                text += " " # trennen mit leerzeichen
            text += tmp # zeilen kombinieren
            counter += 1 # zähler erhöhen
            tmp = lines[i+counter] # tmp updaten
        if not text: # text ist leer
            continue # nächste zeile
        if name in speakerText: # key (name des sprechers) vorhanden
            speakerText[name].append(text) # array anfügen
        else: # key unbekannt
            speakerText[name] = [text] # neues array mit text

# für jeden sprecher die worthäufigkeit zählen
speakerWordCount = dict()
for name, lines in speakerText.items():
    wordCount = dict()
    for l in lines: # für jede zeile
        # ignoriere alle satzzeichen, finde wörter
        words = re.findall("[A-Za-z\[\]äöüß]+", l.lower())
        for w in words:
            if w in wordCount: # key vorhanden
                wordCount[w] += 1
            else: # key unbekannt
                wordCount[w] = 1
    speakerWordCount[name] = wordCount

# wortanzahl pro sprecher
speakerCount = dict()
for name in wordFrequency:
    total = 0
    for key,value in wordFrequency[name].items():
        total += value # summiere worthäufigkeit
    speakerCount[name] = total

# sortierte wortzahl
sorted(speakerCount.items(), key=operator.itemgetter(1),reverse=True)

# justus häufigste wörter
sorted(wordFrequency["Justus"].items(), key=operator.itemgetter(1),reverse=True)

# peters häufigste wörter
sorted(wordFrequency["Peter"].items(), key=operator.itemgetter(1),reverse=True)

# bobs häufigste wörter
sorted(wordFrequency["Bob"].items(), key=operator.itemgetter(1),reverse=True)


