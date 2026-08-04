"""
TradingBot PRO V3.2
Sistema di Punteggio
"""

from config import (
    TECHNICAL_WEIGHT,
    FUNDAMENTAL_WEIGHT,
    MOMENTUM_WEIGHT
)


def total_score(
    technical_score,
    fundamental_score,
    momentum_score
):
    """
    Calcola il punteggio finale.
    """

    score = (
        technical_score * TECHNICAL_WEIGHT +
        fundamental_score * FUNDAMENTAL_WEIGHT +
        momentum_score * MOMENTUM_WEIGHT
    )

    return round(min(score, 100), 2)