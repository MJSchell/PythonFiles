import random
from time import sleep
import turtle as t

#Varibles
RADIUS = 300
WEDGES = 8
ANGLE = 360 / WEDGES
setup = True
go = True

#main Screen
mainScreen = t.Screen()
mainScreen.screensize(canvwidth=800,canvheight=400)
mainScreen.setup(1400,700)
mainScreen.tracer(False)

#turtle
t.speed(1)
t.penup()
t.hideturtle()
t.goto(-400,0)

#turtle drawing
turtle = t.Turtle()
turtle.penup()
center = t.position()
turtle.goto(-400,0)
turtle.sety(turtle.ycor() - RADIUS)

#button
button = t.Turtle()
button.penup()
button.shapesize(3)
button.setheading(-160)
button.goto(-120,90)
button.showturtle()

#writing tool
writing = t.Turtle()
writing.hideturtle()
writing.penup()
writing.goto(100,0)
writing.write(arg=f"Press the Arrow on the wheel to start.",move=True, align="center", font=("Arial", 16, "normal"))

#Big Colors
hues = ["red","orange","yellow","green","blue","purple","pink","teal","maroon"]
money = ["100","100","100","200","200","200","300","400","500"]

#Wheel Setup Runs ONLY ONCE
while setup == True:
    for hue in hues:
        turtle.color(hue)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(RADIUS, extent=ANGLE)
        position = turtle.position()
        turtle.goto(center)
        turtle.end_fill()
        turtle.penup()
        turtle.goto(position)  
        mainScreen.update()
    break

#Set Go True
time = 0
def wheelSpin(x,y):
    global setup,time
    setup = True
    stopVal = random.randint(60,90)
    while setup == True:
        for hue in hues:
            colorDoneLast = hue
            turtle.color(hue)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(RADIUS, extent=ANGLE)
            position = turtle.position()
            turtle.goto(center)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(position)  
            mainScreen.update()
            time+=1
            print(time)
            colorDoneLast = hue
            
            if time >= stopVal:
                index = hues.index(colorDoneLast)
                cash = money[index]
                writing.clear()
                writing.write(arg=f"Current Cash: ${cash}",move=True, align="center", font=("Arial", 16, "normal"))
                time=0
                setup = False
                mainScreen.bye()
                break
            
            else:
                sleep(.1)

button.onclick(wheelSpin)
mainScreen.mainloop()