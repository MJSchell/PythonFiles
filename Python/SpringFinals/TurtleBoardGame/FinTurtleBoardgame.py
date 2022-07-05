import turtle as t
import random
SCREENW,SCREENH=300,300
wn=t.Screen()

# -- Variables --

Turn=1




listofturtles=[]
fontsetup=('Arial',20)
row1=[]
row2=[]
row3=[]
row4=[]
row5=[]
row6=[]
row7=[]
listofrows=[row1,row2,row3,row4,row5,row6,row7]
numbersrow1=[]
numbersrow2=[]
numbersrow3=[]
numbersrow4=[]
numbersrow5=[]
numbersrow6=[]
numbersrow7=[]
numberlistofrows=[numbersrow1,numbersrow2,numbersrow3,numbersrow4,numbersrow5,numbersrow6,numbersrow7]
gamemode=False
# -- Pre-Functions --

def cpu(x,y):
    global Turn
    global listoffunctions
    global gamemode
    if gamemode=="pvc":
        if Turn%2==0:
            function=random.choice(listoffunctions)
            if function == greenfun0 and numberlistofrows[0][0]==0:
                function(x,y)
            elif function == greenfun1 and numberlistofrows[1][0]==0:
                function(x,y)
            elif function == greenfun2 and numberlistofrows[2][0]==0:
                function(x,y)
            elif function == greenfun3 and numberlistofrows[3][0]==0:
                function(x,y)
            elif function == greenfun4 and numberlistofrows[4][0]==0:
                function(x,y)
            elif function == greenfun5 and numberlistofrows[5][0]==0:
                function(x,y)
            elif function == greenfun6 and numberlistofrows[6][0]==0:
                function(x,y)
            else:
                cpu(x,y)
        

def checkForWinner(sym):#see if anyone has won
    x,y=0,0
    global winner
    global numberlistofrows
    global gamemode
    #check for horizontal wins
    for row in numberlistofrows:
        for i in range(0,len(row)):
            if i < len(row)-3:
                if row[i] == row[i+1] == row[i+2] == row[i+3] == sym:
                    gamemode=False
                    drawmainmenu(x,y)
                    arty.goto(-120,-150)
                    arty.pencolor("black")
                    arty.write(f"The Winner is: {winner}",font=fontsetup)
    #check for vertical wins
    for row in range(7-3):
        for i in range(6):
            if numberlistofrows[row][i] == numberlistofrows[row+1][i] == numberlistofrows[row+2][i] == numberlistofrows[row+3][i] ==sym:
                gamemode=False
                drawmainmenu(x,y)
                arty.goto(-120,-150)
                arty.pencolor("black")
                arty.write(f"The Winner is: {winner}",font=fontsetup)
    #check for ascending diagonals wins
    for row in range(7):
        for col in range(6-3):
            if numberlistofrows[row][col] == numberlistofrows[abs(row-1)][abs(col+1)] == numberlistofrows[abs(row-2)][abs(col+2)] == numberlistofrows[abs(row-3)][abs(col+3)] ==sym:
                gamemode=False
                drawmainmenu(x,y)
                arty.goto(-120,-150)
                arty.pencolor("black")
                arty.write(f"The Winner is: {winner}",font=fontsetup)
    #check for descending diagonal wins
    for row in range(7):
        for col in range(6):
            if numberlistofrows[row][col] == numberlistofrows[abs(row-1)][abs(col-1)] == numberlistofrows[abs(row-2)][abs(col-2)] == numberlistofrows[abs(row-3)][abs(col-3)] ==sym:
                gamemode=False
                drawmainmenu(x,y)
                arty.goto(-120,-150)
                arty.pencolor("black")
                arty.write(f"The Winner is: {winner}",font=fontsetup)
                
    
winner=""


a=6
def greenfun0(x,y):
    global winner
    global Turn
    global a
    global gamemode
    if Turn%2:
        if numberlistofrows[0][a-1]==0:
            listofrows[0][a].color("Red")
            numberlistofrows[0][a-1]=1
            winner="RED"
    else:
        if numberlistofrows[0][a-1]==0:
            listofrows[0][a].color("Blue")
            numberlistofrows[0][a-1]=2
            winner="BLUE"
    a-=1
    Turn+=1
    checkForWinner(1)
    checkForWinner(2)
    if gamemode=="pvc":
        cpu(x,y)
b=6    
def greenfun1(x,y):
    global winner
    global Turn
    global b
    global gamemode
    if Turn%2:
        if numberlistofrows[1][b-1]==0:
            listofrows[1][b].color("Red")
            numberlistofrows[1][b-1]=1
            winner="RED"
    else:
        if numberlistofrows[1][b-1]==0:
            listofrows[1][b].color("Blue")
            numberlistofrows[1][b-1]=2
            winner="BLUE"
    b-=1
    Turn+=1
    checkForWinner(1)
    checkForWinner(2)
    if gamemode=="pvc":
        cpu(x,y)
