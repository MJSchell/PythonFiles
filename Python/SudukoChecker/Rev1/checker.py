
def filetolist(filein):
    file=open(filein,"r")
    I=file.read()
    file.close()
    filelist=I.splitlines()
    return filelist



#turning horizontal to vertical -- Uneeded
def HtoV(file):
    z=0
    fileout=[]
    for i in range(len(file)):
        string=''
        for i in range(len(file)):
            string+=file[i][z]
        z+=1
        fileout.append(string)
    return fileout



#checking function
def checkthisout(tocheckfileH,horizontalcorrect):
    z=0
    wrong=[]
    section=0
    for i in range(len(horizontalcorrect)):
        for z in range(len(horizontalcorrect)):
            if z in range(0,3) and i in range(0,3):
                section=1
            if z in range(3,6) and i in range(0,3):
                section=2
            if z in range(6,9) and i in range(0,3):
                section=3
            if z in range(0,3) and i in range(3,6):
                section=4
            if z in range(3,6) and i in range(3,6):
                section=5
            if z in range(6,9) and i in range(3,6):
                section=6
            if z in range(0,3) and i in range(6,9):
                section=7
            if z in range(3,6) and i in range(6,9):
                section=8
            if z in range(6,9) and i in range(6,9):
                section=9
            if not(tocheckfileH[i][z]==horizontalcorrect[i][z]):
                string='\n\tSection '+str(section)+'\n\t(Horizontal) Row '+str(i+1)+' (Vertical) Collumn '+str(z+1)
                wrong.append(string)
    if len(wrong)<1:
        print('\tNo Issues')
    else:
        for i in range(len(wrong)):
            print(wrong[i])

#opening and reading file into the Python file
correctlist=filetolist('PuzzleCorrect.txt')
section9issuelist=filetolist('Section9Issue.txt')
verticalissuelist=filetolist('VerticalIssue.txt')
horizontalissuelist=filetolist('HorizontalIssue.txt')

print('\n')
print('Horizontal Issue:\n')
checkthisout(horizontalissuelist,correctlist)
print('\n')
print('Section 9 Issue:\n')
checkthisout(section9issuelist,correctlist)
print('\n')
print('Vertical Issue:\n')
checkthisout(verticalissuelist,correctlist)
print('\n')
print('Correct:\n')
checkthisout(correctlist,correctlist)
print('\n')