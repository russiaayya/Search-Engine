def termCount(ngram):
    filename = ngram+".txt"
    file_contents = open(filename, 'r', encoding='utf-8')
    terms = eval(file_contents.read())
    termFreq={}
    count = 0
    for token in terms.keys():
        for key in terms[token].keys():
            count+=terms[token][key]
        termFreq[token]=count
        count = 0

    revSortedTermFreq = sorted(termFreq, key=termFreq.get, reverse=True)# reverse sorting
    filename = r"corpusStatistics/"+"task3"+ngram+".txt"
    newFile = open(filename, 'w', encoding='utf-8')
    for token in revSortedTermFreq:
        newFile.write(str(token)+"-")
        newFile.write(str(termFreq[token]))
        newFile.write("\n")
    newFile.close()

def docFreqTable(ngram):
    filename = ngram + ".txt"
    file_contents = open(filename, 'r', encoding='utf-8')
    terms = eval(file_contents.read())
    docfreq={}
    listOfTokens=[]
    for t in terms.keys():
        listOfTokens.append(t)
        for doc in terms[t]:
            if t in docfreq:
                docfreq[t].append(doc)
            else:
                docfreq[t]=[doc]
    listOfTokens.sort()
    filename = r"corpusStatistics/" + "task3(2)" + ngram + ".txt"
    newFile = open(filename, 'w', encoding='utf-8')
    for term in listOfTokens:
        newFile.write("\n")
        newFile.write("******TERM*********")
        newFile.write("\n")
        newFile.write(term)
        newFile.write("\n")
        newFile.write("******Document id*********")
        newFile.write("\n")
        newFile.write(str(docfreq[term]))
        newFile.write("\n")
        newFile.write("******Document df**********")
        newFile.write("\n")
        newFile.write(str(len(docfreq[term])))
        newFile.write("\n")
        newFile.write("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    newFile.close()

if __name__ == "__main__":
    termCount("unigram")
    #termCount("bigram")
    #termCount("trigram")
    #docFreqTable("unigram")
    #docFreqTable("bigram")
    #docFreqTable("trigram")
