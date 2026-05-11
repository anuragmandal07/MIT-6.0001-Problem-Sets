# -*- coding: utf-8 -*-
"""
Created on Mon May 11 03:24:36 2026

@author: ANURAG MANDAL
"""

"""Getting the inputs"""
annual_salary = float(input("Enter your annual salary:"))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal:"))
total_cost = float(input("Enter the cost of your dream home:"))
semi_annual_raise = float(input("Enter the semi­annual raise, as a decimal:"))

"""Intitial Conditions"""
portion_down_payment = 0.25
current_savings = 0
r = 0.04
months = 0
down_payment = portion_down_payment*total_cost

"""Calculations"""
while current_savings < down_payment:
    monthly_return = current_savings*r/12
    monthly_savings = annual_salary/12*portion_saved
    current_savings += monthly_return + monthly_savings
    months +=1
    if months%6 == 0:
        annual_salary += semi_annual_raise*annual_salary
    
"""Output"""
print("Number of months: ", months)
