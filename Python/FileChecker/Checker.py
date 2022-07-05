import os
#https://careerkarma.com/blog/python-list-files-in-directory/
#https://stackoverflow.com/questions/52419117/not-able-to-read-file-due-to-unicode-error-in-python

#C:\Users\Mason\Documents\textbasedboardgame-schellerhorstman
#C:\Users\Mason\Documents\textbasedboardgame

listoffiles1=[]
listoffiles2=[]
listofdirectory1=[]
listofdirectory2=[]
listofdifferances=[]


#input for file in directory
print('\t‎ Refers to a blank line')         #https://www.fileformat.info/info/unicode/char/200e/index.htm U+200E is a semi-blank character
path1=input('Path to Directory 1:\n')
path2=input('Path to Directory 2:\n')
for root, directories, files in os.walk(path1,topdown=False):   #help from #https://careerkarma.com/blog/python-list-files-in-directory/
    for name in files:
        listoffiles1.append((os.path.join(root,name)))
        listofdirectory1.append(os.path.join(root,name))
    for name in directories:
        listofdirectory1.append((os.path.join(root,name)))

for root, directories, files in os.walk(path2,topdown=False):
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



#prints what is different about each file
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
print('\nFiles in Repo 2:\n')
for i in range(len(listofdirectory2)):
    print(listofdirectory2[i])