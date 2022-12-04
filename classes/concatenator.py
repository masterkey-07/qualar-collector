from pandas import read_csv
from io import StringIO


class Concatenator:

    def __to_dataframe(self, data):
        return read_csv(StringIO(data), sep=';')

    def concatenate(self, datas):

        for index in range(len(datas)):
            datas[index] = self.__to_dataframe(datas[index])

        output = datas[0]

        for index in range(1, len(datas)):

            output = output.merge(
                datas[index],  how='outer', on=['Data', 'Hora'])

        return output
