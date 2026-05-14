# # Lesson 14 - Advanced Projects with Lists

# ## Recap 1: Die Rolling Simulator​
# ### 1a
# Create a program that simulates the rolling of a die 5 times by storing each roll in a list.​

# At the end of the 5 rolls, print the list.​

# Example output:​ [4, 6, 5, 3, 4]​

# Import the ‘random’ library​

# Create an empty list called ‘rolls’​

# Using a ‘for’ loop, and the ‘random.randint()’ function, append a​
# random number generated into the list. Repeat 5 times.​

# Print the ‘rolls’ list.

# import random
# rolls = []

# for i in range(5):
#     number = random.randint(1, 6)
#     rolls.append(number)
# print(rolls) 



# ### 1b
# Using a ‘for’ loop, expand your answer in Recap 1a to add up all the numbers in the list generated.

# Example Output:​
# [4, 6, 5, 3, 4]​
# Sum: 22​

# Create a variable ‘sum’ with the value of 0.​

# Using a ‘for’ loop, loop through the ‘rolls’ list:​ Add each item in the list into the variabl‘sum’​.

# Print the sum of all values in the list using string concatenation.

# import random
# rolls = []

# for i in range(5):
#     number = random.randint(1, 6)
#     rolls.append(number)
# print(rolls) 

# total = 0
# for i in range(len(rolls)):
#     total += rolls[i]

# print(f"Sum: {total}")

# ## Task 1: Printing Parallel Lists​
# Create 2 parallel lists with 4 values each.​

# fruits: List of fruits​
# prices: List of prices of the fruits​

# Use a for loop to print each fruit with its price in this format:​
#  costs $.

# fruits = [
#     "Apple",
#     "Banana",
#     "Grapes",
#     "Strawberry",
# ]

# prices = [
#     2,
#     4.50,
#     7.90,
#     8.70,
# ]

# for i in range(len(fruits)):
#     print(f"{fruits[i]} costs ${prices[i]}.")

# ## Task 2: Inventory Stock Checker​
# ### 2a
# Create a program that: ​
# checks a supermarket’s inventory stock levels and ​allows the user to search for an item.​

# Loop through the given lists to check the status of the stock, if the stock is:​

# Equal to 0 → Status: Out of Stock​
# Less than 10 → Status: Low Stock​
# 10 or more → Status: Well Stocked​

# Print the result in this format:​
# Item:  | Stock:  | Status: ​

# items = ["Apple", "Milk", "Bread", "Egg", "Chocolate"]
# stock = [15, 0, 8, 25, 3]

# for i in range(len(stock)):
#     if stock[i] == 0:
#         status = "Out of stock"
#     elif stock[i] < 10:
#         status = "Low stocked"
#     else:
#         status = "Well stocked"
#     print(f"Item: {items[i]} | Qty: {stock[i]} | Status: {status}")

# ### 2b
# Ask the user to input an item to
# check.​
# Check if the item is in the list.​
# 1. If the item is in the list:​
# - Find its index​
# - Print the result in this format:​
# - Result: We have  (s) remaining.​
# 2. If the item is not in the list:​
# - Print an error message​
# - Error: Item not found in database.

# user = input("What item do you want to check? ")

# if user in items:
#     number = items.index(user)
#     print(f"We have {stock[number]} remaining.")
# else:
#     print("Error: Item not found in database.")
    

# ## Task 3: Bookshop Shopping List​
# ### 3a​
# Create a program that:​
# - add items to a shopping list​
# - calculate their costs​
# - print a receipt​

# 1. Print the current shopping list.​
# shopping_list = ["Pens", "Pencils", "Erasers", "Notebooks"]​

# 2. Ask the user how many more items they
# want to buy.​

# 3. Use a for loop to ask what the items are and append it to the shopping list.​

# 4. Print the updated shopping list.​

# shopping_list = ["Pens", "Pencils", "Erasers", "Notebooks"]
# number = int(input("How many more items do you want to buy? "))

# for i in range(number):
#     item = input(f"What is item {i + 1}? ")
#     shopping_list.append(item)

# print(shopping_list)

# ### 3b
# 1. Create an empty list to store the
# prices: price_list​

# 2. For each item in the shopping
# list:​
# - Ask for price​
# - Ask for quantity​
# - Multiply the price and quantity and append it to the price list​

# 3. Print the price list

# price_list = []

# for i in range(len(shopping_list)):
#     price = int(input(f"What is the price of item {i + 1}?"))
#     qty = int(input(f"What is the quantity of item {i + 1}? "))
#     price_list.append(price * qty)

# print(price_list)
# print(shopping_list)

# ### 3c
# Use a for loop to print the shopping list and price list following
# the format.

# Add up the total cost in the price list and print it.


# ----------------------------------------------
# ## Task 4: Scissors Paper Stone​
# Create a scissors paper stone game, the user plays against a computer that picks randomly.

# ### 4a
# Create a list of possible moves:​
# ["scissors", "paper", "stone"]​

# Initialize 2 variables:​
# - player_score​
# - computer_score​

# Use a while loop to ask for the user’s move while player_score and computer_score is less than 3.​
# ----------------------------------------------------
# ### 4b
# In the while loop:​

# 1. Import the random library, use random.choice() to let the computer pick from the move list and print it.​

# 2. Compare the user’s choice and computer’s choice to determine the result.​

# 3. Increment player_score or computer_score depending on the result.​

# 4. Print the result and scores.
# -------------------------------------------------------
# ### 4c
# 1. Print the final result after the while loop has ended.​

# 2. Modify the loop to check for invalid choices.​
# ----------------------------------------------------------------------

# import random
# moves = ["scissors", "paper", "stone"]

# player_score = 0
# computer_score = 0

# while player_score < 3 and computer_score < 3:
#     player = input("Pick scissors, paper or stone: ")
#     computer = random.choice(moves)
#     print(f"Computer chose: {computer}")

#     if player == computer:
#         print("It's a draw!")
#         print(f"Player's score: {player_score} | Computer's score: {computer_score}")
#     elif (player == "scissors" and computer == "paper") or (player == "paper" and computer == "stone") or (player == "stone" and computer == "scissors"):
#         print("Player wins this round!")
#         player_score += 1
#         print(f"Player's score: {player_score} | Computer's score: {computer_score}")
#     else:
#         print("Computer wins this round!")
#         computer_score += 1
#         print(f"Player's score: {player_score} | Computer's score: {computer_score}")

# print(f"Player's score: {player_score} | Computer's score: {computer_score}")

# if player_score > computer_score:
#     print("Player won!")
# else:
#     print("Computer won!")


