import sys
import collections
from  bm25 import *


tokenized_dir = "tokenized_Files"
# do required stopping to remove high frequent stop words


def pseudoRelevance(queryId, numExpandedQueryTerms, queries):
    n = 10
    # topK = getTopK_Results()
    kExpandedQueryTerms = []
    expPseudoRel_queries = {}
    docScore = createTfRelevanceDocs(getTopK_Results())
    revTerms = sorted(docScore, key=docScore.get,reverse=True) #list of high frequency non-stopped terms in the selected top k docs
    #print (revTerms)
    # queries = open("queries.txt", 'r', encoding='utf-8')
    # rawQueryTerms = eval(queries.read())
    queryTerms = queries[queryId]
    print (queryTerms)
    num = 0
    for term in revTerms:
        # avoid selecting terms already in query
        if term not in queryTerms:
            kExpandedQueryTerms.append(term)
            num += 1
            if num == numExpandedQueryTerms:
                break
    print ("queryTerms",queryTerms)
    print("kexpanded",kExpandedQueryTerms)
    completeRelevantList=list(set(queryTerms+kExpandedQueryTerms))
    print ("checking",completeRelevantList)
    expPseudoRel_queries[queryId]=completeRelevantList

    print (expPseudoRel_queries)





def createTfRelevanceDocs(docIds):
    tfHmRelevanceDocs ={}
    if (docIds == None or docIds.__len__() == 0):
        print ("not found")
    stopWords = open("common_words", 'r', encoding='utf-8')
    stopWordsList = stopWords.read()
    for i in range(docIds.__len__()):
        filename = tokenized_dir + "/" +docIds[i]+".txt"
        file_contents = open(filename, 'r', encoding='utf-8')
        fileList = eval(file_contents.read())
        for term in fileList:
            if term in stopWordsList:
                continue

            if term in tfHmRelevanceDocs:
                tfHmRelevanceDocs[term] = tfHmRelevanceDocs[term] + 1
            else:
                tfHmRelevanceDocs[term] = 1
    return tfHmRelevanceDocs
    # print (tfHmRelevanceDocs)


# get top N docs from BM25
def getTopK_Results(queryId):
    file_contents = open("bm25_Ranking_WithRelevance.txt", 'r', encoding='utf-8')
    topK_Result = eval(file_contents.read)
    # topK_Result = file_contents.readlines()
    queryDocIds = topK_Result[queryId]
    topK = []
    i=0
    while(i!=12):
        topK.append(queryDocIds)
        # topK.append(topK_Result[i].split()[2])
        # print (topK_Result[i].split()[2])
        i +=1
    return topK




if __name__ == "__main__":
    content = open("queries.txt", 'r', encoding='utf-8')
    queries = eval(content.read())
    numQuery = len(queries.keys())
    for qId in queries.keys():
        pseudoRelevance(qId, 5,queries)




