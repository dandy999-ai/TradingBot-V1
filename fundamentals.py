"""
TradingBot V6
Analisi Fondamentale
"""

import yfinance as yf


def get_fundamentals(symbol):
    """
    Restituisce un punteggio fondamentale da 0 a 100
    """

    score = 0

    try:

        stock = yf.Ticker(symbol)
        info = stock.info

        market_cap = info.get("marketCap")
        revenue_growth = info.get("revenueGrowth")
        earnings_growth = info.get("earningsGrowth")
        forward_pe = info.get("forwardPE")
        beta = info.get("beta")

        # -------------------------
        # Capitalizzazione
        # Preferiamo Small/Mid Cap
        # -------------------------

        if market_cap:

            if 300_000_000 <= market_cap <= 5_000_000_000:
                score += 20

            elif 5_000_000_000 < market_cap <= 50_000_000_000:
                score += 10

        # -------------------------
        # Crescita ricavi
        # -------------------------

        if revenue_growth is not None:

            if revenue_growth > 0.30:
                score += 20

            elif revenue_growth > 0.15:
                score += 10

        # -------------------------
        # Crescita utili
        # -------------------------

        if earnings_growth is not None:

            if earnings_growth > 0.30:
                score += 20

            elif earnings_growth > 0.15:
                score += 10

        # -------------------------
        # Valutazione
        if forward_pe is not None:

            if 10 <= forward_pe <= 30:
                score += 20

            elif forward_pe < 40:
                score += 10

        # Beta (rischio)
        if beta is not None:

            if beta < 1.5:
                score += 20

            elif beta < 2:
                score += 10

    except Exception:
        return 0

    return min(score, 100)