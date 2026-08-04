"""
TradingBot PRO V2.1
Configurazione principale
"""

# ======================================================
# INFORMAZIONI BOT
# ======================================================

BOT_NAME = "TradingBot PRO"
VERSION = "2.1"

# ======================================================
# CAPITALE
# ======================================================

INITIAL_CAPITAL = 500.0

RISK_PER_TRADE = 0.01      # 1%

MAX_OPEN_TRADES = 3

MAX_DAILY_LOSS = 0.03      # 3%

# ======================================================
# STRATEGIA
# ======================================================

BUY_SCORE = 70

EMA_FAST = 50
EMA_SLOW = 200

RSI_BUY_MIN = 50
RSI_BUY_MAX = 60

BREAKOUT_LOOKBACK = 20

VOLUME_LOOKBACK = 20

ATR_STOP = 2.0
ATR_TARGET = 3.0

# ======================================================
# PESI DEL PUNTEGGIO
# ======================================================

TECHNICAL_WEIGHT = 0.50
FUNDAMENTAL_WEIGHT = 0.30
MOMENTUM_WEIGHT = 0.20

# ======================================================
# WATCHLIST
# ======================================================

WATCHLIST_GROWTH = "watchlists/growth.txt"
WATCHLIST_ETF = "watchlists/etf.txt"
WATCHLIST_QUALITY = "watchlists/quality.txt"

# Watchlist attualmente utilizzata

WATCHLIST_FILE = WATCHLIST_GROWTH

# ======================================================
# SCANNER
# ======================================================

TOP_RESULTS = 10

USE_FUNDAMENTALS = True
USE_VOLUME_FILTER = True
USE_BREAKOUT_FILTER = True
USE_GROWTH_FILTER = True

# ======================================================
# REPORT
# ======================================================

SAVE_REPORT = True
SAVE_TRADES = True

REPORT_FOLDER = "reports"

# ======================================================
# MODALITÀ BOT
# ======================================================

PAPER_TRADING = True

LIVE_TRADING = False
