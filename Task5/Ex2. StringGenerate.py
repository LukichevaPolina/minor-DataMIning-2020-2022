import random


def StringGenerate(string, size, repetition):
    if not repetition and (size > len(string)):
        return 'Error: unable to compose a string!'

    result = ''
    if repetition:
        for i in range(size):
            result = result + string[random.randint(0, len(string) - 1)]

    else:
        for i in range(size):
            i = random.randint(0, len(string) - 1)
            result = result + string[i]
            string = string.replace(string[i], '', 1)

    return result


print(StringGenerate('asaaaqwe', 7, False))
