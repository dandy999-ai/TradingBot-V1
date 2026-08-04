"""
TradingBot V3
Report finale
"""

def print_report(results):

    print("\n" + "=" * 40)
    print("      TRADING BOT REPORT")
    print("=" * 40)

    print(f"Operazioni: {results['trades']}")
    print(f"Vincenti:   {results['wins']}")
    print(f"Perdenti:   {results['losses']}")
    print(f"Win Rate:   {results['win_rate']} %")
    print(f"Profitto:   {results['profit']} %")

    print("=" * 40)