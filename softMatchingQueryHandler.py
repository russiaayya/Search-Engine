from difflib import get_close_matches
from autocorrect import spell
def getSoftMatchingQueryTerm(index,word,query,corpus,unigrams,bigrams):
    listOfCorrections=get_close_matches(word, corpus)
    bestMatch=""
    maxFreq = 0
    for w in listOfCorrections:
        corelation=getCorelation(index,w,query,bigrams)
        if corelation>0:
            return w
        freq=getFrequency(w,unigrams)
        if freq>maxFreq and w not in stop_Words and abs(len(w)-len(word))<=1:
            maxFreq=freq
            bestMatch=w
    return bestMatch

def getCorelation(index,w,query,bigrams):
    value = 0
    if index>0:
        bigram_word=query[index-1]+" "+w
    else:
        return 0
    if bigram_word in bigrams:
        listOfDocs=bigrams[bigram_word]
        for doc in listOfDocs:
            value+=listOfDocs[doc]
    return value
def getFrequency(w,unigrams):
    freq=0
    listOfDocs=unigrams[w]
    for doc in listOfDocs.keys():
        freq+=listOfDocs[doc]
    return freq

if __name__ == "__main__":
    count=0
    correctedQuery={}
    file_contents = open("SEG_queries.txt", 'r', encoding='utf-8')
    queries = eval(file_contents.read())
    file_contents.close()
    file_contents = open("common_words.txt", 'r', encoding='utf-8')
    stop_Words = file_contents.read()
    file_contents.close()
    file_contents = open("unigram_index.txt", 'r', encoding='utf-8')
    unigrams = eval(file_contents.read())
    file_contents.close()
    file_contents = open("bigram_index.txt", 'r', encoding='utf-8')
    bigrams = eval(file_contents.read())
    file_contents.close()
    corpus=[]
    for term in unigrams:
        corpus.append(term)
    for qid in queries.keys():
        #print("Erroneous Queries",queries[qid])
        updatedQList=[]
        for index,word in enumerate(queries[qid]):
            if word in stop_Words:
                updatedQList.append(word)
                continue
            #print("Original word:",word)
            correctWord = ""
            if word not in corpus:
                correctWord=getSoftMatchingQueryTerm(index,word,queries[qid],corpus,unigrams,bigrams)
            else:
                updatedQList.append(word)
                continue
            if correctWord=="" or correctWord is None:
                correctWord=word
            else:
                updatedQList.append(correctWord)
            #print("Corrected word:",correctWord)
            if correctWord not in corpus:
                count+=1
                # print("not corrected for ",correctWord)
                if spell(correctWord) in corpus:
                    count-=1
                    updatedQList.append(spell(correctWord))
                    #print("Autocorrected word is",(correctWord,spell(correctWord)))
                else:
                    updatedQList.append(correctWord)
        correctedQuery[qid]=updatedQList
    print(count)
    filename = "softMatchingQuery.txt"
    newFile = open(filename, 'w', encoding='utf-8')
    newFile.write(str(correctedQuery))
    newFile.close()
