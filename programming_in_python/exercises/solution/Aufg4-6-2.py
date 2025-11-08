#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 23:04:55 2021

@author: mf
"""




txt="Anna".lower()
# txt_rev = txt[::-1]
# print(txt_rev)

# if (txt_rev==txt):
#     print("Palindrom")

liste=list(txt)
liste2=liste[:]
liste2.reverse()
if (liste==liste2):
      print("Palindrom")



