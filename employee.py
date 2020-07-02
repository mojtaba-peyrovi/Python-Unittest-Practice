# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 00:09:25 2020

@author: hero144
"""
import requests

raise_amt = 1.05

class Employee:
    def __init__ (self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        

    def email(self):
        return f"{self.first}.{self.last}@email.com"



    def fullname(self):
        return f"{self.first} {self.last}"
    
    
    def apply_raise(self):
        self.pay = int(self.pay * raise_amt)
    

    def monthly_schedule(self, month):
        response = requests.get(f'http://company.com/{self.last}/{month}')
        if response.ok:
            return response.text
        else:
            return "Bad Response!"





Employee_1 = Employee('mojtaba','peyrovi',20000)
        
        
# print(Employee.email(Employee_1),Employee.fullname(Employee_1),Employee.apply_raise(Employee_1))
# Employee.fullname(Employee_1)



    