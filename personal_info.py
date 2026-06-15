# Name: A. Haricharan

# Project: Personal Information Manager

# Welcome Message

print("====================================")
print(" Welcome to My Personal Information Manager ")
print("====================================")

# Static Information

# Stores my name

name = "Hari Charan"

# Stores my age

age = 19

# Stores my city

city = "Anantapur"

# Stores my hobby

hobby = "Playing Games"

# Calculate age in months

age_months = age * 12

# Get User Input

print("\nEnter Your Favorite Information")

favorite_food = input("What is your favorite food? ")

# Input validation for favorite food

while favorite_food.strip() == "":
print("Favorite food cannot be empty.")
favorite_food = input("Please enter your favorite food: ")

favorite_color = input("What is your favorite color? ")

# Input validation for favorite color

while favorite_color.strip() == "":
print("Favorite color cannot be empty.")
favorite_color = input("Please enter your favorite color: ")

# Display Information

print("\n====================================")
print("      PERSONAL INFORMATION")
print("====================================")

print(f"Name           : {name.title()}")
print(f"Age            : {age} years")
print(f"Age in Months  : {age_months} months")
print(f"City           : {city.title()}")
print(f"Hobby          : {hobby.title()}")

print("------------------------------------")

print(f"Favorite Food  : {favorite_food.title()}")
print(f"Favorite Color : {favorite_color.title()}")

print("====================================")

# Goodbye Message

print("\nThank you for using this program!")
print("Good Bye!")



    

   


