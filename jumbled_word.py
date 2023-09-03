# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 22:46:47 2023

@author: Prashant
"""

import random

def choose():
    words = ["Prashant","Khomnath","Nirmala","Prasanna","Saurav","Smriti","Sanjeeta","Sangita","Tilak","Bihantika","Bikram"]
    pick = random.choice(words)
    return pick

def jumble(picked_word):
    jumbled = "".join(random.sample(picked_word,len(picked_word)))
    return jumbled

def thank(p1n, p2n, p1p, p2p):
    print(p1n," Your score is ",p1p)
    print(p2n," Your score is ",p2p)
    print("Thanks for playing")
    
def play():
    p1name = input("Player 1, Enter your name: ")
    p2name = input("Player 2, Enter your name: ")
    p1p = 0
    p2p = 0
    turn = 0
    
    while(1):
        #computer task
        picked_word = choose()
        #create jumbled word
        qn = jumble(picked_word)
        print("\n",qn)
        
        # Player 1 
        
        if turn%2==0:
            print(p1name,' Your turn.')
            ans = input("What is your answer?: ")
            if (ans == picked_word):
                p1p = p1p + 1 
                print("Your score is ",p1p)
            else:
                print("Incorrect, Better luck next time")
            c = int(input("Press 1 to continue and 0 to quit: "))
            if (c == 0):
                thank(p1name,p2name,p1p,p2p)
                break
        # Player 2
        
        else:
            print(p2name,' Your turn.')
            ans = input("What is your answer?: ")
            if (ans == picked_word):
                p2p = p2p + 1
                print("Your score is ",p2p)
            else:
                print("Incorrect, Better luck next time")
            c = int(input("Press 1 to continue and 0 to quit: "))
            if (c == 0):
                thank(p1name,p2name,p1p,p2p)
                break
        turn = turn + 1
                
play()


            
            