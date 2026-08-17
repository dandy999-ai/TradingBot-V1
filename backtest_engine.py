"""
TradingBot PRO V6.1
Backtest Engine
"""

from portfolio import Portfolio

from scanner import (
    get_watchlist,
    download_data
)

from indicators import add_indicators


class BacktestEngine:

    def __init__(self):

        # Portafoglio
        self.portfolio = Portfolio()

        # Watchlist
        self.watchlist = get_watchlist()

        # Dizionario dati storici
        self.market = {}

        # Data corrente del backtest
        self.current_date = None

        # Storico Equity
        self.equity_curve = []

        # Storico Trade
        self.trade_log = []

    # ==================================================
    # Carica dati di mercato
    # ==================================================

    def load_market(self):

        print()
        print("=" * 60)
        print("CARICAMENTO MERCATO")
        print("=" * 60)

        loaded = 0

        for symbol in self.watchlist:

            print(f"Scarico {symbol}...")

            try:

                df = download_data(
                    symbol,
                    period="5y"
                )

                if df.empty:
                    print("   Nessun dato")
                    continue

                df = add_indicators(df)

                self.market[symbol] = df

                loaded += 1

            except Exception as e:

                print(f"   Errore: {e}")

        print()
        print(f"Dataset caricati : {loaded}")
        print()

    # ==================================================
    # Avanza di un giorno
    # ==================================================

    def next_day(self):

        pass

    # ==================================================
    # Aggiorna posizioni
    # ==================================================

    def update_positions(self):

        pass

    # ==================================================
    # Cerca nuovi segnali
    # ==================================================

    def search_signals(self):

        pass

    # ==================================================
    # Salva Equity
    # ==================================================

    def save_equity(self):

        self.equity_curve.append(
            self.portfolio.total_value()
        )

    # ==================================================
    # Report
    # ==================================================

    def summary(self):

        print()
        print("=" * 60)
        print("BACKTEST ENGINE")
        print("=" * 60)

        print(f"Titoli caricati : {len(self.market)}"
        )


        print(
            f"Trade aperti    : {len(self.portfolio.positions)}"
        )


        print(
            f"Trade chiusi    : {len(self.portfolio.closed_trades)}"
        )


        print(
            f"Equity finale   : {self.portfolio.total_value():.2f} €"
        )


        print("=" * 60)



if __name__ == "__main__":


    engine = BacktestEngine()

    engine.run()
