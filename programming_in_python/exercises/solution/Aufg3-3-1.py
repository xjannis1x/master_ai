#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 11:01:24 2021
Aufgabe 3.3.1
@author: mf
"""
import random

produkt=1
# For-Schleife
for i in range(15):
    w=random.randint(1, 6)
    produkt=produkt*w
    print(w, produkt)
    
print("Das Produkt ist: ",produkt)