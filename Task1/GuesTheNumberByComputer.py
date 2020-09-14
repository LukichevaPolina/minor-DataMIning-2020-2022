def BinarySearch(userNum, left, right, count):
    mid = (left + right)//2
    if mid == userNum:
        return mid, count
    elif mid > userNum:
        count += 1
        return (BinarySearch(userNum, left, mid-1, count))
    else:
        count += 1
        return (BinarySearch(userNum, mid + 1, right, count))


maxNum = int(input("Enter the biggest number:\n"))
userNum = int(input("Enter a search number:\n"))
counter = 0
print(BinarySearch(userNum, 1, maxNum, counter))
