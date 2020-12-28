#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 19:08:23 2020

@author: samuelpalmer
"""

def Downpayment_Calculator(annual_salary, portion_saved,
                            total_cost, portion_down_payment,
                            annual_savings_rate, semi_annual_rise,
                            current_savings, number_of_months):
    
    for i in range(0, number_of_months):
        current_savings += Increase_Savings(current_savings,annual_savings_rate,
                                            annual_salary,portion_saved)

        
        annual_salary = Raise_Salary_Semi_Annually(annual_salary,
                                                   semi_annual_rise, i) 
        
    return current_savings

def Raise_Salary_Semi_Annually(annual_salary, semi_annual_rise, month):
    if month % 6 == 0 and month != 0:
        return annual_salary*(1.0 + semi_annual_rise)
    else:
        return annual_salary
    
def Increase_Savings(current_savings,annual_savings_rate,annual_salary,portion_saved):
    return current_savings*annual_savings_rate/12 + \
                            float(annual_salary)*float(portion_saved)/12 

def Bisection_Search(x, epsilon, num_Guesses, low, high):
    ans = (high + low) / 2.0
    while abs(ans**2 - x) >= epsilon:
        print('low =', low, 'high =', high, 'ans =', ans)
        num_Guesses += 1
        if ans**2 < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2.0
    return num_Guesses, ans

# x is the portion of the downpayment
# epsilon is 100 
# numGuesses doesn't need changing 
# low = 0 
# high = 10000
# we need to convert ans into a decimal percentage for the value of
# portion_saved. we then run the DownPayment Calculator to get a value for the 
# current_savings. We can then test using our Is_Current_Savings function
# if we need to keep doing a bisection search.

def Bisection_Search_2(down_payment, initial_savings, epsilon, num_Guesses, low, high):
    
    # Initialisers 
    ans = (high + low) / 2.0
    current_savings = -1 
    
    while Is_Current_Savings_Within_100_Down_Payment(current_savings,
                                                     down_payment, epsilon):
        
        portion_saved = Convert_to_Decimal_Percentage(ans)
        print("Portion Saved: {0}".format(portion_saved))
        
        current_savings = Downpayment_Calculator(initial_salary,
                                    portion_saved, total_cost, 
                                    portion_down_payment, annual_savings_rate,
                                    semi_annual_rise, initial_savings, number_of_months)
        
        print("Current Savings: {0}".format(current_savings))
        
        print('low =', low, 'high =', high, 'ans =', ans)
        num_Guesses += 1
        if current_savings < down_payment:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2.0
        
    return num_Guesses, portion_saved

def Convert_to_Decimal_Percentage(n):
    return n / 10000.0

def Is_Current_Savings_Within_100_Down_Payment(current_savings, down_payment, epsilon):
    return abs(down_payment - current_savings) >= epsilon





initial_salary = 15000
portion_saved_guess = 0.4411 # we want to find this value so that we get a current savings
                        # value that is as close to 250,000 as possible in this case
total_cost = 1000000
portion_down_payment = 0.25
annual_savings_rate = 0.04
semi_annual_rise = 0.07
current_savings = 0
number_of_months = 36

print("Bisection Search 2")

initial_savings = 0
epsilon = 100
low = 0
high = 10000
num_Guesses = 0
down_payment = total_cost * portion_down_payment
num_Guesses, portion_saved = Bisection_Search_2(down_payment, initial_savings, epsilon, num_Guesses, low, high)

print("Number of Guesses: {0}".format(num_Guesses))
print("Portion Saved: {0}".format(portion_saved))

print("You can see that we can now work out exactly how much we need to save to \
      be able to afford the downpayment within 36 months.")

#def Set_Goal(number_of_months, initial_salary):
#    return portion_saved, num_Guesses

# I think we want to fix the number of months so instead of using a while loop
# Inside of DownpaymentCalculator we we want to do a for loop for 36 iterations
# We then use bisection search and test different portion saved so that we get a
# float that tells us what percentage of our salary we need to save in order to 
# return what we are after. 

