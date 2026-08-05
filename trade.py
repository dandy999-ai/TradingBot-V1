"""
TradingBot PRO V5
Classe Trade
"""


class Trade:

    def __init__(
        self,
        symbol,
        entry,
        stop,
        target,
        capital,
        date
    ):

        self.symbol = symbol

        self.entry = float(entry)
        self.stop = float(stop)
        self.target = float(target)

        self.capital = float(capital)

        self.date = date

        self.shares = (
            self.capital / self.entry
            if self.entry > 0 else 0
        )

        self.exit = None

        self.profit = 0

        self.closed = False

    # ==========================================
    # Chiude il trade
    # ==========================================

    def close(self, price):

        self.exit = float(price)

        self.profit = (
            self.exit - self.entry
        ) * self.shares

        self.closed = True

    # ==========================================
    # Valore attuale
    # ==========================================

    def value(self, current_price):

        return self.shares * current_price

    # ==========================================
    # Profitto %
    # ==========================================

    def performance(self):

        if self.closed:

            return round(
                self.profit /
                self.capital * 100,
                2
            )

        return 0

    # ==========================================
    # Dizionario
    # ==========================================

    def to_dict(self):

        return {

            "symbol": self.symbol,

            "entry": self.entry,

            "exit": self.exit,

            "stop": self.stop,

            "target": self.target,

            "capital": self.capital,

            "shares": round(self.shares, 4),

            "profit": round(self.profit, 2),

            "performance": self.performance(),

            "closed": self.closed,

            "date": self.date
        }