
from scoring import total_score

from config import (
    BUY_SCORE,
    INITIAL_CAPITAL,
    RISK_PER_TRADE
)


def run_backtest(symbol):

    capital = INITIAL_CAPITAL

    trades = 0
    wins = 0
    losses = 0

    df = download_data(symbol, period="5y")

    if df.empty:
        print("Nessun dato.")
        return

    df = add_indicators(df)

    for i in range(220, len(df) - 10):

        history = df.iloc[:i + 1]

        technical = analyze(history)["score"]

        fundamental = get_fundamentals(symbol)

        momentum = momentum_score(history)

        score = total_score(
            technical,
            fundamental,
            momentum
        )

        # Soglia temporanea per testare la strategia
if score < 70:
    continue

        entry = float(df["Close"].iloc[i])

        exit_price = float(df["Close"].iloc[i + 10])

        variation = (exit_price - entry) / entry

        risk_capital = capital * RISK_PER_TRADE

        profit = risk_capital * variation

        capital += profit

        trades += 1

        if profit > 0:
            wins += 1
        else:
            losses += 1

    print()
    print("=" * 60)
    print("BACKTEST")
    print("=" * 60)
    print(f"Ticker             : {symbol}")
    print(f"Operazioni         : {trades}")
    print(f"Vincenti           : {wins}")
    print(f"Perdenti           : {losses}")

    if trades > 0:
        print(f"Win Rate           : {wins / trades * 100:.2f}%")

    print(f"Capitale iniziale  : {INITIAL_CAPITAL:.2f} €")
    print(f"Capitale finale    : {capital:.2f} €")
    print(f"Rendimento         : {(capital / INITIAL_CAPITAL - 1) * 100:.2f}%")

    print("=" * 60)


if __name__ == "__main__":
    run_backtest("SPY")