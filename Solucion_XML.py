# -*- coding: utf-8 -*-
from lxml import etree
document = etree.parse("pokemon.xml")
root = document.getroot()
poke = root.xpath("//pokedex/pokemon")
tipo = root.findall("pokemon/type")

for l in tipo:
  print l.getparent().find("name").text, l.text, "\n"
