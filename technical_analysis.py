import pandas as pd
import ta

def analyze_coin(df):
    if df is None or len(df) < 20:
        return None

    df["rsi"] = ta.momentum.RSIIndicator(df["price"]).rsi()
    macd = ta.trend.MACD(df["price"])
    df["macd"] = macd.macd()
    df["signal"] = macd.macd_signal()

    latest = df.iloc[-1]
    return {
        "rsi": latest["rsi"],
        "macd": latest["macd"],
        "signal": latest["signal"]
    }
