#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 17:29:14 2021

@author: mf
"""

jungs=["Leon", "Luis", "Paul", "Finn", "Noah", "Ben", "Jonas", "Luca", "Theo", "Henry"]


with open('Mädchennamen2021.txt','r') as f:
    maedchen=f.readlines()      # beachte \n am Ende jedes Elements


# with open('Namen2021.txt','w') as f:
#     for nam in jungs:
#         f.write(nam+'\n')   # bei den Jungs muss \n noch angehängt werden
#     for nam in maedchen:
#         f.write(nam)
        


#maed=[]
# for nam in maedchen:
#     a=nam.rstrip('\n')
#     maed.append(a)