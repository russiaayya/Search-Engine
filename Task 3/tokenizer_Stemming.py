import os
import string
import bs4 as bsnew


def generateTokens():
    inputFile = open(r'Input\cacm_stem.txt', 'r', encoding='utf8')
    files = inputFile.read().split('#')
    docID = 0
    for file in files:
        validTokens = []
        if len(file.split()) == 0:
            continue
        else:
            docID += 1
            outputFile = open(r'tokenized_Files_Stemmed\CACM-%04d.txt' % docID, 'w', encoding='utf8')
            contents = file.split()
            contents.pop(0)
            lastIndex = 0
            if "am" in contents:
                lastIndex = rindex(contents, "am")
            if "pm" in contents:
                lastIndex = rindex(contents, "pm")
            for t in contents:
                if contents.index(t) == lastIndex + 1:
                    break
                validTokens.append(t)
            outputFile.write(str(validTokens))
    outputFile.close()


def rindex(mylist, myvalue):
    return len(mylist) - mylist[::-1].index(myvalue) - 1


if __name__ == "__main__":
    generateTokens()
