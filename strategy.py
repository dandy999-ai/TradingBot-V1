
"""
TradingBot V2
Strategia con punteggio
"""

from config import BUY_SCORE


def analyze(df):

    if len(df) < 200:
        return {
            "buy": False,
            "score": 0
        }

    last = df.iloc[-1]

    score = 0

    # Trend
    if last["EMA50"] > last["EMA200"]:
        score += 40

    # Momentum
    if last["MACD"] > last["MACD_SIGNAL"]:
        score += 30

    # RSI
    if 50 <= last["RSI"] <= 65:
        score += 30

    return {
        "buy": score >= BUY_SCORE,
        "score": score
    }