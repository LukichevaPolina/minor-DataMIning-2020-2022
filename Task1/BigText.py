f = open('textIn.txt', 'r')
text = f.read()
listWords = [str(s) for s in (text.replace('.', '').replace(',', '').replace('-', '').replace('!', '').replace('?', '').lower()).split()]
# print number of words in file
print("Number of words: ", len(listWords))

# search popular words
dictWords = {}
for i in listWords:
    if i in dictWords:
        dictWords[i] += 1
    else:
        dictWords[i] = 1

listKeys = list(dictWords.keys())
listValues = list(dictWords.values())
print("Top10:")
for i in range(10):
    print(listKeys[listValues.index(max(listValues))], max(listValues))
    listKeys.pop(listValues.index(max(listValues)))
    listValues.pop(listValues.index(max(listValues)))

# reverse of sentances
fOut = open('textOut.txt', 'w')
listWordsWithPunctuationMark = [str(s) for s in (text.replace('.', ' .').replace('!', ' !').replace('?', ' ?')).split()]
left = 0
right = -1
i = 0
while i != len(listWordsWithPunctuationMark):
    count = 0
    while listWordsWithPunctuationMark[i] != '.' and listWordsWithPunctuationMark[i] != '!' and listWordsWithPunctuationMark[i] !='?':
        i += 1
    else:
        left = right
        right = i
    for j in range(right, left, -1):
        fOut.write(listWordsWithPunctuationMark[j] + ' ')
    i += 1










