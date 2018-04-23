from urllib.request import urlopen
import bs4 as bsnew
import re
import time
import collections


def bfsIterative(seed,maxLevel):
    visited=collections.deque()
    queue=collections.deque([seed])
    depth=1
    titleVisited=[]
    while queue and len(visited)<1000:
        seed=queue.popleft()
        if seed is None:#delimiter is used to keep track of the depth in BFS
            depth=depth+1
            continue
        if seed in visited:
            continue
        visited.append(seed)
        html = urlopen(seed)
        bs = bsnew.BeautifulSoup(html, "html.parser")
        title=bs.title.string
        if title in titleVisited:#To handle redirects
            visited.pop()
            continue
        titleVisited.append(title)
        content = bs.find("div", {"id": "mw-content-text"})
        urlindex=seed.index('wiki/')
        fileName=seed[urlindex+5:]#The filename just contains the last part of the url for easy access
        if '/' in fileName:
            visited.pop()
            continue
        fullPath = r"bfsFiles/%s.html" % fileName
        with open(fullPath, "w",encoding='utf-8') as file:#Saving the html in different files.
            file.write(str(content))
        listOfLinks=[]
        for link in content.findAll("a", href=re.compile("(^/wiki/)")):
                tempLink=link.get('href')
                if '#' in tempLink:
                    indexOf = tempLink.index('#')
                    tempLink=tempLink[:indexOf]
                    listOfLinks.append("https://en.wikipedia.org"+tempLink)
                elif ':' not in tempLink:
                    listOfLinks.append("https://en.wikipedia.org"+tempLink)
        if depth<maxLevel:
            queue.extend(listOfLinks)
            queue.append(None)

        #time.sleep(1)#Politeness policy.One second wait between requests
    bfsFile = open('bfs.txt', 'w',encoding='utf-8')
    for link in visited:
        bfsFile.write(link + '\n')
    bfsFile.write("The final depth reached in BFS is:::::" + str(depth) + '\n')
    bfsFile.close()
    return


if __name__== "__main__":
        seed = "https://en.wikipedia.org/wiki/Solar_eclipse"
        level=6
        bfsIterative(seed,level)
