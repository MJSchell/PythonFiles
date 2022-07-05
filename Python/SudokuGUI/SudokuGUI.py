import random
from tkinter import *
from Class import *

#http://lipas.uwasa.fi/~timan/sudoku/

listOfButtons=[]
listofnumbers=[]
TextList=['-','1','2','3','4','5','6','7','8','9']
ToCheck=[]
rows=0
columns=0
index=0
text=StringVar

root=Tk()
root.title("Sudoku")
root.geometry('500x700')

buttonframe=Frame(root).grid(row=0,column=0)

def Done():
    rows=0
    multiplyby=0
    string=''
    while rows != 9:
        for i in range(9):
            i+=multiplyby
            string+=listofnumbers[i]
        ToCheck.append(string)
        string=''
        multiplyby+=9
        rows+=1
    wrong=Checker.checkthisout(ToCheck,c)
    string=''
    for i in range(len(wrong)):
        string+=wrong[i]
    print(string)

def switchtext(index,textnumber):
    if textnumber <8:
        textnumber+=1
    else:
        textnumber=0
    listofnumbers[index]=TextList[textnumber]
    listOfButtons[index].configure(text=TextList[textnumber],command=lambda:switchtext(index,textnumber))

cp1=['832456791','957182463','416973258','679541832','523768149','184329576','761834925','295617384','348295617']
cp2=['845632179','732918654','196745328','683574912','457291836','219863547','361429785','574186293','928357461']
cp3=['832456791','957182463','416973258','679541832','523768149','184329576','761834925','295617384','348295617']

p3=['040000179','002008054','006005008','080070910','050090030','019060040','300400700','570100200','928000060']
p2=['802050701','007082460','010900000','600001832','500000009','184300006','000004020','095610300','308090607']
p1=['000000007','720309001','008705060','502890000','040501090','000063705','030906100','200107053','900000000']

listy=[p1,p2,p3]
while rows !=9:
    for i in range(9):
        button=Tk.button=Button(buttonframe,text=TextList[0],command=lambda index=index:switchtext(index,0),width=5,height=3)
        button.grid(row=rows,column=columns,padx=1,pady=1)
        listOfButtons.append(button)
        listofnumbers.append(TextList[0])
        columns+=1
        index+=1
    listofnumbers.append(TextList[0])
    columns=0
    rows+=1

rows=0
columns=0
multiplyby=0
p=random.choice(listy)
if p==p3:
    c=cp3
elif p==p2:
    c=cp2
else:
    c=cp1
while rows!=9:
    for i in range(9):
        i+=multiplyby
        stringtouse=p[rows][columns]
        if not(stringtouse=='0'):
            listOfButtons[i].configure(text=stringtouse,command='Nothing')
            listofnumbers[i]=stringtouse
        columns+=1
    multiplyby+=9
    columns=0
    rows+=1


Donebutton=Button(buttonframe,text='Done',width=50,height=3,command=Done).grid(row=10,column=0,columnspan=25)
Textlabel=Label(buttonframe,text=text).grid(row=1,column=0,columnspan=25)
    
root.mainloop()