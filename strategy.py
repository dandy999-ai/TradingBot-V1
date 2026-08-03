"""
TradingBot-V2
Strategia con punteggio
"""

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
