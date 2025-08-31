def calculate_profit_loss(buy_price: float, sell_price: float, shares: int) -> float:
    """
    Calculates the total profit or loss from a stock transaction.

    Args:
        buy_price: The price per share the stock was bought at.
        sell_price: The price per share the stock was sold at.
        shares: The number of shares bought and sold.

    Returns:
        The total profit (positive) or loss (negative) amount.
    """
    return (sell_price - buy_price) * shares

def calculate_percentage_change(buy_price: float, sell_price: float) -> float:
    """
    Calculates the percentage gain or loss from a stock transaction.

    Args:
        buy_price: The price per share the stock was bought at.
        sell_price: The price per share the stock was sold at.

    Returns:
        The percentage change (positive for gain, negative for loss).
    """
    if buy_price == 0:
        return 0.0  # Avoid division by zero
    return ((sell_price - buy_price) / buy_price) * 100
