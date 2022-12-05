from classes.collector import Collector
from classes.payloadconstructor import PayloadConstructor
from classes.concatenator import Concatenator
from classes.errors import WrongVariables, WrongStation, WrongYear
from config import SJC_OPTIONS, USERNAME, PASSWORD
import pytest


def create_constructor():
    station = SJC_OPTIONS['station']
    variables = SJC_OPTIONS['variables'][0]

    return PayloadConstructor(station, [variables], [2022, 2021])


def test_payload_constuctor():
    constructor = create_constructor()

    yearly_payloads = constructor.get_yearly_payloads()

    initial_date = yearly_payloads[0][0]['dataInicialStr']

    assert initial_date == "01/01/2022"

    with pytest.raises(WrongStation):
        constructor = PayloadConstructor('199', [[61, 16, 120]], [2021])

    with pytest.raises(WrongYear):
        constructor = PayloadConstructor(88, [[61, 16, 120]], [20])

    with pytest.raises(WrongVariables):
        constructor = PayloadConstructor(88, [2333], [2021])


def test_collector():
    constructor = create_constructor()

    collector = Collector(USERNAME, PASSWORD)

    csvs = collector.collect_yearly_csvs(constructor)

    csv = csvs[0][0]

    assert csv.count(';') >= 8760 * 4


def test_concatenator():
    constructor = create_constructor()

    collector = Collector(USERNAME, PASSWORD)

    csvs = collector.collect_yearly_csvs(constructor)

    csv = Concatenator().concatenate(csvs)

    assert csv.size > 8760 * 2
