import bs4 as bsnew
import string
import tokenizer
def extractQueries():
    file_contents = open("rawQueries.txt", "r", encoding='utf-8').read()
    bs = bsnew.BeautifulSoup(file_contents, "html.parser")
    content = bs.findAll("doc")
    queryId={}
    for q in content:
        qid=q.find("docno").get_text()
        q=q.get_text().strip('')
        q=q.replace("\n"," ")
        q=q.replace("\t", " ")
        q=q.replace(qid,"").strip()
        qTokens=queryPunctuations(q)
        queryId[qid]=qTokens
        qTokens=[]
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
extractQueries()
