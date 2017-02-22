# -*- coding: utf-8 -*-
from lxml import etree
document = etree.parse("pokemon.xml")
root = doc.getroot()
poke = raiz.xpath("//pokedex/pokemon")
for type in poke:
  print type.find("type").text 
