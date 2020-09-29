def Maximum(a, b, c):
    if not isinstance(a, type(b)):
        return 'It is imposible to compare'
    if (c == '>'):
        if (a > b):
            return True
        return False
    else:
        if (a > b):
            return False
        return True


def TrueOrFalse(a):
    if a:
        return 'a'
    return 'b'


def MaximumList(a, b, c):
    if Maximum(len(a), len(b), c) == Maximum(len(b), len(a), c):
        #если длины равные
        for i in range(len(a)):
            if Maximum(a[i], b[i], c) == Maximum(b[i], a[i], c):
                if Maximum(a[i],b[i],c)== 'It is imposible to compare':
                    return (Maximum(a[i], b[i], c))
            else:
                return(Maximum(a[i], b[i], c))

    else:
        return(Maximum(len(a), len(b), c))


def MaximumSequences(a, c):
    maximum = a[0]
    for i in a:
        if not(Maximum(maximum, i, c)):
            maximum = i
    return maximum


def MaxiListOfList(a, c):
    maximum = a[0]
    for i in a:
        print(maximum)
        if MaximumList(maximum, i, c) == 'It is imposible to compare':
            return 'It is imposible to compare'
        else:
            if not (MaximumList(maximum, i, c)):
                maximum = i

    return maximum


#print('Finded:'TrueOrFalse(Maximum(int(input('Enter a, b and sign')), int(input()), input())))
#print('Element: ', TrueOrFalse(Maximum(input('Enter a, b and sign:'), input(), input())))
#print('Element: ', (MaximumList(['aa', 81], ['aa', 1], input('Enter sign: '))))
print('Element: ', MaximumSequences([int(i) for i in input().split()], input()))
#print('Element from string: ', MaximumSequences([str(i) for i in input().split()], input()))
print('Finded from list of lists: ', MaxiListOfList([[8, 'ajnaj', 'akja'], [8, 'ajakj', 'nn'], [7, 'xmsbd', 8]], input()))

