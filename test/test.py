from classes.payloadconstructor import PayloadConstructor
from classes.errors import WrongVariables, WrongStation, WrongYear
import pytest


def test_payload_constuctor():
    request = PayloadConstructor(88, [[61, 16, 23]], [2021])

    assert request.get_yearly_payloads(
    )[0][0]['dataInicialStr'] == "01/01/2021"

    with pytest.raises(WrongStation):
        request = PayloadConstructor('199', [[61, 16, 120]], [2021])

    with pytest.raises(WrongYear):
        request = PayloadConstructor(88, [[61, 16, 120]], [20])

    with pytest.raises(WrongVariables):
        request = PayloadConstructor(88, [2333], [2021])
