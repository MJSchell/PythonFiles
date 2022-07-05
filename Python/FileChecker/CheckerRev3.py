import os
#https://careerkarma.com/blog/python-list-files-in-directory/
#https://stackoverflow.com/questions/52419117/not-able-to-read-file-due-to-unicode-error-in-python
#https://docs.python.org/3/library/os.path.html
#https://www.w3schools.com/python/python_try_except.asp

listoffiles1=[]
listoffiles2=[]
listofdirectory1=[]
listofdirectory2=[]
listofdifferances=[]
fileexplorerlist=[]
selectlist=['Select','select','SELECT']
clearlist=['Clear','CLEAR','clear']
exploring=True
Pass=0
diddo=True
path1=''
path2=''
tolistdirectory=[]

#file explorer
while exploring==True:
    for i in range(len(tolistdirectory)):
        print(tolistdirectory[i])
    print(fileexplorerlist)
    pathinput=input('\nChoose directory 1 (if Starting its Usually C:)\nNo Need for Slashes\n\nCommands:\n\t .. : go back a file in the directory\n\t Clear : Start from the begining\n\t Select : Select the current point as your directory for use\n')
    diddo=True
    correct=False
    if Pass==0:
        pathinput+='\\'
        for i in range(len(selectlist)):
            if selectlist[i] in pathinput:
                for i in range(len(fileexplorerlist)):
                    path1+=str(fileexplorerlist[i])
                exploring=False
                fileexplorerlist=[]
                correct=True
            elif clearlist[i] in pathinput:
                fileexplorerlist=[]
                tolistdirectory=''
                Pass=0
                diddo=False
                correct=True
        if os.path.isdir(pathinput) and correct==False:
            try:
                stringtoappend=pathinput
                fileexplorerlist.append(stringtoappend)
                tolistdirectory=os.listdir(pathinput)
                print('\n')
                correct=True
            except:
                print('\t\t\t\t\t\t\t\t\t\tSorry Not A Valid Path or Command in os')
                correct=True
                fileexplorerlist.remove(stringtoappend)
                tosearch=''
                for i in range(len(fileexplorerlist)):
                    tosearch+=str(fileexplorerlist[i])
        elif correct==False:
            print('\t\t\t\t\t\t\t\t\t\tSorry Not A Valid Path or Command')
    else:
        tosearch=''
        for i in range(len(fileexplorerlist)):
            tosearch+=str(fileexplorerlist[i])
        if pathinput=='..':
            fileexplorerlist.remove(stringtoappend)
            tosearch=''
            for i in range(len(fileexplorerlist)):
                tosearch+=str(fileexplorerlist[i])
            correct=True
            if len(fileexplorerlist)==0:
                fileexplorerlist=[]
                tolistdirectory=''
                diddo=False
            else:
                tolistdirectory=os.listdir(tosearch)
        for i in range(len(selectlist)):
            if selectlist[i] in pathinput:
                for i in range(len(fileexplorerlist)):
                    path1+=str(fileexplorerlist[i])
                exploring=False
                fileexplorerlist=[]
                correct=True
            elif clearlist[i] in pathinput:
                fileexplorerlist=[]
                tolistdirectory=''
                Pass=0
                diddo=False
                correct=True
        if os.path.isdir(tosearch) and correct==False:
            try:
                stringtoappend=pathinput+'\\'
                fileexplorerlist.append(stringtoappend)
                tosearch=''
                for i in range(len(fileexplorerlist)):
                    tosearch+=str(fileexplorerlist[i])
                tolistdirectory=os.listdir(tosearch)
                print('\n')
                correct=True
                print(tosearch)
            except:
                print('\t\t\t\t\t\t\t\t\t\tSorry Not A Valid Path or Command in os')
                correct=True
                fileexplorerlist.remove(stringtoappend)
                tosearch=''
                for i in range(len(fileexplorerlist)):
                    tosearch+=str(fileexplorerlist[i])
        elif correct==False:
            print('\t\t\t\t\t\t\t\t\t\tSorry Not A Valid Path or Command')
    if diddo==True:
        Pass+=1

exploring=True
Pass=0
tolistdirectory=[]

