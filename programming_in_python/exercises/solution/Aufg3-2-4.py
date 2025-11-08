#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 00:17:37 2021

@author: mf
"""
wetter=input("Wetter? ")
temp=float(input("Temperatur? "))
if (wetter=="Sonne"):
    if (temp<10.0):
        print ("Mach einen Spaziergang und zieh dich warm an!")
    elif (temp>=10.0 and temp<20.0):
        print ("Fahr mit dem Fahrrad")
    else: 
        print ("Ab ins Schwimmbad")
else:
    print("Bleib daheim.")
    