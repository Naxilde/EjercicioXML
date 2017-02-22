# -*- coding: utf-8 -*-
from lxml import etree
document = etree.parse("pokemon.xml")
root = document.getroot()
poke = root.xpath("//pokedex/pokemon")
tipo = root.findall("pokemon/type")

lista = []
for l in tipo:
  if l.getparent().find("name").text not in lista:
    print "\n", l.getparent().find("name").text
    lista.append(l.getparent().find("name").text)
  print l.text
