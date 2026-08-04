"""
TradingBot V7
Strategia Avanzata
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

    # ==========================================
    # MOMENTUM
    # ==========================================

    if last["MACD"] > last["MACD_SIGNAL"]:
        score += 20

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

    highest20 = df["High"].tail(20).max()

    if last["Close"] >= highest20 * 0.98:
        score += 15

    # ==========================================
    # TREND LUNGO PERIODO
    # ==========================================

    ema200_old = df["EMA200"].iloc[-20]

    if last["EMA200"] > ema200_old:
        score += 10

    # ==========================================
    # VOLUME
    # ==========================================

    avg_volume = df["Volume"].tail(20).mean()

    if last["Volume"] > avg_volume:
        score += 10

    return {
        "buy": score >= BUY_SCORE,
        "score": score
    }