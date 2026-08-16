"""
TradingBot-V1
Gestione del rischio
"""

from config import CAPITALE_INIZIALE, RISCHIO_PER_OPERAZIONE


def calcola_dimensione_posizione(prezzo_ingresso, stop_loss):
    """
    Calcola quante azioni acquistare.
    """

    rischio_massimo = CAPITALE_INIZIALE * RISCHIO_PER_OPERAZIONE

    rischio_per_azione = abs(prezzo_ingresso - stop_loss)

    if rischio_per_azione == 0:
        return 0

    quantita = rischio_massimo / rischio_per_azione

    return int(quantita)

