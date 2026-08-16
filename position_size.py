"""
TradingBot V3
Calcolo della dimensione della posizione
"""

def calculate_position(capital, risk_percent, entry_price, stop_price):

    risk_amount = capital * (risk_percent / 100)

    risk_per_share = abs(entry_price - stop_price)

    if risk_per_share == 0:
        return 0

    shares = int(risk_amount / risk_per_share)

    return shares
