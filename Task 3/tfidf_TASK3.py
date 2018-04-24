import math
import sys
import io


def generateranking(indexTxt, queriesTxt, docTermCountTxt, rankingTxt, system_name):
    N = 3204  # total no. of docs
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

    flag = 0
    for qid, q in queries.items():
        qfi = {}
        for word in q:
            if word not in qfi:
                qfi[word] = 1
            else:
                qfi[word] += 1
        for word in q:
            if word in unigrams.keys():
                ni = len(unigrams[word])  # no. of documents having that word
                for docID in unigrams[word]:
                    fi = unigrams[word][docID]  # term frequency in that document
                    dl = documentLen[docID]  # length of the document
                    tf = float(fi) / float(dl)
                    idf = math.log(float(N) / float(ni))
                    score = tf * idf
                    if docID not in docScore:
                        docScore[docID] = score
                    else:
                        docScore[docID] += score
        revSortedDocScore = sorted(docScore, key=docScore.get, reverse=True)  # sorting in descending order
        if flag == 0:  # create a new file
            filename = rankingTxt + ".txt"
            newFile = open(filename, 'w', encoding='utf-8')
            flag = 1
        newFile.write("\n")
        newFile.write("q_id  Q0   doc_id   rank        score        system_name\n")
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


if __name__ == "__main__":
    # stopping
    generateranking(r'Invereted_Indexes\unigram_index_stopping.txt', 'queries.txt', 'doc-termCount_stopped.txt',
                    'Ranked_docs\Tidf-stopping-ranking', 'tf-idfStopping')
    # Stemmed
    generateranking(r'Invereted_Indexes\unigram_index_stemmed.txt', 'queries_stemmed.txt', 'doc-termCount_stemmed.txt',
                    'Ranked_docs\Tidf-stemmed-ranking', 'tf-idfStemmed')
