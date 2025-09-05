def main():
    print("Welcome to Mini Stock Calculator!")

    while True:
        buy_price = float(input("Enter the buy price per share: "))
        if buy_price < 0:
            print("Buy price cannot be negative.")
        else:
            break

    while True:
        sell_price = float(input("Enter the sell price per share: "))
        if sell_price < 0:
            print("Sell price cannot be negative.")
        else:
            break

    while True:
        shares = int(input("Enter the number of shares: "))
        if shares <= 0:
            print("Number of shares must be greater than 0.")
        else:
            break

    profit_loss = calculate_profit_loss(buy_price, sell_price, shares)
    percentage_change = calculate_percentage_change(buy_price, sell_price)

    print(f"\n--- Results ---")
    print(f"Total Profit/Loss: {profit_loss:.2f} USD")
    print(f"Percentage Change: {percentage_change:.2f}%")

    if profit_loss > 0 and percentage_change > 15:
        print("It's a great investment!")
    elif profit_loss > 0 and percentage_change <15:
        print("It's a good investment!")
    elif profit_loss == 0 and percentage_change == 0:
        print("It's a neutral investment.")
    elif profit_loss < 0 and percentage_change > -20:
        print("You should consider cutting your losses next time.")
    else:
        print("Wow, more than -20%? At this rate, you’re not investing—you’re donating to the market.")

if __name__ == "__main__":
    main()
