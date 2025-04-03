import os
import json

def get_pct_change(path_to_candles, comparison_period):
    with open(path_to_candles) as file:
        candles = json.load(file)
        candle_list = []

        for candle in candles:
            candle_list.append(candle)

        if len(candle_list) == 0:
            return 0

        comparison_candles = candle_list[-comparison_period:]
        starting_candle = candles[comparison_candles[0]]['close']
        ending_candle = candles[comparison_candles[-1]]['close']
        return (ending_candle - starting_candle) / starting_candle


# Enter the period to compare against the benchmark in months
comparison_period = 120
# Enter the benchmark ticker to compare against
benchmark_ticker = 'QQQ'

benchmark_path = 'data/benchmark/' + benchmark_ticker + '_candles.json'

benchmark_pct_change = get_pct_change(benchmark_path, comparison_period)
print(f'Benchmark PCT Change: {benchmark_pct_change}')

comparison_path = 'data/comparison/'

dir_list = os.listdir(comparison_path)

outperform_list = []
underperform_list = []

for file_name in dir_list:
    ticker = file_name.split('_')[0]
    pct_change = get_pct_change(comparison_path+file_name, comparison_period)
    if pct_change >= benchmark_pct_change:
        outperform_list.append(ticker)
        # print(f'{ticker} PCT Change {pct_change}')
    else:
        underperform_list.append(ticker)
        # print(f'{ticker} PCT Change {pct_change}')

print(f'Outperformers ({len(outperform_list)}):')
print(outperform_list)
print(f'Underperformers ({len(underperform_list)}):')
print(underperform_list)

