"""
TradingBot PRO V2.2
Esportazione Report
"""

import os
import pandas as pd
from datetime import datetime

from config import REPORT_FOLDER


def save_results(results):

    if not results:
        print("Nessun risultato da salvare.")
        return

    # Crea la cartella se non esiste
    os.makedirs(REPORT_FOLDER, exist_ok=True)

    # Ordina dal punteggio più alto
    results = sorted(
        results,
        key=lambda x: x["score"],
        reverse=True
    )

    df = pd.DataFrame(results)

    # Ordine colonne
    columns = [
        "symbol",
        "score",
        "technical",
        "fundamental",
        "signal",
        "entry",
        "stop",
        "target",
        "rr"
    ]

    df = df[columns]

    filename = os.path.join(
        REPORT_FOLDER,
        f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    )

    df.to_csv(
        filename,
        index=False
    )

    print()
    print("=" * 60)
    print("REPORT SALVATO")
    print("=" * 60)
    print(filename)
    print("=" * 60)