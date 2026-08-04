"""
TradingBot V2
Calcolo delle performance
"""

def calculate_trade(entry_price, exit_price):

    profit = ((exit_price - entry_price) / entry_price) * 100

    return round(profit, 2)