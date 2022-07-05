import turtle as t

COURT_HEIGHT = 600
COURT_WIDTH = 1000

wn = t.Screen()

painter=t.Turtle(visible=False)   #same as hideturtle
painter.penup()
painter.speed(0)

painter.goto(-500,300)
painter.pendown()
painter.forward(1000)
painter.penup()
painter.goto(-500,-300)
painter.pendown()
painter.forward(1000)
painter.penup()
painter.goto(0,-326)
painter.left(90)
i=25
while i>0:
     painter.forward(26)
     if i%2==1:
          painter.pendown()
     if i%2==0:
          painter.penup()
     i-=1
wn.mainloop()
