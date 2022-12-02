from config import possibilities, URL, BROWSER
from datetime import datetime
from os import system
from os.path import dirname, join, expanduser
from time import sleep
from shutil import move, rmtree


class Collector:

    def __init__(self, years):
        self.__years = years

    def __create_url(self, year: int, station: str, selected):
        output = URL

        output = output + '&dataInicialStr=01/01/' + str(year)
        output = output + '&dataFinalStr=31/12/' + str(year)
        output = output + '&estacaoVO.nestcaMonto=' + station

        for var in selected:
            output = output + '&nparmtsSelecionados=' + var

        return output

    def __create_urls(self):
        present_year = datetime.now().year

        urls = []

        for index in range(self.__years):
            year = present_year - index

            for possibility in possibilities:
                station = possibility['station']

                for vars in possibility['selections']:
                    selected = []
                    for var in vars:
                        if var != None:
                            selected.append(var)

                    urls.append(self.__create_url(year, station, selected))

        return urls

    def collect_csvs(self):
        urls = self.__create_urls()

        download_path = join(expanduser('~'), 'Downloads')
        base_path = join(dirname(dirname(__file__)), 'data', 'base')

        rmtree(download_path)

        for url in urls:
            command = BROWSER + ' \"' + url + "\""
            system(command)
            sleep(10)

        sleep(30)

        rmtree(base_path)

        move(download_path, base_path)
