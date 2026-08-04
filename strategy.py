"""
TradingBot V6
Strategia avanzata
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

    # 1. Trend principale
    if last["EMA50"] > last["EMA200"]:
        score += 20

    # 2. Prezzo sopra EMA50
    if last["Close"] > last["EMA50"]:
        score += 15

    # 3. Momentum
    if last["MACD"] > last["MACD_SIGNAL"]:
        score += 20

    # 4. RSI
    if 50 <= last["RSI"] <= 60:
        score += 15

    # 5. Vicino ai massimi degli ultimi 20 giorni
    highest = df["High"].tail(20).max()

    if last["Close"] >= highest * 0.98:
        score += 15

    # 6. Trend di lungo periodo
    if last["EMA200"] > df["EMA200"].iloc[-20]:
        score += 15

    return {
        "buy": score >= BUY_SCORE,
        "score": score
    }