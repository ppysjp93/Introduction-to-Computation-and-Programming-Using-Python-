#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 15:04:23 2020

@author: samuelpalmer
"""
# annual_salary = input("Enter your annual salary? ")
# portion_saved = input("Enter the percent of your salary to save, as a decimal: ")
# total_cost = input("Enter the cost of your dream home? ")

initial_salary = 150000
portion_saved = 0.4453125
total_cost = 1000000
portion_down_payment = 0.25
annual_savings_rate = 0.04
semi_annual_rise = 0.07
current_savings = 0

def Downpayment_Calculator(annual_salary, portion_saved,
                            total_cost, portion_down_payment,
                            annual_savings_rate, semi_annual_rise,
                            current_savings):

    number_of_months = 0
    diff = - 1.0 # place holder
    while(diff < 0):
        current_savings += Increase_Savings(current_savings,annual_savings_rate,
                                            annual_salary,portion_saved)

        
        annual_salary = Raise_Salary_Semi_Annually(annual_salary,
                                                   semi_annual_rise, number_of_months)

        diff = current_savings - portion_down_payment*float(total_cost)
        number_of_months += 1   
        
    return number_of_months, annual_salary

def Raise_Salary_Semi_Annually(annual_salary, semi_annual_rise, month):
    if month % 6 == 0 and month != 0:
        return annual_salary*(1.0 + semi_annual_rise)
    else:
        return annual_salary
    
def Increase_Savings(current_savings,annual_savings_rate,annual_salary,portion_saved):
    return current_savings*annual_savings_rate/12 + \
                            float(annual_salary)*float(portion_saved)/12
    
(number_of_months, final_salary) = Downpayment_Calculator(initial_salary,
                                    portion_saved, total_cost, 
                                    portion_down_payment, annual_savings_rate,
                                    semi_annual_rise, current_savings)

print("Number of months: {0}".format(number_of_months))
