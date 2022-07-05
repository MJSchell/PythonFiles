import sys
from tkinter import *
import pandas

df=pandas.read_csv("atmData.csv")
root=Tk()
root.title("ATM")
root.geometry('1080x900')
windowheight=900
windowlength=1080









#GUI

#               Vars

#StringVars
sText1=StringVar()
sText2=StringVar()
sText3=StringVar()


#                            Button Frame
                            
buttonframe=Frame(root).grid(row=0,column=0)

j=2
#           Selection Buttons
for i in range(3):
    button=Tk.button=Button(buttonframe,command=lambda var=i+1:selection(var),text='⦿',width=5,height=2)
    button.grid(row=j,column=3)
    j+=2

blueBackground=Label(buttonframe,width=75,height=25,background="Blue",).grid(row=1,column=0,rowspan=8,columnspan=3)

sText2.set("Input Card Number")

# Labels in ATM
topLabel1=Label(buttonframe,textvariable=sText1,width=30,height=2,background="Blue").grid(row=2,column=2)
topLabel2=Label(buttonframe,textvariable=sText2,width=30,height=2,background="Blue").grid(row=4,column=2)
topLabel3=Label(buttonframe,textvariable=sText3,width=30,height=2,background="Blue").grid(row=6,column=2)

#                           Input Frame
inputframe=Frame(root).grid(row=9,column=0)

#           Number Buttons
j=9
k=0
# 1 - 9
for i in range(9):
    button=Tk.button=Button(inputframe,text=i+1,command=lambda var=str(i+1):textupdate(var),width=5,height=2,sticky=inputframe)
    button.grid(row=j,column=k)
    k+=1
    if k ==3:
        k=0
        j+=1
# X - Green
redButton=Button(inputframe,text='✖',command=lambda:textupdate("clear"),width=5,height=2,background='Red')
redButton.grid(row=12,column=0)
zeroButton=Button(inputframe,text='0',width=5,height=2,command=lambda:textupdate("0")).grid(row=12,column=1)
greenButton=Button(inputframe,text='■',command=lambda:donebutton(-1),width=5,height=2,background='Green')
greenButton.grid(row=12,column=2)

#                   -- Functions --

buttonswork=True
buttonselection=False
pinIndex=0
clearing=True
limit=0

def updatecsv():
    df.to_csv("./atmData.csv",mode='w')

#update input text for Pin Input
def textupdate(input):
    global buttonswork
    global clearing
    if buttonswork==True:
        sText3.set(sText3.get()+input)
        if input == "clear":
            sText3.set("")
        if "Pin" in sText2.get():
            if len(sText3.get())>4:
                sText3.set("")
        elif "Card" in sText2.get():
            if len(sText3.get())>16:
                sText3.set("")

chances=0

# done button
def donebutton(when):
    global buttonswork
    #Keypad input for Pin
    if buttonswork==True:
        global chances
        global buttonselection
        global pinIndex
        global limit
        torf=False
        amount=sText3.get()
        if when ==-1:
            for i in range(len(df["CreditCard"])):
                if amount == str(df["CreditCard"][i]):
                    torf=True
                    pinIndex=i
                    sText2.set("Input Pin Code")
                    sText3.set("")
                    chances=0
                    greenButton.configure(command=lambda:donebutton(0))
            if torf==False:
                chances+=1
            if chances==3:
                sys.exit()
        if when==0:
            if amount == str(df["Pin"][pinIndex]):
                torf=True
                buttonselection=True
                buttonswork=False
                sText1.set("Withdrawl")
                sText2.set("Deposit")
                sText3.set("Other")
                chances=0
            # Adds To Chances
            if torf==False:
                chances+=1
            if chances==3:
                sys.exit()
        if when==1:
            if int(amount)>500:
                sText2.set("Warning No Withdrawls Over $500")
            elif df["Checkings"][pinIndex] - int(amount)<10:
                sText2.set("Warning $10 required in account")
            elif int(amount)%5!=0:
                sText2.set("Warning $5 Denominations required")
            elif limit >=3:
                sText2.set("Reached Transcation Limit")
            else:
                sText1.set("$"+str(df["Checkings"][pinIndex] - int(amount)))
                df["Checkings"][pinIndex]=int(df["Checkings"][pinIndex])-int(amount)
                sText3.set("")
                limit +=1
                updatecsv()
        if when==2:
                if limit >=3:
                    sText2.set("Reached Transcation Limit")
                else:
                    sText1.set("$"+str(df["Checkings"][pinIndex] + int(amount)))
                    df["Checkings"][pinIndex]=int(df["Checkings"][pinIndex])+int(amount)
                    sText3.set("")
                    updatecsv()
                
        if when==3:
            sText3.set("")
            if len(amount)==4:
                df["Pin"][pinIndex]=str(amount)
                updatecsv()
                sys.exit()
            else:
                sText1.set("Pin Too Short")
selectionvar=0

#selection menu (withdraw deposit etc.)
def selection(stringvar):
    global clearing
    global buttonswork
    global buttonselection
    if buttonselection==True:
        global selectionvar
        if stringvar==1:
            text=sText1.get()
            if text=="Withdrawl":
                sText1.set("$"+str(df["Checkings"][pinIndex]))
                sText2.set("Input Withdrawl Amount")
                sText3.set("")
                buttonswork=True
                clearing = False
                greenButton.configure(command=lambda:donebutton(1))
            elif text=="Balance Inquiry":
                sText2.set("")
                sText3.set("$"+str(df["Checkings"][pinIndex]))
            else:
                sText1.set("")
                sText3.set("")
                sText2.set("Input New Pin")
                buttonswork=True
                clearing = True
                greenButton.configure(command=lambda:donebutton(3))
        elif stringvar==2:
            text=sText2.get()
            if text=="Deposit":
                text=sText1.get()
                sText1.set("$"+str(df["Checkings"][pinIndex]))
                sText2.set("Input Deposit Amount")
                sText3.set("")
                buttonswork=True
                clearing = False
                greenButton.configure(command=lambda:donebutton(2))
            elif text=="Transfer Balance":
                ''
            else:
                updatecsv()
                sys.exit()
        #Other button
        else:
            selectionvar+=1
            if selectionvar==3:
                selectionvar=0
            if selectionvar==0:
                sText1.set("Withdrawl")
                sText2.set("Deposit")
            if selectionvar==1:
                sText1.set("Balance Inquiry")
                sText2.set("Transfer Balance")
            if selectionvar==2:
                sText1.set("Change Pin")
                sText2.set("Log out")
            sText3.set("Other")

root.mainloop()