#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 20:13:58 2021

@author: mf
"""

def parallel_Widerstand(r1,r2):
    r_ges=(r1*r2)/(r1+r2)
    return r_ges

r1=float(input("Widerstand R1 (Ohm) eingeben: "))
r2=float(input("Widerstand R2 (Ohm) eingeben: "))

rges=parallel_Widerstand(r1,r2)
print("Der Gesamtwiderstand ist {:.2f} Ohm".format(rges))
