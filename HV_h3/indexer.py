
from utilities import *
import collections
from collections import OrderedDict
import time
from constants import *



unigramindexer = {}
bigramindexer = {}
trigramindexer = {}
totalunitokens = 0
totalbitokens = 0
totaltritokens = 0

unitokendict = {}
bitokendict = {}
tritokendict = {}



def create_index():
    docidlist = write_file_tolist(docid_lists_file +".txt")
    docidlist.sort()

    for docid in docidlist:
        filename = docid+".txt"
        filepath = tokenized_file_dir + filename

        if not os.path.exists(filepath):
            continue

        with open(filepath) as f:
            filetext = " ".join(line.strip() for line in f.readlines())
        #print "file text extracted"
        wordslist =  filetext.split(' ')

        # creating three indexers for unigram , bigram , trigram
        add_to_index(unigramindexer, 1, wordslist, docid, unitokendict)
        add_to_index(bigramindexer, 2, wordslist, docid, bitokendict)
        add_to_index(trigramindexer, 3, wordslist, docid, tritokendict)

    start = time.time()
    write_index_to_file("index_files/unigram_indexer.txt", unigramindexer)
    write_index_to_file("index_files/bigram_indexer.txt", bigramindexer)
    write_index_to_file("index_files/trigram_indexer.txt", trigramindexer)
    end = time.time()
    print "total time taken to write indexer", str(end - start)


def add_to_index(index, n, terms, docid, tokenfiledict):
    global totalunitokens
    global totalbitokens
    global totaltritokens
    ngramdict = {}

    #n-grams dict for given words based on n = 1,2,3
    ngramdict = ngrams(terms,n)

    #key : term (unigram or bigram or trigram)
    #value : terms frequency
    for key, value in ngramdict.iteritems():
        # if key not present then create one set and add to index
        if key not in index:
            dict = {}
            dict[docid]=value
            index[key] = dict
        else:
            dict = index[key]

            if docid not in dict:
                dict[docid] = value
            else:
                dict[docid] += value


    wordscount =len(ngramdict)
    #print "no. of words in ngramdict ",wordscount

    if n ==1:
        totalunitokens += wordscount
    elif n ==2:
        totalbitokens += wordscount
    else:
        totaltritokens += wordscount

    tokenfiledict[docid] = wordscount


def ngrams(terms, n):
    # get the list of tuples for the words as per specified ngram index
    #Unzipping mapped values using *
    nglist = zip(*[terms[c:] for c in range(n)])

    # convert the tuples to str for saving as key in dict
    nglist = [" ".join(w) for w in nglist]

    # generate the dict sorted by term-frequency & having terms and frequency using counter
    termsbyfreqdict = collections.Counter(nglist)

    return termsbyfreqdict


def get_indexer(n):
    if n == 1:
        return unigramindexer
    elif n == 2:
        return bigramindexer
    else:
        return trigramindexer









