# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 15:00:31 2023

@author: Prashant
"""

with open("file.txt","r+") as myfile:
    print(myfile.read())
    myfile.write("\n I live in Nepal")
    print(myfile.read())
myfile.close()
