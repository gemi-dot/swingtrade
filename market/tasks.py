import yfinance as yf
import pandas as pd
from market.models import TradingSignal

SYMBOLS = ["AAPL", "MSFT", "NVDA"]

def generate_sma_signals():
    for symbol in SYMBOLS:
        df = yf.download(symbol, period="3mo", interval="1d")

        if df.empty:
            continue

        df["SMA_FAST"] = df["Close"].rolling(window=10).mean()
        df["SMA_SLOW"] = df["Close"].rolling(window=30).mean()

        latest = df.iloc[-1]

        if latest["SMA_FAST"] > latest["SMA_SLOW"]:
            signal = "BUY"
        elif latest["SMA_FAST"] < latest["SMA_SLOW"]:
            signal = "SELL"
        else:
            signal = "HOLD"

        TradingSignal.objects.create(
            symbol=symbol,
            sma_fast=round(latest["SMA_FAST"], 2),
            sma_slow=round(latest["SMA_SLOW"], 2),
            signal=signal,
        )
