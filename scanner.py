import yfinance as yf
import pandas as pd

# La watchlist verrà letta da watchlist.txt


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

    with open("watchlist.txt", "r") as file:

        watchlist = []

        for line in file:

            symbol = line.strip()

            if symbol:
                watchlist.append(symbol)

        return watchlist
