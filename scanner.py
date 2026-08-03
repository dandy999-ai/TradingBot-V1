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

      if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    return df


def get_watchlist():
    return ETF_LIST + STOCK_LIST
Fai Commit

    return df


def get_watchlist():
    """
    Restituisce tutti i titoli da analizzare.
    """

    return ETF_LIST + STOCK_LIST
