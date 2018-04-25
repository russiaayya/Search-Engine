import math


def generateranking(indexTxt, queriesTxt, docTermCountTxt, rankingTxt, system_name):
    # Emperical values for BM25
    k1 = 1.2
    k2 = 100
    b = 0.75
    N = 3204
    r = 0
    R = 0.0
    # Initialization
    ni = 0
    docScore = {}
    score = 0
    file_contents = open(indexTxt, 'r', encoding='utf-8')
    unigrams = eval(file_contents.read())
    file_contents = open(queriesTxt, 'r', encoding='utf-8')
    queries = eval(file_contents.read())
    file_contents = open(docTermCountTxt, 'r', encoding='utf-8')
    documentLen = eval(file_contents.read())
    totalCount = 0
    for value in documentLen.values():
        totalCount += value
    averageDl = totalCount / 3204
    flag = 0
    prfqueries = {}
    retrieved_docs = {}
    for qid, q in queries.items():
        qfi = {}
        for word in q:
            if word not in qfi:
                qfi[word] = 1
            else:
                qfi[word] += 1
        for word in q:
            if word in unigrams.keys():
                ni = len(unigrams[word])
                for docID in unigrams[word]:
                    fi = unigrams[word][docID]
                    dl = documentLen[docID]
                    K = k1 * ((1 - b) + b * (float(dl) / averageDl))  # taking full decimal values
                    score = math.log(((r + 0.5) / (R - r + 0.5)) / ((ni - r + 0.5) / (N - ni - R + r + 0.5))) * (
                    ((k1 + 1) * fi) / (K + fi)) * (((k2 + 1) * qfi[word]) / (k2 + qfi[word]))
                    if docID not in docScore:
                        docScore[docID] = score
                    else:
                        docScore[docID] += score
        revSortedDocScore = sorted(docScore, key=docScore.get, reverse=True)  # sorting in descending order
        retrieved_docs[qid] = revSortedDocScore[:100]
        if flag == 0:
            filename = rankingTxt + ".txt"
            newFile = open(filename, 'w', encoding='utf-8')
            flag = 1
        newFile.write("\n")
        newFile.write("query_id   Q0   doc_id   rank   score   system_name\n")
        for index, token in enumerate(revSortedDocScore):
            index += 1
            newFile.write(str(qid) + "   ")
            newFile.write("Q0   ")
            newFile.write(str(token) + " ")
            newFile.write(str(index) + "   ")
            newFile.write(str(docScore[token]))
            newFile.write("   " + system_name + "   ")
            newFile.write("\n")
            if index == 100:  # For getting only top 100
                break
        docScore = {}
    newFile.close()
    filename = "BM25_task3_TOP100_retrieved" + ".txt"
    newFile = open(filename, 'w', encoding='utf-8')
    newFile.write(str(retrieved_docs))
    newFile.close()


if __name__ == "__main__":
    # stopping
    generateranking(r'Invereted_Indexes\unigram_index_stopping.txt', 'queries.txt', 'doc-termCount_stopped.txt',
                    'Ranked_docs\BM25-stopping-ranking', 'smoothedQueryLikelihoodStopping')
    # Stemmed
    generateranking(r'Invereted_Indexes\unigram_index_stemmed.txt', 'queries_stemmed.txt', 'doc-termCount_stemmed.txt',
                    'Ranked_docs\BM25-stemmed-ranking', 'smoothedQueryLikelihoodStemmed')
