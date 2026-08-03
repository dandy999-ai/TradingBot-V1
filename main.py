"""
TradingBot-V1
Programma principale
"""

from scanner import get_watchlist, download_data
from indicators import add_indicators
from strategy import check_buy_signal


def main():

    watchlist = get_watchlist()

    print("=== TradingBot V1 ===")

    for symbol in watchlist:

        print(f"Analizzo {symbol}...")

        try:

            df = download_data(symbol)

            df = add_indicators(df)

            if check_buy_signal(df):

                print(f"✅ Segnale BUY su {symbol}")

            else:

                print(f"❌ Nessun segnale su {symbol}")

        except Exception as e:

            print(f"Errore su {symbol}: {e}")


if __name__ == "__main__":
    main()