import math
def generateranking():
    #Emperical values for BM25
    k1=1.2
    k2=100
    b=0.75
    N=3204
    r=0
    R=0.0
    #Initialization
    ni = 0
    docScore={}
    score=0
    file_contents = open("unigram_index.txt", 'r', encoding='utf-8')
    unigrams = eval(file_contents.read())
    file_contents = open("queries.txt", 'r', encoding='utf-8')
    queries = eval(file_contents.read())
    file_contents = open("doc-termCount.txt", 'r', encoding='utf-8')
    documentLen = eval(file_contents.read())
    totalCount=0
    for value in documentLen.values():
        totalCount+=value
    averageDl=totalCount/3204
    flag=0
    for qid,q in queries.items():
            R=getRvalue(qid)
            qfi={}
            for word in q:
                if word not in qfi:
                    qfi[word]=1
                else:
                    qfi[word]+=1
            for word in q:
                if word in unigrams.keys():
                    r = getr(qid, word)
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
            if flag==0:
                filename = "bm25_Ranking_WithRelevance" + ".txt"
                newFile = open(filename, 'w', encoding='utf-8')
                flag=1
            newFile.write("\n")
            newFile.write("query_id   Q0   doc_id   rank   BM_25   system_name\n")
            for index,token in enumerate(revSortedDocScore):
                index+=1
                newFile.write(str(qid)+"   ")
                newFile.write("Q0   ")
                newFile.write(str(token) + " ")
                newFile.write(str(index)+"   ")
                newFile.write(str(docScore[token]))
                newFile.write("   BM_25   ")
                newFile.write("\n")
                if index==100:#For getting only top 100
                    break
            docScore={}
    newFile.close()

def getRvalue(qid):
    R = 0
    file_contents = open("queryRelevance.txt", 'r', encoding='utf-8')
    queryRel = eval(file_contents.read())
    file_contents.close()
    qid = qid.strip()
    if qid not in queryRel:
        return 0
    relevantDocList = queryRel[qid]
    R = len(relevantDocList)
    return R
def getr(qid,word):
    r=0
    file_contents = open("queryRelevance.txt", 'r', encoding='utf-8')
    queryRel = eval(file_contents.read())
    file_contents.close()
    file_contents=open("unigram_index.txt", 'r', encoding='utf-8')
    unigram=eval(file_contents.read())
    file_contents.close()
    qid=qid.strip()
    if qid not in queryRel:
        return 0
    relevantDocList=queryRel[qid]
    wordPresentinDoc=[]
    for i in unigram[word].keys():
        wordPresentinDoc.append(i)
    r=len(list(set(relevantDocList).intersection(wordPresentinDoc)))
    print(r)
    return r
if __name__ == "__main__":
    generateranking()