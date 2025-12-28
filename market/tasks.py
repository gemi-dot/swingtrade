import yfinance as yf
from django.utils import timezone
from market.models import TradingSignal

SYMBOLS = ["AAPL", "MSFT", "NVDA"]

def generate_sma_signals():
    now = timezone.now()
    today = now.date()

    for symbol in SYMBOLS:
        df = yf.download(symbol, period="3mo", interval="1d")

        if df.empty:
            continue

        # Make sure we are only looking at the Close column
        df["SMA_FAST"] = df["Close"].rolling(10).mean()
        df["SMA_SLOW"] = df["Close"].rolling(30).mean()

        latest = df.iloc[-1]

        # Convert to float to ensure scalar comparison
        sma_fast = float(latest["SMA_FAST"])
        sma_slow = float(latest["SMA_SLOW"])

        if sma_fast > sma_slow:
            signal = "BUY"
        elif sma_fast < sma_slow:
            signal = "SELL"
        else:
            signal = "HOLD"

        # Create or update row to prevent duplicates
        TradingSignal.objects.update_or_create(
            symbol=symbol,
            created_at__date=today,
            defaults={
                "sma_fast": round(sma_fast, 2),
                "sma_slow": round(sma_slow, 2),
                "signal": signal,
                "created_at": now,
            }
        )
