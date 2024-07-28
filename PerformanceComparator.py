import os
import json
import time
import datetime
from AnnualPerformanceComparator import *

output_list = []
winners_list = []
loser_list = []


def add_to_dict(ticker, benchmark_pct_chg, ticker_pct_increase, first_ticker_candle, last_ticker_candle):
    period_start = datetime.datetime.fromtimestamp((int(first_ticker_candle) / 1000))
    period_end = datetime.datetime.fromtimestamp((int(last_ticker_candle) / 1000))
    comparison_period = (period_end - period_start).days
    benchmark_beat = ticker_pct_increase - benchmark_pct_chg
    annual_beat_pct = None
    if ticker in annual_perf.keys():
        annual_beat_pct = annual_perf[ticker]

    temp_dict = {'ticker': ticker, 'benchmark_pct_change': benchmark_pct_chg, 'benchmark_beat': benchmark_beat,
                 'ticker_pct_change': ticker_pct_increase, 'period_start': period_start.strftime('%Y-%m-%d'),
                 'period_end': period_end.strftime('%Y-%m-%d'), 'comparison_period': f"{comparison_period / 365} years",
                 'annual_benchmark_beat_pct': annual_beat_pct}

    if (temp_dict['benchmark_beat'] > 5 and temp_dict['annual_benchmark_beat_pct']
            and temp_dict['annual_benchmark_beat_pct'] > 0.65):
        winners_list.append(temp_dict)

    if (temp_dict['benchmark_beat'] < 0 and temp_dict['annual_benchmark_beat_pct']
            and temp_dict['annual_benchmark_beat_pct'] < 0.35):
        loser_list.append(temp_dict)

    output_list.append(temp_dict)


def write_file(benchmark, output_list, file_name):
    with open(benchmark + file_name, "w+") as test:
        test.seek(0)  # <- This is the missing piece
        test.truncate()
        json.dump(output_list, test, indent=4, sort_keys=True)


def overall_performance_comparator(benchmark):
    path = "C:/Users/tyler/OneDrive/Desktop/Financial Statement Analysis/StatementDB"
    dir_list = os.listdir(path)

    benchmark_candles = {}

    with open(path + "/" + benchmark + "/" + benchmark + "_candles.json") as json_file:
        benchmark_candles = json.load(json_file)

    benchmark_first_candle = list(benchmark_candles.keys())[0]
    benchmark_last_candle = list(benchmark_candles.keys())[-1]
    benchmark_pct_chg = (benchmark_candles[benchmark_last_candle]['close'] - benchmark_candles[benchmark_first_candle][
        'open']) / benchmark_candles[benchmark_first_candle]['open']

    for ticker in dir_list:
        with open(path + "/" + ticker + "/" + ticker + "_candles.json") as json_file:
            ticker_candles = json.load(json_file)
            if ticker_candles:
                first_ticker_candle = list(ticker_candles.keys())[0]
                last_ticker_candle = list(ticker_candles.keys())[-1]
                ticker_pct_increase = (ticker_candles[last_ticker_candle]['close'] -
                                       ticker_candles[first_ticker_candle][
                                           'open']) / ticker_candles[first_ticker_candle]['open']

                if ticker_candles[first_ticker_candle]['open'] > 0.1:
                    if first_ticker_candle == benchmark_first_candle:
                        add_to_dict(ticker, benchmark_pct_chg, ticker_pct_increase, first_ticker_candle,
                                    last_ticker_candle)
                    else:
                        special_qqq_inc = (benchmark_candles[benchmark_last_candle]['close'] -
                                           benchmark_candles[first_ticker_candle]['open']) / \
                                          benchmark_candles[first_ticker_candle]['open']
                        add_to_dict(ticker, special_qqq_inc, ticker_pct_increase, first_ticker_candle,
                                    last_ticker_candle)


benchmarks = ["SPY", "QQQ"]

annual_perf = {}

for benchmark in benchmarks:
    annual_perf = annual_benchmark_beat_pct(benchmark)
    overall_performance_comparator(benchmark)
    output_list_1 = sorted(output_list, key=lambda d: d['benchmark_beat'])
    winners_list_1 = sorted(winners_list, key=lambda d: d['benchmark_beat'])
    loser_list_1 = sorted(loser_list, key=lambda d: d['benchmark_beat'])
    write_file(benchmark, output_list_1, "_overall.json")
    write_file(benchmark, winners_list_1, "_winners.json")
    write_file(benchmark, loser_list_1, "_losers.json")
    output_list = []
    winners_list = []
    loser_list = []

