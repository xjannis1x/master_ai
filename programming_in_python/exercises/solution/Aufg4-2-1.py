#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 12:39:49 2021
Aufg. 4.2.1
@author: mf
"""
import random

jungs=["Leon", "Luis", "Paul", "Finn", "Noah", "Ben", "Jonas", "Luca", "Theo", "Henry"]

# a)
i=random.randint(0,9)
print(jungs[i])

#b)
print(jungs[1])

#c)
print(jungs[-2])

#d)
jungs[8]="Max"
print(jungs)

