# # Lesson 8 - Importing Libraries, Boolean & Conditions

import time 
import random

# ## Recap 1: Product of 5 numbers

# Write a program to calculate the product (multiplication) of 5
# numbers.

# 1. Using a for loop, ask the user for 5 numbers one at a time.
# 2. Calculate the multiplication for these 5 numbers and print
#    it out.
   
# ---------------------------------------------------------------
# total = 1

# for i in range(1, 6):
#     num = int(input(f"What is number {i}? "))
#     total *= num

# print(f"Total: {total}")




# ## Task 1: 'time' library

# **Task 1a**:
# Import the 'time' library and make use of the 'time.sleep()'
# function to create a 10 seconds countdown timer that counts
# to 1, printing the number of seconds remaining every second.


# for i in range(10, 0, -1):
#     print(f"{i} seconds left")
#     time.sleep(1)
# print("Time's up!")

# **Task 1b**:
# Modify your code from Task 1a to include an 'input()' function
# asking the user for the number to countdown from, before
# counting down every second from the number given by the user.

# number = int(input("Choose a number: "))

# for i in range(number, 0, -1):
#     print(f"{i} seconds left")
#     time.sleep(1)


# ---------------------------------------------------------------

# ## Task 2: 'random' library

# **Task 2a**:
# Import the 'random' library and create a program that randomly
# output a number between 1 to 6

# print(random.randint(1, 6))

# **Task 2b**:
# Using the 'random' library, create 20 numbers between 0 and
# 9999 randomly.

# import random

# for i in range(1, 20):
#     print(random.randint(0, 9999))



# ---------------------------------------------------------------

# ## Task 3: Print Boolean Value & Condition

# **Task 3a**:
# Assign a boolean value to a variable and print it.

# bool1 = True
# print(bool1)


# **Task 3b**:
# Create 2 variables both holding the "True" boolean.
# Print out the result of comparing the 2 variables using
# the "==" operator.

# bool1 = True
# bool2 = True
# print(bool1 == bool2)



# **Task 3c**:
# Now, assign 1 variable the "True" boolean, and assign another
# variable the "False" boolean.

# Print out the result of comparing the 2 variables using
# the "==" operator.


# bool1 = True
# bool2 = False
# print(bool1 == bool2)


# ---------------------------------------------------------------

## Task 4: Random Number Guessing Game

# Create a simple program to guess a random number:​
# - Create a variable called ‘random_num’ and assign a random integer between 1 to 10.​
# - Ask the user for an input 'guess'​

# Your program will check if ‘guess’ is equal to 'random_num'.​

# The output should be one of the following:​
# - If the answer is correct – output "Correct!" ​
# - If the answer is wrong – output "Wrong!​

# random_num = random.randint(1, 10)
# guess = int(input("Type a random number: "))

# if random_num == guess:
#     print("Correct!")
# else:
#     print("Wrong!")



# ---------------------------------------------------------------

## Task 5: Math Question Generator

# Create a simple program that generate 2 numbers
# between 1 and 50 that the user must add together.​

# Ask the user to input the answer.​

# The output should be one of the following:​
# - If the answer is correct – output "Correct!"​
# - If the answer is wrong – output "Wrong!​
# ---------------------------------------------------------------
# num1 = random.randint(1, 50)
# num2 = random.randint(1, 50)

# correct_ans = num1 + num2
# user_ans = int(input(f"{num1} + {num2} =\n"))

# if user_ans == correct_ans:
#     print("Correct!")
# else:
#     print("Wrong!")

## Task 6: Random Multiplication Quiz

# Create a program that generates a certain number of
# random multiplication questions.​
# 1. Ask the user to input how many questions should be asked.​
# 2. Multiply 2 random numbers between 1 and10 and save the 'answer'.​
# 3. Ask the user to input their answer, 'user_answer'.​
# 4. Check if 'user_answer' is equal to 'answer'.

# The output should be one of the following:​
# - If the answer is correct – output "Correct!" ​
# - If the answer is wrong – output "Wrong!​

# num_Q = int(input("How many questions would you like? "))

# for i in range(num_Q):
#     num1 = random.randint(1, 10)
#     num2 = random.randint(1, 10)

#     user_ans = int(input(f"{num1} x {num2} = ?\n"))
#     ans = num1 * num2

#     if user_ans == ans:
#         print("Correct!")
#     else:
#         print("Wrong!")

# ---------------------------------------------------------------

# ## Task 7: Even or Odd Checker

# Write a program that asks the user to enter a number. The
# program then tells the user whether the number is even
# (True) or odd (False).

# Your program needs to:
# 1. Ask user for an integer input.
# 2. Check if there is any remainder when user input is divided
#    by 2 (using '%').
# 3. Print 'True' if number is even, otherwise print 'False'.

# num = int(input("Input a number:\n"))
# r = num % 2

# if r == 0:
#     print("The number is even.")
# else:
#     print("The number is odd.")
# ---------------------------------------------------------------

## Task 8: Multiple Check Program

# Create a program where the user enters 2 numbers. The
# program then checks if the first number is a multiple of
# the second number.

# Your program needs to:
# 1. Get user to input 2 numbers.
# 2. Check if there is any remainder when number #1 is divided
#    by number #2
# 3. Print 'True' if number #1 is a multiple of number #2,
#    otherwise print 'False'.

# num1 = int(input("Type in a 1st number:\n"))
# num2 = int(input("Type in a 2nd number:\n"))

# if num1 % num2 == 0:
#     print("True")
# else:
#     print("False")
# ---------------------------------------------------------------

# ## Challenge 1: Multiple Check Program

# Create a console-based quiz game that tests the user on general
# knowledge questions. The game will keep track of the user’s score
# and provide immediate feedback on each question.​

# Hints:​
# - Your input() is always a string, andupper or lower case matters.​
# - i.e. "Hello" != "hello"​
# - Use .lower() or .upper() to change to a same case.​

# ---------------------------------------------------------------

# ## Challenge 2: Guess the Number Game

# Write a Python program that generates a random number between 1 and 100
# and then allows the user to guess what the number is. The program should give
# the user feedback on whether their guess is too high, too low, or correct. The
# user should have a limited number of attempts to guess the number correctly.​

# Advanced features:​

# 1. Allow the user to choose a difficulty level at the beginning of the
# game, which will adjust the range from which the random number
# is generated, or the number of attempts allowed.​

# 2. Implement a scoring system where the user starts with a certain
# score, and points are deducted based on the number of attempts
# taken to guess the number correctly. The fewer attempts used, the
# higher the final score.​

# 3. After a game finishes, whether the user guesses the number or
# runs out of attempt, offer them the option to play again.​

# 4. Provide a hint after a certain number of incorrect guesses, such as
# indicating if the guess is within a certain range of the target
# number (e.g. within 10 numbers higher or lower).​# Lesson 8 - Importing Libraries, Boolean & Conditions



