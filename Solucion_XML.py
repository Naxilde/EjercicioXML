# -*- coding: utf-8 -*-
from lxml import etree
document = etree.parse("pokemon.xml")
root = document.getroot()
poke = root.xpath("//pokedex/pokemon")

tipo = root.findall("pokemon/type")
for i in tipo:
  if i.getparent().find("nombre").text
  print i.getparent().find("name").text
  print i.text
