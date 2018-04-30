import math
import sys
import io



def tfidf_ranking():
    N=3204  #total no. of docs
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
    flag=0
    retrieved_docs = {}
    for qid,q in queries.items():
            qfi={}
            for word in q:
                if word not in qfi:
                    qfi[word]=1
                else:
                    qfi[word]+=1

            for word in q:
                if word in unigrams.keys():
                    ni = len(unigrams[word])  # no. of documents having that word
                    for docID in documentLen.keys():
                        if docID in unigrams[word]:
                            fi = unigrams[word][docID] # term frequency in that document
                        else:
                            fi=0
                        dl=documentLen[docID]   #length of the document
                        tf = float(fi)/float(dl)
                        # idf with smoothing
                        idf = 1 + (math.log(float(N) / float(ni+1)))
                        score = tf * idf
                        if docID not in docScore:
                            docScore[docID]=score
                        else:
                            docScore[docID]+=score
            revSortedDocScore = sorted(docScore, key=docScore.get, reverse=True)# sorting in descending order
            retrieved_docs[qid] = revSortedDocScore[:100]
            if flag==0: #create a new file
                filename = "tfidf_Ranking" + ".txt"
                newFile = open(filename, 'w', encoding='utf-8')
                flag=1
            newFile.write("\n")
            newFile.write("q_id  Q0   doc_id   rank        score        system_name\n")
            for index,token in enumerate(revSortedDocScore):
                index+=1
                newFile.write(str(qid)+"   ")
                newFile.write("Q0   ")
                newFile.write(str(token) + " ")
                newFile.write(str(index)+"   ")
                newFile.write(str(docScore[token]))
                newFile.write(" tf-idf ")
                newFile.write("\n")

                if index==100:#For getting only top 100
                    break
            docScore={}
    newFile.close()
    filename = "tfidf_TOP100_retrieved" + ".txt"
    File = open(filename, 'w', encoding='utf-8')
    File.write(str(retrieved_docs))
    File.close()

if __name__ == "__main__":
    tfidf_ranking()