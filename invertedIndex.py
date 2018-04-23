import os
def generateIndex(fullPath):
    FilesName = os.listdir(os.path.abspath(fullPath))
    termDoctf = {}
    docTf={}
    totalCount=0
    totalTermsInDoc={}
    for file in FilesName:
        file = file.strip("\n")
        filename = fullPath + "\\"+file
        file_contents = open(filename, 'r', encoding='utf-8')
        tokens = eval(file_contents.read())
        file=file.replace(".txt","")
        for t in tokens:
            totalCount+=1
            if t not in termDoctf:
                termDoctf[t]={}
                docTf[file]=1
                termDoctf[t][file] = docTf[file]
            elif termDoctf[t].get(file) == None:
                termDoctf[t][file] = 1
            else:
                termDoctf[t][file] += 1
        totalTermsInDoc[file] = totalCount
        totalCount=0
    filename = "doc-termCount" + ".txt"
    newFile = open(filename, 'w', encoding='utf-8')
    newFile.write(str(totalTermsInDoc))
    newFile.close()
    filename="unigram_index.txt"
    newFile = open(filename, 'w', encoding='utf-8')
    newFile.write(str(termDoctf))
    newFile.close()


if __name__ == "__main__":
    fullPath = input("Enter the absolute path to the folder having tokenized files")
    type(fullPath)
    #D:\Search-Engine\tokenized_files
    generateIndex(fullPath)# unigram
