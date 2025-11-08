#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 16:13:33 2021
Aufg. 4.5.2 und Aufg. 4.5.3
@author: mf
"""
import random

# Aufg. 4.5.2
random.seed(42)
lzz=[]
for i in range(100):
    lzz.append(random.randint(1,6))

for j in range(1,7):   
     print("Anzahl {}en: {}".format(j,lzz.count(j)))
          
     
# Aufg. 4.5.3
jungs=["Leon", "Luis", "Paul", "Finn", "Noah", "Ben", "Jonas", "Luca", "Theo", "Henry"]

jungs.remove("Theo")
indx=jungs.index("Luis")
jungs.insert(indx+1,"Daniel")



