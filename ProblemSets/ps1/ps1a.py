#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 13:35:01 2020

@author: samuelpalmer
"""

# annual_salary = input("Enter your annual salary? ")
# portion_saved = input("Enter the percent of your salary to save, as a decimal: ")
# total_cost = input("Enter the cost of your dream home? ")

annual_salary = 120000
portion_saved = 0.1
total_cost = 1000000

portion_down_payment = 0.25
r = 0.04
number_of_months = 0
current_savings = 0.0 
diff = - 1.0 # place holder
monthly_portion_saved = float(annual_salary)*float(portion_saved)/12

while(diff < 0):
    current_savings += current_savings*r/12 + monthly_portion_saved
    number_of_months += 1
    diff = current_savings - portion_down_payment*float(total_cost)

print("Number of months: {0}".format(number_of_months))
