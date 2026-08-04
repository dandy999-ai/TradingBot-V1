"""
TradingBot V6
Sistema di punteggio
"""


def total_score(technical_score, fundamental_score):

    # 60% tecnica
    technical = technical_score * 0.60

    # 40% fondamentali
    fundamental = fundamental_score * 0.40

    score = technical + fundamental

    return round(score, 2)