c=6    
def greenfun2(x,y):
    global winner
    global Turn
    global c
    global gamemode
    if Turn%2:
        if numberlistofrows[2][c-1]==0:
            listofrows[2][c].color("Red")
            numberlistofrows[2][c-1]=1
            winner="RED"
    else:
        if numberlistofrows[2][c-1]==0:
            listofrows[2][c].color("Blue")
            numberlistofrows[2][c-1]=2
            winner="BLUE"
    c-=1
    Turn+=1
    checkForWinner(1)
    checkForWinner(2)
    if gamemode=="pvc":
        cpu(x,y)
d=6    
def greenfun3(x,y):
    global winner
    global Turn
    global d
    global gamemode
    if Turn%2:
        if numberlistofrows[3][d-1]==0:
            listofrows[3][d].color("Red")
            numberlistofrows[3][d-1]=1
            winner="RED"
    else:
        if numberlistofrows[3][d-1]==0:
            listofrows[3][d].color("Blue")
            numberlistofrows[3][d-1]=2
            winner="BLUE"
    d-=1
    Turn+=1
    checkForWinner(1)
    checkForWinner(2)
    if gamemode=="pvc":
        cpu(x,y)
e=6    
def greenfun4(x,y):
    global winner
    global Turn
    global e
    global gamemode
    if Turn%2:
        if numberlistofrows[4][e-1]==0:
            listofrows[4][e].color("Red")
            numberlistofrows[4][e-1]=1
            winner="RED"
    else:
        if numberlistofrows[4][e-1]==0:
            listofrows[4][e].color("Blue")
            numberlistofrows[4][e-1]=2
            winner="BLUE"
    e-=1
    Turn+=1
    checkForWinner(1)
    checkForWinner(2)
    if gamemode=="pvc":
        cpu(x,y)
f=6    
def greenfun5(x,y):
    global winner
    global Turn
    global f
    global gamemode
    if Turn%2:
        if numberlistofrows[5][f-1]==0:
            listofrows[5][f].color("Red")
            numberlistofrows[5][f-1]=1
            winner="RED"
    else:
        if numberlistofrows[5][f-1]==0:
            listofrows[5][f].color("Blue")
            numberlistofrows[5][f-1]=2
            winner="BLUE"
    f-=1
    Turn+=1
    checkForWinner(1)
    checkForWinner(2)
    if gamemode=="pvc":
        cpu(x,y)
g=6    
def greenfun6(x,y):
    global winner
    global Turn
    global g
    global gamemode
    if Turn%2:
        if numberlistofrows[6][g-1]==0:
            listofrows[6][g].color("Red")
            numberlistofrows[6][g-1]=1
            winner="RED"
    else:
        if numberlistofrows[6][g-1]==0:
            listofrows[6][g].color("Blue")
            numberlistofrows[6][g-1]=2
            winner="BLUE"
    g-=1
    Turn+=1
    checkForWinner(1)
    checkForWinner(2)
    if gamemode=="pvc":
        cpu(x,y)

listoffunctions=[greenfun0,greenfun2,greenfun3,greenfun4,greenfun5,greenfun6]

# -- Initialize Turtles2-
#     General Use
pw=t.Turtle(shape='circle',)
pw.hideturtle()
pw.penup()
pw.speed(0)
pw.goto(-100,250)
pw.write("Please Wait..",font=fontsetup)

arty=t.Turtle(shape='circle',)
arty.hideturtle()
arty.penup()
arty.speed(0)

#                               Main Menu Turtles

#       Buttons
pvc=t.Turtle(shape='square',)
pvc.hideturtle()
pvc.penup()
pvc.speed(0)
pvc.color("Black")
pvc.shapesize(2)

pvp=t.Turtle(shape='square',)
pvp.hideturtle()
pvp.penup()
pvp.speed(0)
pvp.color("Black")
pvp.shapesize(2)

direct=t.Turtle(shape='square',)
direct.hideturtle()
direct.penup()
direct.speed(0)
direct.color("Black")
direct.shapesize(2)

cred=t.Turtle(shape='square',)
cred.hideturtle()
cred.penup()
cred.speed(0)
cred.color("Black")
cred.shapesize(2)

back=t.Turtle(shape='square',)
back.hideturtle()
back.penup()
back.speed(0)
back.color("Red")
back.shapesize(2)

#                                Board Game Turtles
# Selection Buttons
green=t.Turtle(shape='circle',)
green.hideturtle()
green.penup()
green.speed(0)
green.color("green")
green.shapesize(3)
listofrows[0].append(green)

green.onclick(greenfun0)

green1=t.Turtle(shape='circle',)
green1.hideturtle()
green1.penup()
green1.speed(0)
green1.color("green")
green1.shapesize(3)
listofrows[1].append(green1)

green1.onclick(greenfun1)

green2=t.Turtle(shape='circle',)
green2.hideturtle()
green2.penup()
green2.speed(0)
green2.color("green")
green2.shapesize(3)
listofrows[2].append(green2)

green2.onclick(greenfun2)

green3=t.Turtle(shape='circle',)
green3.hideturtle()
green3.penup()
green3.speed(0)
green3.color("green")
green3.shapesize(3)
listofrows[3].append(green3)

