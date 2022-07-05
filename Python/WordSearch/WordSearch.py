puzzlelist=[]
vertlist=[]
diagonallist=[]
wordlist=["BINARY","COMPUTERSCIENCE","DECIMAL","HEXADECIMAL","JUPYTER","MATPLOTLIB","NOTEBOOK","OCTAL","PANDAS","POWERSHELL"]
#Reading Board In
file=open("Book1.csv","r")                  #Put File Here (As CSV) <----------------------
z=file.read()
adminlist=z.splitlines()
file.close()

init(convert=True)
#Horizontal
for i in range(len(adminlist)):
    string=''
    for z in range(len(adminlist[i])):
        string+=adminlist[i][z]
    puzzlelist.append(string.replace(',',''))
    
#Vertical
for i in range(len(puzzlelist)):
    string=''
    for j in range(len(puzzlelist)):
        string+=puzzlelist[j][i]
    vertlist.append(string)
        
#print
def printpuzzle(puzzlelist):
    for i in range(len(puzzlelist)):
        for j in range(len(puzzlelist[i])):
            print(f"{puzzlelist[i][j]}",end=" ")
        print()
        
#Diagonal 1/2
for i in range(len(puzzlelist)):
    string=''
    for j in range(len(puzzlelist)):
        if i >=len(puzzlelist) or j >=(len(puzzlelist[i])):
            break
        string+=puzzlelist[i][j]
        i+=1
        j+=1
    diagonallist.append(string)
    
#Diagonal 2/2
for i in range(len(puzzlelist)):
    string=''
    for j in range(len(puzzlelist)):
        if i >=len(puzzlelist) or j >=(len(puzzlelist[i])):
            break
        string+=puzzlelist[j][i]
        i+=1
        j+=1
    diagonallist.append(string)

#Horizontal/VerticalCheck
def checklisty(listy):
    wordindexstart=[]
    rowindex=[]
    wordindexend=[]
    wordlisty=[]
    for word in wordlist:
        for row in listy:
            if word in row:
                rowindex.append(listy.index(row))
                wordindexstart.append(row.index(word)),
                wordindexend.append(len(word)+row.index(word))
                wordlisty.append(word)
            elif word[::-1] in row:
                rowindex.append(listy.index(row))
                wordindexstart.append(row.index(word[::-1])),
                wordindexend.append(len(word)+row.index(word[::-1]))
                wordlisty.append(word[::-1])
    dictionary={"word":wordlisty,"rowIndex": rowindex,"wordStartIndex":wordindexstart,"wordEndIndex":wordindexend}
    return(dictionary)

def diagonalcheck(listy):
    wordindexstart=[]
    rowindex=[]
    wordindexend=[]
    wordlisty=[]
    for word in wordlist:
        for row in listy:
            if word in row:
                rowindex.append(listy.index(row)+row.index(word))
                wordindexstart.append(row.index(word)),
                wordindexend.append(len(word)+row.index(word))
                wordlisty.append(word)
            elif word[::-1] in row:
                rowindex.append(listy.index(row)+row.index(word[::-1]))
                wordindexstart.append(row.index(word[::-1])),
                wordindexend.append(len(word)+row.index(word[::-1]))
                wordlisty.append(word[::-1])
    dictionary={"word":wordlisty,"rowIndex": rowindex,"wordStartIndex":wordindexstart,"wordEndIndex":wordindexend}
    return(dictionary)

#Check
diagonaldict=diagonalcheck(diagonallist)
horizontaldict=checklisty(puzzlelist)
verticaldict=checklisty(vertlist)

#Horizontal Check
for i in range(len(horizontaldict["word"])):
    word=horizontaldict["word"][i]
    rowindex=horizontaldict["rowIndex"][i]
    wordstartindex=horizontaldict["wordStartIndex"][i]
    wordendindex=horizontaldict["wordEndIndex"][i]
    supportstring=puzzlelist[rowindex].replace(word," "*len(word))
    puzzlelist[rowindex]=supportstring
    
#Vertical Check
for i in range(len(verticaldict["word"])):
    word=verticaldict["word"][i]
    for letter in range(len(word)):
        rowindex=verticaldict["wordStartIndex"][i]+letter
        wordstartindex=verticaldict["rowIndex"][i]
        supportstring=puzzlelist[rowindex][0:wordstartindex]+' '+puzzlelist[rowindex][wordstartindex+1:]
        puzzlelist[rowindex]=supportstring


#Diagonal Check
for i in range(len(diagonaldict["word"])):
    word=diagonaldict["word"][i]
    for letter in range(len(word)):
        rowindex=diagonaldict["rowIndex"][i]+letter
        if rowindex>15:
            rowindex=rowindex-15
        wordstartindex=diagonaldict["wordStartIndex"][i]+letter
        supportstring=puzzlelist[rowindex][0:wordstartindex]+' '+puzzlelist[rowindex][wordstartindex+1:]
        puzzlelist[rowindex]=supportstring
printpuzzle(puzzlelist)
