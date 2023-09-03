# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 17:08:27 2023

@author: Prashant
"""
import statistics
import matplotlib.pyplot as plt
estimates = [25,1,10,24,23,19,15,25,25,11,5,18,18,13,13,16,20,23,22]
y = []

estimates.sort()
tv = int(0.1*(len(estimates)))
estimates = estimates[tv:]
estimates = estimates[:len(estimates)-tv]

for i in range (len(estimates)):
    y.append(5)
    
plt.plot(estimates,y,"r--")
plt.plot([statistics.mean(estimates)],[5],"ro")
plt.plot([statistics.median(estimates)],[5],"bs")
plt.plot([17],[5],'g^')