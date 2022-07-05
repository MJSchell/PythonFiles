import turtle as t


def dotted():
    #if in center square
    if art.xcor() in range(50,300) and art.ycor() in range(-100,150):
        art.pencolor('White')  
    else:
        art.pencolor('gold')
    art.penup()
    art.forward(10)
    art.pendown()
    art.forward(10)
    
#drawing intersection
art=t.Turtle()
art.width(2)
art.speed(0)
art.penup()


#black lines
art.goto(300,400)
art.pendown()
art.setheading(270)
for i in range(4):
    art.forward(250)
    art.left(90)
    for i in range(2):
        art.forward(250)
        art.right(90)
art.right(90)
art.penup()
art.goto(120,400)
art.left(90)


#yellow dotted lines
for i in range(38):
    dotted()
art.penup()
art.goto(240,400)
for i in range(38):
    dotted()
art.penup()
art.goto(180,400)
for i in range(38):
    dotted()
art.penup()
art.right(90)
art.goto(550,100)
for i in range(38):
    dotted()
    
    
    
    #Trouble
art.penup()
art.goto(550,35)
for i in range(38):
    dotted()
art.penup()
art.goto(550,-30)
for i in range(38):
    dotted()


def click(x,y):
    print(x,y)
#window
wn=t.Screen()
wn.onscreenclick(click)
wn.mainloop()