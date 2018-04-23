import nltk


def generateIndex(choice):
    file = open('bfs.txt', "r")
    validFilesName = file.readlines()
    file.close()
    termDoctf = {}
    termsInDoc={}
    totalCount=0
    ngrams=[]
    docTf={}
    for file in validFilesName:
        if len(file) <= 1:
            continue
        fileindex = file.index('wiki/')
        specificFile = file[fileindex + 5:]
        specificFile = specificFile.strip("\n")
        filename = r"corpus/" + specificFile + ".txt"
        file_contents = open(filename, 'r', encoding='utf-8')
        tokens = eval(file_contents.read())
        if choice=="1":
            ngrams=tokens
        if choice == "2":
            ngrams=[]
            bigrams = list(nltk.bigrams(tokens))
            for b in bigrams:
                ngrams.append(b[0] + " " + b[1])
        if choice == "3":
            ngrams=[]
            trigrams = list(nltk.trigrams(tokens))
            for t in trigrams:
                     ngrams.append(t[0] + " " + t[1] + " " + t[2])
        for t in ngrams:
            if choice=="1":
                totalCount+=1
            if t not in termDoctf:
                termDoctf[t]={}
                docTf[specificFile]=1
                termDoctf[t][specificFile] = docTf[specificFile]
            elif termDoctf[t].get(specificFile) == None:
                termDoctf[t][specificFile] = 1
            else:
                termDoctf[t][specificFile] += 1
        termsInDoc[specificFile]=totalCount
        totalCount=0
    if choice=="1":
        fn = r"NoOfTerms/" + "doc-termCount" + ".txt"
        newFile = open(fn, 'w', encoding='utf-8')
        newFile.write(str(termsInDoc))
        newFile.close()
    if choice=='1':
        filename="unigram.txt"
    elif choice=='2':
        filename="bigram.txt"
    else:
        filename="trigram.txt"
    newFile = open(filename, 'w', encoding='utf-8')
    newFile.write(str(termsInDoc))
    newFile.close()


def generatePos():
    file = open('bfs.txt', "r")
    validFilesName = file.readlines()
    file.close()
    termPos={}
    docTf={}
    for file in validFilesName:
        if len(file) <= 1:
            continue
        fileindex = file.index('wiki/')
        specificFile = file[fileindex + 5:]
        specificFile = specificFile.strip("\n")
        filename = r"corpus/" + specificFile + ".txt"
        file_contents = open(filename, 'r', encoding='utf-8')
        tokens = eval(file_contents.read())
        for count,t in enumerate(tokens):
            if t not in termPos:
                termPos[t]={}
                docTf[specificFile]=[count]
                termPos[t][specificFile] = docTf[specificFile]
            elif termPos[t].get(specificFile) == None:
                termPos[t][specificFile] = [count]
            else:
                termPos[t][specificFile].append(count)
    filename="indexTermPosition.txt"
    newFile = open(filename, 'w', encoding='utf-8')
    for k, v in termPos.items():
        newFile.write(k)
        newFile.write("\n")
        newFile.write(str(v))
        newFile.write("\n")
        newFile.write("*********************************")
        newFile.write("\n")
    newFile.close()

if __name__ == "__main__":
    generateIndex("1")# unigram
    #generateIndex("2")# bigram
    #generateIndex("3")# tri gram
    #generatePos()# index term positions
