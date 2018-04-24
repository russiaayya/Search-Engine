import math
from random import randint

#synthetic spelling error generator model

def generator():
    #reading the original queries
    contents = open("queries.txt", 'r', encoding='utf-8')
    queries = eval(contents.read())
    modifiedQueries = {}
    queriesDict = {}
    cutOff = 0.4 #synthetic noise occurence value
    for qid in queries:
        newQueries= queries[qid].copy()
        qlist=queries[qid]
        qlist.sort(key =len, reverse=True)   #sorting in decreasing order of term-length in query
        modifiedQueries[qid]=qlist[:math.floor(cutOff * len(qlist))]
        for term in modifiedQueries[qid]:
            if len(term)  >=4:
                modifiedterm = generatespellingError(term)
                newQueries[newQueries.index(term)] = modifiedterm
        queriesDict[qid]= newQueries
    filename = "SEG_queries.txt"
    newFile = open(filename, 'w', encoding='utf-8')
    newFile.write(str(queriesDict))
    newFile.close()


#generate spelling error for the given word
def generatespellingError(word):
    l = len(word)
    word1=list(word)
    #running for three swapping
    for i in range(3):
        # using random index
        r1 = randint(1, l - 2)
        r2 = randint(1, l - 2)
        if (r1 != r2):
            temp = word1[r1]
            word1[r1]=word1[r2]
            word1[r2] = temp
        word="".join(word1)
    return word


if __name__ == '__main__':
    generator()



