import bs4 as bsnew
import string
import tokenizer
def extractQueries():
    file_contents = open("rawQueries.txt", "r", encoding='utf-8').read()
    bs = bsnew.BeautifulSoup(file_contents, "html.parser")
    content = bs.findAll("doc")
    queryId={}
    filename = "queriesForLucene.txt"
    newFile1 = open(filename, 'w', encoding='utf-8')
    for q in content:
        qid=q.find("docno").get_text()
        q=q.get_text().strip('')
        q=q.replace("\n"," ")
        q=q.replace("\t", " ")
        q=q.replace(qid,"").strip()
        qTokens=queryPunctuations(q)
        queryId[qid]=qTokens
        str1 = ' '.join(qTokens)
        newFile1.write(str1)
        newFile1.write("\n")
    newFile1.close()
    filename = "queries.txt"
    newFile = open(filename, 'w', encoding='utf-8')
    newFile.write(str(queryId))
    newFile.close()

def queryPunctuations(q):
    punctuation = string.punctuation.replace("-", "")  # retaining hyphen- question
    nums_punctuation = "!\"#$%&'()*+/;<=>?@[\]^_`{|}~"  # removing . , - : for digits
    queryTerms=q.split()
    validQterms=[]
    for term in queryTerms:
        if tokenizer.numsOnly(term):
            for t in term:
                if t in nums_punctuation:
                    term = term.replace(t, "")
            continue
        term=term.lower()
        for char in term:
            if char in punctuation:
                if char in punctuation:
                    term = term.replace(char, "")
        if len(term) == 1 and term == "-":
            continue
        if len(term) >= 1:
            validQterms.append(term)
    return validQterms



def extractRelevence():
    file_contents = open("cacm.rel.txt", "r", encoding='utf-8')
    queryRel={}
    relevance=file_contents.readlines()
    for r in relevance:
        r=r.split()
        if r[0] not in queryRel:
            queryRel[r[0]]=[r[2]]
        else:
            queryRel[r[0]].append(r[2])
    filename = "queryRelevance.txt"
    newFile = open(filename, 'w', encoding='utf-8')
    newFile.write(str(queryRel))
    newFile.close()
#extractQueries()
extractRelevence()