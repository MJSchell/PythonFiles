import turtle as t

SCREENW,SCREENH=300,300
wn=t.Screen()

# -- Variables --

listofturtles=[]
fontsetup=('Arial',20)
mainmenu=True
row1=[]
row2=[]
row3=[]
row4=[]
row5=[]
row6=[]
row7=[]
listofrows=[row1,row2,row3,row4,row5,row6,row7]
# -- Initialize Turtles --

#                               General Use
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
for i in range (7):
    green=t.Turtle(shape='circle',)
    green.hideturtle()
    green.penup()
    green.speed(0)
    green.color("green")
    green.shapesize(3)
    listofrows[i].append(green)

#   Row buttons
for i in range(7):
    for j in range(6):
        turt=t.Turtle(shape='circle')
        turt.hideturtle()
        turt.penup()
        turt.speed(0)
        turt.color("orange")
        turt.shapesize(3)
        listofrows[i].append(turt)

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
    mainmenu=True
    
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
        for i in range(7):
            for j in listofrows[i]:
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
            # Green Button Turtles
            j.goto (rowx,rowy)
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


# -- Listen For Clicks --
pvc.onclick(drawboard)
pvp.onclick(drawboard)
direct.onclick(drawdirections)
cred.onclick(drawcred)
back.onclick(drawmainmenu)

#-- Starting Function(s) --
pw.clear()
drawmainmenu(0,0)

wn.mainloop()