green3.onclick(greenfun3)

green4=t.Turtle(shape='circle',)
green4.hideturtle()
green4.penup()
green4.speed(0)
green4.color("green")
green4.shapesize(3)
listofrows[4].append(green4)

green4.onclick(greenfun4)

green5=t.Turtle(shape='circle',)
green5.hideturtle()
green5.penup()
green5.speed(0)
green5.color("green")
green5.shapesize(3)
listofrows[5].append(green5)

green5.onclick(greenfun5)

green6=t.Turtle(shape='circle',)
green6.hideturtle()
green6.penup()
green6.speed(0)
green6.color("green")
green6.shapesize(3)
listofrows[6].append(green6)

green6.onclick(greenfun6)

#   Row buttons
for i in range(7):
    for j in range(6):
        turt=t.Turtle(shape='circle')
        turt.hideturtle()
        turt.penup()
        turt.speed(0)
        turt.color("white")
        turt.shapesize(3)
        listofrows[i].append(turt)
        numberlistofrows[i].append(0)
# -- Add Turtles to a List for Later Hiding --

listofturtles.append(pvc)
listofturtles.append(pvp)
listofturtles.append(direct)
listofturtles.append(cred)

# -- Functions --

#                                Main Menu Functions
def drawmainmenu(x,y):
    clear(x,y)
    
    #-- Show Turtles --
    for i in listofturtles:
        i.showturtle()
    
    
    global mainmenu
    
    #-- Moving Buttons --
    pvc.goto(0,225)
    pvp.goto(0,125)
    direct.goto(0,25)
    cred.goto(0,-75)
    
    #-- Drawing --
    arty.pencolor("Red")
    arty.goto(-25,250)
    arty.write("PvC",font=fontsetup)
    arty.goto(-25,150)
    arty.write("PVP",font=fontsetup)
    arty.goto(-60,50)
    arty.write("Directions",font=fontsetup)
    arty.goto(-40,-50)
    arty.write("Credits",font=fontsetup)

def clear(x,y):
    for i in listofturtles:
        i.hideturtle()
    back.hideturtle()
    if listofrows[0][0].isvisible()== True:
        global Turn
        Turn=1
        global gamemode
        gamemode=False
        global a
        global b
        global c
        global d
        global e
        global f
        global g
        a=6
        b=6
        c=6
        d=6
        e=6
        f=6
        g=6
        for i in range(len(numberlistofrows)):
            for j in range(len(numberlistofrows[i])):
                numberlistofrows[i][j]=0
        for i in range(7):
            for j in listofrows[i]:
                if not(j==listofrows[i][0]):
                    j.color("white")
                j.hideturtle()
    arty.clear()
    
def drawboard(x,y):
    clear(x,y)
    backbutton()
    arty.pencolor("black")
    
    # Drawing X-axis Lines --
    yaxis=275
    for i in range (7):
        arty.goto(-250,yaxis)
        arty.pendown()
        arty.forward(525)
        arty.penup()
        yaxis-=75
    # Drawing Y-axis Lines |
    xaxis=-250
    arty.right(90)
    for i in range (8):
        arty.goto(xaxis,300)
        arty.pendown()
        arty.forward(475)
        arty.penup()
        xaxis+=75
    arty.penup()
    arty.pencolor("red")
    arty.left(90)
    
    # Moving Turtles
    rowx=(-285)
    for i in range(7):
        rowy=(310)
        rowx+=75
        for j in listofrows[i]:
            j.goto(rowx,rowy)
            rowy-=75    
            j.showturtle() # Delete to keep turtles hidden when you're making the game its just for visuals
            

def drawdirections(x,y):
    clear(x,y)
    backbutton()
    arty.goto(-57,275)
    arty.write("Directions:",font=('Arial',25,'bold'))
    arty.goto(-210,0)
    arty.write("      Press the Green Circle To \nDrop your colored puck in the row\n   Try to connect 4 of your color!",font=fontsetup)

def drawcred(x,y):
    clear(x,y)
    backbutton()
    arty.goto(-50,100)
    arty.write("  Rome \n\n  Mason\n\nMr. Bander",font=fontsetup)
    arty.goto(-240,50)
    arty.write("GeeksForGeeks  StackOverFlow  Python.org",font=fontsetup)
    arty.goto(-57,275)
    arty.write("Credits:",font=('Arial',25,'bold'))
    
def backbutton():
    back.showturtle()
    back.goto(-390,275)
    arty.goto(-420,300)
    arty.write("Back",font=fontsetup)
#                                Board Game Functions


def pvclick(x,y):
    global gamemode
    gamemode="pvc"
    drawboard(x,y)
# -- Listen For Clicks --
pvc.onclick(pvclick)
pvp.onclick(drawboard)
direct.onclick(drawdirections)
cred.onclick(drawcred)
back.onclick(drawmainmenu)

#-- Starting Function(s) --
pw.clear()
drawmainmenu(0,0)

wn.mainloop()