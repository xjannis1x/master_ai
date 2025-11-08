#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 21:51:34 2021
Aufgabe 3.3.3 Berechnen des Notendurchschnitts einer beliebigen 
Anzahl von Noten, die über Konsole eingegeben werden.
Errorhandling.
@author: mf
"""
a=""
summe=0.0
i=0
while (a!="n"):
    a=input("Noteneingabe (Ende mit n): ")
    if (a=="n"):
        break
    try:
        note=float(a)
        summe=summe+note
        i=i+1
    except ValueError:
        print ("Falsche Eingabe.")
     
try:
    av=summe/i
    
    if av<1.5:
        result="sehr gut"
    elif av<2.5:
        result="gut"
    elif av<3.5:
        result="befriedigend"
    elif av<=4.0:
        result="ausreichend"
    else:
        result="nicht bestanden"
        
    print("Dein aktueller Notendurchschnitt ist: {:.1f} Ergebnis: {}".format(av, result))   
    
except ZeroDivisionError:
    pass

