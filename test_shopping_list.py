# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 22:42:27 2020

@author: "mojtaba@heroleads.com"
"""

import unittest
from shoppingList import ShoppingList

class test_shoppingList(unittest.TestCase):
    
    def test_calculate_tax(self):
        
        test_item = ShoppingList("apple","fruits",100)
        self.assertEqual(ShoppingList.calculate_tax(test_item), 130)
        

if __name__ == "__main__":
    unittest.main()        
    
    
    
    