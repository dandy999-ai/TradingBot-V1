"""
TradingBot PRO V4.1
Generazione Segnale
"""


def generate_signal(
    symbol,
    technical,
    fundamental,
    score
):

    if score >= 90:
        signal = "⭐ STRONG BUY"

    elif score >= 80:
        signal = "🟢 BUY"

    elif score >= 70:
        signal = "👀 WATCH"

    else:
        signal = "⚪ HOLD"

    return {
        "symbol": symbol,
        "technical": technical,
        "fundamental": fundamental,
        "score": score,
        "signal": signal
    }
