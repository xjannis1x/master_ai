#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 12:58:59 2021
Aufg. 2.4.2
@author: mf
"""

#a)
#x=231

#b)

x=int(input("Teilnehmerzahl eingeben: "))

a=x//6
r=x%6

if r==1:
    verb="bleibt"
else:
    verb="bleiben"
    
print("Es gibt {} 6er-Gruppen. {} Teilnehmer {} übrig.".format(a,r,verb))
  
