import pandas
import numpy as np


#подсчет числа землетрясений сильнее num баллов
def CountQuake(data, num):
    return len(data[data.Richter > num])


#топ 10 земдетрясений по параметру
def Top10(data, top, parametr):
    return data.nlargest(top, parametr)


#количество землятресений в полушарии
def DefineHemicphere(data, parametr, border1, border2):
    filtr = data[(data[parametr] >= border1) & (data[parametr] <= border2)]
    return filtr


def Top10TwoParametrs(data, parametr1, parametr2):
    return data.sort_values(by=[parametr1, parametr2]).tail(10)


def TheMostHemicsphere(north, south, east, west, parametr):
    max_v = max(north[parametr].mean(), south[parametr].mean(), east[parametr].mean(), west[parametr].mean())
    if max_v == north[parametr].mean():
        return 'northen'
    elif max_v == south[parametr].mean():
        return 'southen'
    elif max_v == east[parametr].mean():
        return 'easten'
    return 'westen'


def FurtherPoint(data):
    a = 0
    #дописать



data = pandas.read_csv(r"quake.csv")
print('Number earthquakes above 6: ', CountQuake(data, 6))

print('Top-10 earthquakes by depth:\n', Top10(data, 10, 'Focal depth'))
print('The most points located in Pacifiс Ocean\n')
print('Top-10 earthquakes by richter:\n', Top10(data, 10, 'Richter'))
print('Three points located in Pechora Sea\n')

north = DefineHemicphere(data, 'Latitude', 0, 90)
south = DefineHemicphere(data, 'Latitude', -90, 0)
east = DefineHemicphere(data, 'Longitude', 0, 180)
west = DefineHemicphere(data, 'Longitude', -180, 0)

print('Northen hemicphere had ', len(north), ' quakes')
print('Top-10 by deph and richter:\n', Top10TwoParametrs(north, 'Focal depth', 'Richter'))

print('\nSouthen hemicphere had ', len(south), ' quakes')
print('Top-10 by deph and richter:\n', Top10TwoParametrs(south, 'Focal depth', 'Richter'))
print('\nEasten hemicphere had ', len(east), ' quakes')
print('Top-10 by deph and richter:\n', Top10TwoParametrs(east, 'Focal depth', 'Richter'))
print('\nWesten hemicphere had ', len(west), ' quakes')
print('Top-10 by deph and richter:\n', Top10TwoParametrs(west, 'Focal depth', 'Richter'))

print('\nThe most depht hemocphere is', TheMostHemicsphere(north, south, east, west, 'Focal depth'))
print('\nThe most rechter hemocphere is', TheMostHemicsphere(north, south, east, west, 'Richter'))
print('\nThe further earthquake has coordinates:', FurtherPoint(data))