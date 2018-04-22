import operator

def corpus_Statistics():
    inputFile = open(r'Inverted_Indexes\index1.txt', 'r', encoding='utf8')
    index1 = eval(inputFile.read())
    inputFile.close()

    inputFile = open(r'Inverted_Indexes\index2.txt', 'r', encoding='utf8')
    index2 = eval(inputFile.read())
    inputFile.close()

    inputFile = open(r'Inverted_Indexes\index3.txt', 'r', encoding='utf8')
    index3 = eval(inputFile.read())
    inputFile.close()

    term_frequency1 = dict()
    term_frequency2 = dict()
    term_frequency3 = dict()

    for term in index1.keys():
        count = 0
        for docID in index1[term].keys():
            count += index1[term][docID]
        term_frequency1[term] = count

    sortedTable1 = sorted(term_frequency1.items(), key=operator.itemgetter(1), reverse=True)
    file = open(r'Corpus_statistics\term_frequency1.txt', 'w', encoding='utf8')
    for item in sortedTable1:
        file.write(item[0] + ' : ' + str(item[1]) + '\n')
    file.close()

    for term in index2.keys():
        count = 0
        for docID in index2[term].keys():
            count += index2[term][docID]
        term_frequency2[term] = count

    sortedTable2 = sorted(term_frequency2.items(), key=operator.itemgetter(1), reverse=True)
    file = open(r'Corpus_statistics\term_frequency2.txt', 'w', encoding='utf8')
    for item in sortedTable2:
        file.write(item[0] + ' : ' + str(item[1]) + '\n')
    file.close()

    for term in index3.keys():
        count = 0
        for docID in index3[term].keys():
            count += index3[term][docID]
        term_frequency3[term] = count

    sortedTable3 = sorted(term_frequency3.items(), key=operator.itemgetter(1), reverse=True)
    file = open(r'Corpus_statistics\term_frequency3.txt', 'w', encoding='utf8')
    for item in sortedTable3:
        file.write(item[0] + ' : ' + str(item[1]) + '\n')
    file.close()

    lexSortedTable1 = sorted(sorted(index1.keys()), key=str.upper)
    file = open(r'Corpus_statistics\doc_frequency1.txt', 'w', encoding='utf8')
    for term in lexSortedTable1:
        file.write(term+' -------->'+'\n')
        file.write('[')
        for docID in index1[term].keys():
            file.write(str(docID)+', ')
        file.write(']')
        file.write('\n')
        file.write(str(len(index1[term])))
        file.write('\n')
        file.write('---------------------------------------------------------------------------'+'\n')
        file.write('---------------------------------------------------------------------------'+'\n')
    file.close()

    lexSortedTable2 = sorted(sorted(index2.keys()), key=str.upper)
    file = open(r'Corpus_statistics\doc_frequency2.txt', 'w', encoding='utf8')
    for term in lexSortedTable2:
        file.write(term+' -------->'+'\n')
        file.write('[')
        for docID in index2[term].keys():
            file.write(str(docID)+', ')
        file.write(']')
        file.write('\n')
        file.write(str(len(index2[term])))
        file.write('\n')
        file.write('---------------------------------------------------------------------------'+'\n')
        file.write('---------------------------------------------------------------------------'+'\n')
    file.close()

    lexSortedTable3 = sorted(sorted(index3.keys()), key=str.upper)
    file = open(r'Corpus_statistics\doc_frequency3.txt', 'w', encoding='utf8')
    for term in lexSortedTable3:
        file.write(term+' -------->'+'\n')
        file.write('[')
        for docID in index3[term].keys():
            file.write(str(docID)+', ')
        file.write(']')
        file.write('\n')
        file.write(str(len(index3[term])))
        file.write('\n')
        file.write('---------------------------------------------------------------------------'+'\n')
        file.write('---------------------------------------------------------------------------'+'\n')
    file.close()

    # Code to generate list of terms in the corpus sorted by document frequency
    # Used to obtain the stoplist

    # document_frequency1 = dict()
    # document_frequency2 = dict()
    # document_frequency3 = dict()
    #
    # for term in index1.keys():
    #     document_frequency1[term] = len(index1[term])
    #
    # sorteddoc1 = sorted(document_frequency1.items(), key=operator.itemgetter(1), reverse=True)
    # file = open(r'Corpus_statistics\doc_frequency_1_DF_Sorted.txt', 'w', encoding='utf8')
    # for item in sorteddoc1:
    #     file.write(str(item[0]) + ' : ' + str(item[1]) + '\n')
    # file.close()
    #
    # for term in index2.keys():
    #     document_frequency2[term] = len(index2[term])
    #
    # sorteddoc2 = sorted(document_frequency2.items(), key=operator.itemgetter(1), reverse=True)
    # file = open(r'Corpus_statistics\doc_frequency_2_DF_Sorted.txt', 'w', encoding='utf8')
    # for item in sorteddoc2:
    #     file.write(str(item[0]) + ' : ' + str(item[1]) + '\n')
    # file.close()
    #
    # for term in index3.keys():
    #     document_frequency3[term] = len(index3[term])
    #
    # sorteddoc3 = sorted(document_frequency3.items(), key=operator.itemgetter(1), reverse=True)
    # file = open(r'Corpus_statistics\doc_frequency_3_DF_Sorted.txt', 'w', encoding='utf8')
    # for item in sorteddoc3:
    #     file.write(str(item[0]) + ' : ' + str(item[1]) + '\n')
    # file.close()



if __name__ == "__main__":
    corpus_Statistics()
