# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 15:41:57 2023

@author: Prashant
"""


ages = [25,1,10,24,23,19,15,25,25,11,5,18,18,13,13,16,20,23,22]

print(ages.count(25))
print(len(ages))
print(ages)
print("\nAfter Sorting in ascending\n")
ages.sort()
print(ages)
print("\nAfter Sorting in descending\n")
ages.reverse()
print(ages)
print("\n")

students = ["Prashant","Aakash","Bibash","Sunit","Nikesh","Jayash"]
print(students)
print("\nAfter Sorting in ascending\n")
students.sort()
print(students)
students.insert(1,"Cyrus")
print(students)


# =============================================================================
# Slicing
# Syntax: list_name(start_index:end_index+1)
# =============================================================================
print(students[1:6])  #it prints from Oth index to (6-1)th index
print(students[:])
print(students[2:])
print(students[:6])
