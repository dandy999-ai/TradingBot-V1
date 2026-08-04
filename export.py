"""
TradingBot PRO
Esporta risultati in CSV
"""

import pandas as pd
from datetime import datetime


def save_results(results):

    if len(results) == 0:
        return

    df = pd.DataFrame(results)

    filename = (
        "report_" +
        datetime.now().strftime("%Y%m%d_%H%M%S") +
        ".csv"
    )

    df.to_csv(filename, index=False)

    print()
    print(f"Report salvato: {filename}")