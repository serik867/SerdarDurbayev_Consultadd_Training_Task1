# After the verification of the user, it must show a welcome note, refer to “welcome_note.txt” file.
# After showing the note It should ask for a choice whether you wanted to get in or not.
# For choice program should take input “Yes” or “No”.
# If choice = “Yes”: It should move forward and show the instructions of the game, refer to “game_instruction.txt”. 


# If choice = “No”: It should terminate the program.

from authenticate_data import authenticate_user
from river_size import riverSizes
from take_matrix import take_matrix_values

import random
import collections


def choice():
    response=input("do you want to play? (Yes/No): ")
    if response=="Yes":
        with open("game_instruction.txt","r") as f:
            content=f.read()
            print(content)

    else:
        quit()


def load_game():
    if authenticate_user():
        with open("welcome_note.txt","r") as f:
            content=f.read()
            print(content)
        choice()
        if press_P():
            matrix = take_matrix_values()
            show(matrix)
            result = riverSizes(matrix)
            while True:
                
                try:
                    enter_river_size=[int(i) for i in input("Enter river sizes seperate by comma: ").split(',')]
                    if collections.Counter(result)==collections.Counter(enter_river_size):
                        print("You Win")
                        break
                    else:
                        raise ValueError
                except ValueError:
                        print("Sorry,Not correct. Try Again")

            #print(enter_river_size)
           
            #print(result)
        
    else:
        return False

def press_P():
    play=input("Press 'P' for Play: ")  
    while True:      
        try:
            if play!='P':
               raise ValueError
            else:
                return True
        except ValueError:
            play =input("You Entered the wrong choice, Enter 'P' to play: ")

def show(matrix):
        for raw in matrix:
                print(raw)



load_game()