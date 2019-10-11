#You need to write a python program file “read_csv.py”  in which you need to write a function that 
#reads the given CSV file “Task_Training_Data.csv”, fetch the data and only return the Name and Email 
#of all the entries.
import csv

def readCSV():
    myList=[]

    with open("Task_Training_Data .csv","r") as f:
        readCSV = csv.reader(f)
        myList=[{'name':row[0],'email': row[1]} for row in readCSV if row[0]!='Name' or row[1]!='Email']
    
    return myList

#print(readCSV())