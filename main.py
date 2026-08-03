"""
TradingBot V1
Main
"""

from scanner import get_watchlist, download_data
from indicators import add_indicators
from strategy import check_buy_signal

print("===================================")
print("      TRADING BOT V1")
print("===================================\n")

watchlist = get_watchlist()

for symbol in watchlist:

    print(f"Analizzo {symbol}...")

    try:

        df = download_data(symbol)

        if df.empty:
            print("Nessun dato trovato\n")
            continue

        df = add_indicators(df)

        if check_buy_signal(df):
            print(">>> SEGNALE BUY\n")
        else:
            print("Nessun segnale\n")

    except Exception as e:
        print("Errore:", e)