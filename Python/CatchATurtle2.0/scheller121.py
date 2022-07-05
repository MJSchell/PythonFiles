#-----Import Statements-----


import turtle as t
import random as r
import time
import datetime


#-----Game Configuration-----


active=False
sc=0
c=0
tsize=20
score=0
SCREENW,SCREENH=300,300
wn=t.Screen()
#tuple vairable = 'Fontstyle',fontsize,'font (B,I,U)'
fontsetup=('Arial',20,'bold')


#-----initialize turtle-----


mole=t.Turtle(shape='circle',)
mole.penup()
mole.speed(5)
mole.shapesize(20)
mole.fillcolor('yellow')
mole.hideturtle()

ref=t.Turtle()
ref.penup()
ref.hideturtle()
ref.speed(0)
ref.goto(225,275)

accuracy=t.Turtle()
accuracy.penup()
accuracy.hideturtle()
accuracy.speed(0)
accuracy.goto(225,250)

start=t.Turtle(shape='square')
start.shapesize(1)
start.penup()
start.speed(0)
start.goto(0,0)
start.write('Press Square to start')
start.goto(0,50)

timerw=t.Turtle()
timerw.penup()
timerw.hideturtle()
timerw.speed(0)
timerw.goto(225,225)


#-----Game Function-----


#no matter what, if it is a mouse click
#pass in x and y
def click(x,y):
    global c
    c+=1
    #x and y are the cursor's cordinates
    changeposition()
    updatescore()
    
#move turtle to a random loction on the screen
def changeposition():
    global tsize
    wn.bgcolor('red')
    mole.fillcolor('red')
    mole.stamp()
    mole.hideturtle()
    tsize=tsize-tsize*.5
    if tsize<1:
        tsize=20
    mole.shapesize(tsize)
    mole.goto(r.randint(-SCREENW,SCREENW),r.randint(-SCREENH,SCREENH))
    mole.fillcolor('yellow')
    mole.showturtle()
    wn.bgcolor('white')
    
def updatescore():
    global score
    #it will see the variable score in other parts of the program
    score+=1
    ref.clear()
    accuracy.clear()
    ref.write('Score: '+str(score),font=fontsetup)
    if sc>0:
        accuracy.write('Accuracy: '+str(c/sc),font=fontsetup)

def screenclick(x,y):
    global sc
    sc+=1

def starts(x,y):
    start.hideturtle()
    mole.showturtle()
    starttimer()
    global active
    active=True
    
def starttimer():
    total_seconds=60
    while total_seconds > 0:
        time.sleep(1)
        total_seconds-=1
        timerw.clear()
        timerw.write('Time: '+str(total_seconds),font=fontsetup)
    if total_seconds<=0:
        active=False
        mole.hideturtle()
        
        
#-----Events-----

wn.onscreenclick(screenclick)
#obj.method(command or function)
start.onclick(starts)
mole.onclick(click)
#wn.onscreenclick(click)
wn.mainloop()

'''
--Incorporate a Countdown timer, that when it goes off, the game will stop.

--Every time the turtle moves, change the Screen background to red and then back to white.

--When you click the turtle leave a red outline of where the turtle was.

--Each time you click the turtle, shrink the turtle by 50% until it is at a certain size then reset the size.

--Create a start game function that forces the user to press start which will trigger the countdown and the ability to click on the turtle.

--Keep track of the accuracy of clicking.  You can display the score and the accuracy right below the score.  Accuracy is defined by the turtle clicks vs amount of clicks.

'''