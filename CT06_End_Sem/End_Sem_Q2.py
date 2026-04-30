
# ============================================================
# Q2. List Operations
# ============================================================
# You are working with a list of planets.
# The program must perform several operations on this list.

# Program Requirements:
# - Use the list:
#   planets = ["mercury","venus", "earth", "mars", "jupiter", "saturn", "uranus"]
# - Print the 3rd item using index
# - Append "neptune" to the list
# - Rename "mars" to "muskworld"
# - Remove "uranus" from the list
# - Using a for loop, print all the planets one by one

# ============================================================


# ============================================================
# Step 1: Create the list
# ============================================================

planets = [
  "mercury",
  "venus", 
  "earth", 
  "mars", 
  "jupiter",
  "saturn",
  "uranus"
]

# ============================================================
# Step 2: Print the 3rd item (Test Case 1)
#     - Comment after testing
# ============================================================

# print(planets[2])

# ============================================================
# Step 3: Append "neptune"
# ============================================================

planets.append("neptune")

# ============================================================
# Step 4: Rename "mars" to "muskworld"
# ============================================================

planets.pop(3)
planets.insert(3,"muskword")

# ============================================================
# Step 5: Remove "uranus"
# ============================================================

planets.pop(6)

# ============================================================
# Step 6: Loop through and print all planets
# ============================================================

for i in range(len(planets)):
  print(planets[i])

