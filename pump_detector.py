from data_fetcher import fetch_top_coins, fetch_ohlcv
from technical_analysis import analyze_coin
from telegram_utils import send_telegram_message

def check_market_and_send_alerts():
    coins = fetch_top_coins(pages=2)
    for coin in coins:
        coin_id = coin["id"]
        symbol = coin["symbol"].upper()
        price_change_1h = coin.get("price_change_percentage_1h_in_currency", 0)

        df = fetch_ohlcv(coin_id)
        indicators = analyze_coin(df)

        if indicators is None:
            continue

        rsi = indicators["rsi"]
        macd = indicators["macd"]
        signal = indicators["signal"]

        # Check for pump
        if rsi > 70 and macd > signal and price_change_1h > 5:
            msg = f"پامپ مشکوک: {symbol}\nRSI: {rsi:.2f}, MACD: {macd:.4f}, 1H Change: {price_change_1h:.2f}%"
            send_telegram_message(msg)

        # Check for dump
        elif rsi < 30 and macd < signal and price_change_1h < -5:
            msg = f"دامپ مشکوک: {symbol}\nRSI: {rsi:.2f}, MACD: {macd:.4f}, 1H Change: {price_change_1h:.2f}%"
            send_telegram_message(msg)
