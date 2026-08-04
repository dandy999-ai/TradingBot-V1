"""
TradingBot PRO V2.0
Programma principale
"""

from scanner import get_watchlist, download_data
from indicators import add_indicators
from strategy import analyze
from fundamentals import get_fundamentals
from scoring import total_score
from ranking import rank_results
from signal import generate_signal
from entry import calculate_entry
from export import save_results

from config import (
    BOT_NAME,
    VERSION,
    BUY_SCORE,
    TOP_RESULTS,
    WATCHLIST_FILE
)


def main():

    watchlist = get_watchlist()
    results = []

    print("=" * 70)
    print(f"{BOT_NAME} - Versione {VERSION}")
    print("=" * 70)
    print(f"Watchlist: {WATCHLIST_FILE}")
    print("=" * 70)
    print()

    for symbol in watchlist:

        print(f"Analizzo {symbol}...")

        try:

            df = download_data(symbol)

            if df.empty:
                print("Nessun dato trovato")
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

            signal["buy"] = final_score >= BUY_SCORE

            results.append(signal)

        except Exception as e:

            print(f"Errore su {symbol}: {e}")

    results = rank_results(
        results,
        top=TOP_RESULTS
    )

    print()
    print("=" * 70)
    print("TOP OPPORTUNITÀ")
    print("=" * 70)

    for i, stock in