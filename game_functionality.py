# After the verification of the user, it must show a welcome note, refer to “welcome_note.txt” file.
# After showing the note It should ask for a choice whether you wanted to get in or not.
# For choice program should take input “Yes” or “No”.
# If choice = “Yes”: It should move forward and show the instructions of the game, refer to “game_instruction.txt”. 


# If choice = “No”: It should terminate the program.

from authenticate_data import authenticate_user

def choice():
    response=input("do you want to play? (Yes/No): ")
    if response=="Yes":
        with open("game_instruction.txt","r") as f:
            content=f.read()
            print(content)

    else:
        pass


def load_game():
    if authenticate_user():
        with open("welcome_note.txt","r") as f:
            content=f.read()
            print(content)
            choice()
    else:
        return False




        


load_game()