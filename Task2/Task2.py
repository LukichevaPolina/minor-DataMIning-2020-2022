def EasyNumbers(n):
    for i in range(1, n+1):
        j = i - 1
        while (j > 1):
            if i % j == 0:
                break
            j -= 1
        else:
            print(i)

def AllDivisors(n):
    for i in range(1, n+1):
        if n % i == 0:
            print(i)

def NOD(a, b):
    if ( a == 0 or b == 0):
        return a+b
    if (a > b):
        return (NOD(a - b, b))
    else:
        return NOD(a, b - a)

EasyNumbers(int(input()))
AllDivisors(int(input()))
print(NOD(int(input()), int(input())))
