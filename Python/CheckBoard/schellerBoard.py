import turtle as trtl

painter = trtl.Turtle()
painter.shape("square")
painter.hideturtle()
painter.penup()

x = -200
number=0
y=200
row=0
z=8
while y>0:
    while (x < 25):
        if number==z:
            x=-200
            y-=25
            number=0
            row+=1 
            if row%2==1:
                z=9
                number+=1
            if row%2==0:
                z=8
            if row==8:
                x=25
                y=0
        x = x + 25
        painter.goto(x,y)
        if number%2==1:
            painter.color("red")
        if number%2==0:
            painter.color("black")
        painter.stamp()
        number+=1


wn = trtl.Screen()
wn.mainloop()