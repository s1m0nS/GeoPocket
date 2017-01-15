#! /usr/bin/env python
# -*- coding: utf-8 -*-

# %% About
print("-------------------------------------------------------------------------------------------")
print("GeoPocket, version 1.0")
print("Predmet: Programiranje GIG-UNI")
print("Mentor: Matevž Dolenc")
print("Avtor: Simon Šanca,  simon.sanca22@gmail.com")
print("-------------------------------------------------------------------------------------------")

about = '''
Program omogoča naslednje izračune:
  0. Izračun smernih kotov in dolžin
  
  1. Izračun koordinat stojišča:
      a) Prosto stojišče (FreeStation)

  2. Izračun približnih koordinat novih točk
      a) Zunanju urez
      b) Notranji urez
      c) Ločni presek
  
  3. Izpis rezultatov v *.txt ali *.csv
'''

print(about)

print("-------------------------------------------------------------------------------------------")
navodila = """
Navodila za uporabo (podrobno na spletni strani: https://simonsanca22.wixsite.com/geopocket)

Vhodne podatke (koordinate točk in meritve); 
vnašaš v funkcije, ki jih kličeš s spodnjimi ukazi.

0. Izračun smernih kotov in dolžin:
    a) Smerni koti --> nidms(ni(y1,x1,y2,x2)) [dms]
                   --> ni(y1,x1,y2,x2) [rad]
    b) Dolžine     --> dol(y1,x1,y2,x2) [m]

1. Prosto stojišče --> freestation(yA,xA,yB,xB,rA_dms,rB_dms,dolA,dolB)
           kjer:
           -rA_dms, rB_dms; polarne meritve kotov,
           -dolA, dolB; dolžine do navezovalnih točk.
           
2. Zunanji urez    --> zunanji(yA,xA,yB,xB,zsA,zsB)
           kjer sta zsA, zsB zunanji smeri do točk A in B.
           
3. Notranji urez   --> notranji(yA,xA,yB,xB,yC,xC,alfa,beta)
           kjer sta alfa in beta notranji smeri do nove točke.
           
4. Ločni presek    --> locni(yA,xA,yB,xB,a,b)
           kjer sta a in b merjeni dolžini do nove točke.
           
Rezultati izračunov se shranjujejo v datoteko: rezultati.txt."""
          
print(navodila)
print("-------------------------------------------------------------------------------------------")
