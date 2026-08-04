"""
TradingBot PRO V3.1
Gestione Universe
"""

from config import (
    WATCHLIST_GROWTH,
    WATCHLIST_ETF,
    WATCHLIST_QUALITY
)


def load_watchlist(filename):

    symbols = []

    try:

        with open(filename, "r") as file:

            for line in file:

                symbol = line.strip().upper()

                if symbol:

                    symbols.append(symbol)

    except FileNotFoundError:

        print(f"File non trovato: {filename}")

    return sorted(list(set(symbols)))


def growth():

    return load_watchlist(
        WATCHLIST_GROWTH
    )


def etf():

    return load_watchlist(
        WATCHLIST_ETF
    )


def quality():

    return load_watchlist(
        WATCHLIST_QUALITY
    )


def all_symbols():

    universe = []

    universe.extend(growth())

    universe.extend(etf())

    universe.extend(quality())

    return sorted(list(set(universe)))