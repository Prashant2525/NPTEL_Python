# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 16:02:12 2023

@author: Prashant
"""
# Example 1
n = input("Enter any number: ")
n = int()
if(n % 3 == 0 and n % 5 == 0):
    print("\nFizzbuzz")
elif(n % 5 == 0):
    print("\nBuzz")
elif (n % 3 == 0):
    print("\nFizz")
else:
    print(n)


# Example 2
for n in range(1,51):
    if(n % 3 == 0 and n % 5 == 0):
        print(n," = Fizzbuzz")
    elif (n % 3 == 0):
        print(str(n)+" = Fizz")
    elif(n % 5 == 0):
        print(str(n)+" = Buzz")
    else:
        print(n)
     
# Example 3
def fizzbuzz(n):
    for i in range (1,n):
        if(i %3 == 0 and i %5 == 0):
            print(i,"= Fizzbuzz")
        elif(i %3 == 0):
            print(i,"= Fizz")
        elif(i %5 == 0):
            print(i,"Buzz")
        else:
            print(i)
fizzbuzz(51)