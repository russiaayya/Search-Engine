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
    snippet_html=open("snippetGeneration.html",'w',encoding='utf-8')
    snippet_html.write("<!DOCTYPE html>")
    snippet_html.write("<html>")
    for qid in queryRanks.keys():
        docList=queryRanks[qid]
        queryWords = queries[qid]
        for doc in docList:
            sentenceDict = {}
            significance = {}
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
            finalSnippet=[]
            for relSentence in revSignificance:
                for word in relSentence.split():
                    if word in queryWords:
                        word="<b>"+word+"</b>"
                        finalSnippet.append(word)
                    else:
                        finalSnippet.append(word)
            snippet_html.write("The query is:\n")
            snippet_html.write("<p>")
            snippet_html.write(" ".join(queryWords))
            snippet_html.write("</p>")
            snippet_html.write("<p>")
            snippet_html.write(" ".join(finalSnippet))
            #snippet_html.write(" ".join(revSignificance))
            snippet_html.write("</p>")
    snippet_html.write("</html>")
    snippet_html.close()
generateSnippet()