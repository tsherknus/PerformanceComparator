import json


def write_file(input, file_name):
    with open(file_name + ".json", "w+") as output:
        output.seek(0)
        output.truncate()
        json.dump(input, output, indent=4, sort_keys=True)


def open_file(path):
    with open(path) as input:
        return json.load(input)

benchmarks = ["SPY", "QQQ"]

for benchmark in benchmarks:
    output = {}

    beats_path = "C:/Users/tyler/OneDrive/Desktop/PerformanceComparator/" + benchmark + "_consistent_beats.json"
    overall_path = "C:/Users/tyler/OneDrive/Desktop/PerformanceComparator/" + benchmark + "_overall.json"

    consistent_beats = open_file(beats_path)
    overall_performance = open_file(overall_path)

    for ticker in consistent_beats:
        temp = overall_performance[ticker]
        temp["annual_beat_history_pct"] = consistent_beats[ticker]
        output[ticker] = temp

    write_file(output, benchmark + "_outperformers")
