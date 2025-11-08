#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 13:25:29 2021
Aufg. 2.7.1
Splittet einen Namen in Vor- und Nachnamen
@author: mf
"""

inname=input("Geben Sie Ihren Namen ein: ")
inname_upper=inname.upper()
vn,nn=inname_upper.split()

print("Vorname: {}\nNachname: {}".format(vn,nn))
