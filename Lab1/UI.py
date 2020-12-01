import TelephoneNumbers
# try:
tb = TelephoneNumbers.OpenTelephoneBook('tbook.txt')
while (True):
    print('It is telephonebook. Choose command:')
    print('[1] - Print PhoneBook')
    print('[2] - Find some record')
    print('[3] - Delete some record')
    print('[4] - Create new record')
    print('[5] - Rewrite some record')
    print('[6] - Age of person')
    print('[7] - People who has birthday in the next 30 days')
    print('[8] - People elder/younger N years')
    print('[9] - Exit from telephonebook')
    command = input()
    if command == '1':
        TelephoneNumbers.PrintPhoneBook(tb)
    elif command == '2':
        res = TelephoneNumbers.FindEntry(tb, input('Enter what do want to find'))
        TelephoneNumbers.PrintString(tb, res)
    elif command == '3':
        tb = TelephoneNumbers.DeleteEntry(tb)
        TelephoneNumbers.Save(tb, 'tbook.txt')
    elif command == '4':
        tb = TelephoneNumbers.NewEntry(tb)
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
        exit('Good bye!')
    else:
        print('Imposible Command. Try Again!')
# except:
#       print('Unable to open file. Try changing the path')
