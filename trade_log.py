"""
TradingBot V2
Registro operazioni
"""

from datetime import datetime
import csv
import os


def save_trade(symbol, score):

    file = "trades.csv"

    exists = os.path.isfile(file)

    with open(file, "a", newline="") as f:

        writer = csv.writer(f)

        if not exists:
            writer.writerow([
                "Data",
                "Ticker",
                "Score"
            ])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            symbol,
            score
        ])