from lxml import etree
import sys

poteri=dict()

for event, element in etree.iterparse("/home/ilich/Progetti/litprojects/DedPowers2/sven.dnd4e",tag="Power"):
    name = element.get('name').strip()
    tipo = element.getchildren()[0].text.strip()
    azione = element.getchildren()[1].text.strip()
    poteri[name]={'tipo':tipo, 'azione':azione}
        
print poteri
