"""
TradingBot V3
Programma principale
"""

from scanner import get_watchlist, download_data
from indicators import add_indicators
from strategy import analyze
from ranking import rank_results


def main():

    watchlist = get_watchlist()
    results = []

    print("=" * 40)
    print("        TRADING BOT V3")
    print("=" * 40)
    print()

    for symbol in watchlist:

        print(f"Analizzo {symbol}...")

        try:

            df = download_data(symbol)

            if df.empty:
                print("Nessun dato trovato")
                continue

            df = add_indicators(df)

            result = analyze(df)

            results.append({
                "symbol": symbol,
                "score": result["score"],
                "buy": result["buy"]
            })

        except Exception as e:
            print(f"Errore su {symbol}: {e}")

    # Ordina per punteggio
    results = rank_results(results, top=10)

    print()
    print("=" * 40)
    print("TOP OPPORTUNITÀ")
    print("=" * 40)

    for i, r in enumerate(results, start=1):

        signal = "BUY ✅" if r["buy"] else "-"

        print(
            f"{i:2}. "
            f"{r['symbol']:<6} "
            f"Score: {r['score']:3}/100   "
            f"{signal}"
        )


if __name__ == "__main__":
    main()