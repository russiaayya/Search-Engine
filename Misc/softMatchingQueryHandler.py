from difflib import get_close_matches
from autocorrect import spell
def getSoftMatchingQueryTerm(index,word,query,corpus,unigrams,bigrams):
    listOfCorrections=get_close_matches(word, corpus)
    bestMatch=""
    maxFreq = 0
    for w in listOfCorrections:
        corelation=getCorelation(index,w,query,bigrams)
        if corelation>0:#if co-occurence of the word exists
            return w
        freq=getFrequency(w,unigrams)
        if freq>maxFreq and w not in stop_Words and abs(len(w)-len(word))<=1:#Frequency of that word in the corpus is checked.Best match is considered
            maxFreq=freq
            bestMatch=w
    return bestMatch

def getCorelation(index,w,query,bigrams):
    value = 0
    if index>0:
        bigram_word=query[index-1]+" "+w#Previous word and this word's proximity count in the corpus is considered.
    else:
        return 0
    if bigram_word in bigrams:#bigrams are considered for corelation between the previous word and the suggested word
        listOfDocs=bigrams[bigram_word]
        for doc in listOfDocs:
            value+=listOfDocs[doc]
    return value
def getFrequency(w,unigrams):# number of times the suggested corrected word in present in the corpus
    freq=0
    listOfDocs=unigrams[w]
    for doc in listOfDocs.keys():
        freq+=listOfDocs[doc]
    return freq

if __name__ == "__main__":
    count=0
    correctedQuery={}
    file_contents = open("SEG_queries.txt", 'r', encoding='utf-8')#Erroneous queries are taken as the input
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
        updatedQList=[]
        for index,word in enumerate(queries[qid]):
            if word in stop_Words:#skipping the stopping words
                updatedQList.append(word)
                continue
            correctWord = ""
            if word not in corpus:#We are finding the best match only if it is not found in the corpus
                correctWord=getSoftMatchingQueryTerm(index,word,queries[qid],corpus,unigrams,bigrams)
            else:
                updatedQList.append(word)
                continue
            if correctWord=="" or correctWord is None:#if no corrrection is found in corelation and frequency,
                # we are taking the original wrong word and trying to correct it with the help of autocorrect.
                correctWord=word
            else:
                updatedQList.append(correctWord)
            if correctWord not in corpus:
                if spell(correctWord) in corpus:#autocorrect is used as the last step if no decent match is found.
                    count-=1
                    updatedQList.append(spell(correctWord))
                else:
                    updatedQList.append(correctWord)
        correctedQuery[qid]=updatedQList
    filename = "softMatchingQuery.txt"
    newFile = open(filename, 'w', encoding='utf-8')
    newFile.write(str(correctedQuery))
    newFile.close()
