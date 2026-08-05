"""
TradingBot PRO V5
Portfolio Backtester
"""

from scanner import get_watchlist, download_data
from indicators import add_indicators
from strategy import analyze
from fundamentals import get_fundamentals
from momentum import momentum_score
from scoring import total_score

from entry import calculate_entry

from portfolio import Portfolio
from trade import Trade

from config import (
    RISK_PER_TRADE,
    MAX_OPEN_TRADES
)


def run_backtest():

    portfolio = Portfolio()

    watchlist = get_watchlist()

    print()
    print("=" * 70)
    print("PORTFOLIO BACKTEST")
    print("=" * 70)

    print(f"Titoli: {len(watchlist)}")
    print(f"Capitale iniziale: {portfolio.initial_capital:.2f} €")

    print()

    for symbol in watchlist:

        print(f"Analizzo {symbol}...")

        try:

            df = download_data(symbol)

            if df.empty:
                continue

            df = add_indicators(df)

            technical = analyze(df)["score"]

            fundamental = get_fundamentals(symbol)

            momentum = momentum_score(df)

            score = total_score(
                technical,
                fundamental,
                momentum
            )

            if score < 70:
                continue

            trade_levels = calculate_entry(df)

            capital = (
                portfolio.available_cash()
                * RISK_PER_TRADE
            )

            trade = Trade(
                symbol=symbol,
                entry=trade_levels["entry"],
                stop=trade_levels["stop"],
                target=trade_levels["target"],
                capital=capital,
                date=df.index[-1]
            )

            portfolio.open_trade(trade)

            if portfolio.open_positions() >= MAX_OPEN_TRADES:
                break

        except Exception as e:

            print(symbol, e)

    portfolio.summary()


if __name__ == "__main__":
    run_backtest()