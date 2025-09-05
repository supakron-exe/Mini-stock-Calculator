def main():
    print("Welcome to Mini Stock Calculator!")

    try:
        buy_price = float(input("Enter the buy price per share: "))
        sell_price = float(input("Enter the sell price per share: "))
        shares = int(input("Enter the number of shares: "))

        profit_loss = calculate_profit_loss(buy_price, sell_price, shares)
        percentage_change = calculate_percentage_change(buy_price, sell_price)

        print(f"\n--- Results ---")
        print(f"Total Profit/Loss: {profit_loss:.2f} THB")
        print(f"Percentage Change: {percentage_change:.2f}%")

        if profit_loss > 0:
            print("Congratulations! You made a profit.")
        elif profit_loss < 0:
            print("Oops! You incurred a loss.")
        else:
            print("You broke even.")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
