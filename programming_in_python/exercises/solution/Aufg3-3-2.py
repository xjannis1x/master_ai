#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 11:10:08 2021
Aufg. 3.3.2 
Umrechnung von km/h in m/s
@author: mf
"""

print("      km/h       m/s")
for i in range(0,251,10):
    km=float(i)
    m=km/3.6
    print("{:10.2f}{:10.2f}".format(km,m))    