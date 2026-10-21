# Stock Portfolio Tracker

# Manually defined stock prices
stock_prices = {
    "TCS": 3500,
    "INFY": 1500,
    "RELIANCE": 2500,
    "HDFC": 1700
}

total_investment = 0

# Number of stocks
n = int(input("Enter number of stocks: "))

# Optional file handling
file = open("portfolio.txt", "w")
file.write("Stock Portfolio Report\n")
file.write("----------------------\n")

for i in range(n):
    stock_name = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    if stock_name in stock_prices:
        investment = stock_prices[stock_name] * quantity
        total_investment += investment

        print(f"{stock_name}: Rs.{investment}")

        file.write(f"{stock_name} | Quantity: {quantity} | Investment: Rs.{investment}\n")
    else:
        print("Stock not found!")
        file.write(f"{stock_name} | Stock not found\n")

print("\nTotal Investment: Rs.", total_investment)
file.write(f"\nTotal Investment: Rs.{total_investment}")

file.close()
print("Portfolio saved in portfolio.txt")