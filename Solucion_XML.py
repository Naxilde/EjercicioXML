# -*- coding: utf-8 -*-
from lxml import etree
document = etree.parse("pokemon.xml")
root = document.getroot()
poke = root.xpath("//pokedex/pokemon")
tipo = root.findall("pokemon/type")

nombres = []
for l in tipo:
  if l.getparent().find("name").text not in nombres:
    print "\n", l.getparent().find("name").text
    nombres.append(l.getparent().find("name").text)
  print l.text

tipos = []
for c in tipo:
  contador = 0
  if c.text not in tipos:
    print "\n", c.text
    tipos.append(c.text)
