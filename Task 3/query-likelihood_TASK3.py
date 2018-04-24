import math


def generateranking(indexTxt, queriesTxt, docTermCountTxt, rankingTxt, system_name):
    # lambda value for Jelinek-Mercer smoothing
    lmd = 0.35
    flag = 0
    docScore = {}
    file_contents = open(indexTxt, 'r', encoding='utf-8')
    unigrams = eval(file_contents.read())
    file_contents = open(queriesTxt, 'r', encoding='utf-8')
    queries = eval(file_contents.read())
    file_contents = open(docTermCountTxt, 'r', encoding='utf-8')
    documentLen = eval(file_contents.read())
    C = 0
    for value in documentLen.values():
        C += value
    snippetQueryDocs = {}
    for qid, q in queries.items():
        for word in q:
            if word in unigrams.keys():
                cq = 0
                for docID in unigrams[word]:
                    cq += unigrams[word][docID]
                for docID in unigrams[word]:
                    fi = unigrams[word][docID]
                    dl = documentLen[docID]
                    score = math.log((((1 - lmd) * fi) / dl) + ((lmd * cq) / C))
                    if docID not in docScore:
                        docScore[docID] = score
                    else:
                        docScore[docID] += score
        revSortedDocScore = sorted(docScore, key=docScore.get, reverse=True)  # sorting in descending order
        for index, token in enumerate(revSortedDocScore):
            index += 1
            if qid not in snippetQueryDocs:
                snippetQueryDocs[qid] = [token]
            else:
                snippetQueryDocs[qid].append(token)
            if index == 100:  # For getting only top 100
                break
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
            newFile.write("   " + system_name + "     ")
            newFile.write("\n")
            if index == 100:  # For getting only top 100
                break
        docScore = {}
    newFile.close()


if __name__ == "__main__":
    # stopping
    generateranking(r'Invereted_Indexes\unigram_index_stopping.txt', 'queries.txt', 'doc-termCount_stopped.txt',
                    'Ranked_docs\Query-likelihood-stopping-ranking', 'smoothedQueryLikelihoodStopping')
    # Stemmed
    generateranking(r'Invereted_Indexes\unigram_index_stemmed.txt', 'queries_stemmed.txt', 'doc-termCount_stemmed.txt',
                   'Ranked_docs\Query-likelihood-stemmed-ranking', 'smoothedQueryLikelihoodStemmed')
