from requests import Session
from config import possibilities, AUTH_URL, EXPORT_URL, LOGIN
from datetime import datetime


class Collector:

    def __init__(self, years: int):
        self.__years: int = years
        self.__session: Session = Session()

    def __authenticate(self):
        self.__session.post(AUTH_URL, data=LOGIN)

    def __create_payload(self, year: int, station: str, selected: list):
        payload = {}

        payload['dataInicialStr'] = '01/01/' + str(year)
        payload['dataFinalStr'] = '31/12/' + str(year)
        payload['estacaoVO.nestcaMonto'] = station
        payload['nparmtsSelecionados'] = selected

        return payload

    def __create_stations_payloads(self):
        present_year = datetime.now().year

        station_payloads = []

        station_index = 0

        for possibility in possibilities:
            station = possibility['station']

            selections = possibility['selections']

            station_payloads.append([])

            for index in range(self.__years):
                year = present_year - index

                for selected in selections:
                    payload = self.__create_payload(year, station, selected)

                    station_payloads[station_index].append(payload)

            station_index += 1

        return station_payloads

    def __treat__response(self, buffer: str):
        lines = buffer.split('\n')

        lines[6] = lines[6] + lines[7]

        lines.remove(lines[7])

        output = "\n".join(lines[6:])

        return output

    def collect_csvs(self):
        self.__authenticate()

        station_payloads = self.__create_stations_payloads()

        station_index = 0

        stations_responeses = []

        for payloads in station_payloads[0:1]:

            stations_responeses.append([])

            for payload in payloads[0:3]:
                response = self.__session.post(EXPORT_URL, data=payload)

                content = str(response.content, encoding='ISO-8859-1')

                treated = self.__treat__response(content)

                stations_responeses[station_index].append(treated)

        return stations_responeses
