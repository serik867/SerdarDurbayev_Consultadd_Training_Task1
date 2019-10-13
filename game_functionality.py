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


def choice():   # Select Yes or No and show game_instruction.txt--> if No quit game
    response=input("Do you want to get in? (Yes/No): ")
    if response=="Yes":
        with open("game_instruction.txt","r") as f:
            content=f.read()
            print(content)
    else:
        quit()


def load_game():  #main function 
    if authenticate_user():
        with open("welcome_note.txt","r") as f:
            content=f.read()
            print(content)
        choice()
        if press_P():
            matrix = take_matrix_values()
            show(matrix)
            result = riverSizes(matrix)
            count=0
            while True:
                count+=1
                try:
                    enter_river_size=[int(i) for i in input("Enter river sizes seperate by comma: ").split(',')]
                    if collections.Counter(result)==collections.Counter(enter_river_size):
                        print("You Win")
                        break
                    else:
                        if count==3:
                            print("Sorry! You lost!!!")
                            break
                        raise ValueError
                except ValueError:
                    print("Sorry,Not correct. Try again: ")
                    
    else:
        return False

def press_P():  # make selection Play or not to Play with try except 
    play=input("Press 'P' for Play: ")  
    while True:      
        try:
            if play!='P':
               raise ValueError
            else:
                return True
        except ValueError:
            play =input("You Entered the wrong choice, Enter 'P' to play: ")

def show(matrix):   #show matrix in raws
        for raw in matrix:
                print(raw)



load_game()