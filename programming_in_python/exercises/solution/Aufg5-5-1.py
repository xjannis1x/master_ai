#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 20:51:15 2021

@author: mf
"""

import myFunctions as mf

mf.printWillkommen()

pali=mf.IsPalindrom("Anna")

print(pali)

mf.hhmmss(3670)

if (mf.IsRightAngle(3, 4, 5)):
    print("rechtwinkllig")
else:
    print("nicht rechtwinklig")

