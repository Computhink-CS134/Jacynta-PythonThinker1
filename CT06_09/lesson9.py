# Lesson 9 - If Statements

# Recap 1: Dice Roll Simulator
# Generate and print 3 random numbers between 1 and 6, followed
# by an output of 'True' if all 3 numbers are either even or odd.

# Example:
# 1st number: 6
# 2nd number: 4
# 3rd number: 6
# All numbers are even/odd: True

# 1. Import the 'random' library
# 2. Create 3 variables to hold a random number that is between
#    1 and 6, generated using 'random.randint()'
# 3. Using string concatenation, print the generated number for
#    each of the 3 numbers
# 4. Using the '%' and '==' operator, check if each number is
#    divisible by 2 (remainder = 0)
# 5. Using multiple '==' operators, a new variable 'all_even_odd'
#    should be assigned 'True' if all 3 numbers are either all
#    even or all odd numbers.
# 6. Print if "All numbers are even/odd" is 'True' or 'False'

# --------------------------------------------------------------
# import random
# num1 = random.randint(1, 6)
# num2 = random.randint(1, 6)
# num3 = random.randint(1, 6)

# print(f"1st number: {num1}")
# print(f"2nd number: {num2}")
# print(f"3rd number: {num3}")

# all_even_odd = False
# if num1 % 2 == 0 and num2 % 2 == 0 and num3 % 2 == 0:
#     all_even_odd = True
# elif num1 % 2 == 1 and num2 % 2 == 1 and num3 % 2 == 1:
#     all_even_odd = True

# print(f"All numbers are even/odd: {all_even_odd}")

# # Task 1: Flowchart for Library Reminder
# Draw out the flowchart (on a piece of paper) of a program
# to remind borrowers to return their books

# 1. Ask the user to input the number of days a book has been
#    borrowed
# 2. If the book has been borrowed for more than 25 days:
#     print "Remember to return your book!"

# done
# --------------------------------------------------------------

# # Task 2: Converting Library Reminder flowchart
# #         into code
# Translate the flowchart that you have drawn (shown on screen)
# into Python code.

# 1. Ask the user to input the number of days a book has been
#    borrowed
# 2. If the book has been borrowed for more than 25 days:
#     print "Remember to return your book!"

# Hint: remember to typecast your variables!

# num_days = int(input("How many days have you borrowed your book?\n"))

# if num_days > 25:
#     print("Remember to return your book!")


# # Task 3: Apple Shop
# **Task 3a**:
# Draw out the flowchart (on a piece of paper) of a program for
# the user to buy apples and calculate the price.

# Each apple costs $1

# 1. Ask the user how many apples they want to buy
# 2. If the user wants to buy more than 10 apples:
#    print "You will get a 10% discount for buying that many
#    apples!"
# 4. Print the price of the purchase

# **Task 3b**:
# Translate the flowchart that you have drawn (shown on screen)
# into Python code.

# num_apples = int(input("How many apples do you want to buy?\n"))

# if num_apples > 10:
#     print("You will get 10% discount for buying so many apples. ")
#     price = num_apples * 0.9 
#     print(f"The price you need to pay is: {price}.")


# --------------------------------------------------------------

# # Task 4: Fruits Shop
# **Task 4a**:
# Draw out the flowchart (on a piece of paper) of a program for
# the fruit shop, "FruitiFresh". FruitiFresh sells 2 fruits,
# Apple & Orange with the following pricing scheme:

# Apple:
# 1 Apple = 60 cents
# If buy more than 5 apples, get 10% discount for all apples

# Orange:
# 1 Orange = 90 cents
# If buy more than 5 oranges, get 10% discount for all oranges

# You want to create a program that:
# 1. Asks the user for the number of apples and oranges they
#    want to buy.
# 2. Print total price of the fruits

# **Task 4b**:
# Translate the flowchart that you have drawn (shown on screen)
# into Python code.

# num_apples = int(input("How many apples do you want to buy?\n"))
# num_oranges = int(input("How many oranges do you want to buy?\n"))

# if num_apples > 5:
#     apple_price = num_apples * 0.6 * 0.9
# else:
#     apple_price = num_apples * 0.6

# if num_oranges > 5:
#     orange_price = num_oranges * 0.9 * 0.9
# else:
#     orange_price = num_oranges * 0.9

# total_price = round(orange_price + apple_price, 2)

# print(f"The total price is ${total_price}")


# --------------------------------------------------------------

# Task 5: Flowchart for Temperature Monitor
# You are analyzing daily temperature readings over a week.
# Write a program to count how many days had a temperature
# that is greater than 30.

# Draw out the flowchart (on a piece of paper) of the above
# program.

# 1. Start with creating and assigning the variable
#    "positive_days" to 0 before the loop.
# 2. Use a for loop to iterate through each day of the week
#    (7 times)
# 3. In each iteration the loop, prompt the user to input the
#    temperature for the day.
# 4. Use an 'if' condition to check if the temperature is greater
#    than 30. If so, increase the variable 'positive_days' by
#    1
# 5. After the loop, print the count of days with temperature
#    higher than 30.

# --------------------------------------------------------------

# # Task 6: Converting Temperature Monitor flowchart
# #         into code
# Translate the flowchart that you have drawn (shown on screen)
# into Python code.

# 1. Start with creating and assigning the variable
#    'positive_days' to 0 before the loop.
# 2. Use a 'for' loop to iterate through each day of the week
#    (7 times)
# 3. In each iteration, prompt the user to input the
#    temperature for the day.
# 4. Use an 'if' condition to check if the temperature is greater
#    than 30. If so, increase the variable 'positive_days' by
#    1
# 5. After the loop, print the count of days with temperature
#    higher than 30.

# --------------------------------------------------------------

# # Task 7: Summing Positive Numbers
# **Task 7a**:
# Draw out the flowchart (on a piece of paper) of a program
# that will calculate the total sum of **savings** 
# (include in total only if savings for that day is positive)
# from a week's worth of data provided by the user every day.

# 1. Create and assign 'sum' variable to 0.
# 2. Use a 'for' loop to iterate through each day of the week
#    (7 times)
# 3. In each iteration, prompt the user to input the
#    savings for the day.
# 4. Use an if condition to check if the savings is greater
#    than 0. If so, increase the variable 'sum' by
#    that day's savings.
# 5. After the loop, print the sum of savings for that week

# **Task 8b**:
# Translate the flowchart that you have drawn (shown on screen)
# into Python code.

# --------------------------------------------------------------

# # Task 9: Experience Survey
# **Task 9a**:
# Draw out the flowchart (on a piece of paper) of the following:

# As part of a data analysis, you would like to create a program
# that surveys 10 hotel guests on their hotel experience based
# on a rating from 1 to 5.

# The program will keep a tally of the number of "desirable"
# ratings (higher than 3), and the number of "undesirable"
# ratings (3 and lower).

# The program will print the number of desirable and undesirable
# ratings after surveying 10 guests.

# 1. Create 2 counter variables, "desirable" and "undesirable",
#    assigning each of them the value of 0
# 2. Create a 'for' loop that repeats 10 times
# 3. In each interation, ask the hotel guest to rate between
#    1 to 5.
# 4. If the rating given is higher than 3, increase the
#    "desirable" variable by 1
# 5. If the rating given is 3 and lower, increase the "undeisrable"
#    variable by 1.
# 6. At the end of the 'for' loop, print the result in the
#    following format:

#    Desirable ratings: <results>, Undesirable ratings: <results>

# **Task 9b**:
# Translate the flowchart that you have drawn (shown on screen)
# into Python code.












