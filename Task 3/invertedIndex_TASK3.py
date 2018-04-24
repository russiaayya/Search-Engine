import os

# function that generates index by removing stop words
def generateStopIndex():
    fullPath = r'..\tokenized_Files'
    FilesName = os.listdir(os.path.abspath(fullPath))
    # create a list of stop words from the given input file
    stop_words = []
    for stopW in open(r'Input\common_words.txt'):
        stop_words.append(stopW.strip())
    termDoctf = {}
    docTf = {}
    totalCount = 0
    totalTermsInDoc = {}
    for file in FilesName:
        file = file.strip("\n")
        filename = fullPath + "\\" + file
        file_contents = open(filename, 'r', encoding='utf-8')
        tokens = eval(file_contents.read())
        file = file.replace(".txt", "")
        for t in tokens:
            if t not in stop_words:
                totalCount += 1
                if t not in termDoctf:
                    termDoctf[t] = {}
                    docTf[file] = 1
                    termDoctf[t][file] = docTf[file]
                elif termDoctf[t].get(file) == None:
                    termDoctf[t][file] = 1
                else:
                    termDoctf[t][file] += 1
        totalTermsInDoc[file] = totalCount
        totalCount = 0
    filename = "doc-termCount_stopped" + ".txt"
    newFile = open(filename, 'w', encoding='utf-8')
    newFile.write(str(totalTermsInDoc))
    newFile.close()
    filename = r"Invereted_Indexes\unigram_index_stopping.txt"
    newFile = open(filename, 'w', encoding='utf-8')
    newFile.write(str(termDoctf))
    newFile.close()


def generateStemmedIndex():
    fullPath = r'tokenized_Files_Stemmed'
    FilesName = os.listdir(os.path.abspath(fullPath))
    termDoctf = {}
    docTf = {}
    totalCount = 0
    totalTermsInDoc = {}
    for file in FilesName:
        file = file.strip("\n")
        filename = fullPath + "\\" + file
        file_contents = open(filename, 'r', encoding='utf-8')
        tokens = eval(file_contents.read())
        file = file.replace(".txt", "")
        for t in tokens:
            totalCount += 1
            if t not in termDoctf:
                termDoctf[t] = {}
                docTf[file] = 1
                termDoctf[t][file] = docTf[file]
            elif termDoctf[t].get(file) == None:
                termDoctf[t][file] = 1
            else:
                termDoctf[t][file] += 1
        totalTermsInDoc[file] = totalCount
        totalCount = 0
    filename = "doc-termCount_stemmed" + ".txt"
    newFile = open(filename, 'w', encoding='utf-8')
    newFile.write(str(totalTermsInDoc))
    newFile.close()
    filename = r"Invereted_Indexes\unigram_index_stemmed.txt"
    newFile = open(filename, 'w', encoding='utf-8')
    newFile.write(str(termDoctf))
    newFile.close()


if __name__ == "__main__":
    # fullPath = input("Enter the absolute path to the folder having tokenized files")
    # type(fullPath)
    # #D:\Search-Engine\tokenized_files
    # generateIndex(fullPath)# unigram

    generateStopIndex()
    generateStemmedIndex()
