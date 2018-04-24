import bs4 as bsnew
def generateSnippet():
    file_contents = open("queries.txt", 'r', encoding='utf-8')
    queries = eval(file_contents.read())
    file_contents.close()
    file_contents = open("bm25_Ranking_PRF.txt", 'r', encoding='utf-8')
    queryRanks = eval(file_contents.read())
    file_contents.close()
    file_contents = open("common_words.txt", 'r', encoding='utf-8')
    stop_Words = file_contents.readline()
    file_contents.close()
    sentenceDict={}
    significance={}
    for qid in queryRanks.keys():
        docList=queryRanks[qid]
        queryWords = queries[qid]
        for doc in docList:
            filename = r"rawDocuments/" + doc + ".html"
            doc_contents = open(filename, 'r', encoding='utf-8')
            bs = bsnew.BeautifulSoup(doc_contents, "html.parser")
            content = bs.find("pre")
            content=content.get_text()
            content=content.strip()
            contentLines=content.splitlines()
            properContents=[]
            for c in contentLines:
                if not c=="":
                    properContents.append(c)
                if " PM" in c:
                    break
                if " AM" in c:
                    break
            for index,sentence in enumerate(properContents):
                sentenceDict[index+1]=sentence
                squareFreq=0
                for w in sentence.split():
                    if w in queryWords:
                        squareFreq+=1
                length=len(sentence)
                score=(squareFreq*squareFreq)/length
                significance[sentence]=score
            revSignificance = sorted(significance, key=significance.get, reverse=True)  # sorting in descending order
            revSignificance=revSignificance[:3]
            print(revSignificance)
            print(queryWords)





            exit(0)

generateSnippet()