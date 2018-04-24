from difflib import get_close_matches

def getSoftMatchingQueryTerm(word,corpus):
    listOfCorrections=get_close_matches(word, corpus)
    for w in listOfCorrections:
        if len(w)==len(word) and w not in stop_Words:
            return w
if __name__ == "__main__":
    file_contents = open("SEG_queries.txt", 'r', encoding='utf-8')
    queries = eval(file_contents.read())
    file_contents.close()
    file_contents = open("common_words.txt", 'r', encoding='utf-8')
    stop_Words = file_contents.read()
    file_contents.close()
    file_contents = open("unigram_index.txt", 'r', encoding='utf-8')
    unigrams = eval(file_contents.read())
    file_contents.close()
    corpus=[]
    for term in unigrams:
        corpus.append(term)
    for qid in queries.keys():
        for word in queries[qid]:
            if word in stop_Words:
                continue
            print("Original word:",word)
            correctWord = ""
            if word not in corpus:
                correctWord=getSoftMatchingQueryTerm(word,corpus)
            if correctWord=="":
                correctWord=word
            print("Corrected word:",correctWord)
            