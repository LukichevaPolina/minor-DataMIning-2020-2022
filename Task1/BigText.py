f = open("text.txt", "r")
text = [str(s) for s in (f.read().replace('.', '').replace(',', '').replace('-', '').replace('!', '').replace('?', '').lower()).split()]
#print number of words in file
print(len(text))

#search popular words
dictWords = {}
for i in text:
    if i in dictWords:
        dictWords[i] += 1
    else:
        dictWords[i] = 1

listKeys = list(dictWords.keys())
listValues = list(dictWords.values())
for i in range(10):
    print(listKeys[listValues.index(max(listValues))], max(listValues))
    listKeys.pop(listValues.index(max(listValues)))
    listValues.pop(listValues.index(max(listValues)))

#reverse of sentances





