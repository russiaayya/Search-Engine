from difflib import get_close_matches

def getSoftMatchingQueryTerm(word,patterns):
    print(get_close_matches(word, patterns))

if __name__ == "__main__":
    file_contents = open("queries.txt", 'r', encoding='utf-8')
    queries = eval(file_contents.read())
    file_contents.close()
    file_contents = open("common_words.txt", 'r', encoding='utf-8')
    stop_Words = file_contents.read()
    file_contents.close()
    file_contents = open("unigram_index.txt", 'r', encoding='utf-8')
    unigrams = eval(file_contents.read())
    file_contents.close()
    pattern=[]
    for term in unigrams:
        pattern.append(term)
    for qid in queries.keys():
        for word in queries[qid]:
            correctWord=getSoftMatchingQueryTerm(word,pattern)