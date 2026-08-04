"""
TradingBot PRO V4.0
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
from explanation import explain


def scan_market():

    results = []

    watchlist = get_watchlist()

    print()
    print(f"Titoli da analizzare: {len(watchlist)}")
    print()

    for symbol in watchlist:

        print(f"Analizzo {symbol}...")

        try:

            # ==========================
            # Download dati
            # ==========================

            df = download_data(symbol)

            if df.empty:
                print("Nessun dato")
                continue

            # ==========================
            # Indicatori
            # ==========================

            df = add_indicators(df)

            # ==========================
            # Analisi tecnica
            # ==========================

            technical = analyze(df)
            technical_score = technical["score"]

            # ==========================
            # Fondamentali
            # ==========================

            fundamental_score = get_fundamentals(symbol)

            # ==========================
            # Momentum
            # ==========================

            momentum = momentum_score(df)

            # ==========================
            # Score finale
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

            # ==========================
            # Motivazione
            # ==========================

            reasons = explain(
                df,
                technical_score,
                fundamental_score,
                momentum
            )

            signal["technical"] = technical_score
            signal["fundamental"] = fundamental_score
            signal["momentum"] = momentum

            signal["score"] = final_score

            signal["entry"] = trade["entry"]
            signal["stop"] = trade["stop"]
            signal["target"] = trade["target"]
            signal["rr"] = trade["rr"]

            signal["reasons"] = reasons

            results.append(signal)

        except Exception as e:

            print(f"Errore su {symbol}: {e}")

    return results