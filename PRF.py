import sys
import collections
from  bm25 import *


tokenized_dir = "tokenized_Files"
# do required stopping to remove high frequent stop words


def pseudoRelevance(queryId, numExpandedQueryTerms, queries,expPseudoRel_queries,k):
    kExpandedQueryTerms = []
    docIds = getTopK_Results(queryId,k)
    docScore = createTfRelevanceDocs(docIds)
   #list of high frequency non-stopped terms in the selected top k docs
    queryTerms = queries[queryId]
    num = 0
    for docId in docIds:
        if docId in docScore.keys():
            for term in docScore[docId]:
                # avoid selecting terms already in query
                if term not in queryTerms:
                    kExpandedQueryTerms.append(term)
                    num += 1
        if num >= numExpandedQueryTerms:
            break

    # print ("queryTerms: ",queryTerms)
    # print("expanded terms",kExpandedQueryTerms)
    # print("expanded terms count",len(kExpandedQueryTerms))
    completeRelevantList=list(queryTerms+kExpandedQueryTerms)
    if queryId not in expPseudoRel_queries:
        expPseudoRel_queries[queryId]=completeRelevantList
    else:
        expPseudoRel_queries[queryId].append(completeRelevantList)
    return expPseudoRel_queries





def createTfRelevanceDocs(docIds):
    stopWords = open("common_words.txt", 'r', encoding='utf-8')
    stopWordsList = stopWords.read()
    relevanceDocs = {}
    for docId in docIds:
        tfHmRelevanceDocs = {}
        filename = tokenized_dir + "/" +docId+".txt"
        file_contents = open(filename, 'r', encoding='utf-8')
        fileList = eval(file_contents.read())

        for term in fileList:
            if term in stopWordsList:
                continue
            if term in tfHmRelevanceDocs:
                tfHmRelevanceDocs[term] = tfHmRelevanceDocs[term] + 1
            else:
                tfHmRelevanceDocs[term] = 1
        relevanceDocs[docId]= tfHmRelevanceDocs
        topResult= sorted(relevanceDocs[docId], key=relevanceDocs[docId].get, reverse=True)
        relevanceDocs[docId]=topResult[:5]
    return relevanceDocs


# get top k docs from BM25 :k = 5
def getTopK_Results(queryId,k):
    file_contents = open("bm25_Ranking_PRF.txt", 'r', encoding='utf-8')
    topK_Result = eval(file_contents.read())
    queryDocIds = topK_Result[queryId]
    return queryDocIds[:5]




if __name__ == "__main__":
    content = open("queries.txt", 'r', encoding='utf-8')
    queries = eval(content.read())
    numQuery = len(queries.keys())
    expPseudoRel_queries = {}
    # PRFdict = pseudoRelevance('1',25, queries, expPseudoRel_queries,5)
    for qId in queries.keys():
        PRFdict=pseudoRelevance(qId, 5,queries,expPseudoRel_queries,5)
    filename = "enrichedQueries" + ".txt"
    newFile = open(filename, 'w', encoding='utf-8')
    newFile.write(str(PRFdict))
    newFile.close()




