# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 21:29:59 2023

@author: Prashant
"""

import random

movies = ['kohinoor','kabbadi','pashupati prasad','chakka panja','loot','adhikatti','prem geet']

def create(movie):
    n = len(movie)
    letters = list(movie)
    temp = []
    for i in range (n):
        if letters[i] == ' ':
            temp.append(' ')
        else:
            temp.append('*')
    qn = "".join(str(x) for x in temp)
    return qn

def is_present(letter, movie):
    d = movie.count(letter)
    if d == 0:
        return False
    else:
        return True
    
def unlock(qn, movie, letter):
    ref = list(movie)
    qn_list = list(qn)
    temp = []
    n = len(movie)
    for i in range(n):
        if(ref[i] == ' ' or ref[i] == letter):
            temp.append(ref[i])
        else:
            if(qn_list[i] == '*'):
                temp.append('*')
            else:
                temp.append(ref[i])
    qn_new = ''.join(str(x) for x in temp)
    return qn_new

def play():
    p1n = input("Player1, Enter your name: ")
    p2n = input("Player2, Enter your name: ")
    p1p = 0
    p2p = 0
    
    turn = 0
    willing = True
    
    while willing:
        
        #Player 1
        if(turn%2 ==0):
            print(p1n,"Your turn")
            picked_mov = random.choice(movies)
            qn = create(picked_mov)
            print (qn)
            
            modified_qn = qn
            not_said = True
            while not_said:
                letter = input("Your letters: ")
                if(is_present(letter, picked_mov)):
                    #unlock
                    modified_qn = unlock(modified_qn, picked_mov, letter)
                    print(modified_qn)
                    c = input("Press 1 to guess or 2 to unlock another letter: ")
                    c = int(c)
                    if c==1 :
                        ans = input("Your answer: ")
                        if(ans == picked_mov):
                            p1p = p1p + 1
                            print('Correct')
                            not_said = False
                            print(p1n,"Score: ",p1p)
                        else:
                            print("Wrong answer. Try again")
                else:
                    print(letter, "not found")
            c = input("Press 1 to continue or 0 to exit")
            c = int(c)
            if(c == 0):
                print(p1n,"Score: ",p1p)
                print(p2n,"Score: ",p2p)
                print("Thank you !")
                willing = False
                
        #Player 2    
        else:
            print(p2n,"Your turn")
            picked_mov = random.choice(movies)
            qn = create(picked_mov)
            print (qn)
            
            modified_qn = qn
            not_said = True
            while not_said:
                letter = input("Your letters: ")
                if(is_present(letter, picked_mov)):
                    #unlock
                    modified_qn = unlock(modified_qn, picked_mov, letter)
                    print(modified_qn)
                    c = input("Press 1 to guess or 2 to unlock another letter: ")
                    c = int(c)
                    if c==1 :
                        ans = input("Your answer: ")
                        if(ans == picked_mov):
                            p2p = p2p + 1
                            print('Correct')
                            not_said = False
                            print(p2n,"Score: ",p2p)
                        else:
                            print("Wrong answer. Try again")
                else:
                    print(letter, "not found")
            c = input("Press 1 to continue or 0 to exit")
            if(c == 0):
                print(p1n,"Score: ",p1p)
                print(p2n,"Score: ",p2p)
                print("Thank you !")
                willing = False
                
        turn = turn + 1
            
play()
        
            
            