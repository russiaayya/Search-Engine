import nltk

def inverted_Indexer():
    index = dict()
    index2 = dict()
    index3 = dict()
    primary_dict = dict()
    primary_dict2 = dict()
    primary_dict3 = dict()
    terms_in_doc = dict()
    term_positions = dict()
    index4 = dict()

    linksFile = r"BFS.txt"
    for link in open(linksFile):
        docID = link.rstrip().partition('wiki/')[2]
        # read the output of task 1
        inputFile = open(r'Parse and Tokenize\%s.txt' % docID, 'r', encoding='utf8')
        tokens = eval(inputFile.read())
        inputFile.close()

        primary_dict[docID] = dict()
        count = 0
        for token in tokens:
            if primary_dict[docID].get(token) is not None:
                primary_dict[docID][token] = primary_dict[docID][token]+1
            else:
                primary_dict[docID][token] = 1
            index[token] = dict()
            count += 1
        terms_in_doc[docID] = count

        bigrms_input = list(nltk.bigrams(tokens))
        bigrms = []
        primary_dict2[docID] = dict()
        for bigrm in bigrms_input:
            bigrm_str = bigrm[0] + ' ' + bigrm[1]
            bigrms.append(bigrm_str)
        for bigrm in bigrms:
            if primary_dict2[docID].get(bigrm) is not None:
                primary_dict2[docID][bigrm] = primary_dict2[docID][bigrm]+1
            else:
                primary_dict2[docID][bigrm] = 1
            index2[bigrm] = dict()

        trigrms_input = list(nltk.trigrams(tokens))
        trigrms = []
        primary_dict3[docID] = dict()
        for trigrm in trigrms_input:
            trigrm_str = trigrm[0] + ' ' + trigrm[1] + ' ' + trigrm[2]
            trigrms.append(trigrm_str)
        for trigrm in trigrms:
            if primary_dict3[docID].get(trigrm) is not None:
                primary_dict3[docID][trigrm] = primary_dict3[docID][trigrm]+1
            else:
                primary_dict3[docID][trigrm] = 1
            index3[trigrm] = dict()

        term_positions[docID] = dict()
        for i, token in enumerate(tokens):
            if term_positions[docID].get(token) is not None:
                term_positions[docID][token].append(i)
            else:
                term_positions[docID][token] = [i]
            index4[token] = dict()


    for docID in primary_dict.keys():
        for term in index.keys():
            # if primary_dict[docID][term] in primary_dict[docID].keys():
            if primary_dict[docID].get(term) is not None:
                index[term][docID] = primary_dict[docID][term]

    for docID in primary_dict2.keys():
        for term in index2.keys():
            if primary_dict2[docID].get(term) is not None:
                 index2[term][docID] = primary_dict2[docID][term]

    for docID in primary_dict3.keys():
        for term in index3.keys():
            if primary_dict3[docID].get(term) is not None:
                 index3[term][docID] = primary_dict3[docID][term]

    for docID in term_positions.keys():
        for term in index4.keys():
            if term_positions[docID].get(term) is not None:
                 index4[term][docID] = term_positions[docID][term]

    f = open(r'Inverted_Indexes\index1.txt', 'w', encoding="utf8")
    f.write(str(index))
    f.close()

    f = open(r'Inverted_Indexes\index2.txt', 'w', encoding="utf8")
    f.write(str(index2))
    f.close()

    f = open(r'Inverted_Indexes\index3.txt', 'w', encoding="utf8")
    f.write(str(index3))
    f.close()

    f = open(r'Inverted_Indexes\index1_readable.txt', 'w', encoding="utf8")
    for term in index.keys():
        f.write(str(term)+'-------> '+'\n')
        for doc in index[term].keys():
            f.write('('+str(doc)+', '+str(index[term][doc])+')')
            f.write(', ')
        f.write('\n')
        f.write('---------------------------------------------------------------------------'+'\n')
        f.write('---------------------------------------------------------------------------'+'\n')
    f.close()

    f = open(r'Inverted_Indexes\index2_readable.txt.txt', 'w', encoding="utf8")
    for term in index2.keys():
        f.write(str(term)+'-------> '+'\n')
        for doc in index2[term].keys():
            f.write('('+str(doc)+', '+str(index2[term][doc])+')')
            f.write(', ')
        f.write('\n')
        f.write('---------------------------------------------------------------------------'+'\n')
        f.write('---------------------------------------------------------------------------'+'\n')
    f.close()

    f = open(r'Inverted_Indexes\index3_readable.txt.txt', 'w', encoding="utf8")
    for term in index3.keys():
        f.write(str(term)+'-------> '+'\n')
        for doc in index3[term].keys():
            f.write('('+str(doc)+', '+str(index3[term][doc])+')')
            f.write(', ')
        f.write('\n')
        f.write('---------------------------------------------------------------------------'+'\n')
        f.write('---------------------------------------------------------------------------'+'\n')
    f.close()

    f = open(r'Inverted_Indexes\number_of_terms_in_doc.txt', 'w', encoding="utf8")
    f.write('DocID' + ' : ' + 'Count' + '\n')
    for doc in terms_in_doc.keys():
        f.write(str(doc) + ' : ' + str(terms_in_doc[doc]) + '\n')
    f.close()

    f = open(r'Inverted_Indexes\index_positions.txt', 'w', encoding="utf8")
    for term in index4.keys():
        f.write(str(term) + '-------> ' + '\n')
        for doc in index4[term].keys():
            f.write(str(doc) + ' : ' + str(index4[term][doc]))
            f.write('\n')
        f.write('\n')
        f.write('---------------------------------------------------------------------------' + '\n')
        f.write('---------------------------------------------------------------------------' + '\n')
    f.close()


if __name__ == "__main__":
    inverted_Indexer()
