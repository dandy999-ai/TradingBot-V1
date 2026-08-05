"""
TradingBot PRO V3.0
Programma Principale
"""

from config import (
    BOT_NAME,
    VERSION,
    TOP_RESULTS,
    WATCHLIST_FILE
)

from market_scanner import scan_market
from ranking import rank_results
from export import save_results


def main():

    print("=" * 70)
    print(f"{BOT_NAME} - Versione {VERSION}")
    print("=" * 70)
    print(f"Watchlist: {WATCHLIST_FILE}")
    print("=" * 70)
    print()

    # Analizza il mercato
    results = scan_market()

    # Ordina i risultati
    results = rank_results(
        results,
        top=TOP_RESULTS
    )

    print()
    print("=" * 70)
    print("TOP OPPORTUNITÀ")
    print("=" * 70)

    for i, stock in enumerate(results, start=1):

        print()
        print(f"{i}. {stock['symbol']}")
        print(f"Score         : {stock['score']}")
        print(f"Tecnico       : {stock['technical']}")
        print(f"Fondamentale  : {stock['fundamental']}")
        print(f"Segnale       : {stock['signal']}")
        print(f"Entrata       : {stock['entry']}")
        print(f"Stop Loss     : {stock['stop']}")
        print(f"Target        : {stock['target']}")
        print(f"Risk/Reward   : {stock['rr']}")

    save_results(results)

    print()
    print("=" * 70)
    print("Analisi completata.")
    print("=" * 70)


if __name__ == "__main__":
    main()
