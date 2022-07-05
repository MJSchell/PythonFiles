from tkinter import *
from tkinter.tix import COLUMN

root=Tk()
root.title("Converter")
root.geometry('200x225')

def anybasetodec(ui,base):
    listy="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    highestexp=len(ui)-1
    decimal=0
    for n in ui:
        numba = listy.index(n)
        decimal+=(numba*base**highestexp)
        highestexp-=1
    return decimal

def dectobin(decimal):
    decimal+=1
    exponent=0
    i=0
    binary=''
    while decimal>exponent:
        i+=1
        exponent=2**i
    while i>=0:
        if decimal-2**i>0:
            binary+='1'
            decimal-=2**i
        else:
            binary+='0'
        i-=1
    return binary

def dectooct(decimal):
    octo=''
    quotient=decimal
    while quotient>0:
        remainder=quotient%8
        quotient=quotient//8
        octo+=str(remainder)
    return octo[::-1]

def dectohex(decimal):
    listy="0123456789ABCDEF"
    hexa=''
    quotient=decimal
    while quotient>0:
        remainder=quotient%16
        quotient=quotient//16
        remainder=listy[remainder]
        hexa+=str(remainder)
    return hexa[::-1]

def convert():
    try:
        number=numberEntry.get()
        base=int(baseEntry.get())
        decimal=anybasetodec(number,base)
        binary=dectobin(decimal)
        octo=dectooct(decimal)
        hexa=dectohex(decimal)
        outputtext.set(f'''
        Binary: {binary}
        Oct: {octo}
        Decimal: {decimal}
        Hex: {hexa}''')
    except:
        outputtext.set('ERROR')

def check():
    correct=True
    number=numberEntry.get()
    base=baseEntry.get()
    if not(base.isdigit()):
        outputtext.set('ERROR')
        correct=False
    elif base=='2':
        for i in range(2,10):
            if str(i) in str(number):
                outputtext.set('ERROR')
                correct=False
    elif base=='8':
        for i in range(8,10):
            if str(i) in str(number):
                outputtext.set('ERROR')
                correct=False
    if correct==True:
        convert()
    
def clear():
    outputtext.set('')
    numberEntry.delete(0,'end')
    baseEntry.delete(0,'end') 
    
outputtext=StringVar()
outputtext.set('')

NumberLBL=Label(root,text='Number')
NumberLBL.pack()

numberEntry=Entry(root,text='')  
numberEntry.pack()

BaseLBL=Label(root,text='Base')
BaseLBL.pack()

baseEntry=Entry(root,text='')  
baseEntry.pack()

outputLBL=Label(root,textvariable=outputtext)
outputLBL.pack()

outBTN=Button(root,text='Done',command=check)
outBTN.pack()

clearBTN=Button(root,text='Clear',command=clear)
clearBTN.pack()

root.mainloop()