import pandas as pd
import numpy as np
import datetime


def check(name):
    if name[0].isnumeric():
        print('Incorrect value. First letter must be upper. Try again!')
        return '-'
    if (not set(".,:;!_*-+()/\'\"#¤%&)").isdisjoint(name)):
        print('Name must not contain special characters. Try again!')
        return '-'
    return name.title()


def checkPhone(phone):

    if (phone[0]=='+' and phone[1]=='7'):
        phone = phone.replace('+7', '8', 1)
    if (phone[0]=='7'):
        phone = phone.replace('7', '8', 1)
    if len(phone) == 11 and phone[0] == '8' and phone.isnumeric():
        return phone
    print('Incorrect number. Try again!')
    return '-'


def checkDate(date):
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
        return date
    except ValueError:
        print('Incorrect data format. Try again!')
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
    inp = [x for x in (input('Enter name, surname, number of phone, (birthday YYYY-MM-DD), separated by space: ').split(' '))]
    while '' in inp:
        inp.remove('')
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
        print('Record with this name and surname is already in the dictionary')
        print('[1] - rewrite record')
        print('[something] - return to main menu')
        action = input()
        if action == '1':
            tb = Rewrite(tb)

    return tb


def DeleteEntry(tb):
    result = FindEntry(tb, input('Enter the fields which you want to delete the record, separated by space: '))
    if len(result) == 0:
        return tb
    PrintString(tb, result)
    if len(result) > 1:
        inp = input('Choose records, that you want to delete. Enter numbers of strings, separated by space: ')
        inp = [x for x in inp.split(' ')]
        while '' in inp:
            inp.remove('')
        for i in range(len(inp)):
            if not(inp[i].isnumeric()):
                print('Enter only numbers. Try again!')
                return tb
            if not(int(inp[i]) in result):
                print('Invalid string value. Try again!')
                return tb
            inp[i] = int(inp[i])
    else:
        inp = result
    tb.drop(index=inp, inplace=True)
    tb.reset_index(drop=True, inplace=True)
    print('Record was deleted!')
    return tb


def FindEntry(tb, string):
    inp = string.split(' ')
    while '' in inp:
        inp.remove('')

    if len(inp) > 4:
        print("To many arguments. Try again!")
        return []
    for i in range(len(inp)):
        inp[i] = inp[i][0].upper() + inp[i][1:]
    # поиск в teleponebook
    result_find = tb.values == '-'
    for x in inp:
        if x.isnumeric():
            x = int(x)
        find_x = tb.values == x
        for i in range(len(result_find)):
            for j in range(len(result_find[i])):
                if not(result_find[i][j]) and find_x[i][j]:
                    result_find[i][j] = find_x[i][j]
    # получение результата
    result = []
    for i in range(len(result_find)):
        count = 0
        for j in range(len(result_find[i])):
            if result_find[i][j]:
                count += 1
        if count == len(inp):
            result.append(i)

    if len(result) == 0:
        print('The record is not found in telephonebook')
    return result


def Rewrite(tb):
    PrintPhoneBook(tb)
    inp = [x for x in input('Choose number row and name of column. Enter separated by a space: ').split()]
    if len(inp) != 2:
        print('Invalid number of parametrs. Try again!')
    row, col = inp[0], inp[1]
    if inp[0].isalpha() and inp[1].isnumeric():
       row, col = inp[1], inp[0]
    row = int(row)
    if 0 > row > len(tb.index):
        print('Incorrect value of row. Try again!')
        return tb
    if not(col in tb.columns.values):
        print('Incorrect value of column. Try again!')
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


def AgePerson(tb):
    inp = [x for x in input('Enter name and surname, separated by space: ').split()]
    if len(inp) != 2:
        print('Incorrect number of values. Try again!')
        return
    if check(inp[0]) == '-' and check(inp[1]) == '-':
        print('Incorrect name or surname. Try again!')
        return
    res = FindEntry(tb, inp[0] + ' ' + inp[1])
    if len(res) == 0:
        return

    if tb.loc[res[0], 'Birthday'] == np.nan:
        print('Day of birthday do not write')
        return
    bday = datetime.datetime.strptime(tb.loc[res[0], 'Birthday'], '%Y-%m-%d')
    return (datetime.datetime.today() - bday).days // 365


def Birthday(tb):
    print('People who has birthday in next 30 days:')
    res = []
    today = datetime.datetime.today()
    rows = 0
    for day in tb['Birthday']:
        if str(day) != 'nan':
            bday = datetime.datetime.strptime(str(day), '%Y-%m-%d')
            bday_in_year = datetime.datetime(today.year, bday.month, bday.day)
            if 0 <= (bday_in_year - today).days <= 30:
                res.append(rows)
        rows += 1
    if res:
        PrintString(tb, res)
    else:
        print('No one has a birthday :_(')


def Years(tb, years):
    if not years.isnumeric():
        print('You enter not number. Try again!')
        return None
    print(' Enter:')
    print('[<] - if you want to see people who younger ', years, ' years')
    print('[=] - if you want to see people who ', years, ' years')
    print('[>] - if you want to see people who elder ', years, ' years')
    comparator = input()
    if comparator != '>' and comparator != '=' and comparator != '<':
        print('Imposible command. Try again!')
        return None
    res = []
    rows = 0
    for day in tb['Birthday']:
        if str(day) != 'nan':
            bday = datetime.datetime.strptime(str(day), '%Y-%m-%d')
            age = (datetime.datetime.today() - bday).days // 365
            if Compare(age, years, comparator):
                res.append(rows)
        rows += 1
    if res:
        PrintString(tb, res)
    else:
        print('No one was found :_(' )


def Compare(age, years, comporator):
    if comporator == '=':
        return age == years

    if comporator == '>':
        return age > years
    return age < years


def Save(tb, path):
    tb.to_csv(path, index=False)



