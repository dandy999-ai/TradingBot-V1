"""
TradingBot PRO V2.1
Strategia
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

    # ==========================================
    # TREND
    # ==========================================

    if last["EMA50"] > last["EMA200"]:
        score += 20

    if last["Close"] > last["EMA50"]:
        score += 10

    if last["EMA200_SLOPE"]:
        score += 10

    # ==========================================
    # MOMENTUM
    # ==========================================

    if last["MACD"] > last["MACD_SIGNAL"]:
        score += 15

    if last["MACD_HIST"] > 0:
        score += 5

    # ==========================================
    # RSI
    # ==========================================

    if 50 <= last["RSI"] <= 60:
        score += 15

    elif 45 <= last["RSI"] <= 70:
        score += 8

    # ==========================================
    # BREAKOUT
    # ==========================================

    if last["Close"] > last["HIGH20"]:
        score += 15

    # ==========================================
    # VOLUME
    # ==========================================

    if last["VOLUME_RATIO"] > 1.5:
        score += 10

    elif last["VOLUME_RATIO"] > 1.2:
        score += 5

    # ==========================================
    # BONUS
    # ==========================================

    if (
        last["EMA50"] > last["EMA200"]
        and last["MACD"] > last["MACD_SIGNAL"]
        and last["RSI"] > 50
    ):
        score += 10

    score = min(score, 100)

    return {
        "buy": score >= BUY_SCORE,
        "score": score
    }