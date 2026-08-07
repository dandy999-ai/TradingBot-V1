"""
TradingBot PRO V6
Backtest Engine
"""

from portfolio import Portfolio


class BacktestEngine:

    def __init__(self):

        self.portfolio = Portfolio()

        self.market = {}

        self.current_date = None

        self.equity_curve = []

        self.trade_log = []

    def load_market(self):

        """
        Carica tutti i dati storici.
        """
        pass

    def next_day(self):

        """
        Avanza di un giorno.
        """
        pass

    def update_positions(self):

        """
        Aggiorna tutte le posizioni aperte.
        """
        pass

    def search_signals(self):

        """
        Cerca nuovi segnali.
        """
        pass

    def save_equity(self):

        """
        Salva il valore giornaliero del portafoglio.
        """
        pass

    def run(self):

        print("Backtest avviato...")