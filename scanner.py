"""
TradingBot V6
Scanner di mercato
"""

import yfinance as yf
import pandas as pd

from universe import get_universe


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

    return get_universe()