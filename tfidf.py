
import sys
import math
from collections import OrderedDict
import operator
# from utils import *



filename = "unigram_indexer.txt"
query_list = ['dark eclipse moon','forecast models','total eclipse solar','japan continental airline','japan continental airlines','solar eclipse fiction','2017 solar eclipse','total eclipse lyrics','nordic marine animals','volcanic eruptions tornadoes eruption tornado']
max = 100
output_file_path = "task2/"



def tfidf(filename):

    index_dic = {}
    # first read the index file and add data to dictionary named index_dic
    file = open(filename, "r")
    for line in file:
        lst = line.strip().split("->")
        term = lst[0]
        posting = lst[1]
        term = term.replace(' ', '')
        term = term.replace("\n", "")
        posting = posting.replace('(' ,'')
        posting = posting.replace(')', '#')
        posting = posting.replace(' ', '')

        # seperating key and value
        key_val = posting.split('#')
        dic = {}

        for k in key_val:
            if k != '':
                key = k.split(",")[0]
                value = int(k.split(",")[1])
                dic[key]= value

        if term not in index_dic:
            index_dic[term] = dic

    print "index size" , len(index_dic)
    total_doc_len = 0
    doc_len_dict = {}

    # computing document length(size) of each document represented by docId
    for word in index_dic:
        index = index_dic[word]
        for docid in index:
            if docid not in doc_len_dict:
                doc_len_dict[docid] = index[docid]
            else:
                doc_len_dict[docid] += index[docid]



     # calculating total length(size) of all the documents
    for docid in doc_len_dict:
        total_doc_len += doc_len_dict[docid]

    no_of_docs = len(doc_len_dict)
    print "N", no_of_docs

    qid = 0
    for q in query_list:
        qid += 1
        qterms = q.split(" ")
        # dictionary having key(query term) and value(set of docIds in which this term appears)
        df_dict = {}
        for term in qterms:
            if term in index_dic:
                index = index_dic[term]
                doc_ids = set()
                for doc_id in index:
                    doc_ids.add(doc_id)
                df_dict[term] = doc_ids
            else:
                df_dict[term] = set()

        docs = set()  # only docIds in which query terms appears

        for word in qterms:
            doc_ids = df_dict[word]
            if doc_ids != None:
                for d in doc_ids:
                    docs.add(d)

        for doc_id in docs:
            score = 0
            dl = doc_len_dict[doc_id]
            for word in qterms:
                qf = qterms.count(word)            #frequency of that word(term) in the query
                n = len(df_dict[word])
                N = len(doc_len_dict)

                if word in index_dic:
                    index = index_dic[word]
                    if doc_id in index:
                        tf = index[doc_id]
                    else:
                        tf = 0




    # sort in order for high relevance score
    top100_bm25_dict = OrderedDict(sorted(tfidf.items(), key=operator.itemgetter(1), reverse=True)[:max])
    rank = 1

    print "writing bm25 score list to file for query " + q
    filename = output_file_path + q.replace(" ", "_") + ".txt"
    file = open(filename, "w")
    format = "qid Q0   doc_id     		           rank   BM25_score      	 system_name"
    file.write(format)
    file.write("\n")

    for key, value in top100_bm25_dict.iteritems():
        file.write(str(qid) + "   " + "Q0" + "   " + str(key) + " " * (35 - len(str(key))) + str(rank) + " " * (6 - len(str(rank))) + str(value) + " " * (18 - len(str(value))) + str(system_name))
        rank += 1
        file.write("\n")

        file.close()







