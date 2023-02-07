import requests
import time


def get_last_trades(symbol, interval):
    endpoint = (
        f"https://api.binance.com/api/v1/klines?symbol={symbol}&interval={interval}"
    )
    response = requests.get(endpoint)
    data = response.json()
    return data


def calculate_vwap(symbol, interval):
    trades = get_last_trades(symbol, interval)
    current_time = int(time.time() * 1000)
    five_minutes_ago = current_time - 5 * 60 * 1000
    vwap_numerator = 0
    vwap_denominator = 0
    for trade in trades:
        trade_time = trade[6]
        if trade_time > five_minutes_ago:
            price = trade[1]
            quantity = trade[5]
            vwap_numerator += price * quantity
            vwap_denominator += quantity
    vwap = vwap_numerator / vwap_denominator
    return vwap


symbol = "BTCUSDT"
interval = "1m"
vwap = calculate_vwap(symbol, interval)
print(
    "Volume-Weighted Average Price (VWAP) for {} in the last 5 minutes: {:.2f}".format(
        symbol, vwap
    )
)
