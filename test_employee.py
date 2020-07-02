# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 01:10:20 2020

@author: hero144
"""

import unittest
from unittest.mock import patch
from employee import Employee


class TestEmployee(unittest.TestCase):
    
    def setUp(self):
        self.emp_1 = Employee('Corey','Schafer',50000)
        self.emp_2 = Employee('Sue','Smith',30000)
    
    def tearDown(self):
        pass
     
    
    def test_email(self):
        # emp_1 = Employee('Corey','Schafer',50000)
        # emp_2 = Employee('Sue','Smith',30000)
        
        self.assertEquals(self.emp_1.email(), 'Corey.Schafer@email.com')
        self.assertEquals(self.emp_2.email(), 'Sue.Smith@email.com')
        
        self.emp_1.first = 'John'
        self.emp_2.last = 'arndt'
        
        self.assertEquals(self.emp_1.email(), 'John.Schafer@email.com')
        self.assertEqual(self.emp_2.email(), 'Sue.arndt@email.com')
        
    def test_monthly_schedule(self):
        # test successful response
        with patch('employee.requests.get') as mock_get:
            mock_get.return_value.ok = True
            mock_get.return_value.text = 'Success'
            
            schedule = self.emp_1.monthly_schedule('May')
            mock_get.assert_called_with('http://company.com/Schafer/May')
            self.assertEqual(schedule, 'Success')
       # test failed response
        with patch('employee.requests.get') as mock_get:
            mock_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('Jun')
            mock_get.assert_called_with('http://company.com/Smith/Jun')
            self.assertEqual(schedule, 'Bad Response!')     
        
        
if __name__ == "__main__":
    unittest.main()        