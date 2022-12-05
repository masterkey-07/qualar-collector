from classes.errors import WrongVariables, WrongStation, WrongYear


class PayloadConstructor:
    def __init__(self, station: int, variables: list[list[int, int, int]], years: list[int]) -> None:
        if not isinstance(station, int):
            raise WrongStation
        elif station > 1000:
            raise WrongStation

        for vars in variables:
            if isinstance(vars, list):
                for var in vars:
                    if not isinstance(var, int):
                        raise WrongVariables
                    elif var > 1000:
                        raise WrongVariables
            else:
                raise WrongVariables

        if isinstance(years, list):
            for year in years:
                if not isinstance(year, int):
                    raise WrongYear
                elif year < 2000:
                    raise WrongYear
        else:
            raise WrongYear

        self.__station = station
        self.__variables = variables
        self.__years = years

    def __create_payload(self, year: int, variables: list[str]) -> dict:
        payload = {}

        payload['dataInicialStr'] = '01/01/' + str(year)
        payload['dataFinalStr'] = '31/12/' + str(year)
        payload['estacaoVO.nestcaMonto'] = self.__station
        payload['nparmtsSelecionados'] = variables

        return payload

    def get_yearly_payloads(self) -> list[list[dict]]:
        payloads = []

        for index in range(len(self.__years)):
            payloads.append([])
            for vars in self.__variables:
                payload = self.__create_payload(self.__years[index], vars)
                payloads[index].append(payload)

        return payloads
