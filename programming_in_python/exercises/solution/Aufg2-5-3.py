#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 17:58:01 2021

@author: mf
"""

import math as m

hypo=10.

alpha=float(input("Winkel in Grad eingeben: "))
arad=alpha/180.*m.pi   # von Grad in Radiant umrechnen


ankat=hypo*m.acos(arad)
gekat=hypo*m.asin(arad)

print("Gegenkathete: {:.2f}".format(gekat))
print("Ankathete: {:.2f}".format(ankat))