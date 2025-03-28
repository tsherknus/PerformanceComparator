import os
import json

def get_pct_change(ticker, comparison_period):
    with open("data/" + ticker + "_candles.json") as file:
        candles = json.load(file)
        candle_list = []

        for candle in candles:
            candle_list.append(candle)

        comparison_candles = candle_list[-comparison_period:]
        starting_candle = candles[comparison_candles[0]]['close']
        ending_candle = candles[comparison_candles[-1]]['close']
        return (ending_candle - starting_candle) / starting_candle


# Enter the period to compare against the benchmark in months
comparison_period = 120
# Enter the benchmark ticker to compare against
benchmark_ticker = "QQQ"

benchmark_pct_change = get_pct_change(benchmark_ticker, comparison_period)
print(f'Benchmark PCT Change: {benchmark_pct_change}')
dir_list = os.listdir("data")
outperform_list = []

for file_name in dir_list:
    ticker = file_name.split("_")[0]
    pct_change = get_pct_change(ticker, comparison_period)
    if pct_change > benchmark_pct_change:
        outperform_list.append(ticker)
        print(f'{ticker} PCT Change {pct_change}')

print(len(dir_list)-1)
print(len(outperform_list))
print(outperform_list)


