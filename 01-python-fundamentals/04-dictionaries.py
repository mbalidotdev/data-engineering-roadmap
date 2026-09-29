# Dictionaries store key-value pairs - like a real dictionary

# Dictionary for a stock
stock = {
    "symbol": "APPL",
    "price": "175.50",
    "change": 1.2,
    "volume": 5000000
}

# Access values by their key
print(stock["symbol"])
print(stock["change"])

# Change a value
stock["price"] = 180.0

# Add a new key-value pair
stock["market_cap"] = 28000000

# Loop through a dictionary
for key, value in stock.items():
    print(f"{key}: {value}")

# Personal Dictionary
person = {
    "name": "Mbali",
    "age": 31,
    "country": "Belgium",
    "interests": ["coding", "data", "finance"]
}

print(
    f"Hello, my name is {person['name']}."
    f"I'm {person['age']} years old and I live in {person['country']}."
)
