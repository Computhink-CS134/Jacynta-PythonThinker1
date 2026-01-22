import math
# recap 1
# blue = 5
# red = 3
# green = 4

# qtyblue = 2
# qtyred = 1  
# qtygreen = 3

# total = (blue * qtyblue) + (red * qtyred) + (green * qtygreen)
# print(total)

# name = input("What is your name? ")
# food = input("What is you favourite food? ")

# sentence = name + " likes to eat " + food
# print(sentence)


## Challenge 1: ask for hobby, then output {name} likes to {}
# name = input("What is your name? ")
# hobby = input("What is your hobby? ")

# sentence = name + " likes to " + hobby
# print(sentence)


## Challenge 2: ask for which is favourite country to go holiday, then output, {name} would like to go to {place}
# name = input("What is your name? ")
# fav_country = input("What is your favourite country to go holiday? ")

# sentence = name + " would like to go to " + fav_country
# print(sentence)



# num1 = input("What is your 1st number? ")
# num2 = input("What is your 2nd number? ")
# num3 = int(num1) + int(num2)
# print(num1 + " + " + num2 + " = " + str(num3))


## Task 3: Type conversion, math, and string concatenation

# **Task 3a**:
# 1. Ask the user for their current age using input(). Convert this
# to an integer.
# 2. Add 1 to their age and convert it back to a string.
# 3. Then print a message saying "Next year, you will be [age+1]
# years old."

# age = input("what is your current age? ")
# nxt_age = int(age) + 1
# print("Next year, you will be " + str(nxt_age) + " years old.")


# **Task 3b**:
# 1. Use input() to ask the user for a number. Convert this number
# from a string to an integer.
# 2. Double the number and convert it back to a string.
# 3. Print "Double your number is [double the number]".

# number = input("type a number: ")
# num_x2 = int(number) * 2
# print("Double your number is " + str(num_x2))


# **Task 3c**:
# 1. Use input() to ask the user for the year they were born and
# convert it to an integer.
# 2. Subtract the birth year from the current year (assume the
# current year as an integer) to find their age.
# 3. Convert the age back to a string and print "You are [age]
# years old".

# year = input("What is the year you were born in? ")
# c_year = 2026 
# age = c_year - int(year)
# sentence = f"You are {age} years old."
# print(sentence)

# ---------------------------------------------------------------


# create an email address for a person
# format is firstname.lastname2018@gmail.com
# ask for firstname, lastname and birth-year

# first_name = input("What is your first name? ")
# last_name = input("What is your surname? ")
# year = input("What year were you born in? ")
# email = f"{first_name}.{last_name}{year}@gmail.com"
# print(f"Your email is {email}")

# Exercise 8: Area of a Circle width 
# Write a program to ask the user for the radius of a circle, convert it to
# a float, calculate the area using the formula (area = 3.14 * r^2), and
# display the result using . Example:
# Input: radius = 7
# Output: "The area of the circle is 153.86."

radius = input("What is the radius of the circle? ")
area = math.pi * int(radius) ** 2
sentence = f"The area of the circle is {round(area, 2) }"
print(sentence)

# num = 10
# squareofnum = num ** 2

