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
pes_min=float(raw_input("Introduce el peso mínimo: "))
pes_max=float(raw_input("Introduce el peso máximo: "))
for p in poke:
  if float(p.find("weight").text) >= pes_min and float(p.find("weight").text) <= pes_max:
    print p.find("name").text
    
# Ejercicio 4
evoluciones = root.findall("pokemon/evolutions/evolution/name")
busqueda = raw_input("Nombre del pokemon a buscar: ")

filtro_evol = []
for b in evoluciones:
  if b.getparent().getparent().getparent().find("name").text==busqueda:
    filtro_evol.append(b.text)

nvl_busqueda = 0
for b in evoluciones:
  if b.getparent().getparent().getparent().find("name").text==busqueda:
    if b.getparent().getparent().getparent().get("id") == b.getparent().get("id") and b.getparent().find("lvl") is not None:
      nvl_busqueda=b.getparent().find("lvl").text

filtro_nom = []
for y in tipo:
  if y.getparent().find("name").text == busqueda:
    if y.getparent().find("name").text not in filtro_nom:
      print "\n", y.getparent().find("name").text
      filtro_nom.append(y.getparent().find("name").text)
    print y.text


for b in evoluciones:
  if b.getparent().getparent().getparent().find("name").text==busqueda:
    if len(filtro_evol) > 1 and b.getparent().getparent().getparent().get("id") != b.getparent().get("id"):
      if b.getparent().find("lvl") is None:
        if b.getparent().find("condition") is not None:
          print b.text, "con la condición de", b.getparent().find("condition").text
        else:
            print "Proviene de", b.text
      else:
        if nvl_busqueda < b.getparent().find("lvl").text:
          print "Evoluciona a", b.text, "al nivel", b.getparent().find("lvl").text
        elif b.getparent().find("lvl") is not None:
          print "Proviene de", b.text, "al nivel", nvl_busqueda 
    if len(filtro_evol) == 1:
      print "El pokemon buscado no evoluciona ni proviene de otro pokemon"

