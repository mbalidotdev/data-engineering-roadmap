# Lists are like containers that hold multiple items.

# Create a list of stock symbols
stocks = ["AAPL", "GOOGLE", "AMZN"]

# Access items by position (starting at 0)
print(stocks[0])
print(stocks[1])
print(stocks[-1])

# Add an item
stocks.append("TSLA")
print(stocks)

# Loop through a list
for stock in stocks:
    print(f"💸 {stock}")
