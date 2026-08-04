"""
TradingBot V3
Backtest con simulazione operazioni
"""

from scanner import download_data
from indicators import add_indicators
from strategy import analyze
from performance import calculate_trade


def run_backtest(symbol):

    df = download_data(symbol, period="5y")
    df = add_indicators(df)

    trades = 0
    wins = 0
    losses = 0
    total_profit = 0

    for i in range(200, len(df) - 10):

        result = analyze(df.iloc[:i+1])

        if result["buy"]:

            entry = float(df["Close"].iloc[i])
            exit_price = float(df["Close"].iloc[i + 10])

            profit = calculate_trade(entry, exit_price)

            trades += 1
            total_profit += profit

            if profit > 0:
                wins += 1
            else:
                losses += 1

    print("\n==============================")
    print("BACKTEST")
    print("==============================")
    print("Ticker:", symbol)
    print("Operazioni:", trades)
    print("Vincenti:", wins)
    print("Perdenti:", losses)

    if trades > 0:
        print("Win Rate:", round((wins / trades) * 100, 2), "%")
        print("Profitto totale:", round(total_profit, 2), "%")
        print("Profitto medio:", round(total_profit / trades, 2), "%")


run_backtest("SPY")