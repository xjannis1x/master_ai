#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 10:15:45 2021
Aufgabe 2.4.4
Zeit in Sekunden einlesen und im Format hh:mm:ss ausgeben
@author: mf
"""
sek_in=int(input("Geben Sie die Sekunden ein: "))

min=sek_in//60
ss=sek_in%60
hh=min//60
mm=min%60
print("{:02d}:{:02d}:{:02d}".format(hh,mm,ss))