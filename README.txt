# Search-Engine

GOAL: Design and build your information retrieval systems, evaluate and compare their performance levels in terms of retrieval effectiveness

FILES SUBMITTED:

# Phase1- Indexing and Retrieval

Task1:-

Task2:-


Task3:- A)

B)

# Phase2- Displaying results

Generate_Snippet.py code to generate the snippets for each results generated. This is used to display results.
Output : snippetGeneration.html file for using BM25 results.

Phase3- Evaluation

Phase3_Evaluation.py used to evaluate the generated results for each retrieval model by taking the results and cacm.rel.txt as input.


Extra Credit-


INSTRUCTIONS:

--> Please maintain the format of each input and output files.
It's important to read the file from disk and write it to memory. --> The file extensions are fixed.
The raw documents have to be in .html (to parse) and every output file or other input files should be in .txt except for snippet generation, the output file is in .html --> For every user input, please make sure to give the full path of the document. --> The retrieval models have results with Query ID, which are not always in ascending order of the Query ID.


LIBRARIES REQUIRED:

import requests from bs4 import BeautifulSoup import os import re from string import maketrans import operator from collections import defaultdict

Note: Please give the full path while giving the input path when asked

HOW TO RUN THE FILES:

