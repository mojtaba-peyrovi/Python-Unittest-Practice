# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 01:10:20 2020

@author: hero144
"""

import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    def test_email(self):
        emp_1 = Employee('Corey','Schafer',50000)
        emp_2 = Employee('Sue','Smith',30000)
        
        self.assertEquals(emp_1.email(), 'Corey.Schafer@email.com')
        self.assertEquals(emp_2.email(), 'Sue.Smith@email.com')
        
        emp_1.first = 'John'
        emp_2.last = 'arndt'
        
        self.assertEquals(emp_1.email(), 'John.Schafer@email.com')
        self.assertEqual(emp_2.email(), 'Sue.arndt@email.com')
        
if __name__ == "__main__":
    unittest.main()        