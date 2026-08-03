"""
TradingBot-V1
Strategia di trading
"""

def check_buy_signal(df):
    """
    Controlla se è presente un segnale di acquisto.
    Restituisce True oppure False.
    """

    last = df.iloc[-1]

    if (
        last["EMA50"] > last["EMA200"] and
        50 <= last["RSI"] <= 65 and
        last["MACD"] > last["MACD_SIGNAL"]
    ):
        return True

    return False


def check_sell_signal(df):
    """
    Controlla se è presente un segnale di vendita.
    """

    last = df.iloc[-1]

    if (
        last["EMA50"] < last["EMA200"] or
        last["MACD"] < last["MACD_SIGNAL"]
    ):
        return True

    return False
