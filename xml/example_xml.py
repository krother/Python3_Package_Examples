
# Create sample XML data

open('hamlet.xml', 'w').write("""<?xml version="1.0" encoding="UTF-8" ?>
<actor_list>
<actor name="Hamlet">the Prince of Denmark</actor>
<actor name="Polonius">Ophelias father</actor>
</actor_list>""")


# Read an XML file and extract content from tags:

from xml.dom.minidom import parse

document = parse('hamlet.xml')

actors = document.getElementsByTagName("actor")
for act in actors:
    name = act.getAttribute('name')
    for node in act.childNodes:
        if node.nodeType == node.TEXT_NODE:
            print("{} - {}".format(name, node.data))
