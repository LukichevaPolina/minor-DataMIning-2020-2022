from random import randint

edgeNumber = int(input("Enter the last number: "))
thoughtNumber = randint(1, edgeNumber + 1)

counterAttempts, enterNum = 0, 0

while ( enterNum != thoughtNumber):
    enterNum = int(input("Enter the number: "))
    if (enterNum > thoughtNumber):
        print("Less")
    else:
        print("More")
    counterAttempts += 1

print("YOU ARE WINNER!!!\nNumber of attempts: ", counterAttempts)

