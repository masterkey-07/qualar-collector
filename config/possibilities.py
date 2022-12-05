SJC = 88
SATELITE = 277
GREENVIEW = 278

BEN = 61
CO = 16
DV = 23
DVG = 21
MP10 = 12
NO = 17
NO2 = 15
NOX = 18
O3 = 63
SO2 = 13
TEMP = 25
TOL = 62
UR = 28
VV = 24
MP25 = 57
PRESS = 29
RADG = 26
RADUV = 56

SJC_OPTIONS = {
    'station': SJC,
    'selections': [
        [BEN, CO, DV],
        [DVG, MP10, NO],
        [NO2, NOX, O3],
        [SO2, TEMP, TOL],
        [UR, VV],
    ],
}

SATELITE_OPTIONS = {
    'station': SATELITE,
    'selections': [
        [CO, DV, DVG],
        [MP10, MP25, NO],
        [NO2, NOX, O3],
        [PRESS, RADG, RADUV],
        [TEMP, UR, VV],
    ],
}


GREENVIEW_OPTIONS = {
    'station': GREENVIEW,
    'selections': [
        [BEN, DV, DVG],
        [PRESS, RADG, RADUV],
        [TEMP, TOL, UR],
        [VV],
    ],
}
