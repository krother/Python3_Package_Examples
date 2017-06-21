
# xml

### What it is good for?

Parse XML files.

The `xml` module contains several XML parsers. They produce a tree of DOM objects for each tag that can be searched and allow access to attributes.

### Installed with Python by default

yes

### Example

Sample XML data:

    <?xml version="1.0" encoding="UTF-8" ?>
    <actor_list>
    <actor name="Hamlet">the Prince of Denmark</actor>
    <actor name="Polonius">Ophelias father</actor>
    </actor_list>

Read an XML file and extract content from tags:

    from xml.dom.minidom import parse

    document = parse('hamlet.xml')

    actors = document.getElementsByTagName("actor")
    for act in actors:
        name = act.getAttribute('name')
        for node in act.childNodes:
            if node.nodeType == node.TEXT_NODE:
                print("{} - {}".format(name, node.data))

    Hamlet - the Prince of Denmark
    Polonius - Ophelias father


### Where to learn more?

[https://docs.python.org/3/library/xml.html](https://docs.python.org/3/library/xml.html)
