import bs4 as bs
import urllib.request
import nltk
import string
import re

def contains_Only_Digits(string):
    for c in string:
        if c.isalpha():
            return False
    return True

def parse_Tokenize(ip):
    linksFile = r"BFS.txt"
    for link in open(linksFile):
        file = r"BFS_docs\%s.html" %link.rstrip().partition('wiki/')[2]
        soup = bs.BeautifulSoup(open(file, encoding="utf8").read(), 'html.parser')
        # remove table tags
        for tag in soup('table'):
            tag.decompose()
        # remove image tags
        for tag in soup('img'):
            tag.decompose()
        # remove formula
        for tag in soup('pre'):
            tag.decompose()
        # remove pseudocode etc
        for tag in soup('code'):
            tag.decompose()
        for item in soup.find_all('a', href=re.compile(r'^http')):
            item.decompose()

        # split the text in the document by space
        tokens = soup.get_text().split()
        # extract and add tokens from the title
        title_tokens = link.rstrip().partition('wiki/')[2].split('_')
        tokens.extend(title_tokens)
        tokenList = []
        if ip == 'Y':
            # excluding '-' in order to preserve hyphens
            translator = str.maketrans('', '', string.punctuation.replace('-',''))
            for token in tokens:
                # if there exists a token with just punctuations
                if len(token.translate(str.maketrans('', '', string.punctuation))) == 0:
                    continue
                if contains_Only_Digits(token):
                    tokenList.append(token.strip(string.punctuation))
                    continue
                tokenList.append(token.translate(translator).lower())
        else:
            for token in tokens:
                if len(token.translate(str.maketrans('', '', string.punctuation))) == 0:
                    continue
                tokenList.append(token)

        f = open(r'Parse and Tokenize\%s.txt'%link.rstrip().partition('wiki/')[2], 'w', encoding="utf8")
        f.write(str(tokenList))
        f.close()

if __name__ == "__main__":
    ip = input('Do you want default parser with case-folding and punctuation handling? Enter Y or N: ')
    type(ip)
    parse_Tokenize(ip)
