countMaxIterrations = 0
findNum = 0
for i in range (1, 1001):
    currentNum = i
    count = 0

    while (currentNum != 1):
        if currentNum % 2:
            currentNum = currentNum*3 + 1
        else:
            currentNum /= 2
        count+=1
    if (count > countMaxIterrations):
        countMaxIterrations = count
        findNum = i

print("Number = ", findNum, "\nCount Iterrations = ", countMaxIterrations)
