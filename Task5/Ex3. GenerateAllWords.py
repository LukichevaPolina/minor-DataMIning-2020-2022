def generate_words(word):
    count_words = count_number_words(word)
    words = []
    word = sorted(word)
    print(word)
    num = 0
    w = word
    words.append(word)
    while num < count_words - 1:
        max_i = 0
        for i in range(len(w) - 1):
            if i > max_i and w[i] <  w[i+1]:
                max_i = i

        max_j = 0
        for j in range(len(w)):
            if j > max_j and w[j] > w[max_i]:
                max_j = j

        w[max_i], w[max_j] = w[max_j], w[max_i]
        w = w[:max_i+1] + w[len(w) - 1:max_i: - 1]
        print(w)

        words.append(w)
        print(words)
        num += 1

    return words


def count_number_words(word):
    znamen = 1
    letters_num = count_letters(word)
    for value in letters_num.values():
        znamen *= fact(value)
    return fact(len(word)) // znamen


def count_letters(word):
    num_letters = {}
    for i in word:
        if i in num_letters:
            num_letters[i] += 1
        else:
            num_letters[i] = 1
    return num_letters


def fact(num):

    result = 1
    for i in range(2, num+1):
        result *= i
    return result


print(generate_words('abac'))