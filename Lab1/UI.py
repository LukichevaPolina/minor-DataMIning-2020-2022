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
    elif command == '4':
        td = TelephoneNumbers.NewEntry(tb)
    elif command == '5':
        tb = TelephoneNumbers.Rewrite(tb)
    elif command == '6':
        TelephoneNumbers.AgePerson(tb)
    elif command == '7':
        TelephoneNumbers.SaveExit(tb, 'tbook.txt')
    else:
        print('Imposible Command. Try Again!')
# except:
#       print('Unable to open file. Try changing the path')
