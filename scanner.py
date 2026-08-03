"""
TradingBot-V1
Scanner di mercato
"""

import yfinance as yf

from config import ETF_LIST, STOCK_LIST


def download_data(symbol, period="1y", interval="1d"):
    """
    Scarica i dati di un titolo.
    """

    df = yf.download(
        symbol,
        period=period,
        interval=interval,
        progress=False
    )

    return df


def get_watchlist():
    """
    Restituisce tutti i titoli da analizzare.
    """

    return ETF_LIST + STOCK_LIST
