# Search-Engine

GOAL: Design and build your information retrieval systems, evaluate and compare their performance levels in terms of retrieval effectiveness

INSTRUCTIONS:

--> Please maintain the format of each input and output files.
It's important to read the file from disk and write it to memory. --> The file extensions are fixed.
The raw documents have to be in .html (to parse) and every output file or other input files should be in .txt except for snippet generation, the output file is in .html --> For every user input, please make sure to give the full path of the document. --> The retrieval models have results with Query ID, which are not always in ascending order of the Query ID.

LIBRARIES REQUIRED:

import requests from bs4 import BeautifulSoup import os import re from string import maketrans import operator from collections import defaultdict

Note: Please give the full path while giving the input path when asked

HOW TO RUN THE FILES:

# Phase1- Indexing and Retrieval
Task1:

Source files:

Tokenizer.py
Enter the path to the folder which has the raw documents to run the code

invertedIndex.py
Path to the folder that has the tokenized files

luceneImplementation.java

Utilities.py to create queries.

Output:
bm25_Ranking.txt
Query-likelihood-ranking.txt
tfidf_Ranking.txt
Lucene_Ranking.txt
invertedIndex_Task3.py

========================================================================
Task 2:
Use the output of Task1 :bm25_Ranking_PRF.txt
Other files required: queries.txt and common_words.txt
Source file: PRF.py

Output : enrichedQueries.txt

========================================================================
Task 3:

Source code : (to be run in below order)
processStemmedQueries.py
tokenizer_Stemming.py
invertedIndex_TASK3.py
bm25_TASK3.py
query-likelihood_TASK3.py
tfidf_TASK3.py

# for running invertedIndex_TASK3.py use  tokenized_Files_Stemmed directory
Output:
BM25-stemmed-ranking.txt
BM25-stopping-ranking.txt
Query-likelihood-stemmed-ranking.txt
Query-likelihood-stopped-ranking.txt
Tidf-stemmed-ranking.txt
tidf-stopped-ranking.txt

==============================================================================
Phase 2

Snippet generation

Source code-snippetGenerator.py
Different queries can be provided in the queries.txt,ranking can be provided in the bm25_Ranking_PRF.txt file,stopping words can be provided in the common_words.txt file and run

Output-snippetGenerator.html can be viewed to see the snippet generation.


==============================================================================

Phase 3
Source code- evaluation.py

Evaluation function takes relevance input is taken as the first input, second in the ranking in top100,output destination file which will provide the recall,precisions in tabular column and also calculate the MRR,MAP values

================================================================================


Extra credit:
Task 1)
Source code:
spellErrorGenerator.py

Queries can be provided in queries.txt

Output 
SEG_queries.text- That will provide the list of queries with the errors


================================================================================

Task 2)
Source code:
softMatchingQueryHandler.py
Error queries are provided in SEG_queries.txt as the input for this step.


Output:
softMatchingQuery.txt has the corrected list of queries.



***All text files with evaluation word has the evaluations for all the models,variations.
