#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 19:55:33 2021

@author: mf
"""

werte = [1, 2, 4, 5, 9,12] 

produkt=1
summe=sum(werte)

for i in werte:
    produkt=produkt*i

print("Summe, Produkt:", summe, produkt)