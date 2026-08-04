"""
TradingBot PRO
Configurazione principale
"""

# ==========================================
# CAPITALE
# ==========================================

INITIAL_CAPITAL = 500

RISK_PER_TRADE = 0.01          # 1%

MAX_OPEN_TRADES = 3

MAX_DAILY_LOSS = 0.03          # 3%

# ==========================================
# STRATEGIA
# ==========================================

BUY_SCORE = 85

EMA_FAST = 50
EMA_SLOW = 200

RSI_BUY_MIN = 50
RSI_BUY_MAX = 60

BREAKOUT_LOOKBACK = 20

VOLUME_LOOKBACK = 20

# ==========================================
# STOP LOSS / TAKE PROFIT
# ==========================================

ATR_STOP = 2.0

ATR_TARGET = 3.0

# ==========================================
# MODALITÀ BOT
# ==========================================

LIVE_TRADING = False

PAPER_TRADING = True

# ==========================================
# SCANNER
# ==========================================

TOP_RESULTS = 10

USE_FUNDAMENTALS = True

USE_VOLUME_FILTER = True

USE_BREAKOUT_FILTER = True

USE_GROWTH_FILTER = True

# ==========================================
# WATCHLIST
# ==========================================

WATCHLIST_FILE = "watchlists/growth.txt"
WATCHLIST_GROWTH = "watchlists/growth.txt"
WATCHLIST_ETF = "watchlists/etf.txt"
WATCHLIST_QUALITY = "watchlists/quality.txt"
# ==========================================
# REPORT
# ==========================================

SAVE_TRADES = True

SAVE_REPORT = True

REPORT_FOLDER = "reports"

# ==========================================
# VERSIONE
# ==========================================

BOT_NAME = "TradingBot PRO"

VERSION = "1.0"
