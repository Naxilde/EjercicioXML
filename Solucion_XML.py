# -*- coding: utf-8 -*-
from lxml import etree
document = etree.parse("pokemon.xml")
root = document.getroot()
poke = root.xpath("//pokedex/pokemon")

tipo = root.findall("pokemon/type")
tipo_traduccion = []
for t in tipo:
  tipo_traduccion.append(t.text)

# Ejercicio 1
nombres = []
for l in tipo:
  if l.getparent().find("name").text not in nombres:
    print "\n", l.getparent().find("name").text
    nombres.append(l.getparent().find("name").text)
  print l.text

# Ejercicio 2
tipos = []
for c in tipo_traduccion:
  if c not in tipos:
    print c, tipo_traduccion.count(c)
    tipos.append(c)
    
# Ejercicio 3
