import tokenizer
from tokenizer import generateTokens
import invertedIndex

if __name__ == "__main__":
    ip = input('Enter 1 for default indexing without stopping or stemming, 2 for stopping , 3 for stemming')
    type(ip)
    # tokenizer.generateTokens()
    parse_Tokenize(ip)