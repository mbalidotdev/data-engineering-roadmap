# A function is a reusable piece of code, like a recipe. You give it ingredients (inputs) => it does something => It gives you a result (output).

# Define a function
def greet(name):
    print(f"Hello, {name}")


greet("Sarah")
greet("John")


# Function that returns a values. Parameters are defined, arguments are called/invoked.
def calculate_price_with_tax(price, tax_rate):
    return price * (1 + tax_rate)


total = calculate_price_with_tax(100, 0.21)  # 21% tax in Belgium
print(total)
