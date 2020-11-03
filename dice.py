#!/usr/bin/env python3.4
import random
import sys

def main():
    try:
        dice = eval(input('How many dice do you want to cast:  '))
        max_val = eval(input('what is the max value of your dice:  '))
        throw_dice(dice, max_val)
    except:
       print ('Please enter a number') 
       quit 
    
def throw_dice(dice, max_val):
    for die in range(dice):
        throw = (random.randint(1,max_val))
        numbers = str(throw)
        print ("your throw is: " + numbers)
        
main()    
