# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 23:07:41 2020

@author: hero144
"""

def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if y==0:
        raise ValueError('Cannot divide by zero!')
    return x/y