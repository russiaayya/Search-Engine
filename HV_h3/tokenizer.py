# coding=utf-8

from utilities import *
import re
from bs4 import BeautifulSoup
from constants import *


def clean_punctuation(text):
    #removing punctions
    text = re.sub(r'[!\"#$%&\'()*+/:;<=>?@[\\\]^_`{|}~]', ' ', text)

    # remove all "-" not between text
    text = re.sub(r'(?<![a-zA-Z0-9])-|-(?![a-zA-Z0-9])', ' ', text)

    # remove all ",", "." in text not between digits
    text = re.sub(r'(?<![0-9])[,.]|[,.](?![0-9])', ' ', text)
    return text


def clean_urls(raw):
    removeurls = re.compile(r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''')
    cleantext = re.sub(removeurls, '', raw)
    return cleantext


def clean_tags(content):
    # remove html entities to clean the text under those entities using decompose
    for tag in content.findAll(['script', 'style', 'sub', 'sup']):
        tag.decompose()
    for tag in content.findAll("sup", {"class": ["reference"]}):
        tag.decompose()
    for tag in content.findAll("span", {"class": ["mw-editsection", "mwe-math-element"]}):
        tag.decompose()
    for tag in content.findAll("span", {"id": "References"}):
        tag.decompose()
    for tag in content.findAll("div", {"id": "toc"}):
        tag.decompose()
    for tag in content.findAll("div", {"class":"reflist"}):
        tag.decompose()
    for tag in content.findAll("span", {"id": "Further_reading"}):
        tag.decompose()
    for tag in content.findAll("table", {"class": "plainlinks"}):
        tag.decompose()
    for tag in content.findAll("span", {"id": "External_links"}):
        tag.decompose()
    for tag in content.findAll("a", {"class": ["external free"]}):
        tag.decompose()
    return content


def format_cleaning(text):
        if text == '':
            return ""
        elif not isinstance(text, basestring):
            return ""
        elif text.strip() == '':
            return ""

        cleantext = text

        # remove whitespace
        cleantext = re.sub(r'&nbsp;', ' ', cleantext)
        cleantext = re.sub(r'  ', ' ', cleantext)

        # split into lines and on each line remove leading & trailing space
        lines = (line.strip() for line in cleantext.splitlines())

        # split each multiple head lines into a line
        mlines = (words.strip() for line in lines for words in line.split("  "))

        # remove blank lines
        cleantext = '\n'.join(lines for lines in mlines if lines)

        #casefolding to lower case
        cleantext = cleantext.lower()
        return cleantext



#NOTE filename format:  "directory_name/file_name"+ ".txt"

def tokenization(filename):
    # read contents of the file
    soup = BeautifulSoup(open(filename), "html.parser")
    # take the main content portion
    content = soup.select("div[id='content']")[0]
    # content= soup.findAll('p')

    content = clean_tags(content)

    # Get the header from the content
    head = content.select("h1[id='firstHeading']")[0]
    textdiv = content.select("div[id='mw-content-text']")[0]

    # get text from header for naming file
    raw = head.get_text() + "\n"

    # get the text part on the content excluding tags
    raw = raw + textdiv.get_text()


    # Remove unprintable characters
    raw = re.sub(r'[^\x00-\x7F]+', ' ', raw)

    #remove urls
    raw = clean_urls(raw)

    # remove punctuation
    raw = clean_punctuation(raw)

    #remove dates format yyyy-mm-dd
    # raw = re.sub(r'\d{4}-\d{2}-\d{2}', ' ', raw)

    #text cleaning
    text = format_cleaning(raw)

    # print text
    return text


def files_tokenization(dir):
    tokenizedfiles = []
    docidlist = []

    # list of files in the given dir
    filelist = os.listdir(os.path.abspath(dir))

    if len(filelist) < 1:
        print "No file exists in directory"

    # create directory for keeping tokenized files
    create_dir(tokenized_file_dir)

    for file in filelist:
        filename = dir + file

        if not os.path.exists(filename):
            continue

        #tokenize text in file
        tokenized_text = tokenization(filename)

        #get docID which is the filename excluding .txt
        suffix = os.path.splitext(file)[0]
        #remove _ - / () , from the filename
        docID = re.sub(r"[-_/(),]", "", suffix)

        if docID in tokenizedfiles:
            docID += str(tokenizedfiles.count(docID))
        else:
            tokenizedfiles.append(docID)

        tfilename = tokenized_file_dir + docID + ".txt"

        # write parsed data to file
        create_file(tfilename)
        write_to_file(tfilename, tokenized_text.encode("utf-8"))
        docidlist.append(docID)
    #print "writing list to file"
    write_list_to_file(docid_lists_file +".txt", docidlist)



