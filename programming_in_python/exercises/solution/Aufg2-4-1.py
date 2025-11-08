#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 13:14:24 2021
Aufg. 2.4.1
@author: mf
"""

try:
    netto=float(input("Nettopreis eingeben: "))
    mwst=float(input("Mehrwertsteuer in % eingeben: "))
    brutto=(1 + mwst/100.)*netto
    print("Der Bruttopreis ist: {:.2f}".format(brutto))
except ValueError:
     print("Falsche Eingabe")
    