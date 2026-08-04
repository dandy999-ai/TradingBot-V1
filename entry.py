"""
TradingBot PRO
Calcolo Entrata - Stop - Target
"""


def calculate_entry(df):

    last = df.iloc[-1]

    entry = round(float(last["Close"]), 2)

    atr = float(last["ATR"])

    stop = round(entry - atr * 2, 2)

    target = round(entry + atr * 3, 2)

    risk = round(entry - stop, 2)

    reward = round(target - entry, 2)

    rr = round(reward / risk, 2) if risk > 0 else 0

    return {
        "entry": entry,
        "stop": stop,
        "target": target,
        "rr": rr
    }