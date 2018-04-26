import math
def generateranking(enrichmentFlag):
    #Emperical values for BM25
    k1=1.2
    k2=100
    b=0.75
    N=3204
    r=0
    R=0.0
    #Initialization
    ni = 0
    # dictionary to hold the computed document score
    docScore={}
    score=0
    # load the inverted index
    file_contents = open("unigram_index.txt", 'r', encoding='utf-8')
    unigrams = eval(file_contents.read())
    if enrichmentFlag:
        file_contents = open("enrichedQueries.txt", 'r', encoding='utf-8')
        #file_contents = open("enrichedQueries-top3.txt", 'r', encoding='utf-8')
        queries = eval(file_contents.read())
    else:
        file_contents = open("queries.txt", 'r', encoding='utf-8')
        # file_contents = open("SEG_queries.txt", 'r', encoding='utf-8')
        queries = eval(file_contents.read())
    file_contents = open("doc-termCount.txt", 'r', encoding='utf-8')
    documentLen = eval(file_contents.read())
    totalCount=0
    for value in documentLen.values():
        totalCount+=value
    averageDl=totalCount/3204
    flag=0
    prfqueries = {}
    retrieved_docs={}
    for qid,q in queries.items():
            qfi={}
            for word in q:
                if word not in qfi:
                    qfi[word]=1
                else:
                    qfi[word]+=1
            for word in q:
                if word in unigrams.keys():
                    ni = len(unigrams[word])
                    for docID in unigrams[word]:
                        fi=unigrams[word][docID]
                        dl=documentLen[docID]
                        K=k1*((1-b)+b*(float(dl)/averageDl))#taking full decimal values
                        score=math.log(((r+0.5)/(R-r+0.5))/((ni-r+0.5)/(N-ni-R+r+0.5)))*(((k1+1)*fi)/(K+fi))*(((k2+1)*qfi[word])/(k2+qfi[word]))
                        if docID not in docScore:
                            docScore[docID]=score
                        else:
                            docScore[docID]+=score
            revSortedDocScore = sorted(docScore, key=docScore.get, reverse=True)# sorting in descending order
            retrieved_docs[qid]=revSortedDocScore[:100]
            if queryEnrichment:
                for index,token in enumerate(revSortedDocScore):
                    index+=1
                    if qid not in prfqueries:
                        prfqueries[qid]=[token]
                    else:
                        prfqueries[qid].append(token)
                    if index==100:#For getting only top 100
                        break
            if flag==0:
                if queryEnrichment:
                    filename = "bm25_Ranking_EnrichedQuery" + ".txt"
                    systemName = "   Pseudo_Relevance_Feedback_BM25   "
                else:
                    filename = "bm25_Ranking" + ".txt"
                    systemName = "   BM_25   "
                    # filename = "bm25_Ranking_SEG_Queries" + ".txt"
                    # systemName = "   bm25_using_SEG_model   "

                newFile = open(filename, 'w', encoding='utf-8')
                flag=1
            newFile.write("\n")
            newFile.write("query_id   Q0   doc_id       rank    score               system_name\n")
            for index,token in enumerate(revSortedDocScore):
                index+=1
                newFile.write(str(qid)+"        ")
                newFile.write("Q0   ")
                newFile.write(str(token) + "        ")
                newFile.write(str(index)+"   ")
                newFile.write(str(docScore[token]))
                newFile.write(str(systemName))
                newFile.write("\n")
                if index==100:#For getting only top 100
                    break
            docScore={}
    newFile.close()
    if queryEnrichment:
        filenamePRF = "bm25_Ranking_PRF" + ".txt"
        #filenamePRF = "bm25_Ranking_PRF_top3" + ".txt"
        newFilePRF = open(filenamePRF, 'w', encoding='utf-8')
        newFilePRF.write(str(prfqueries))
        newFilePRF.close()
    filename = "bm25_Ranking_TOP100_retrieved_PRF" + ".txt"
    newFile = open(filename, 'w', encoding='utf-8')
    newFile.write(str(retrieved_docs))
    newFile.close()


if __name__ == "__main__":
    queryEnrichment=True
    generateranking(queryEnrichment)
    # queryEnrichment=False
    # generateranking(queryEnrichment)
