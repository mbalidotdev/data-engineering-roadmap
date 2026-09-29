# Your Profile

# Create variables for your profile
name = "Mbali"
age = 31
city = "Antwerp"
hobby = "Piano"

# Print Sentence
print(
    f"Hi, I'm {name}, I'm {age} years old, I love in {city} and I love {hobby}.")

# ----------------------------------------------

# Budget Calculator

# Monthly Income & Expenses
income = 3000
rent = 900
groceries = 400
transport = 100
entertainment = 200
other = 150

# Calculate
total_expenses = rent + groceries + transport + entertainment + other

savings = income - total_expenses

print(f"Total Expenses: {total_expenses}")
print(f"Savings: {savings}")

# -----------------------------------------------

# Frituur List

# Create a list of frituurs
frituurs = [
    {"name": "Frituur Antwerp", "rating": 4.5},
    {"name": "Frituur Place Jourdan", "rating": 4.7},
    {"name": "Frituur Maison", "rating": 4.3}
]

# Find the highest rated
highest = None
max_rating = 0

for frituur in frituurs:
    if frituur["rating"] > max_rating:
        max_rating = frituur["rating"]
        highest = frituur["name"]

print(f"Best frtuur: {highest} (rating: {max_rating})")
