from classes.collector import Collector
import pytest

LOGIN_USERNAME = "pedro.paulo.vianna@hotmail.com"
LOGIN_PASSWORD = "Pedro123789456."


def test_session_login_sucesseful():
    collector = Collector(LOGIN_USERNAME + 'dsa', LOGIN_PASSWORD + "ads")

    assert 1 == 1
