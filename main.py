"""
TradingBot V2
Programma principale
"""

from scanner import get_watchlist, download_data
from indicators import add_indicators
from strategy import analyze


def main():

    watchlist = get_watchlist()

    print("===================================")
    print("      TRADING BOT V2")
    print("===================================\n")

    for symbol in watchlist:

        print(f"Analizzo {symbol}...")

        try:

            df = download_data(symbol)

            if df.empty:
                print("Nessun dato trovato\n")
                continue

            df = add_indicators(df)

            result = analyze(df)

            print(f"Punteggio: {result['score']}/100")

            if result["buy"]:
                print(">>> SEGNALE BUY\n")
            else:
                print("Nessun segnale\n")

        except Exception as e:

            print(f"Errore: {e}")


if __name__ == "__main__":
    main()