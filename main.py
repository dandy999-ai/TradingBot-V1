"""
TradingBot V6
Programma principale
"""

from scanner import get_watchlist, download_data
from indicators import add_indicators
from strategy import analyze
from fundamentals import get_fundamentals
from scoring import total_score
from ranking import rank_results


def main():

    watchlist = get_watchlist()
    results = []

    print("=" * 50)
    print("         TRADING BOT V6")
    print("=" * 50)
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

            results.append({
                "symbol": symbol,
                "technical": technical_score,
                "fundamental": fundamental_score,
                "score": final_score,
                "buy": final_score >= 85
            })

        except Exception as e:

            print(f"Errore su {symbol}: {e}")

    results = rank_results(results, top=10)

    print()
    print("=" * 50)
    print("TOP 10 OPPORTUNITÀ")
    print("=" * 50)

    for i, r in enumerate(results, start=1):

        signal = "BUY ✅" if r["buy"] else "-"

        print(
            f"{i:2}. "
            f"{r['symbol']:<6} | "
            f"Score: {r['score']:>5} | "
            f"Tecnica: {r['technical']:>3} | "
            f"Fond.: {r['fundamental']:>3} | "
            f"{signal}"
        )


if __name__ == "__main__":
    main()