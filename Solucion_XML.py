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
for v in evoluciones:
  if v.getparent().getparent().getparent().find("name").text==busqueda:
    filtro_evol.append(v.text)

nvl_busqueda = 0
for e in evoluciones:
  if e.getparent().getparent().getparent().find("name").text==busqueda:
    if e.getparent().getparent().getparent().get("id") == e.getparent().get("id") and b.getparent().find("lvl") is not None:
      nvl_busqueda=e.getparent().find("lvl").text

filtro_nom = []
for y in tipo:
  if y.getparent().find("name").text == busqueda:
    if y.getparent().find("name").text not in filtro_nom:
      print "\n", y.getparent().find("name").text
      filtro_nom.append(y.getparent().find("name").text)
    print y.text

print "\n", "Evolucion/es:", "\n"
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

movimientos = root.findall("pokemon/moves/move")
print "\n", "Movimientos por nivel:", "\n"
for m in movimientos:
  if m.getparent().getparent().find("name").text == busqueda:
    if m.get("type") == "level-up":
      print m.find("name").text, "al nivel", m.find("lvl").text

# Ejercicio 5
pokemon1=raw_input("Nombre del primer pokemon: ")
pokemon2=raw_input("Nombre del segundo pokemon: ")

HP_1 = 0
ATK_1 = 0
DEF_1 = 0
SAT_1 = 0
SDF_1 = 0
SPD_1 = 0

HP_2 = 0
ATK_2 = 0
DEF_2 = 0
SAT_2 = 0
SDF_2 = 0
SPD_2 = 0

for g in poke:
  if g.find("name").text == pokemon1:
    HP_1 = g.find("stats/HP").text
    ATK_1 = g.find("stats/ATK").text
    DEF_1 = g.find("stats/DEF").text
    SAT_1 = g.find("stats/SAT").text
    SDF_1 = g.find("stats/SDF").text
    SPD_1 = g.find("stats/SPD").text
  if g.find("name").text == pokemon2:
    HP_2 = g.find("stats/HP").text
    ATK_2 = g.find("stats/ATK").text
    DEF_2 = g.find("stats/DEF").text
    SAT_2 = g.find("stats/SAT").text
    SDF_2 = g.find("stats/SDF").text
    SPD_2 = g.find("stats/SPD").text
if int(HP_1) > int(HP_2):
  print pokemon1, "tiene mas HP base por", int(HP_1)-int(HP_2), "puntos,", pokemon1, "tiene:", HP_1, "puntos."
if int(HP_1) < int(HP_2):
  print pokemon2, "tiene mas HP base por", int(HP_2)-int(HP_1), "puntos,", pokemon2, "tiene:", HP_2, "puntos."
if int(HP_1) == int(HP_2):
  print pokemon1, "y", pokemon2, "tienen la misma HP base:", HP_1

if int(ATK_1) > int(ATK_2):
  print pokemon1, "tiene mas ATK base por", int(ATK_1)-int(ATK_2), "puntos,", pokemon1, "tiene:", ATK_1, "puntos."
if int(ATK_1) < int(ATK_2):
  print pokemon2, "tiene mas ATK base por", int(ATK_2)-int(ATK_1), "puntos,", pokemon2, "tiene:", ATK_2, "puntos."
if int(ATK_1) == int(ATK_2):
  print pokemon1, "y", pokemon2, "tienen el mismo ATK base:", ATK_1

if int(DEF_1) > int(DEF_2):
  print pokemon1, "tiene mas DEF base por", int(DEF_1)-int(DEF_2), "puntos,", pokemon1, "tiene:", DEF_1, "puntos."
if int(DEF_1) < int(DEF_2):
  print pokemon2, "tiene mas DEF base por", int(DEF_2)-int(DEF_1), "puntos,", pokemon2, "tiene:", DEF_2, "puntos."
if int(DEF_1) == int(DEF_2):
  print pokemon1, "y", pokemon2, "tienen la misma DEF base:", DEF_1

if int(SAT_1) > int(SAT_2):
  print pokemon1, "tiene mas SAT base por", int(SAT_1)-int(SAT_2), "puntos,", pokemon1, "tiene:", SAT_1, "puntos."
if int(SAT_1) < int(SAT_2):
  print pokemon2, "tiene mas SAT base por", int(SAT_2)-int(SAT_1), "puntos,", pokemon2, "tiene:", SAT_2, "puntos."
if int(SAT_1) == int(SAT_2):
  print pokemon1, "y", pokemon2, "tienen el mismo SAT base:", SAT_1

if int(SDF_1) > int(SDF_2):
  print pokemon1, "tiene mas SDF base por", int(SDF_1)-int(SDF_2), "puntos,", pokemon1, "tiene:", SDF_1, "puntos."
if int(SDF_1) < int(SDF_2):
  print pokemon2, "tiene mas SDF base por", int(SDF_2)-int(SDF_1), "puntos,", pokemon2, "tiene:", SDF_2, "puntos."
if int(SDF_1) == int(SDF_2):
  print pokemon1, "y", pokemon2, "tienen la misma SDF base:", SDF_1

if int(SPD_1) > int(SPD_2):
  print pokemon1, "tiene mas SPD base por", int(SPD_1)-int(SPD_2), "puntos,", pokemon1, "tiene:", SPD_1, "puntos."
if int(SPD_1) < int(SPD_2):
  print pokemon2, "tiene mas SPD base por", int(SPD_2)-int(SPD_1), "puntos,", pokemon2, "tiene:", SPD_2, "puntos."
if int(SPD_1) == int(SPD_2):
  print pokemon1, "y", pokemon2, "tienen la misma SPD base:", SPD_1

for h in poke:
  if h.find("name").text == pokemon1:
    if h.find("egg-group") is not None:
      grp_huevo1= h.find("egg-group")
    else:
      print pokemon1, "no tiene grupo huevo"
      grp_huevo1 = "None"
  if h.find("name").text == pokemon2:
    if h.find("egg-group") is not None:
      grp_huevo2= h.find("egg-group")
    else:
      print pokemon2, "no tiene grupo huevo"
      grp_huevo2 = "None"

if grp_huevo1 == "None" or grp_huevo2 == "None":
  print "\n","Uno de los dos pokemon no puede criar"
elif grp_huevo1 == grp_huevo2:
  print "\n","Pertenecen al mismo grupo y pueden criar"
elif grp_huevo1 != grp_huevo2:
  print "\n","No pertenecen al mismo grupo y no pueden criar"
