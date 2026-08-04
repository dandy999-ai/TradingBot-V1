"""
TradingBot PRO V3.2
Momentum Score
"""


def momentum_score(df):

    if len(df) < 252:
        return 0

    last = df.iloc[-1]

    score = 0

    # ==========================================
    # Performance 1 mese
    # ==========================================

    perf_1m = (
        last["Close"] /
        df["Close"].iloc[-21] - 1
    ) * 100

    if perf_1m > 15:
        score += 25

    elif perf_1m > 8:
        score += 15

    elif perf_1m > 3:
        score += 8

    # ==========================================
    # Performance 3 mesi
    # ==========================================

    perf_3m = (
        last["Close"] /
        df["Close"].iloc[-63] - 1
    ) * 100

    if perf_3m > 40:
        score += 25

    elif perf_3m > 20:
        score += 15

    elif perf_3m > 10:
        score += 8

    # ==========================================
    # Vicinanza al massimo annuale
    # ==========================================

    high52 = df["High"].tail(252).max()

    distance = (
        last["Close"] / high52
    )

    if distance > 0.95:
        score += 25

    elif distance > 0.90:
        score += 15

    # ==========================================
    # Volumi
    # ==========================================

    if last["VOLUME_RATIO"] > 2:
        score += 25

    elif last["VOLUME_RATIO"] > 1.5:
        score += 15

    return min(score, 100)