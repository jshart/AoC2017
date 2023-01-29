
import math


textfile = open(
    'C:\\Users\\jsh27\\OneDrive\\Documents\\GitHub\\AoC2017\\day4_part1\\data\\input.txt', 'r')
input = textfile.read().split('\n')
# str = open('data\\input.txt', 'r').read()



def checkPassword(pw):
    words = pw.split(' ')
    wordLists = []
    for word in words:
        wordList = []
        for letter in word:
            wordList.append(letter)
        #print("word={} list={}".format(word, wordList))
        wordList.sort()
        wordLists.append(wordList)

    # print("lists:{}".format(wordLists))

    for index1, w1 in enumerate(wordLists):
        for index2, w2 in enumerate(wordLists):
            if index1 != index2:
                #print("Comparing w1 {} w2 {}".format(w1, w2))
                if w1 == w2:
                    return False
    return True


totalValid = 0
for i in input:
    if checkPassword(i):
        print("valid:{}".format(i))
        totalValid = totalValid+1
    else:
        print("invalid:{}".format(i))

print("totalValid:{}".format(totalValid))

# print(checkPassword("abcde fghij"))
# print(checkPassword("abcde xyz ecdab"))
# print(checkPassword("a ab abc abd abf abj"))
# print(checkPassword("iiii oiii ooii oooi oooo"))
# print(checkPassword("oiii ioii iioi iiio"))
