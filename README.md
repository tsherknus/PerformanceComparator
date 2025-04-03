# Performance Comparator

## Description

This project is used to compare the percentage change of a benchmark to a
larger list of stocks.

## Instructions

1. Generate the list of <ticker>_candles.json files using the HistoricPriceAggregator project
2. Delete the temp_candle.json file from the benchmark and comparison folder
3. Copy the <benchmark>_candles.json file from the HistoricPriceAggregator into the benchmark folder
4. Copy the tickers to compare <ticker>_candles.json files from the HistoricPriceAggregator into the comparison folder
5. Specify the duration in months that the pct increase will be benchmarked over in StocksToBenchmark.py
6. Specify the benchmark ticker that will be used to measure individual stocks in StocksToBenchmark.py
7. This project will generate a list of tickers that have outperformed the benchmark and a list of tickers that have underperformed the benchmark
