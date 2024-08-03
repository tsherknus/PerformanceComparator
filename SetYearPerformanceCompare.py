import os
import json
from datetime import datetime
import time

def pricePctChange(ticker, start_year, end_year):
    start_date = datetime(start_year, 1, 1, 1)
    end_date = datetime(end_year, 1, 1, 1)
    # Convert the reference date to epoch time
    start_epoch = int(time.mktime(start_date.timetuple())) * 1000
    # print(start_epoch)
    end_epoch = int(time.mktime(end_date.timetuple())) * 1000
    # print(end_epoch)

    path = "C:/Users/tyler/OneDrive/Desktop/Financial Statement Analysis/StatementDB"

    ticker_candles = {}

    with open(path + "/" + ticker + "/" + ticker + "_candles.json") as json_file:
        ticker_candles = json.load(json_file)

    # print(ticker_candles)

    if str(start_epoch) in list(ticker_candles.keys()) and str(end_epoch) in list(ticker_candles.keys()):
        return ((ticker_candles[str(end_epoch)]['close'] - ticker_candles[str(start_epoch)]['open']) / ticker_candles[str(start_epoch)]['open'])
    else:
        return 0

benchmarks = ["SPY"]



for benchmark in benchmarks:
    print(benchmark)
    output_list = []
    benchmark_pct_change = pricePctChange(benchmark, 2019, 2024)

    path = "C:/Users/tyler/OneDrive/Desktop/Financial Statement Analysis/StatementDB"
    dir_list = os.listdir(path)

    for ticker in dir_list:
        ticker_pct_change = pricePctChange(ticker, 2019, 2024)
        if ticker_pct_change > (benchmark_pct_change * 1.75):
            output_list.append(ticker)
            # print(ticker)
            # print('ticker change %s' % ticker_pct_change)
            # print('benchmark change %s' % benchmark_pct_change)

    print(output_list)