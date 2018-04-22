# coding: utf-8

#corpus statistics

from utilities import *
import collections
from indexer import *
from tokenizer import *
from constants import *
from operator import itemgetter


def tf_table(indexer):

    dict = {}
    for key, value in indexer.iteritems():
        #adding up the term frequency
        dict[key] = sum(value.itervalues())

    #Sort from	most to	least frequent
    dict = collections.OrderedDict(reversed(sorted(dict.items(),key=itemgetter(1))))
    return dict


# create term frequency table comprising of	two	columns: term (key) and tf(value)
def create_tf_table(indexer, n):
    entrylist = []
    tfdict = tf_table(indexer)

    for key in tfdict:
        postingstr = key + "    " + str(tfdict[key])
        entrylist.append(postingstr)

    if n == 1:
        filename = unigram_tftable_file
    elif n == 2:
        filename = bigram_tftable_file
    else:
        filename = trigram_tftable_file

    filepath = TF_OUTPUT_DIR + filename + ".txt"

    create_file(filepath)
    write_list_to_file(filepath, entrylist)


def create_df_table(indexer, n):
    dflist = []
    for key , value in indexer.iteritems():
        value = collections.OrderedDict(sorted(value.iteritems()))

    #Sort lexicographically based on term
    indexer = collections.OrderedDict(sorted(indexer.iteritems()))

    #key :term , arr: docIDs , len(arr) : document frequency
    for key,value in indexer.iteritems():
        a = value.keys()
        posting = key + "\t\t" + ','.join(map(str, a)) + "    " + str(len(a))
        dflist.append(posting)


    if n == 1:
        filename = "Unigram_df_table"
    elif n == 2:
        filename = "Bigram_df_table"
    elif n == 3:
        filename = "trigram_df_table"

    # creating file document frequency table
    filename = DF_OUTPUT_DIR + filename + ".txt"

    create_file(filename)
    write_list_to_file(filename, dflist)


def create_stoplist(tffile,n,cutoff):
    #templst = []
    stoplst = []
    # templst = write_file_tolist(tffile)
    stoplst = write_file_tolist(tffile)

    if n == 1:
        filename = "Unigram_Stoplist"
    elif n == 2:
        filename = "Bigram_Stoplist"
    elif n == 3:
        filename = "trigram_Stoplist"

    #taking stoplist till cutoff value
    stoplst = stoplst[:cutoff+1]
    #stoplst = stoplst[:cutoff]

    # creating file for stoplist
    filename = SL_OUTPUT_DIR + filename + ".txt"

    create_file(filename)
    write_list_to_file(filename, stoplst)




if __name__ == '__main__':
    
    # creating required directories
    create_dir(tokenized_file_dir)
    create_dir(indexers_file_dir)
    create_dir(TF_OUTPUT_DIR)
    create_dir(DF_OUTPUT_DIR)
    create_dir(SL_OUTPUT_DIR)

    s4 = time.time()
    files_tokenization(dir)
    e4 = time.time()
    print "tokenizing time", str(e4-s4)
    create_index()
    print "indexer created"

    s1 = time.time()
    print "creating unigram term frequency table......"
    create_tf_table(get_indexer(1),1)
    print "creating bigram term frequency table......"
    create_tf_table(get_indexer(2), 2)
    print "creating trigram term frequency table......"
    create_tf_table(get_indexer(3), 3)
    e1 = time.time()
    print "time taken for creating tf table", str(e1-s1)

    s2 = time.time()
    print "creating unigram document frequency table......"
    create_df_table(get_indexer(1),1)
    print "creating bigram document frequency table......"
    create_df_table(get_indexer(2), 2)
    print "creating trigram document frequency table......"
    create_df_table(get_indexer(3), 3)
    e2 = time.time()
    print "time taken for creating df table", str(e2 - s2)

    s3 = time.time()
    print "creating stopword list for unigram indexer"
    create_stoplist(TF_OUTPUT_DIR + unigram_tftable_file + ".txt" , 1, 20)
    print "creating stopword list for bigram indexer"
    create_stoplist(TF_OUTPUT_DIR + bigram_tftable_file + ".txt", 2, 20)
    print "creating stopword list for trigram indexer"
    create_stoplist(TF_OUTPUT_DIR + trigram_tftable_file + ".txt", 3, 75)
    e3 = time.time()
    print "time taken for creating stoplist", str(e3 - s3)












