from difflib import get_close_matches

def getSoftMatchingQueryTerm(word,corpus,unigrams):
    listOfCorrections=get_close_matches(word, corpus)
    bestMatch=""
    maxFreq = 0
    for w in listOfCorrections:
        freq=getFrequency(w,unigrams)
        if freq>maxFreq and w not in stop_Words and abs(len(w)-len(word))<=1:
            maxFreq=freq
            bestMatch=w
    return bestMatch
def getFrequency(w,unigrams):
    freq=0
    listOfDocs=unigrams[w]
    for doc in listOfDocs.keys():
        freq+=listOfDocs[doc]
    return freq

if __name__ == "__main__":
    count=0
    file_contents = open("SEG_queries.txt", 'r', encoding='utf-8')
    queries = eval(file_contents.read())
    file_contents.close()
    file_contents = open("common_words.txt", 'r', encoding='utf-8')
    stop_Words = file_contents.read()
    file_contents.close()
    file_contents = open("unigram_index.txt", 'r', encoding='utf-8')
    unigrams = eval(file_contents.read())
    file_contents.close()
    corpus=[]
    for term in unigrams:
        corpus.append(term)
    for qid in queries.keys():
        for word in queries[qid]:
            if word in stop_Words:
                continue
            print("Original word:",word)
            correctWord = ""
            if word not in corpus:
                correctWord=getSoftMatchingQueryTerm(word,corpus,unigrams)
            if correctWord=="" or correctWord is None:
                correctWord=word
            print("Corrected word:",correctWord)
            if correctWord not in corpus:
                count+=1
                print("not corrected for ",correctWord)
    print(count)