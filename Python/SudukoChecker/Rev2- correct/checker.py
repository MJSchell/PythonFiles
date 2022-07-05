from turtle import pu


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
def checkH(tocheck):
    for row in range(len(tocheck)):
        checkagainst=['1','2','3','4','5','6','7','8','9']
        for collumn in range(len(tocheck)):
            if tocheck[row][collumn] in checkagainst:
                checkagainst.remove(tocheck[row][collumn])
            else:
                print('Error at Row:',row+1)
                
def checkV(tocheck):
    tocheck=HtoV(tocheck)
    for row in range(len(tocheck)):
        checkagainst=['1','2','3','4','5','6','7','8','9']
        for collumn in range(len(tocheck)):
            if tocheck[row][collumn] in checkagainst:
                checkagainst.remove(tocheck[row][collumn])
            else:
                print('Error at Collumn:',collumn+1)

#opening and reading file into the Python file
correctlist=filetolist('PuzzleCorrect.txt')
section9issuelist=filetolist('Section9Issue.txt')
verticalissuelist=filetolist('VerticalIssue.txt')
horizontalissuelist=filetolist('HorizontalIssue.txt')

print('\n')
print('Horizontal Issue:\n')
checkH(horizontalissuelist)
checkV(horizontalissuelist)
print('\n')
print('Section 9 Issue:\n')
checkH(section9issuelist)
checkV(horizontalissuelist)
print('\n')
print('Vertical Issue:\n')
checkH(verticalissuelist)
checkV(horizontalissuelist)
print('\n')
print('Correct:\n')
checkH(correctlist)
checkV(horizontalissuelist)
print('\n')

'''
Horizontal Issue:


        Section 6
        (Horizontal) Row 5 (Vertical) Collumn 9


Section 9 Issue:


        Section 9
        (Horizontal) Row 7 (Vertical) Collumn 7

        Section 9
        (Horizontal) Row 7 (Vertical) Collumn 8

        Section 9
        (Horizontal) Row 7 (Vertical) Collumn 9

        Section 9
        (Horizontal) Row 8 (Vertical) Collumn 7


Vertical Issue:


        Section 2
        (Horizontal) Row 2 (Vertical) Collumn 4


Correct:

        No Issues
'''