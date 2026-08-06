"""
TradingBot PRO V5
Gestione Portafoglio
"""

from config import (
    INITIAL_CAPITAL,
    MAX_OPEN_TRADES
)


class Portfolio:

    def __init__(self):

        self.initial_capital = INITIAL_CAPITAL
        self.cash = INITIAL_CAPITAL

        self.positions = []
        self.closed_trades = []

    # ==========================================
    # Capitale disponibile
    # ==========================================

    def available_cash(self):
        return round(self.cash, 2)

    # ==========================================
    # Posizioni aperte
    # ==========================================

    def open_positions(self):
        return len(self.positions)

    # ==========================================
    # Posso aprire un nuovo trade?
    # ==========================================

    def can_open(self):

        return (
            self.open_positions() < MAX_OPEN_TRADES
            and self.cash > 0
        )

    # ==========================================
    # Apre una posizione
    # ==========================================

    def open_trade(self, trade):

        if not self.can_open():
            return False

        if trade.capital > self.cash:
            return False

        self.positions.append(trade)

        self.cash -= trade.capital

        return True

    # ==========================================
    # Chiude una posizione
    # ==========================================

    def close_trade(self, index, exit_price):

        trade = self.positions.pop(index)

        trade.close(exit_price)

        self.cash += trade.value(exit_price)

        self.closed_trades.append(trade)

    # ==========================================
    # Valore del portafoglio
    # ==========================================

    def total_value(self):

        invested = sum(
            trade.capital
            for trade in self.positions
        )

        return round(
            self.cash + invested,
            2
        )

    # ==========================================
    # Report
    # ==========================================

    def summary(self):

        print()
        print("=" * 60)
        print("PORTAFOGLIO")
        print("=" * 60)

        print(f"Capitale iniziale : {self.initial_capital:.2f} €")
        print(f"Liquidità         : {self.cash:.2f} €")
        print(f"Posizioni aperte  : {len(self.positions)}")
        print(f"Trade chiusi      : {len(self.closed_trades)}")
        print(f"Valore totale     : {self.total_value():.2f} €")

        print("=" * 60)

