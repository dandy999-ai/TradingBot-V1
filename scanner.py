"""
TradingBot PRO V2.0
Scanner di Mercato
"""

import yfinance as yf
import pandas as pd

from config import WATCHLIST_FILE


def download_data(symbol, period="1y", interval="1d"):

    df = yf.download(
        symbol,
        period=period,
        interval=interval,
        progress=False,
        auto_adjust=True,
        group_by="column"
    )

    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    return df


def get_watchlist():

    watchlist = []

    try:

        with open(WATCHLIST_FILE, "r") as file:

            for line in file:

                symbol = line.strip().upper()

                if symbol:
                    watchlist.append(symbol)

    except FileNotFoundError:

        print(f"Watchlist non trovata: {WATCHLIST_FILE}")

    return watchlist