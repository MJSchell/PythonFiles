import glob
'''
#realtive file path -> path from your file to another file
with open("Data/Book 1.txt","r",encoding="utf8")as f:
    file=f.readlines()


rfile=[]
for line in file:
    if line !="\n":
        rfile.append(line)
with open('Out/Book1Reduced.txt','w+',encoding='utf8') as f:
    for line in rfile:
        f.writelines(line)
'''


books=(glob.glob("data/*.txt")) #* stands for wildcard (placeholder)


booklist=[]
for b in books:
    booklist.append(b[5:])
    
#realtive file path -> path from your file to another file
def openfile(path):
    with open("Data/"+path,"r",encoding="utf8")as f:
        file=f.readlines()
    rfile=makerfile(file)
    write(path,rfile)

def makerfile(file):
    rfile=[]
    for line in file:
        if line !="\n":
            rfile.append(line)
    return rfile

def write(path,rfile):
    with open('Out/Reduced'+path,'w+',encoding='utf8') as f:
        for line in rfile:
            f.writelines(line)

for book in booklist:
    openfile(book)