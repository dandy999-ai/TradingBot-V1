"""
TradingBot V4
Growth Scanner
"""

from fundamentals import get_fundamentals


def is_growth_stock(symbol):

    data = get_fundamentals(symbol)

    if data is None:
        return False

    market_cap = data["market_cap"]
    revenue_growth = data["revenue_growth"]
    earnings_growth = data["earnings_growth"]

    # Capitalizzazione tra 300 milioni e 5 miliardi
    if market_cap is None:
        return False

    if market_cap < 300_000_000:
        return False

    if market_cap > 5_000_000_000:
        return False

    # Crescita dei ricavi
    if revenue_growth is None or revenue_growth <= 0:
        return False

    # Crescita degli utili
    if earnings_growth is None or earnings_growth <= 0:
        return False

    return True