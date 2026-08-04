"""
TradingBot PRO V1.0
Programma principale
"""

from scanner import get_watchlist, download_data
from indicators import add_indicators
from strategy import analyze
from fundamentals import get_fundamentals
from scoring import total_score
from ranking import rank_results
from signal import generate_signal

from config import (
    BOT_NAME,
    VERSION,
    BUY_SCORE,
    TOP_RESULTS
)


def main():

    watchlist = get_watchlist()

    results = []

    print("=" * 60)
    print(f"{BOT_NAME} - Versione {VERSION}")
    print("=" * 60)
    print()

    for symbol in watchlist:

        print(f"Analizzo {symbol}...")

        try:

            df = download_data(symbol)

            if df.empty:
                print("Nessun dato trovato\n")
                continue

            df = add_indicators(df)

            technical_score = analyze(df)["score"]

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

            signal["buy"] = final_score >= BUY_SCORE

            results.append(signal)

        except Exception as e:

            print(f"Errore su {symbol}: {e}")

    results = rank_results(
        results,
        top=TOP_RESULTS
    )

    print()
    print("=" * 60)
    print("TOP OPPORTUNITÀ")
    print("=" * 60)

    for i, stock in enumerate(results, start=1):

        print(
            f"{i:2}. "
            f"{stock['symbol']:<6} | "
            f"Score {stock['score']:>5} | "
            f"Tec {stock['technical']:>3} | "
            f"Fond {stock['fundamental']:>3} | "
            f"{stock['signal']}"
        )

    print()
    print("=" * 60)
    print("Analisi completata.")
    print("=" * 60)


if __name__ == "__main__":
    main()