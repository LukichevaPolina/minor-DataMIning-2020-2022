import datetime


def check(name):
    """
    Проверка корректности введеного имени или фамилии.

    Происходит замена первой буквы на заглавную, проверка корректости первого символа,
    проверка на отсутствие в имени/фамилии специальных символов.

    :param name:
    :return name or -:
    """
    if name[0].isnumeric():
        print('Incorrect value. First letter must be upper. Try again!')
        return '-'
    if not set(".,:;!?_*-+()/\'\"#¤%&)").isdisjoint(name):
        print('Name must not contain special characters. Try again!')
        return '-'
    return name.title()


def checkPhone(phone):
    """
    Проверка корректности телефонного номера.

    Замена +7 или 7 на 8, проверка корректности длины номера телефона, проверка на содержание только цифр в номере.

    :param phone:
    :return phone or -:
    """

    if phone[0] == '+' and phone[1] == '7':
        phone = phone.replace('+7', '8', 1)
    if phone[0] == '7':
        phone = phone.replace('7', '8', 1)
    if len(phone) == 11 and phone[0] == '8' and phone.isnumeric():
        return phone
    print('Incorrect number. Try again!')
    return '-'


def checkDate(date):
    """
    Проверка кореектности введенной даты рождения с помощью datetime.

    :param date:
    :return date or -:
    """
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
        return date
    except ValueError:
        print('Incorrect data format. Try again!')
        return '-'


def PrintString(tb, index):
    """
    Печать строк, чьи номера находятся в списке index.

    :param tb:
    :param index:
    """
    for i in index:
        print(tb.iloc[[i]])


def Compare(age, years, comparator):
    """
    Сравнение age и years по параметру comparator.

    :param age:
    :param years:
    :param comparator:
    :return True or False:
    """
    if comparator == '=':
        return age == years

    if comparator == '>':
        return age > years
    return age < years


def DeleteGap(inp):
    """
    Удаление пустых элементов из списка inp.

    :param inp:
    :return inp:
    """
    while '' in inp:
        inp.remove('')
    return inp