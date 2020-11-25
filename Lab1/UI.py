import TelephoneNumbers
# try:
tb = TelephoneNumbers.OpenTelephoneBook('tbook.txt')
while (True):
    print('It is telephonebook. Choose command:')
    print('[1] - Print PhoneBook')
    print('[2] - Find some entry')
    print('[3] - Delete some entry')
    print('[4] - Create entry')
    print('[5] - Rewrite some entry')
    print('[6] - Age of person')
    print('[7] - Save and exit')
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
        TelephoneNumbers.Save(tb, 'tbook.txt')
        exit('Good bye!')
    else:
        print('Imposible Command. Try Again!')
# except:
#       print('Unable to open file. Try changing the path')
