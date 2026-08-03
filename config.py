# ==========================
# TradingBot-V1
# Configurazione principale
# ==========================

# Capitale iniziale (simulazione)
CAPITALE_INIZIALE = 500

# Gestione del rischio
RISCHIO_PER_OPERAZIONE = 0.01   # 1%
MAX_POSIZIONI = 3
STOP_GIORNALIERO = 0.03         # 3%

# Strategia
EMA_VELOCE = 50
EMA_LENTA = 200

RSI_MIN = 50
RSI_MAX = 65

ATR_STOP = 2
ATR_TARGET = 3

# ETF monitorati
ETF_LIST = [
    "SPY",
    "QQQ",
    "DIA",
    "IWM"
]

# Azioni monitorate
STOCK_LIST = [
    "AAPL",
    "MSFT",
    "NVDA",
    "AMZN",
    "V",
    "JNJ",
    "KO",
    "JPM"
]
# Punteggio minimo per comprare
BUY_SCORE = 80

# Volume
VOLUME_FILTER = True

# Numero massimo di operazioni
MAX_OPEN_TRADES = 3
# Modalità del bot
LIVE_TRADING = False
