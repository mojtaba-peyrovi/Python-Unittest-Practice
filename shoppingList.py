# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 22:09:16 2020

@author: "mojtaba@heroleads.com"
"""

import pandas as pd

tax = 0.3
class ShoppingList:
    
    def __init__(self, item, category, fee):
        self.item = item
        self.category = category
        self.fee = fee
        
    def calculate_tax(self):
        self.final_price = self.fee * (1 + tax)
        return self.final_price
    






