"""
TradingBot V5
Classifica delle migliori opportunità
"""

def rank_results(results, top=10):

    # Ordina dal punteggio più alto al più basso
    results = sorted(
        results,
        key=lambda x: x["score"],
        reverse=True
    )

    return results[:top]