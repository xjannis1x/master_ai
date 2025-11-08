#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 11:25:17 2021
Euklidscher Algorithmus zur Berechnung des GGT
@author: mf
"""

m=int(input("Geben Sie die erste Zahl M ein: "))
n=int(input("Geben Sie die zweite Zahl N ein: "))

p=m
q=n
r=-1
while(r!=0):
    r=p%q
    if(r!=0):
        p=q
        q=r

GGT=q

print ("Der GGT ist:",GGT)