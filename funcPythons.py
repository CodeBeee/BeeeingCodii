# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 23:03:12 2020

@author: amitha
"""


def addition(x,y):
    return x+y

def multiply(x,y):
    return x*y


def ulta(name:str):
    t=len(name)
    namex = ""
    while t>0:
        namex += name[t-1]
        t = t-1 
        
    print(namex)

ulta("aarnav")
