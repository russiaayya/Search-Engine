import math
def generateranking():
    # lambda value for Jelinek-Mercer smoothing
    lmd = 0.35
    flag=0
    docScore={}
    file_contents = open("unigram_index.txt", 'r', encoding='utf-8')
    unigrams = eval(file_contents.read())
    file_contents = open("queries.txt", 'r', encoding='utf-8')
    queries = eval(file_contents.read())
    file_contents = open("doc-termCount.txt", 'r', encoding='utf-8')
    documentLen = eval(file_contents.read())
    C = 0
    for value in documentLen.values():
        C += value
    snippetQueryDocs={}
    retrieved_docs = {}
    for qid,q in queries.items():
            for word in q:
                if word in unigrams.keys():
                    cq = 0
                    for docID in unigrams[word]:
                        cq += unigrams[word][docID]
                    for docID in documentLen.keys():
                        if docID in unigrams[word]:
                            fi = unigrams[word][docID]
                        else:
                            fi=0
                        dl = documentLen[docID]
                        score = math.log((1 - lmd) * (fi / dl) + lmd * (cq / C))
                        if docID not in docScore:
                            docScore[docID] = score
                        else:
                            docScore[docID] += score
            revSortedDocScore = sorted(docScore, key=docScore.get ,reverse=True)# sorting in descending order
            retrieved_docs[qid] = revSortedDocScore[:100]
            for index, token in enumerate(revSortedDocScore):
                index += 1
                if qid not in snippetQueryDocs:
                    snippetQueryDocs[qid] = [token]
                else:
                    snippetQueryDocs[qid].append(token)
                if index == 100:  # For getting only top 100
                    break
            if flag==0:
                filename = "Query-likelihood-ranking" + ".txt"
                newFile = open(filename, 'w', encoding='utf-8')
                flag=1
            newFile.write("\n")
            newFile.write("query_id  Q0   doc_id   rank     score              system_name\n")
            for index,token in enumerate(revSortedDocScore):
                index+=1
                newFile.write(str(qid)+"        ")
                newFile.write("Q0   ")
                newFile.write(str(token) + "    ")
                newFile.write(str(index)+"   ")
                newFile.write(str(docScore[token]))
                newFile.write("   smoothedQueryLikelihood     ")
                newFile.write("\n")
                if index==100:#For getting only top 100
                    break
            docScore={}
    newFile.close()
    filenameSnippet = "snippetQueryDocsDictionary" + ".txt"
    newFileSnippet= open(filenameSnippet, 'w', encoding='utf-8')
    newFileSnippet.write(str(snippetQueryDocs))
    filename = "QLM_Ranking_TOP100_retrieved" + ".txt"
    newFile = open(filename, 'w', encoding='utf-8')
    newFile.write(str(retrieved_docs))
    newFile.close()





if __name__ == "__main__":
    generateranking()