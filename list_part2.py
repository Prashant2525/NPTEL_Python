# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 18:12:19 2023

@author: Prashant
"""
shopping = ["Mobile","Headphone","Charger"]


for item in shopping:
  print(item)
  
shopping.append("Console")
print("\n")

for item in shopping:
  print(item)
print("\n")

shopping.insert(1,"Keyboard")


for item in shopping:
  print(item)
  
print(len(shopping))


for i in range(len(shopping)):
    print(shopping[i])
