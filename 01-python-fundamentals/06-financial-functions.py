# 1. Calculate salary after tax (Belgium)
def calculate_net_salary(gross, tax_rate):
    net = gross * (1 - tax_rate)
    return net


# Test it
gross = 3000
tax_rate = 0.45
net = calculate_net_salary(gross, tax_rate)
print(f"Gross: €{gross}")
print(f"Net: €{net}")


# 2. Calculate monthly expenses
def monthly_expenses(rent, food, transport, other):
    return rent + food + transport + other


# Test it
rent = 900
food = 400
transport = 100
other = 200
total = monthly_expenses(rent, food, transport, other)
print(f"Total monthly expenses: €{total}")


# 3. Calculate savings
def calculate_savings(income, expenses):
    return income - expenses


savings = calculate_savings(net, total)
print(f"Monthly savings: €{savings}")
