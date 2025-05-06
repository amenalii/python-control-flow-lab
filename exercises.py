""" -------------------------------------------------------------- Exercise 0 --------------------------------------------------------------"""
# Exercise 0: Example
#
# This is a practice exercise to help you understand how to write code "inside" a provided Python function.
#
# We'll create a function that checks a condition and prints a specific greeting message based on that condition.
#
# Requirements:
# - The function is named `print_greeting`.
# - Inside the function, declare a variable `python_is_fun` and set it to `True`.
# - Use a conditional statement to check if `python_is_fun` is `True`.
# - If `python_is_fun` is `True`, print the message "Python is fun!"

def print_greeting():
    # Your code goes here. Remember to indent!
    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")

# Call the function
#print_greeting()


""" -------------------------------------------------------------- Exercise 1 --------------------------------------------------------------"""
# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.

def check_letter():
    letter = input("Enter a letter ").upper()  # .upper() can be attached to the input function to convert the input to uppercase. dont need seperate line.
        # The isalpha() method checks if all characters in the string are alphabets.
    if len(letter) == 1 and letter.isalpha(): 
        if letter in "AEIOU":  
            print(f"The letter {letter} is a vowel.")
        else:
            print(f"The letter {letter} is a consonant.")
    else:
        print("Invalid input!")  
   
# Call the function
#check_letter()


""" -------------------------------------------------------------- Exercise 2 --------------------------------------------------------------"""
# Exercise 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting age.
# - Print a message indicating whether the user is eligible to vote based on the entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# - Use a conditional statement to check if the age meets the minimum voting age requirement.

""" Code below works but does give error when input is not number. """
# def check_voting_eligibility():
#     age = input("Please enter your age: ").int()   #.int() is not a method of the input function. 

#     age = int(input("Please enter your age: ")) #input needs to placed inside the int() function to convert the input to an integer as .int() only works on strings 
    
#     if age <= 0:
#         print("Invalid age entered.")
#     elif age >= 18:
#         print("You are eligible to vote.")
#     else:
#         print("You are not eligible to vote yet.")


def check_voting_eligibility():
    age = input("Please enter your age: ")

    if age.isdigit(): # Will handle conversion error as str.isdigit() checks whether all characters in the string are numeric returning True if the string contains only digits and False otherwise.
        # Once we verify that entered age is a number, we can convert it to an integer
        age = int(age)
        # if age < 0:
        #     print("Invalid age entered.")           # This condition is no longer needed as the isdigit() method will not allow negative numbers to be entered.
        if age >= 18:
            print("You are eligible to vote.")
        else:
            print("You are not eligible to vote yet.")
    else:
        print("Invalid input! Please enter a valid age.")


# Call the function
# check_voting_eligibility()

""" -------------------------------------------------------------- Exercise 3 --------------------------------------------------------------"""
# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.

def calculate_dog_years():
    dog_age = input("Input a dog's age: ")

    if dog_age.isdigit():
        dog_age = int(dog_age)  
        if dog_age == 0:    # Only need to check for 0 since the isdigit() method will not allow negative numbers to be entered.
            print("Invalid age entered.")
        elif dog_age <= 2:
            print(f"The dog's age in dog years is {dog_age * 10}.")
        else:
            print(f"The dog's age in dog years is {20 + ((dog_age - 2) * 7)}.")
    else:
        print("Invalid input! Please enter a valid age.")

# Call the function
# calculate_dog_years()

""" -------------------------------------------------------------- Exercise 4 --------------------------------------------------------------"""
# Exercise 4: Weather Advice
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.

def weather_advice():
    is_cold = input("Is it cold outside? ").lower()  
    is_raining = input("Is it raining outside? ").lower()  

    if is_cold == "yes" and is_raining == "yes":
        print("Wear a waterproof coat.")
    elif is_cold == "yes" and is_raining == "no":
        print("Wear a warm coat.")
    elif is_cold == "no" and is_raining == "yes":
        print("Carry an umbrella.")
    elif is_cold == "no" and is_raining == "no":
        print("Wear light clothing.")
    else:
        print("Please answer with Yes or No.")


# Call the function
# weather_advice()


""" -------------------------------------------------------------- Exercise 5 --------------------------------------------------------------"""
# Exercise 5: What's the Season?
#
# Write a Python function named `determine_season` that figures out the season based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure to validate input formats and handle unexpected inputs gracefully.

def determine_season():
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    month = input("Enter the first three letters of the month (Jan - Dec): ").capitalize()  # .capitalize() can be attached to the input function to convert the input to uppercase. dont need seperate line.
    # month = month.capitalize() 
    # day = int(input("Enter the day of the month: ")) 

# Run checks for months and days
    if month not in months: 
        print("Invalid entry. Please check the month.")
        return
    else:
        day = int(input("Enter the day of the month: "))  


    if day > 31 or day < 1:
        print("Invalid entry. Enter a date between 1 and 31.")
        return
    

    # Dec 21 - Mar 19
    if (month == "Dec" and day >= 21) or (month in ["Jan", "Feb"]) or (month == "Mar" and day <= 19):  
        season = "Winter"

    # Mar 20 - Jun 20
    elif (month == "Mar" and day >= 20) or (month in ["Apr", "May"]) or (month == "Jun" and day <= 20):
        season = "Spring"

    # Jun 21 - Sep 21
    elif (month == "Jun" and day >= 21) or (month in ["Jul", "Aug"]) or (month == "Sep" and day <= 21):
        season = "Summer"

    # Sep 22 - Dec 20
    elif (month == "Sep" and day >= 22) or (month in ["Oct", "Nov"]) or (month == "Dec" and day <= 20):
        season = "Fall"
    # else:
    #    if day > 31 or day < 1:                                                                             
    #         print("Invalid entry. Please check the month and day.")
    #         return

    print(f"{month} {day} is in {season}.")




# Call the function
determine_season()
