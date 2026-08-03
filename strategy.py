
"""
TradingBot-V1
Strategia di trading
"""

def check_buy_signal(df):

    if len(df) < 200:
        return False

    last = df.iloc[-1]

    ema50 = float(last["EMA50"])
    ema200 = float(last["EMA200"])
    rsi = float(last["RSI"])
    macd = float(last["MACD"])
    macd_signal = float(last["MACD_SIGNAL"])

    return (
        ema50 > ema200
        and 50 <= rsi <= 65
        and macd > macd_signal