#Name:A.Haricharan
#This is my personal_info project

#welcome message
print("*************************************")
print("welcome to my personal info program")
print("*************************************")
#messages
#stores names 
NAME="Hari charan"
#stores numbers
AGE= 19
#stores city names
CITY="anantapur"
#stores hobbys
HOBBY="playing games"

#calculating my age in months
AGE_month=AGE * 12

#get user input aand basic validation

print("_______________________")
print("FAVORITE FOOD")
print("________________________")
favorite_food=input("what is your favorite food?")
while  favorite_food=="":
    print("please enter your favorite food.")
    favorite_food=input("enter you favorite food?")
   
favorite_color=input("what is your favorite color?")
while favorite_color=="":
    print("please enter your favorite color:")
    favorite_color=input("enter your favorite color?")

#personal information

print("__________________________")
print("PERSIONAL INFORMATION")
print("___________________________")
print(f"NAME    :     {NAME}")
print(f"AGE     :     {AGE}years({AGE_month})months")
print(f"CITY    :     {CITY}")
print(f"HOBBY   :     {HOBBY}")
print("-----------------------------")

#Goodbye Message


print("Thakyou for using this program!")
print("Good Bye!")



    

   


