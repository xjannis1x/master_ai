#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 20:35:55 2021

@author: mf
"""


alter=int(input("Geben Sie ihr Alter ein: "))
if alter < 12:
    preis = 0.0
    print ("Für Kinder ist der Eintritt kostenlos")
elif (alter >= 12) and (alter < 18):
    preis = 6.0
    print ("Jugendliche zahlen {:.2f} Euro".format(preis))
elif (alter >= 18) and (alter < 65):
    preis = 10.0
    print ("Normalpreis {:.2f} Euro".format(preis))
else:
    preis = 8.0
    print ("Seniorentarif {:.2f} Euro".format(preis))