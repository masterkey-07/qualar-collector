from classes.collector import Collector
from classes.payloadconstructor import PayloadConstructor
from classes.concatenator import Concatenator
from config import PASSWORD, USERNAME, SJC_OPTIONS,  SATELITE_OPTIONS, GREENVIEW_OPTIONS

options = [SJC_OPTIONS, SATELITE_OPTIONS, GREENVIEW_OPTIONS]

years = [2022, 2021, 2020, 2019]

for option in options:
    label = option['label']
    station = option['station']
    variables = option['variables']

    collector = Collector(USERNAME, PASSWORD)

    constructor = PayloadConstructor(station, variables, years)

    response = collector.collect_yearly_csvs(constructor)

    concatenator = Concatenator()

    csv = concatenator.concatenate(response)

    csv.to_csv('./data/' + label + '.csv')
