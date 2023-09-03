# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 16:46:58 2023

@author: Prashant
"""

from statistics import mean

estimates = [25,1,10,24,23,19,15,25,25,11,5,18,18,13,13,16,20,23,22]
estimates.sort()
tv = int(0.1*len(estimates))
estimates = estimates[tv:]
estimates = estimates[:len(estimates)-tv]
print(mean(estimates))


from scipy import stats
estimates = [25,1,10,24,23,19,15,25,25,11,5,18,18,13,13,16,20,23,22]
estimates.sort()
m = stats.trim_mean(estimates,0.1)
print(m)
