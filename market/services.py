import yfinance as yf
from .models import DailyCandle

def fetch_daily_data(symbol="AAPL"):
    df = yf.download(symbol, period="6mo", interval="1d")
    for date, row in df.iterrows():
        DailyCandle.objects.update_or_create(
            symbol=symbol,
            date=date.date(),
            defaults={
                "open": row["Open"],
                "high": row["High"],
                "low": row["Low"],
                "close": row["Close"],
                "volume": row["Volume"]
            }
        )
