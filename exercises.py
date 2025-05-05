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
check_voting_eligibility()

""" -------------------------------------------------------------- Exercise 3 --------------------------------------------------------------"""
