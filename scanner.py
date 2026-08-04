"""
TradingBot PRO V3.1
Scanner di Mercato
"""

import yfinance as yf
import pandas as pd

from config import WATCHLIST_FILE
from universe import (
    load_watchlist,
    all_symbols
)


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

    if WATCHLIST_FILE == "ALL":
        return all_symbols()

    return load_watchlist(WATCHLIST_FILE)