"""
TradingBot V2
Backtest semplice
"""

from scanner import download_data
from indicators import add_indicators
from strategy import analyze


def run_backtest(symbol):

    df = download_data(symbol, period="5y")

    df = add_indicators(df)

    total = 0
    buy = 0

    for i in range(200, len(df)):

        result = analyze(df.iloc[:i+1])

        total += 1

        if result["buy"]:
            buy += 1

    print("==============")
    print(symbol)
    print("Giorni analizzati:", total)
    print("Segnali BUY:", buy)
    print("Percentuale:", round((buy / total) * 100, 2), "%")


run_backtest("SPY")