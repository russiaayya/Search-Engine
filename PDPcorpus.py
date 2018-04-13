import string
from urllib.request import urlopen
import bs4 as bsnew
from nltk import word_tokenize
from string import punctuation


def hasNumbersNoAlpha(inputString):# function to make sure it contains only the digits and punctuations and no letters
    if any(c.isalpha() for c in inputString):
        return False
    if any(char.isdigit() for char in inputString):
        return True



def generateCorpus(choice):
    file = open("bfs.txt", "r")
    validLinks = file.readlines()
    file.close()
    validTokens = []
    punctuation = string.punctuation.replace("-", "")  # retaining hyphen- question
    count = 0
    for url in validLinks:
        print(url)
        if len(url) <= 1:
            continue
        urlindex = url.index('wiki/')
        specificUrl = url[urlindex + 5:]
        specificUrl = specificUrl.strip("\n")
        filename = r"bfsFiles/" + specificUrl + ".html"
        file_contents = open(filename, "r", encoding='utf-8').read()
        bs = bsnew.BeautifulSoup(file_contents, "html.parser")
        titles = specificUrl.split("_")
        content = bs.find("div", {"id": "mw-content-text"})
        for a in content.findAll("table"):
            a.decompose()
        for a in content.findAll("img"):
            a.decompose()
        for a in content.findAll("pre"):
            a.decompose()
        for a in content.findAll("code"):
            a.decompose()
        raw = content.get_text()
        contents = str(raw).split()
        contents.extend(titles)
        for t in contents:
            if "http" in t:#ignoring links
                continue
            if hasNumbersNoAlpha(t):
                validTokens.append(t)
                continue
            if choice == "1":
                t = t.lower()
                for char in t:
                    if char in punctuation:
                        t = t.replace(char, "")
            if len(t) >= 1:
                validTokens.append(t)
        urlindex = url.index('wiki/')
        specificUrl = url[urlindex + 5:]
        specificUrl = specificUrl.strip("\n")
        filename = r"corpus/" + specificUrl + ".txt"
        newFile = open(filename, 'w', encoding='utf-8')
        newFile.write(str(validTokens))
        validTokens = []
        newFile.close()


if __name__ == "__main__":
    choice = input(
        "Enter 0 for no case folding/punctuation handling \nEnter 1 for default settings where casefolding and punctions are removed")
    type(choice)
    generateCorpus(choice)
