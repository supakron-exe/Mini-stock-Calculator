def calculate_profit_loss(buy_price: float, sell_price: float, shares: int) -> float:
    return (sell_price - buy_price) * shares

def calculate_percentage_change(buy_price: float, sell_price: float) -> float:
    if buy_price == 0:
        return 0.0  # Avoid division by zero
    return ((sell_price - buy_price) / buy_price) * 100
