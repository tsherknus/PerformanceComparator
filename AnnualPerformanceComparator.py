import os
import json

annual_stock_performance = {}
consistent_beats = {}
def key_list_generator(ticker_candles):
    key_list = []
    i = 0
    for x in range(len(ticker_candles.keys()) // 12):
        key_list.append(list(ticker_candles.keys())[i])
        i += 12

    return key_list

def write_file(input, file_name):
    with open(file_name + ".json", "w+") as file:
        file.seek(0)
        file.truncate()
        json.dump(input, file, indent=4, sort_keys=True)

def annual_performance_comparator(benchmark):
    path = "C:/Users/tyler/OneDrive/Desktop/Financial Statement Analysis/StatementDB"
    dir_list = os.listdir(path)

    benchmark_candles = {}

    with open(path + "/" + benchmark + "/" + benchmark + "_candles.json") as json_file:
        benchmark_candles = json.load(json_file)

    for ticker in dir_list:
        temp_dict = {}
        with open(path + "/" + ticker + "/" + ticker + "_candles.json") as json_file:
            ticker_candles = json.load(json_file)
            if ticker_candles:
                key_list = key_list_generator(ticker_candles)

                for i in range(len(key_list)):
                    if i+1 < len(key_list):
                        benchmark_performance = (benchmark_candles[key_list[(i+1)]]['close'] - benchmark_candles[key_list[i]]['open']) / benchmark_candles[key_list[i]]['open']
                        ticker_performance = (ticker_candles[key_list[(i+1)]]['close'] - ticker_candles[key_list[i]]['open']) / ticker_candles[key_list[i]]['open']
                        temp_dict[i] = {'benchmark_performance': benchmark_performance, 'ticker_performance': ticker_performance}
        annual_stock_performance[ticker] = temp_dict


def annual_benchmark_beat_pct(benchmark):
    annual_performance_comparator(benchmark)

    for x in annual_stock_performance:
        i = 0
        if annual_stock_performance[x]:
            for y in range(len(annual_stock_performance[x])):
                ticker_performance = annual_stock_performance[x][y]['ticker_performance']
                benchmark_performance = annual_stock_performance[x][y]['benchmark_performance']
                if ticker_performance > benchmark_performance:
                    i += 1
            performance = i / len(annual_stock_performance[x])
            if len(annual_stock_performance[x]) > 5:
                consistent_beats[x] = performance
            else:
                consistent_beats[x] = None

    # write_file(annual_stock_performance, benchmark + "_annual_stock_performance")
    #write_file(consistent_beats, benchmark + "_consistent_beats")
    return consistent_beats
