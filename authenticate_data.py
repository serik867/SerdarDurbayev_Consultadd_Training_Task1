#Write a separate python file “authenticate_data.py” in which the program takes Name and Email 
#from the user as input and matches the data returned from the first read_csv.py file that is 
# Name and Email.
#If Name and Email Matches with the data returned from “read_csv.py” then the user is allowed to move 
#forward otherwise it should give maximum two chances and after 2 wrong attempts, it should exit.
from read_csv import readCSV

def clean_data(): # clean data and return list of dictionaries
    list_dict=readCSV()
    for element in list_dict:
        element['name']=element['name'].strip()
        element['email']=element['email'].strip()
    return list_dict

def check_user(name,email): # check name and email if it is match return True else False
    list_csv=clean_data()
    try:
        result= next(item for item in list_csv if item["name"] == name)
        if result['email']==email:
            return True
        else:
            return False
    except:
        return False



def authenticate_user(): # authenticating a user, try two time only
    count=1
    while count<3:
        name = input("Enter your name: ")
        email = input("Enter your email: ")

        if check_user(name,email):
            print("file authenticcate")
            return True
        elif count==2:
            print("Sorry!!!")
            count+=1
        else:
            print("Try again")
            count+=1


        

