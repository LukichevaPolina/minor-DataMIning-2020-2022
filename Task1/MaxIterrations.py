countMaxIterrations = 0
findNum = 0
dictIterrations = {}
for i in range(1, 1001):
    currentNum = i
    count = 0
    while currentNum != 1:
        if currentNum in dictIterrations:
            dictIterrations[i] = count + dictIterrations[currentNum]
            break
        if currentNum % 2:
            currentNum = currentNum*3 + 1
        else:
            currentNum /= 2
        count += 1
    else:
        dictIterrations[i] = count

keys = list(dictIterrations.keys())
values = list(dictIterrations.values())

print(keys[values.index(max(values))], (max(values)))

