#! /usr/bin/python
# -*- coding: utf-8 -*-

from structures import *
from os import system, name           
            

def clear():   
    # for windows 
    if name == 'nt': 
        _ = system('cls')  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 
        

def show_intro():
    print("___________________________________________________________________")
    print("|                                                                 |")
    print("|    XXXX  X   X    XX    X     X  X   XXXXX   X    XX    X   X   |")
    print("|    X     X   X   X  X   X     X  X     X     X   X  X   XX  X   |")
    print("|    XXX   X   X   X  X   X     X  X     X     X   X  X   X X X   |")
    print("|    X      X X    X  X   X     X  X     X     X   X  X   X  XX   |")
    print("|    XXXX    X      XX    XXX    XX      X     X    XX    X   X   |")
    print("|_________________________________________________________________|")
    print("\n\n")

if __name__ == "__main__":
    
    clear()
    show_intro()
    
    n = int(input("Number of players:\t"))
    max_level = int(input("Max level:\t"))
    number_of_iterations = int(input("Number of iterations:\t"))
    filename = input("file to save: ") + str(".txt")
    
    if n<1 or n%2!=0:
        raise ValueError("Wrong input parameter: n={:}. The number of players have to be nonnegative and odd!".format(n))

    elif max_level<1:
        raise ValueError("Wrong input parameter: max level = {:}.\
                        The maximum level have to be nonnegative!".format(max_level))

    elif number_of_iterations<1:
        raise ValueError("Wrong input parameter: mx number of iterations{:}.\
                        The number of iterations have to be nonnegative!".format(number_of_iterations))

    EG = EvolutionGame( n, max_level, number_of_iterations)
    EG.run()   
    EG.save(filename)
        
        
        
        
        