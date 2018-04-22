import os
import string
from urllib.request import urlopen
import bs4 as bsnew
from nltk import word_tokenize
from string import punctuation



def numsOnly(inputString):# function to make sure it contains only the digits and punctuations and no alphabets
    if any(c.isalpha() for c in inputString):
        return False
    if any(char.isdigit() for char in inputString):
        return True

def generateTokens(dir):
    filelist = os.listdir(os.path.abspath(dir))
    #print(filelist)
    validTokens = []
    punctuation = string.punctuation.replace("-", "")  # retaining hyphen- question
    count = 0
    for f in filelist:
        if len(f) <= 1:
            continue
        full_path=dir+"//"+f
        file_contents = open(full_path, "r", encoding='utf-8').read()
        bs = bsnew.BeautifulSoup(file_contents, "html.parser")
        content = bs.find("pre")
        raw = content.get_text()
        contents = str(raw).split()
        for t in contents:
            if numsOnly(t):
                validTokens.append(t.strip(string.punctuation))
                continue
            t = t.lower()
            for char in t:
                if char in punctuation:
                    t = t.replace(char, "")
            if len(t)==1 and t== "-":
                continue
            if len(t) >= 1:
                validTokens.append(t)
        f=f.replace(".html","")
        filename = r"tokenized_Files/" + f + ".txt"
        newFile = open(filename, 'w', encoding='utf-8')
        newFile.write(str(validTokens))
        validTokens = []
        newFile.close()


if __name__ == "__main__":
    generateTokens("D:\\IR_project\\rawDocuments")
