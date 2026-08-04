"""
TradingBot PRO V2.1
Indicatori Tecnici
"""

import pandas as pd

from config import (
    EMA_FAST,
    EMA_SLOW
)


def add_indicators(df):

    if df.empty:
        return df

    # ==================================================
    # EMA
    # ==================================================

    df["EMA50"] = df["Close"].ewm(
        span=EMA_FAST,
        adjust=False
    ).mean()

    df["EMA200"] = df["Close"].ewm(
        span=EMA_SLOW,
        adjust=False
    ).mean()

    # Trend EMA200
    df["EMA200_SLOPE"] = (
        df["EMA200"] > df["EMA200"].shift(1)
    )

    # ==================================================
    # MACD
    # ==================================================

    ema12 = df["Close"].ewm(span=12, adjust=False).mean()
    ema26 = df["Close"].ewm(span=26, adjust=False).mean()

    df["MACD"] = ema12 - ema26
    df["MACD_SIGNAL"] = df["MACD"].ewm(
        span=9,
        adjust=False
    ).mean()

    df["MACD_HIST"] = (
        df["MACD"] - df["MACD_SIGNAL"]
    )

    # ==================================================
    # RSI
    # ==================================================

    delta = df["Close"].diff()

    gain = delta.where(delta > 0, 0.0)
    loss = -delta.where(delta < 0, 0.0)

    avg_gain = gain.rolling(14).mean()
    avg_loss = loss.rolling(14).mean()

    rs = avg_gain / avg_loss

    df["RSI"] = 100 - (100 / (1 + rs))

    # ==================================================
    # ATR
    # ==================================================

    high_low = df["High"] - df["Low"]

    high_close = (
        df["High"] - df["Close"].shift()
    ).abs()

    low_close = (
        df["Low"] - df["Close"].shift()
    ).abs()

    tr = pd.concat(
        [high_low, high_close, low_close],
        axis=1
    ).max(axis=1)

    df["ATR"] = tr.rolling(14).mean()

    # ==================================================
    # VOLUME
    # ==================================================

    df["AVG_VOLUME"] = (
        df["Volume"].rolling(20).mean()
    )

    df["VOLUME_RATIO"] = (
        df["Volume"] / df["AVG_VOLUME"]
    )

    # ==================================================
    # BREAKOUT
    # ==================================================

    df["HIGH20"] = (
        df["High"]
        .rolling(20)
        .max()
        .shift(1)
    )

    df["LOW20"] = (
        df["Low"]
        .rolling(20)
        .min()
        .shift(1)
    )

    return df