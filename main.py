from classes.collector import Collector
from classes.concatenator import Concatenator
from pandas import DataFrame

collector = Collector(4)
concatenator = Concatenator()

yearly_csvs = collector.collect_yearly_csvs()
