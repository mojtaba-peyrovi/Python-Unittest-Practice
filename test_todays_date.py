# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 10:44:17 2020

@author: "mojtaba@heroleads.com"
"""

import unittest
import todays_date
from datetime import date

class TestTodaysDate(unittest.TestCase):
    
    def test_return_todays_date(self):
        self.assertEqual(todays_date.return_todays_date(), date(2020,7,1))
        
        
    def test_return_yesterdays_date(self):
        self.assertEqual(todays_date.return_yesterdays_date(), date(2020,6,30))
            
    def test_check_date(self):
        # self.assertRaises(ValueError, todays_date.check_date, date(2019,1,1))
        
        with self.assertRaises(ValueError):
            todays_date.check_date(date(2019,1,1))
        
if __name__ == "__main__":
    unittest.main()        
    
    
    
    