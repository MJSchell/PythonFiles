import glob
from string import punctuation
'''
books=(glob.glob("data/*.txt")) #* stands for wildcard (placeholder)
'''

numberlist=[]
for i in range(0,1000):
    numberlist.append(str(i))
books=(glob.glob("Data/*.txt"))

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
    number=0
    for line in file:
        if "Page" in line:
                string=''
                for c in line:
                    if c.isdigit() :
                        string+=c
                line=string
                rfile.append(line)
        else:
            rfile.append(line)
    return rfile

def write(path,rfile):
    with open('Page/Page'+path,'w+',encoding='utf8') as f:
        for line in rfile:
            f.writelines(line)

for b in booklist:
    openfile(b)
            
'''
Pages=0
Harry=0
Ron=0
Dumbledore=0
Hagrid=0
Hermione=0
Draco=0
Name=0
Voldemort=0
for b in booklist:
    file=openfile(b)
    file=file.splitlines()
    
    for i in range(len(file)):
        if 'Page' in file[i]:
            Pages+=1
        if 'Harry'in file[i] or 'Potter'in file[i] or 'harry'in file[i] or 'potter' in file[i]:
            Harry+=1
        if 'Ron'in file[i] or 'ron'in file[i]or'weasley'in file[i]or'Weasley' in file[i]:
            Ron+=1
        if 'Albus'in file[i]or'albus'in file[i]or'Dumbledore'in file[i]or'dumbledore' in file[i]:
            Dumbledore+=1
        if 'Hermione'in file[i]or'hermione'in file[i]or'Granger'in file[i]or'granger' in file[i]:
            Hermione+=1
        if 'Draco'in file[i]or'draco'in file[i]or'Malfoy'in file[i]or'malfoy'in file[i]:
            Draco+=1
        if "Voldemort"in file[i]or'voldemort' in file[i]:
            Voldemort+=1
        if 'Hagrid'in file[i]or'hagrid' in file[i]:
            Hagrid+=1
        if "He Who Must Not Be Named" in file[i] or "he who must not be named"in file[i]:
            Name+=1
print(f"""
    Pages: {Pages}
    Harry: {Harry}
    Ron: {Ron}
    Dumbledore: {Dumbledore}
    Hagrid: {Hagrid}
    Hermione: {Hermione}
    Draco: {Draco}
    Name: {Name}
    Voldemort: {Voldemort}""")
'''
'''
threew=0
fivew=0
sevenw=0
ninew=0
elevenplusw=0
punctuationlist=[',','.','?','!','$','&','`','"',"'",'”','’','-','|','“',':']
for b in booklist:
    file=openfile(b)
    for i in range(len(file)):
        string=str(file[i])
        string=re.split('\s+',string)
        for z in range(len(string)):
            for y in range(len(punctuationlist)):
                string[z]=string[z].replace(punctuationlist[y],'')
            if len(string)==3:
                threew+=1
            if len(string)==5:
                fivew+=1
            if len(string)==7:
                sevenw+=1
            if len(string)==9:
                ninew+=1
            if len(string)>=11:
                elevenplusw+=1
''''''
total=(elevenplusw+ninew+sevenw+fivew+threew)
print(f"""
      3: {threew}
      5: {fivew}
      7: {sevenw}
      9: {ninew}
      11+: {elevenplusw}
      total: {total}""")           
'''
'''
total=0
for b in booklist:
    file=openfile(b)
    for i in range(len(file)):
        string=str(file[i])
        string=re.split('\s+',string)
        for z in range(len(string)):
            string2=string[z]
            total+=len(string2)
print(total)
'''
