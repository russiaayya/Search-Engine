import bs4 as bsnew

def generateSnippet():
    file_contents = open("queries.txt", 'r', encoding='utf-8')
    queries = eval(file_contents.read())
    file_contents.close()
    file_contents = open("bm25_Ranking_PRF.txt", 'r', encoding='utf-8')
    queryRanks = eval(file_contents.read())
    file_contents.close()
    file_contents = open("common_words", 'r', encoding='utf-8')
    stop_Words = file_contents.readline()
    file_contents.close()

    for qid in queryRanks.keys():
        docList=queryRanks[qid]
        for doc in docList:
            filename = r"rawDocuments/" + doc + ".html"
            doc_contents = open(filename, 'r', encoding='utf-8')
            bs = bsnew.BeautifulSoup(doc_contents, "html.parser")
            content = bs.find("pre")
            content=content.get_text()
            content=content.strip()
            print(content)
            queryWords=queries[qid]
            for word in queryWords:
                if word in stop_Words:
                    print("continue",word)
                    continue
                if word in content:
                    print(word)
            exit(0)


generateSnippet()