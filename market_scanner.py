"""
TradingBot PRO V3
Market Scanner
"""

from scanner import get_watchlist, download_data
from indicators import add_indicators
from strategy import analyze
from fundamentals import get_fundamentals
from scoring import total_score
from signal import generate_signal
from entry import calculate_entry


def scan_market():

    results = []

    watchlist = get_watchlist()

    for symbol in watchlist:

        print(f"Analizzo {symbol}...")

        try:

            df = download_data(symbol)

            if df.empty:
                continue

            df = add_indicators(df)

            technical = analyze(df)

            technical_score = technical["score"]

            fundamental_score = get_fundamentals(symbol)

            final_score = total_score(
                technical_score,
                fundamental_score
            )

            signal = generate_signal(
                symbol,
                technical_score,
                fundamental_score,
                final_score
            )

            trade = calculate_entry(df)

            signal["entry"] = trade["entry"]
            signal["stop"] = trade["stop"]
            signal["target"] = trade["target"]
            signal["rr"] = trade["rr"]

            results.append(signal)

        except Exception as e:

            print(f"{symbol}: {e}")

    return results