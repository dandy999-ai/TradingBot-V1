"""
TradingBot V5
Analisi fondamentale con punteggio
"""

import yfinance as yf


def get_fundamentals(symbol):

    try:

        info = yf.Ticker(symbol).info

        score = 0

        market_cap = info.get("marketCap", 0)

        if 300_000_000 <= market_cap <= 5_000_000_000:
            score += 20

        revenue = info.get("revenueGrowth")

        if revenue is not None and revenue > 0.20:
            score += 15

        earnings = info.get("earningsGrowth")

        if earnings is not None and earnings > 0.20:
            score += 15

        return score

    except Exception:

        return 0