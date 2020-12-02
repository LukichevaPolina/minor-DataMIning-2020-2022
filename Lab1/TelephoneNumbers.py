import pandas as pd
import numpy as np
import datetime
import AuixiliaryFunctions


def OpenTelephoneBook(path):
    """
    Открытие телефонной книги.

    :return DataFrame with phonebook:
    """
    return pd.read_csv(path)


def PrintPhoneBook(tb):
    """
    Вывод телефонной книги в консоль без номера строк.

    :param tb:
    :return None:
    """
    with pd.option_context('display.max_row', None, 'display.max_columns', None):

        print('\n', tb.to_string(), '\n')


def NewRecord(tb):
    """
    Добавление новой записи в телефонную книгу.

    Происходит проверка на корректность введенных данных.

    Необходимо ввести name, surname, number of phone, (birthday YYYY-MM-DD), разделенные пробелом.

    :param tb:
    :return tb:
    """
    inp = [x for x in (input(
        'Enter name, surname, number of phone, (birthday YYYY-MM-DD), separated by space: ').split(' '))]
    inp = AuixiliaryFunctions.DeleteGap(inp)
    if len(inp) < 3:
        print('Not enough values. Try again!')
        return tb
    elif len(inp) > 4:
        print('Too many values. Try again!')
        return tb
    res = FindRecord(tb, inp[0]+' '+inp[1])
    if len(res) == 0:
        inp[0] = AuixiliaryFunctions.check(inp[0])
        inp[1] = AuixiliaryFunctions.check(inp[1])
        inp[2] = AuixiliaryFunctions.checkPhone(inp[2])
        if inp[0] != '-' and inp[1] != '-' and inp[2] != '-':
            if len(inp) == 3:
                inp.append(np.nan)
            else:
                if AuixiliaryFunctions.checkDate(inp[3]) == '-':
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


def DeleteRecord(tb):
    """
    Удаление записи из телефонной книги по одному или нескольким параметрам.

    Необходимо ввести поля, по которым будет совершен поиск записи в телефонной книги (возможен ввод имени, фамилии
    с маленькой буквы).
    В случае нахождения единственной записи, подходящей под введенные параметры, она будет удалена.
    В случае нахождения нескольких подходящих записей, пользователь должен ввести номера строк записей, которые он хочет
    удалить через пробел.

    :param tb:
    :return tb:
    """
    result = FindRecord(tb, input('Enter some fields of the line you want to delete in phonebook, separated by space: '))
    if len(result) == 0:
        return tb
    AuixiliaryFunctions.PrintString(tb, result)
    if len(result) > 1:
        inp = input('Choose records, that you want to delete. Enter numbers of strings, separated by space: ')
        inp = AuixiliaryFunctions.DeleteGap([x for x in inp.split(' ')])
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
    print('Record(s) was deleted!')
    return tb


def FindRecord(tb, string):
    """
    Поиск записи в телефонной книге.

    Поиск осуществляется по одному или нескольким параметрам.
    Пользователю необходимо ввести параметры, по которым будет осуществлен поиск через пробел (возможен ввод имени и
    фамилии с маленькой буквы).
    После выполнения функции пользователь увидит строки, подходящие под введеные параметры.

    :param tb:
    :param string:
    :return list of numbers strings in DataFrame or empty list:
    """

    inp = AuixiliaryFunctions.DeleteGap(string.split(' '))
    if len(inp) == 0:
        print("Anything was entered. Try again!")
        return []
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
    """
    Перезаписывание одного из полей существующей записи в телефонной книге.

    Пользователю необходимо ввести номер строки и название столбца того поля, которое необходимо редактировать.
    Далее необходимо ввести корректное новое содержимое для ячейки.
    После завершения функции, в случае корректного ввода, телефонная книга будет изменена.

    :param tb:
    :return tb:
    """
    PrintPhoneBook(tb)
    inp = AuixiliaryFunctions.DeleteGap(
        [x for x in input('Choose number row and name of column. Enter separated by a space: ').split(' ')])
    if len(inp) != 2:
        print('Invalid number of parametrs. Try again!')
        return tb
    row, col = inp[0], inp[1]
    if inp[0].isalpha() and inp[1].isnumeric():
       row, col = inp[1], inp[0]
    if row.isalpha():
        print('Incorrect value of row. Try again!')
        return tb
    row = int(row)

    if 0 > row > len(tb.index):
        print('Incorrect value of row. Try again!')
        return tb
    if not(col in tb.columns.values):
        print('Incorrect value of column. Try again!')
        return tb
    rewrite = input('Enter value: ')
    if col == 'Name' or col == 'Surname':
        rewrite = AuixiliaryFunctions.check(rewrite)
    elif col == 'Phone':
        rewrite = AuixiliaryFunctions.checkPhone(rewrite)
    else:
        rewrite = AuixiliaryFunctions.checkDate(rewrite)
    if rewrite != '-':
        tb.loc[row, col] = rewrite
        print('The record was rewrite!')

    return tb


def AgePerson(tb):
    """
    Вычисление возраста человека, записанного в телефонной книге.

    Пользователю необходимо ввести имя и фамилию человека, чей возраст он хочет узнать.
    В случе отсутствия записи о возрасте, пользователь получит об этом сообщение и будет возвращен в главное меню,
    иначе увидит вывод возраста человека в годах.

    :param tb:
    :return age of person or None:
    """
    inp = AuixiliaryFunctions.DeleteGap(
        [x for x in input('Enter name and surname of person, separated by space: ').split(' ')])
    if len(inp) != 2:
        print('Incorrect number of values. Try again!')
        return None
    if AuixiliaryFunctions.check(inp[0]) == '-' and AuixiliaryFunctions.check(inp[1]) == '-':
        print('Incorrect name or surname. Try again!')
        return None
    res = FindRecord(tb, inp[0] + ' ' + inp[1])
    if len(res) == 0:
        return None
    if type(tb.loc[res[0], 'Birthday']) == type(np.nan):
        print('Day of birthday do not write')
        return None
    bday = datetime.datetime.strptime(tb.loc[res[0], 'Birthday'], '%Y-%m-%d')
    return (datetime.datetime.today() - bday).days // 365


def Birthday(tb):
    """
    Вывод записей о тех людях, чьи дни рождения находятся в диапозоне близжайшего месяца.

    :param tb:
    :return None:
    """
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
        AuixiliaryFunctions.PrintString(tb, res)
    else:
        print('No one has a birthday :_(')


def Years(tb, years):
    """
    Вывод записей о людях, кто старше/младше/ровно N лет.

    Пользователю нужно ввести интересующий его возраст, а так же выбрать параметр, по которому необходимо отобрать
    записи из телефонной книги ( < - для людей страше N лет;
                                 = - для людей ровно N лет;
                                 > - для людей младше N лет).


    :param tb:
    :param years:
    :return:
    """
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
            if AuixiliaryFunctions.Compare(age, int(years), comparator):
                res.append(rows)
        rows += 1
    if res:
        AuixiliaryFunctions.PrintString(tb, res)
    else:
        print('No one was found :_(')


def Save(tb, path):
    """
    Сохранение DataFrame в файл, указанный в параметрах функции.

    :param tb:
    :param path:
    :return:
    """
    tb.to_csv(path, index=False)



