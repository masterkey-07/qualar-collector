from pandas import read_csv, concat
from io import StringIO


class Concatenator:

    def __to_dataframe(self, data):
        return read_csv(StringIO(data), sep=';')

    def __concatenate_year(self, datas: list[str]):
        concatenated = self.__to_dataframe(datas[0])

        for data in datas[1:]:
            dataframe = self.__to_dataframe(data)

            concatenated = concatenated.merge(
                dataframe, on=['Data', 'Hora'], how='outer')

        return concatenated

    def concatenate(self, yearly_datas: list[list[str]]):

        concatenated = self.__concatenate_year(yearly_datas[0])

        for datas in yearly_datas[1:]:
            dataframe = self.__concatenate_year(datas)

            concatenated = concat([concatenated, dataframe])

        return concatenated
