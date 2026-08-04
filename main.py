"""
TradingBot V3
Programma principale
"""

from scanner import get_watchlist, download_data
from indicators import add_indicators
from strategy import analyze


def main():

    watchlist = get_watchlist()
    results = []

    print("===================================")
    print("      TRADING BOT V3")
    print("===================================\n")

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
            print(f"Errore: {e}")

    results.sort(key=lambda x: x["score"], reverse=True)

    print("\n===================================")
    print("TOP OPPORTUNITÀ")
    print("===================================\n")

    for r in results:

        signal = "BUY" if r["buy"] else "-"

        print(
            f"{r['symbol']:6} "
            f"Score: {r['score']:3}/100   "
            f"{signal}"
        )


if __name__ == "__main__":
    main()