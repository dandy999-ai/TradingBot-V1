"""
TradingBot PRO V3.2
Market Scanner
"""

from scanner import get_watchlist, download_data
from indicators import add_indicators
from strategy import analyze
from fundamentals import get_fundamentals
from momentum import momentum_score
from scoring import total_score
from signal import generate_signal
from entry import calculate_entry


def scan_market():

    results = []

    watchlist = get_watchlist()

    for symbol in watchlist:

        print(f"Analizzo {symbol}...")

        try:

            df = download_data(symbol)

            if df.empty:
                continue

            df = add_indicators(df)

            # ==========================
            # Analisi Tecnica
            # ==========================

            technical = analyze(df)
            technical_score = technical["score"]

            # ==========================
            # Analisi Fondamentale
            # ==========================

            fundamental_score = get_fundamentals(symbol)

            # ==========================
            # Momentum
            # ==========================

            momentum = momentum_score(df)

            # ==========================
            # Score Finale
            # ==========================

            final_score = total_score(
                technical_score,
                fundamental_score,
                momentum
            )

            # ==========================
            # Segnale
            # ==========================

            signal = generate_signal(
                symbol,
                technical_score,
                fundamental_score,
                final_score
            )

            # ==========================
            # Livelli operativi
            # ==========================

            trade = calculate_entry(df)

            signal["technical"] = technical_score
            signal["fundamental"] = fundamental_score
            signal["momentum"] = momentum

            signal["score"] = final_score

            signal["entry"] = trade["entry"]
            signal["stop"] = trade["stop"]
            signal["target"] = trade["target"]
            signal["rr"] = trade["rr"]

            results.append(signal)

        except Exception as e:

            print(f"{symbol}: {e}")

    return results