while exploring==True:
    for i in range(len(tolistdirectory)):
        print(tolistdirectory[i])
    print(fileexplorerlist)
    pathinput=input('\nChoose directory 2 (if Starting its Usually C:)\nNo Need for Slashes\n\nCommands:\n\t .. : go back a file in the directory\n\t Clear : Start from the begining\n\t Select : Select the current point as your directory for use\n')
    diddo=True
    correct=False
    if Pass==0:
        pathinput+='\\'
        for i in range(len(selectlist)):
            if selectlist[i] in pathinput:
                for i in range(len(fileexplorerlist)):
                    path2+=str(fileexplorerlist[i])
                exploring=False
                fileexplorerlist=[]
                correct=True
            elif clearlist[i] in pathinput:
                fileexplorerlist=[]
                tolistdirectory=''
                Pass=0
                diddo=False
                correct=True
        if os.path.isdir(pathinput) and correct==False:
            try:
                stringtoappend=pathinput
                fileexplorerlist.append(stringtoappend)
                tolistdirectory=os.listdir(pathinput)
                print('\n')
                correct=True
            except:
                print('\t\t\t\t\t\t\t\t\t\tSorry Not A Valid Path or Command in os')
                correct=True
                fileexplorerlist.remove(stringtoappend)
                tosearch=''
                for i in range(len(fileexplorerlist)):
                    tosearch+=str(fileexplorerlist[i])
        elif correct==False:
            print('\t\t\t\t\t\t\t\t\t\tSorry Not A Valid Path or Command')
    else:
        tosearch=''
        for i in range(len(fileexplorerlist)):
            tosearch+=str(fileexplorerlist[i])
        if pathinput=='..':
            fileexplorerlist.remove(stringtoappend)
            tosearch=''
            for i in range(len(fileexplorerlist)):
                tosearch+=str(fileexplorerlist[i])
            correct=True
            if len(fileexplorerlist)==0:
                fileexplorerlist=[]
                tolistdirectory=''
                diddo=False
            else:
                tolistdirectory=os.listdir(tosearch)
        for i in range(len(selectlist)):
            if selectlist[i] in pathinput:
                for i in range(len(fileexplorerlist)):
                    path2+=str(fileexplorerlist[i])
                exploring=False
                fileexplorerlist=[]
                correct=True
            elif clearlist[i] in pathinput:
                fileexplorerlist=[]
                tolistdirectory=''
                Pass=0
                diddo=False
                correct=True
        if os.path.isdir(tosearch) and correct==False:
            try:
                stringtoappend=pathinput+'\\'
                fileexplorerlist.append(stringtoappend)
                tosearch=''
                for i in range(len(fileexplorerlist)):
                    tosearch+=str(fileexplorerlist[i])
                tolistdirectory=os.listdir(tosearch)
                print('\n')
                correct=True
                print(tosearch)
            except:
                print('\t\t\t\t\t\t\t\t\t\tSorry Not A Valid Path or Command in os')
                correct=True
                fileexplorerlist.remove(stringtoappend)
                tosearch=''
                for i in range(len(fileexplorerlist)):
                    tosearch+=str(fileexplorerlist[i])
        elif correct==False:
            print('\t\t\t\t\t\t\t\t\t\tSorry Not A Valid Path or Command')
    if diddo==True:
        Pass+=1


#input for file in directory
print('\t‎ Refers to a blank line')         #https://www.fileformat.info/info/unicode/char/200e/index.htm U+200E is a semi-blank character
for root, directories, files in os.walk(path1,topdown=True):   #help from #https://careerkarma.com/blog/python-list-files-in-directory/
    for name in files:
        listoffiles1.append((os.path.join(root,name)))
        listofdirectory1.append(os.path.join(root,name))
    for name in directories:
        listofdirectory1.append((os.path.join(root,name)))

for root, directories, files in os.walk(path2,topdown=True):
    for name in files:
        listoffiles2.append((os.path.join(root,name)))
        listofdirectory2.append(os.path.join(root,name))
    for name in directories:
        listofdirectory2.append((os.path.join(root,name)))



#opens files and saves to lists         #Used from advent of Code project
def fileopen(file1in,file2in):
    file=open(file1in,"r",encoding='charmap')   #For UnicodeDecodeError use encoding=''
    I=file.read()
    file.close()
    filelist1=I.splitlines()
    file=open(file2in,"r",encoding='charmap')
    I=file.read()
    file.close()
    filelist2=I.splitlines()
    checkfordifference(filelist1,filelist2,file1in,file2in)



#checks for which list is longer
def checkfordifference(filelist1,filelist2,file1in,file2in):
    difference=int(abs(len(filelist1)-len(filelist2)))
    if difference!=0:
        if len(filelist1)>len(filelist2):
            for i in range(difference):
                filelist2.append('‎')
        else:
            for i in range(difference):
                filelist1.append('‎')
    printing(difference,filelist1,filelist2,file1in,file2in)



#what is different about each file
def printing(difference,filelist1,filelist2,file1in,file2in):
    global listofdifferances
    #print(file1in+'\n&\n'+file2in+' have a ',difference,'line difference')
    for i in range(len(filelist1)):
        if not(filelist1[i] in filelist2[i]):
            listofdifferances.append(file1in+'\n line:'+str(i)+"\t"+filelist1[i]+'\n'+file2in+'\n line:'+str(i)+"\t"+filelist2[i])


#each file in directory compared to other file
differenceoffiles=abs(len(listoffiles1)-len(listoffiles2))
if len(listoffiles1)>len(listoffiles2):
    amountoffiles=len(listoffiles2)
else:
    amountoffiles=len(listoffiles1)
for i in range(amountoffiles):
        fileopen(listoffiles1[i],listoffiles2[i])
for i in range(len(listofdifferances)):
    print(listofdifferances[i]+'\n\n')
print('Files in Repo 1:\n')
for i in range(len(listofdirectory1)):
    print(listofdirectory1[i])
print('Files in Repo 2:\n')
for i in range(len(listofdirectory2)):
    print(listofdirectory2[i])