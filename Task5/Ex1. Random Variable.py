import random


def TossResult(number_toss, chance):
    result = []

    for i in range(number_toss):
        result.append(random.random() < chance)

    return result


def NumberOfSuccess(number_toss, chance, number_experiments):
    result = []

    for i in range(number_experiments):
        success = 0
        for j in range(number_toss):
            if random.random() < chance:
                success += 1
        result.append(success)

    return result


print(TossResult(1, 0.9))
print(NumberOfSuccess(10, 0.2, 12))