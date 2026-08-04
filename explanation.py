"""
TradingBot PRO V4.0
Spiegazione del punteggio
"""


def explain(df, technical, fundamental, momentum):

    last = df.iloc[-1]

    reasons = []

    # ==========================================
    # Trend
    # ==========================================

    if last["EMA50"] > last["EMA200"]:
        reasons.append("Trend rialzista (EMA50 > EMA200)")

    if last["EMA200_SLOPE"]:
        reasons.append("Trend di lungo periodo positivo")

    # ==========================================
    # Momentum
    # ==========================================

    if last["MACD"] > last["MACD_SIGNAL"]:
        reasons.append("MACD positivo")

    if last["MACD_HIST"] > 0:
        reasons.append("Momentum in accelerazione")

    # ==========================================
    # RSI
    # ==========================================

    if 50 <= last["RSI"] <= 60:
        reasons.append("RSI in zona favorevole")

    # ==========================================
    # Breakout
    # ==========================================

    if last["Close"] > last["HIGH20"]:
        reasons.append("Breakout dei massimi a 20 giorni")

    # ==========================================
    # Volume
    # ==========================================

    if last["VOLUME_RATIO"] > 1.5:
        reasons.append("Volume sopra la media")

    # ==========================================
    # Score
    # ==========================================

    reasons.append(f"Score Tecnico: {technical}")

    reasons.append(f"Score Fondamentale: {fundamental}")

    reasons.append(f"Momentum: {momentum}")

    return reasons