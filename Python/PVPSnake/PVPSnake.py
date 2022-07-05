#import
from tracemalloc import stop
import turtle as t
import time
import random

#game configuration
delay = 0.1
bodyParts=[]
bodyParts2=[]
snake1speed=20
snake2speed=20
pausecount=1
paused=False
colorlist=['yellow','gold','orange','red','maroon','violet','magenta','purple','navy','blue','skyblue','cyan','turquoise','lightgreen','green','darkgreen','chocolate','brown','black','gray','white']
#create turtle objects
wn = t.Screen()
wn.title('Snake')
wn.bgcolor("pink")
wn.setup(width=600,height=600)        #give a default screen size

head = t.Turtle(shape="square")
head.speed(0)
head.penup()
head.direction="stop"

head2 = t.Turtle(shape="square")
head2.color('blue')
head2.speed(0)
head2.penup()
head2.direction="stop"

#create the food
food = t.Turtle()
food.speed(0)
food.shape("circle")
food.shapesize(.5,.5)    #scaling the food down by 50%
food.color("green")
food.penup()
food.goto(100,100)


#function 
def up():
     if paused==False:
          if head.direction != "down":
               head.direction="up"  
          color=random.choice(colorlist)
          for part in bodyParts:
               part.color(color)
def down():
     if paused==False:
          if head.direction != "up":
               head.direction="down"   
          color=random.choice(colorlist)
          for part in bodyParts:
               part.color(color)
def left():
     if paused==False:
          if head.direction!="right":
               head.direction="left"
          color=random.choice(colorlist)
          for part in bodyParts:
               part.color(color)
def right():
     if paused==False:
          if head.direction!="left":
               head.direction="right" 
          color=random.choice(colorlist)
          for part in bodyParts:
               part.color(color)     
def right2():
     if paused==False:
          if head2.direction!="left":
               head2.direction="right"
          color=random.choice(colorlist)
          for part2 in bodyParts2:
               part2.color(color)
def up2():
     if paused==False:
          if head2.direction != "down":
               head2.direction="up"
          color=random.choice(colorlist)
          for part2 in bodyParts2:
               part2.color(color)  
def down2():
     if paused==False:
          if head2.direction != "up":
               head2.direction="down"
          color=random.choice(colorlist)
          for part2 in bodyParts2:
               part2.color(color)   
def left2():
     if paused==False:
          if head2.direction!="right":
               head2.direction="left" 
          color=random.choice(colorlist)
          for part2 in bodyParts2:
               part2.color(color)     
def right2():
     if paused==False:
          if head2.direction!="left":
               head2.direction="right"
          color=random.choice(colorlist)
          for part2 in bodyParts2:
               part2.color(color)
def move():
     #depending on the direction, the coordinates change
     if paused==False:
          if head.direction == "up":
               y = head.ycor()     #get the y coordinate
               head.sety(y+snake1speed)     #set the new y coordinate
               
          elif head.direction == "down":
               y = head.ycor()     #get the y coor
               head.sety(y-snake1speed)     #set the new y coordinate
          
          elif head.direction == "right":
               x = head.xcor()     #get the x coor
               head.setx(x+snake1speed)     #set the new x coordinate
          
          elif head.direction == "left":
               x = head.xcor()     #get the x coor
               head.setx(x-snake1speed)     #set the new x coordinate
def move2():
     #depending on the direction, the coordinates change
     if head2.direction == "up":
          y = head2.ycor()     #get the y coordinate
          head2.sety(y+snake2speed)     #set the new y coordinate
          
     elif head2.direction == "down":
          y = head2.ycor()     #get the y coor
          head2.sety(y-snake2speed)     #set the new y coordinate
     
     elif head2.direction == "right":
          x = head2.xcor()     #get the x coor
          head2.setx(x+snake2speed)     #set the new x coordinate
     
     elif head2.direction == "left":
          x = head2.xcor()     #get the x coor
          head2.setx(x-snake2speed)     #set the new x coordinate
def hideTheBodyParts():       #gameover
     global bodyParts
     time.sleep(1)            #wait a second
     head.goto(0,0)
     head.direction="stop"
     #hide the parts
     for eachPart in bodyParts:
          eachPart.goto(1000,1000)
     bodyParts=[]
     snake1speed=20
def hideTheBodyParts2():       #gameover
     global bodyParts2
     time.sleep(1)            #wait a second
     head2.goto(0,0)
     head2.direction="stop"
     #hide the parts
     for eachPart in bodyParts2:
          eachPart.goto(1000,1000)
     bodyParts2=[]
     snake2speed=20
#Pause
def pause():
     global pausecount
     global paused
     if pausecount%2==1:
          head.direction='stop'
          head2.direction='stop'
          paused=True
     elif pausecount%2==0:
          paused=False
     pausecount+=1
