
"""
TradingBot PRO V2.1
Analisi Fondamentale
"""

import yfinance as yf


def get_fundamentals(symbol):

    score = 0

    try:

        stock = yf.Ticker(symbol)
        info = stock.info

        market_cap = info.get("marketCap")
        revenue_growth = info.get("revenueGrowth")
        earnings_growth = info.get("earningsGrowth")
        forward_pe = info.get("forwardPE")
        beta = info.get("beta")
        roe = info.get("returnOnEquity")
        operating_margin = info.get("operatingMargins")
        debt_to_equity = info.get("debtToEquity")

        # ==========================================
        # CAPITALIZZAZIONE
        # ==========================================

        if market_cap is not None:

            if 300_000_000 <= market_cap <= 5_000_000_000:
                score += 15

            elif 5_000_000_000 < market_cap <= 50_000_000_000:
                score += 10

        # ==========================================
        # CRESCITA RICAVI
        # ==========================================

        if revenue_growth is not None:

            if revenue_growth >= 0.30:
                score += 15

            elif revenue_growth >= 0.15:
                score += 10

        # ==========================================
        # CRESCITA UTILI
        # ==========================================

        if earnings_growth is not None:

            if earnings_growth >= 0.30:
                score += 15

            elif earnings_growth >= 0.15:
                score += 10

        # ==========================================
        # P/E
        # ==========================================

        if forward_pe is not None:

            if 10 <= forward_pe <= 30:
                score += 15

            elif forward_pe < 40:
                score += 10

        # ==========================================
        # ROE
        # ==========================================

        if roe is not None:

            if roe >= 0.20:
                score += 15

            elif roe >= 0.10:
                score += 10

        # ==========================================
        # MARGINE OPERATIVO
        # ==========================================

        if operating_margin is not None:

            if operating_margin >= 0.20:
                score += 10

            elif operating_margin >= 0.10:
                score += 5

        # ==========================================
        # DEBITO
        # ==========================================

        if debt_to_equity is not None:

            if debt_to_equity < 50:
                score += 10

            elif debt_to_equity < 100:
                score += 5

        # ==========================================
        # BETA
        # ==========================================

        if beta is not None:

            if beta < 1.5:
                score += 5

    except Exception:
        return 0

    return min(score, 100)