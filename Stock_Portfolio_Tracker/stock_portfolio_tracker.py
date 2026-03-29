# Step 1: Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 130,
    "MSFT": 300
}

portfolio = {}
total_investment = 0

# Step 2: User input
while True:
    stock = input("Enter stock name (or 'done' to finish): ").upper()
    
    if stock == "DONE":
        break
    
    if stock not in stock_prices:
        print("Stock not available!")
        continue
    
    try:
        quantity = int(input(f"Enter quantity for {stock}: "))
    except ValueError:
        print("Invalid quantity!")
        continue
    
    portfolio[stock] = portfolio.get(stock, 0) + quantity

# Step 3: Calculation
print("\n📊 Portfolio Summary:")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    total_investment += value
    print(f"{stock} -> {qty} shares × ${price} = ${value}")

print("\n💰 Total Investment Value: $", total_investment)

# Step 4 (Optional): Save to file
save = input("\nDo you want to save to file? (yes/no): ").lower()

if save == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        file.write("------------------------\n")
        
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            value = price * qty
            file.write(f"{stock} -> {qty} × ${price} = ${value}\n")
        
        file.write(f"\nTotal Investment: ${total_investment}")
    
    print("✅ Saved to portfolio.txt")
