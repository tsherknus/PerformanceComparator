# Performance Comparator

## Description

This project is used to compare the percentage change of a benchmark to a
larger list of stocks.

## Instructions

1. Generate the list of <ticker>_candles.json files using the HistoricPriceAggregator project
2. Delete the temp_candle.json file from the data folder
3. Copy the <ticker>_candles.json files from the HistoricPriceAggregator into the data folder
4. Specify the duration in months that the pct increase will be benchmarked over in StocksToBenchmark.py
5. Specify the benchmark ticker that will be used to measure individual stocks in StocksToBenchmark.py
6. This project will generate a list of tickers that have outperformed the benchmark