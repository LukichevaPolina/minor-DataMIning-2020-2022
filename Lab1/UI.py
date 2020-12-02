import TelephoneNumbers
import AuixiliaryFunctions
try:
    tb = TelephoneNumbers.OpenTelephoneBook('tbook.txt')
    """
        Основной цикл программы, в котором реализован интерфейс для взаимодейсвтия с основными функциями телефонной книги.
        Пользователь с помощью предложенных номеров команд, может вызвать ту или иную функцию.
        После выполнения каждой функции, изменения сохраняются в файл.
    
        comannd: переменная, хранящая выбор пользователя
    """
    while True:
        print('This is PhoneBook. Choose command:')
        print('[1] - Print PhoneBook')
        print('[2] - Find some record')
        print('[3] - Delete some record')
        print('[4] - Create new record')
        print('[5] - Rewrite some record')
        print('[6] - Age of person')
        print('[7] - People who has birthday in the next 30 days')
        print('[8] - People elder/younger N years')
        print('[9] - Exit from phonebook')
        command = input('>>>')
        if command == '1':
            TelephoneNumbers.PrintPhoneBook(tb)
        elif command == '2':
            res = TelephoneNumbers.FindRecord(tb, input('Enter what do you want to find: '))
            AuixiliaryFunctions.PrintString(tb, res)
        elif command == '3':
            tb = TelephoneNumbers.DeleteRecord(tb)
            TelephoneNumbers.Save(tb, 'tbook.txt')
        elif command == '4':
            tb = TelephoneNumbers.NewRecord(tb)
            TelephoneNumbers.Save(tb, 'tbook.txt')
        elif command == '5':
            tb = TelephoneNumbers.Rewrite(tb)
            TelephoneNumbers.Save(tb, 'tbook.txt')
        elif command == '6':
            age = TelephoneNumbers.AgePerson(tb)
            if age:
                print('The age of person: ', age)
        elif command == '7':
            TelephoneNumbers.Birthday(tb)
        elif command == '8':
            TelephoneNumbers.Years(tb, input('Enter number of years: '))
        elif command == '9':
            TelephoneNumbers.Save(tb, 'tbook.txt')
            quit('Good bye!')
        else:
            print('Incorrect command. Try Again!')
except:
    print('Unable to open file. Try changing the path')
