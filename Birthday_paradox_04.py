# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 13:13:35 2023

@author: Prashant
"""

import random
import datetime

birthday = []

i = 0

while(i<50):
    
    year = random.randint(1901, 2023)
    
    if(year%4 == 0 and year%100 !=0 or year%400 == 0 ):
        leap = 1
    else:
        leap = 0
    
    month = random.randint(1,12)
    
    if(month == 2 and leap == 1): #feb
        day = random.randint(1, 29)
    elif(month == 2 and leap == 0):
        day = random.randint(1, 28)
    elif(month == 7 and month == 8): #Jul and Aug
        day = random.randint(1, 31)
    elif(month%2 != 0 and month < 7): #Odd month for < 7
        day = random.randint(1, 31)
    elif(month%2 == 0 and month > 7 and month < 12): #Even month > 7 and < 12
        day = random.randint(1, 31)
    else:
        day = random.randint(1, 30)
        
    dd = datetime.date(year,month,day)
    day_of_year = dd.timetuple().tm_yday
    i = i + 1
    birthday.append(day_of_year)

birthday.sort()
i = 0
while(i < 50):
    print(birthday[i])
    i = i + 1
    

    
    
    
    
        