import http.client
import json


class CandleData:
    def __init__(self, time, low, high, open_price, close_price, volume):
        self.time = time
        self.low = low
        self.high = high
        self.open_price = open_price
        self.close_price = close_price
        self.volume = volume


def fetch_candle_data():
    conn = http.client.HTTPSConnection("api.pro.coinbase.com")
    start_time = "2018-07-01T00:00:00"
    end_time = "2018-07-15T12:00:00"
    granularity = 86400
    endpoint = f"/products/BTC-USD/candles?start={start_time}&end={end_time}&granularity={granularity}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    conn.request("GET", endpoint, headers=headers)
    res = conn.getresponse()
    data = res.read()
    return data.decode("utf-8")


def parse_candle_data(data):
    candle_data_list = []
    json_data = json.loads(data)
    for item in json_data:
        candle_data = CandleData(item[0], item[1], item[2], item[3], item[4], item[5])
        candle_data_list.append(candle_data)
    return candle_data_list


def handler(event, context):
    data = fetch_candle_data()
    candle_data_list = parse_candle_data(data)
    for candle_data in candle_data_list:
        print("Time:", candle_data.time)
        print("Low:", candle_data.low)
        print("High:", candle_data.high)
        print("Open Price:", candle_data.open_price)
        print("Close Price:", candle_data.close_price)
        print("Volume:", candle_data.volume)
        print()


if __name__ == "__main__":
    handler(None, None)
