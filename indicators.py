
"""
TradingBot PRO
Indicatori Tecnici
"""

import pandas as pd


def add_indicators(df):

    # ==========================================
    # EMA
    # ==========================================

    df["EMA50"] = df["Close"].ewm(span=50, adjust=False).mean()
    df["EMA200"] = df["Close"].ewm(span=200, adjust=False).mean()

    # ==========================================
    # MACD
    # ==========================================

    ema12 = df["Close"].ewm(span=12, adjust=False).mean()
    ema26 = df["Close"].ewm(span=26, adjust=False).mean()

    df["MACD"] = ema12 - ema26
    df["MACD_SIGNAL"] = df["MACD"].ewm(span=9, adjust=False).mean()

    # ==========================================
    # RSI REALE
    # ==========================================

    delta = df["Close"].diff()

    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(14).mean()
    avg_loss = loss.rolling(14).mean()

    rs = avg_gain / avg_loss

    df["RSI"] = 100 - (100 / (1 + rs))

    # ==========================================
    # ATR
    # ==========================================

    high_low = df["High"] - df["Low"]
    high_close = (df["High"] - df["Close"].shift()).abs()
    low_close = (df["Low"] - df["Close"].shift()).abs()

    tr = pd.concat(
        [high_low, high_close, low_close],
        axis=1
    ).max(axis=1)

    df["ATR"] = tr.rolling(14).mean()

    # ==========================================
    # Volume Medio
    # ==========================================

    df["AVG_VOLUME"] = df["Volume"].rolling(20).mean()

    return df