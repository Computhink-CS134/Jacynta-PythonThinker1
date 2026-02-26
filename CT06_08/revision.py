# print("Hello from lesson 8")

# # ===============================
# # PART B — FOR LOOPS
# # ===============================

# # Q21
# for i in range(3):
#     print(i)

# # A) 1 2 3
# # B) 0 1 2
# # C) 0 1 2 3
# # D) 1 2
# B ✅

# # Q22
# for i in range(2, 8, 2):
#     print(i)

# # A) 2 times
# # B) 3 times
# # C) 4 times
# # D) 5 times
# B ✅

# # Q23
# total = 0
# for i in range(1, 4):
#     total += i (total = total + i)
# print(total)

# # A) 6
# # B) 10
# # C) 4
# # D) 3
# A ✅

# # Q24
# for i in range(5, 1, -1):
#     print(i)

# # A) 5 4 3 2
# # B) 5 4 3 2 1
# # C) 4 3 2
# # D) 5 4 3
# A ✅

# # Q25
# s = ""
# for i in range(3):
#     s += "A"
# print(s)

# # A) A
# # B) AA
# # C) AAA
# # D) Error
# C ✅

# # Q26
# for i in range(1, 6, 2):
#     print(i)

# # A) 1 3 5
# # B) 1 2 3 4 5
# # C) 2 4 6
# # D) 1 3
# A ✅

# # Q27
# total = 1
# for i in range(1, 4):
#     total *= i
# print(total)

# # A) 6
# # B) 24
# # C) 4
# # D) 3
# A ✅

# # Q28
# for ch in "cat":
#     print(ch)

# # A) cat
# # B) c a t
# # C) c
# # D) Error
# B  ✅

# # Q29
# count = 0
# for i in range(4):
#     count += 2
# print(count)

# # A) 6
# # B) 8
# # C) 4
# # D) 2
# A ✅

# # Q30
# for i in range(3):
#     print("Hi" + str(i))

# # A) Hi
# # B) Hi0 Hi1 Hi2
# # C) Hi012
# # D) Error
# B ✅

# # Q31
# x = 0
# for i in range(1, 5):
#     x += 1
# print(x)

# # A) 4
# # B) 5
# # C) 3
# # D) 1
# A ✅

# # Q32
# for i in range(4, 0, -2):
#     print(i)

# # A) 4 2
# # B) 4 2 0
# # C) 3 1
# # D) 4
# A ✅

# # Q33
# s = ""
# for i in range(1, 4):
#     s += str(i)
# print(s)

# # A) 123
# # B) 6
# # C) 321
# # D) Error
# A ✅

# # Q34
# for i in range(10, 5, -1):
#     print(i)

# # A) 4 times
# # B) 5 times
# # C) 6 times
# # D) 3 times
# B ✅

# # Q35
# for i in range(0, 5):
#     if i % 2 == 0:
#         print(i)

# # A) 0 2 4
# # B) 1 3 5
# # C) 2 4
# # D) 0 1 2 3 4 


# # Q36
# x = 5
# for i in range(3):
#     x += i
# print(x)

# # A) 8
# # B) 9
# # C) 11
# # D) 6
# A ✅

# # Q37
# for i in range(1, 5):
#     print(i * 2)

# # A) 2 4 6 8
# # B) 1 2 3 4
# # C) 2 4 6
# # D) 8
# A ✅

# # Q38
# s = "A"
# for i in range(2):
#     s += s
# print(s)

# # A) AA
# # B) AAAA
# # C) AAA
# # D) Error
# B ✅

# # Q39
# total = 0
# for i in range(2, 6):
#     total += i
# print(total)

# # A) 14
# # B) 12
# # C) 10
# # D) 8
# A ✅

# # Q40
# for i in range(1, 4):
#     print(str(i) + "!")

# # A) 1! 2! 3!
# # B) 123!
# # C) 6!
# # D) Error
# A ✅



# ============================================================
# Question 1 — Total Spending Calculator
# ============================================================

# """
# Write a program that:

# 1. Asks the user how many items they bought.
# 2. Uses a for loop to ask the price of each item.
# 3. Calculates the total cost.
# 4. Prints:

# You bought X items.
# Total cost is $Y.

# Requirements:
# - Prices may include decimals.
# - Must use input()
# - Must use type conversion (int/float)
# - Must use accumulation (total += ...)
# - Must use string concatenation for printing.
# - Must round off to two decimal places for the total.
# """

# Example Input:
# 3
# 2.5
# 3
# 4.5

# Expected Output:
# You bought 3 items.
# Total cost is $10.0.

# number_items = int(input("How many items did you buy? "))
# number_items = number_items + 1
# price = 0
# total_price = 0

# for i in range(1, number_items):
#     price = float(input("What is the price of item " + str(i) + " ? $"))
#     total_price += price 

# total_price = round(total_price, 2)
# print("You bought " + str(number_items) + " items.")
# print("The total cost is $" + str(total_price) + ".")

# task 1a






























































