import random
listy=[]
a=0
def rdm(listy):
    i=0
    amntN=int(input('Amount of Numbers?'))
    s=int(input('Smallest Number?'))
    b=int(input('Biggest Number?'))
    while i<amntN:
        listy.append(random.randint(s,b))
        i+=1
    print(listy)
    return listy

def avg(listy):
    a=sum(listy)/len(listy)
    print(a)
    return(a)

def range(listy):
    rw

def isPrime():

rdm(listy)
#avg(listy)
#range(listy)