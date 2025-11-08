#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 15:59:11 2021

@author: mf
"""

werte = [4, 25, 'Mannheim', 34.5, "Aalen", 102.45, 1110, 12.3, 52]
s=[]
f=[]
i=[]

for elm in werte:
    if type(elm)==str:
        s.append(elm)
    elif type(elm)==float:
        f.append(elm)
    else:
        i.append(elm)