#slitherio
def slitherio(number):
     if number == '1':
          for i in bodyParts2:
               part = t.Turtle()
               part.speed(0)
               part.shape("triangle")
               part.color("gray")
               part.penup()
               bodyParts.append(part)
               if len(bodyParts)>1:
                    bodyParts[-2].shape('square')
     elif number == '2':
          for i in bodyParts:
               part2 = t.Turtle()
               part2.speed(0)
               part2.shape("triangle")
               part2.color("gray")
               part2.penup()
               bodyParts2.append(part2)
               if len(bodyParts2)>1:
                    bodyParts2[-2].shape('square')
#events or running code
wn.listen()
wn.onkeypress(up,"w")
wn.onkeypress(right,"d")
wn.onkeypress(left,"a")
wn.onkeypress(down,"s")
wn.onkeypress(up2,"Up")
wn.onkeypress(right2,"Right")
wn.onkeypress(left2,"Left")
wn.onkeypress(down2,"Down")
wn.onkeypress(pause,"Escape")

#main game loop
while True:
     wn.update()    #updates or refreshes the screen
     
     #Border Collision?
     if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
          hideTheBodyParts()
     if head2.xcor()>290 or head2.xcor()<-290 or head2.ycor()>290 or head2.ycor()<-290:
          hideTheBodyParts2()
     #Food Collision?
     #if head and food's distance < 20
     # turtle.distance(turtle) -> distance between 2 turtle obj
     if head.distance(food) < 20:
          #move the food
          x=random.randint(-290,290)
          y=random.randint(-290,290)
          food.goto(x,y)
          #add a body part
          part = t.Turtle()
          part.speed(0)
          part.shape("triangle")
          part.color("gray")
          part.penup()
          bodyParts.append(part)
          snake1speed+=1
          if len(bodyParts)>1:
               bodyParts[-2].shape('square')
          color=random.choice(colorlist)
          for part in bodyParts:
               part.color(color)
     if head2.distance(food) < 20:
          #move the food
          x=random.randint(-290,290)
          y=random.randint(-290,290)
          food.goto(x,y)
          #add a body part
          part2 = t.Turtle()
          part2.speed(0)
          part2.shape("triangle")
          part2.color("cyan")
          part2.penup()
          bodyParts2.append(part2)
          if len(bodyParts2)>1:
               bodyParts2[-2].shape('square')
          color=random.choice(colorlist)
          for part2 in bodyParts2:
               part2.color(color)
          snake2speed+=1
     
     #move the snake
     #Move the butt to the neck
     for i in range(len(bodyParts)-1, 0, -1): #last index to the first index
          if paused==False:
               x=bodyParts[i-1].xcor()  #get the x of the next bodypart
               y=bodyParts[i-1].ycor()  #get the y of the next bodypart
               bodyParts[i].goto(x,y)   #reset the current bodypart x,y
     for i in range(len(bodyParts2)-1, 0, -1):    #last index to the first index
          if paused==False:
               x=bodyParts2[i-1].xcor()  #get the x of the next bodypart
               y=bodyParts2[i-1].ycor()  #get the y of the next bodypart
               bodyParts2[i].goto(x,y)   #reset the current bodypart x,y
          
     #Move the neck to the head
     if len(bodyParts)>0:
          if paused==False:
               x=head.xcor()
               y=head.ycor()
               bodyParts[0].goto(x,y)
     if len(bodyParts2)>0:
          if paused==False:
               x=head2.xcor()
               y=head2.ycor()
               bodyParts2[0].goto(x,y)
          
     move()
     move2()#Move the head
     
     #Did we hit ourselves?
     for part in bodyParts:
          if part.distance(head) < 10:
               hideTheBodyParts()
     for part2 in bodyParts2:
          if part2.distance(head2) < 10:
               hideTheBodyParts2()
     #Did we hit eachother?
     for part in bodyParts:
          if part.distance(head2) < 20:
               slitherio('1')
               hideTheBodyParts2()
     for part2 in bodyParts2:
          if part2.distance(head) < 20:
               slitherio('2')
               hideTheBodyParts()
     time.sleep(delay)







'''
/required - (+5) PVP
/required - (+5) Speeds up as you eat food


(+2) Code is DRY (functions where appropriate)
(+1) /Window has a title
(+5) /Pause Button
(+2) /Have head rotate in direction traveled
(+5) Main Menu that asks the user which version they want to play: normal, PVP, autonomous, PVC (include which versions you have)
(+1) Directions for the user (which keys move the snake in the console) *include pause if you have it*
(+3) Directions on the screen (which keys move the snake) *include pause if you have it*
(+3) /Snake's tail (last bodyPart) is a triangle that points in the opposite direction of travel
(+3) /Change color of snake after each time it eats
(+2) /Change color of snake after each time it moves (can only get this if get color change on eat)
(+2) Hard mode - Food teleports every {soManySeconds} seconds
(+2) PVP record (who won how many times and it prints out after every game)
(+2) Enter your name for score titles (utilize console)
(+3) Option to play PVP or PVC
(+10) autonomous snake that can last longer than 20 food spawns
(+10) PVC: basically you verses the autonomous snake
(+5) Add sound for when you run into something
(+5) /Slither.io edition where if the enemy snake runs into you, you obtain their body parts.
'''