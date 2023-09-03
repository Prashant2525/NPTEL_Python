# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 18:00:18 2023

@author: Prashant
"""

def magic_square(n):
    magicSqr = []
    for i in range (n):
        l = []
        for j in range(n):
            l.append(0)
        magicSqr.append(l)
        

    i = n//2
    j = n - 1
    count = 1
    num = n*n
    
    while (count <= num):
        if(i == -1 and j == n):
            j = n - 2
            i = 0
            
        else:
            if(j == n):
                j = 0
                
            if(i < 0):
                i = n - 1
                
        if(magicSqr[i][j] != 0):
            j = j - 2
            i = i + 1
            continue
        
        else:
            magicSqr[i][j] = count
            count += 1
        
        i = i - 1
        j = j + 1
        
    for i in range (n):
        for j in range (n):
            print(magicSqr[i][j], end=" ")
        print()
    print("Sum of row, column and diagonal is: ", int(n*(n**2 + 1)/2))

magic_square(3)
    
        
        
        
# =============================================================================
# ***** NOTE *****
# We can add for loop inside list 
# magic = [0 for i in range(3)]
# magic = [[0 for i in range(3)] for j in range(3)]
# =============================================================================
# =============================================================================
# after each iteration, the next number will be placed in the cell that is one row above and one column to the 
# right of the current position.
# =============================================================================
