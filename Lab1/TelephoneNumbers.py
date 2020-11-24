import pandas as pd
import numpy as np
import datetime


def check(name):
    if name[0].isnumeric():
        print('Incorrect value. First letter must be upper. Try again')
        return '-'
    if (not set(".,:;!_*-+()/\'\"#¤%&)").isdisjoint(name)):
        print('Name must not contain special characters. Try again')
        return '-'
    if name[0].islower():
        return name.title()
    return name


def checkPhone(phone):

    if (phone[0]=='+' and phone[1]=='7'):
        phone = phone.replace('+7', '8', 1)
    if (phone[0]=='7'):
        phone = phone.replace('7', '8', 1)
    if len(phone) > 11 or phone[0] != '8' or not(phone.isnumeric()):
        print('Incorrect number. Try again!')
        return '-'
    return phone


def checkDate(date):
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
        return date
    except ValueError:
        print('Incorrect data format. Try again')
        return '-'


def PrintString(tb, index):
    for i in index:
        print(tb.iloc[[i]])


def OpenTelephoneBook(path):
    return pd.read_csv(path)


def PrintPhoneBook(tb):
    #печать без пропусков
    with pd.option_context('display.max_row', None, 'display.max_columns', None):
        #печать без номера строк
        print('\n', tb.to_string(), '\n')


def NewEntry(tb):
    inp = [x for x in (input('Enter: NAME SURNAME PHONE (BIRTHDAY)').split(' '))]
    if len(inp) < 3:
        print('Not enough values. Try again!')
        return tb
    elif len(inp) > 4:
        print('Too much values. Try again!')
        return tb
    res = FindEntry(tb, inp[0]+' '+inp[1])
    if len(res) == 0:
        inp[0] = check(inp[0])
        inp[1] = check(inp[1])
        inp[2] = checkPhone(inp[2])
        if inp[0] != '-' and inp[1] != '-' and inp[2] != '-':
            if len(inp) == 3:
                inp.append(np.nan)
            else:
                if checkDate(inp[3]) == '-':
                    return tb

            tb.loc[len(tb.index)] = inp
            print('Entry was added!')
    else:
        print('Entry with this name and surname is already in the dictionary')
        print('[1] - rewrite record')
        print('[something] - return to main menu')
        action = input()
        if action == '1':
            tb = Rewrite(tb)

    return tb


def DeleteEntry(tb):
    result = FindEntry(tb, input('Enter something: '))
    if len(result) == 0:
        return tb
    PrintString(tb, result)
    if len(result) > 1:
        inp = input('Choose records, that you want to delete. Enter numbers of strings: ')
        inp = [x for x in inp.split(' ')]
        for i in range(len(inp)):
            if not(inp[i].isnumeric()):
                print('Enter only numbers! Try again')
                return tb
            if not(int(inp[i]) in result):
                print('Invalid string value. Try again')
                return tb
            inp[i] = int(inp[i])
    else:
        inp = result
    tb.drop(index=inp, inplace=True)
    tb.reset_index(drop=True, inplace=True)
    print('Record was deleted!')
    return tb


def FindEntry(tb, str):
    inp = str.split(' ')

    if len(inp) > 4:
        print("To many arguments. Try again")
        return []

    df1 = tb.values == '-'
    #замена первых букв на заглавные
    for i in range(len(inp)):
        inp[i] = inp[i][0].upper() + inp[i][1:]

    #поиск в df
    for x in inp:
        if x.isnumeric():
            x = int(x)
        df2 = tb.values == x
        for i in range(len(df1)):
            for j in range(len(df1[i])):
                if df1[i][j] == False and df2[i][j] == True:
                    df1[i][j] = df2[i][j]

    result = []
    #получение результата
    for i in range(len(df1)):
        count = 0
        for j in range(len(df1[i])):
            if df1[i][j] == True:
                count += 1
        if count == len(inp):
            result.append(i)

    if len(result) == 0:
        print('The record is not found\n')
    return result


def Rewrite(tb):
    PrintPhoneBook(tb)
    inp = [x for x in input('Choose number row and name of column. Enter separated by a space: ').split()]
    if len(inp) != 2:
        print('Invaliid number of parametrs. Try again')
    row, col = inp[0], inp[1]
    if inp[0].isalpha() and inp[1].isnumeric():
       row, col = inp[1], inp[0]
    row = int(row)
    if 0 > row > len(tb.index):
        print('Incorrect value of row. Try again')
        return tb
    if not(col in tb.columns.values):
        print('Incorrect value of column. Try again')
        return tb
    rewrite = input('Enter value: ')
    if col == 'Name' or col == 'Surname':
        rewrite = check(rewrite)
    elif col == 'Phone':
        rewrite = checkPhone(rewrite)
    else:
        rewrite = checkDate(rewrite)
    if rewrite != '-':
        tb.loc[row, col] = rewrite
    return tb




def SaveExit(tb, path):
    tb.to_csv(path)
    exit()


