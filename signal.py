"""
TradingBot V7
Generazione del segnale finale
"""


def generate_signal(symbol, technical, fundamental, final_score):

    if final_score >= 90:
        signal = "🔥 STRONG BUY"

    elif final_score >= 80:
        signal = "🟢 BUY"

    elif final_score >= 65:
        signal = "🟡 WATCH"

    else:
        signal = "🔴 NO TRADE"

    return {
        "symbol": symbol,
        "technical": technical,
        "fundamental": fundamental,
        "score": final_score,
        "signal": signal
    }