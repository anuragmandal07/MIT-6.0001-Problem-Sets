# -*- coding: utf-8 -*-
"""
Created on Mon May 11 03:38:43 2026

@author: ANURAG MANDAL
"""
"""Getting Inputs"""
annual_salary = float(input("Enter the starting salary:​ "))

"""Initialisation"""
semi_annual_raise = 0.07
r = 0.04
total_cost = 1000000
down_payment = 0.25*total_cost

"""Impossible Case Check"""
current_savings = 0
salary = annual_salary
for month in range(1,37):
    monthly_return = current_savings*1/12
    monthly_savings = salary/12*1
    current_savings += monthly_return + monthly_savings
    if month%6 == 0:
        salary += semi_annual_raise*salary
        
if current_savings < down_payment - 100:
    print("It is impossible to pay the downpayment in three years")
else:
    """Bisection Searcg"""
    low = 0
    high = 10000
    steps = 0
    
    """Bisection Loop"""
    while True:
        guess = (low + high) // 2
        portion_saved = guess/10000
        #Simulate 36 months
        current_savings = 0
        salary = annual_salary
        for month in range(1,37):
            monthly_return = current_savings*r/12
            monthly_savings = salary/12*portion_saved
            current_savings += monthly_return + monthly_savings
            if month%6 == 0:
                salary += semi_annual_raise*salary
        if abs(current_savings - down_payment) < 100:
            break
        elif current_savings < down_payment:
            low = guess
        else:
            high = guess
            
        steps += 1
        
    print("Best savings rate: ", portion_saved)
    print("Steps in bisection search:​ ", steps)
    
    

