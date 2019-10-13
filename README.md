# Guess River Size 

Guess river size on two dimensional array. 

##Installation

Python3 

## Usage

```python

#run

python3 game_functionality.py
```

## Instructions and Functions

### Module: authentication_data.py

The `authenticate_user()` function takes Name and Email from the user as input and matches the data returned from the first *read_csv.py* file that is Name and Email.If Name and Email Matches with the data returned from “read_csv.py” then the user is allowed to move forward otherwise it should give maximum two chances and after 2 wrong attempts, it should exit. If Name and Email matches `return True`

### Main function: game_functionality.py

The `load_game()` function, after the verification of the user, it shows a welcome note, refer to “welcome_note.txt” file. After showing the note It asks for a choice whether you wanted to get in or not.For choice program should take input “Yes” or “No”. If choice = “Yes”: It moves forward and show the instructions of the game, refer to “game_instruction.txt”. After that user select how many raws and colunms want to enter as a two dimensional array. After that user enter elements of that array as a 0 or 1.
Ther is another helper functions(modules) `take_matrix.py-->take_matrix_values()` that takes array elements one by one. Second is `river_size.py-->riverSizes(matrix)` that makes calculation of river sizes of matrix(array). 

## Game Instructions:

Main Python program: 


You are given a two-dimensional array (matrix) of potentially unequal height and width
containing only Os and 1s. Each 0 represents land, and each 1 represents part of a river.
A river consists of any number of 1s that are either horizontally or vertically adjacent
(but not diagonally adjacent). The number of adjacent 1s forming a river determine its
size. Write a function that returns an array of the sizes of all rivers represented in the
input matrix. Note that these sizes do not need to be in any particular order.

Now from returned array of sizes You need to print "Guess the size of River" on each index, take input from user as guesses for each entry.

If all entered sizes match then show You are the winner.
User has three chances to guess.



Sample input:
[[1,0,0,1,0]
[1,0,1,0,0]
[0,0,1,0,1]
[1,0,1,0,1]
[1,0,1,1,0]

Sizes of River = [1,2,2,2,5] note:  This should not be visible to the user , this a reference for accuracy of output. 







