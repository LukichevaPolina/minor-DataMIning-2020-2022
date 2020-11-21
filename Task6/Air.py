import pandas
import numpy as np


def DayAndHourConcentration(data, func, row):
    return data.loc[data[row] == (func(data[row])), 'Date'].iloc[0] + ' ' + data.loc[data[row] == (func(data[row])), 'Time'].iloc[0]


data = pandas.read_csv(r'AirQualityUCI.csv', sep =';')
data.replace(to_replace=-200.0, value=np.nan, inplace=True)

for header in list(data)[2:]:
    print('Min concentration of ', header, 'was ', DayAndHourConcentration(data, min, header))
    print('Max concentration of ', header, 'was ', DayAndHourConcentration(data, max, header), '\n')



