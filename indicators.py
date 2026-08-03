"""
TradingBot-V1
Modulo indicatori
"""

import pandas as pd
import pandas_ta as ta


def add_indicators(df):
    """
    Aggiunge gli indicatori tecnici al DataFrame.
    """

    # Medie mobili
    df["EMA50"] = ta.ema(df["Close"], length=50)
    df["EMA200"] = ta.ema(df["Close"], length=200)

    # RSI
    df["RSI"] = ta.rsi(df["Close"], length=14)

    # ATR
    df["ATR"] = ta.atr(
        high=df["High"],
        low=df["Low"],
        close=df["Close"],
        length=14
    )

    # MACD
    macd = ta.macd(df["Close"])
    df["MACD"] = macd["MACD_12_26_9"]
    df["MACD_SIGNAL"] = macd["MACDs_12_26_9"]

    return df
