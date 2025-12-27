from .indicators import SMA, EMA, RSI, ATR

def generate_daily_signal(df):
    df['sma20'] = SMA(df['close'], 20)
    df['sma50'] = SMA(df['close'], 50)
    df['ema20'] = EMA(df['close'], 20)
    df['rsi'] = RSI(df['close'], 14)
    df['atr'] = ATR(df)

    last = df.iloc[-1]

    if last.close > last.sma20 > last.sma50 and last.close > last.ema20 and 45 < last.rsi < 65:
        return {
            "signal": "BUY",
            "entry": last.close,
            "stop": last.close - (1.2 * last.atr),
            "target": last.close + (2 * last.atr)
        }

    return {"signal": "NO_TRADE"}
