#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 17:52:17 2021

@author: mf
"""

import math as m

F=float(input("Geben Sie die Kreisfläche ein: "))

r=m.sqrt(F/m.pi)

print("Der Radius ist {:.2f}".format(r))