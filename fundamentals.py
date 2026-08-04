"""
TradingBot V4
Analisi fondamentale
"""

import yfinance as yf


def get_fundamentals(symbol):

    try:

        stock = yf.Ticker(symbol)
        info = stock.info

        return {
            "market_cap": info.get("marketCap", 0),
            "pe": info.get("trailingPE", None),
            "forward_pe": info.get("forwardPE", None),
            "revenue_growth": info.get("revenueGrowth", None),
            "earnings_growth": info.get("earningsGrowth", None),
            "beta": info.get("beta", None),
            "sector": info.get("sector", "Unknown")
        }

    except Exception:

        return None