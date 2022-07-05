import random

num=random.randrange(1,101)
a="bleh"
time=3
while(time!=0 and a!=num):
    time=str(time)
    print('You have '+time+' Chances')
    time=int(time)
    time=time-1
    a=input("Guess A Number Between 0-100")
    if not(a.isdigit()):
        print('Please Put a Number in!')
        a=input("Guess A Number Between 0-100")
    if a.isdigit():
        a=int(a)
        if a==num:
            print('You Got It!')
        elif a>num:
            print('Go Lower!')
        elif a<num:
            print('Go Higher!')