from classes.collector import Collector
from classes.concatenator import Concatenator
from pandas import DataFrame

collector = Collector(4)
concatenator = Concatenator()

stations_csvs = collector.collect_csvs()

for csvs in stations_csvs:
    csv: DataFrame = concatenator.concatenate(csvs)

    csv.to_csv('')
