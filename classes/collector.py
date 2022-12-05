from requests import Session
from config import AUTH_URL, EXPORT_URL
from classes.payloadconstructor import PayloadConstructor


class Collector:

    def __init__(self, username: str, password: str) -> None:
        self.__session: Session = Session()

        self.__authenticate(username, password)

    def __authenticate(self, username, password):
        login = {}

        login['cetesb_login'] = username
        login['cetesb_password'] = password
        login['envia'] = 'OK'

        self.__session.post(AUTH_URL, data=login)

    def __treat__response(self, buffer: str):
        lines = buffer.split('\n')

        lines[6] = 'Data;Hora;' + lines[7][3:]

        lines.remove(lines[7])

        output = "\n".join(lines[6:])

        return output

    def collect_yearly_csvs(self, constructor: PayloadConstructor) -> list[list[str]]:
        yearly_csvs = []

        yearly_payloads = constructor.get_yearly_payloads()

        for index in range(len(yearly_payloads)):
            yearly_csvs.append([])

            for payload in yearly_payloads[index]:

                response = self.__session.post(EXPORT_URL, data=payload)

                content = str(response.content, encoding='ISO-8859-1')

                treated = self.__treat__response(content)

                yearly_csvs[index].append(treated)

        return yearly_csvs
