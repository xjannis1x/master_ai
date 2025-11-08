#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 10:21:46 2021

@author: mf
"""

zahl=int(input("Geben Sie eine ganze Zahl ein: "))

if(zahl%7):
    print("Die Zahl ist nicht durch 7 teilbar.")
else:
    print ("Die Zahl ist durch 7 teilbar: {}:{}={}"\
           .format(zahl,7,zahl//7))