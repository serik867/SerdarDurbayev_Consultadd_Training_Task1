import random

def show(matrix):     

    for i in range(len(matrix)):
        print(matrix[i])

#arr=[[random.randint(0,1) for i in range(4)] for i in range(6)]
#show(arr)

def take_matrix_values():
    weight=int(input("Enter please colunm size of array: "))
    height=int(input("Enter please raw size of array: "))
    zero_array=[[0 for i in range(weight)] for i in range(height)]
    count=0
    show(zero_array)
    while count<(weight*height):
        for i in range(len(zero_array)):
            for j in range(len(zero_array[i])):
                while True:
                    try:
                        element= int(input("Enter 0 or 1 row {0} and column {1} : ".format(i,j)))
                        if element==1 or element==0:
                            zero_array[i][j]=element
                            count+=1
                            break
                        else:
                            raise ValueError
                    except ValueError:
                            print("Enter only 1 or 0!!!")  
                    # show(zero_array)  
    return zero_array

# print(take_matrix_values())