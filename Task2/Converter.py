alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def ToTen(inFoundation, num):
    degree, result = 0, 0
    for i in num:
        result += alphabet.find(i) * (inFoundation ** degree)
        degree += 1
    return result

def InTen(outFoundation, num):
    result = ''
    degree = 0
    while num:
        a = num % outFoundation
        result += alphabet[a]
        num //= outFoundation
        degree += 1
    return result[::-1]


inFoundation = int(input())
outFoundation = int(input())
num = input()
result = (ToTen(inFoundation, num))
print(result)
print(InTen(outFoundation, result))