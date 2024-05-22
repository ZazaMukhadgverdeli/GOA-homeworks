from turtle import *


speed(10)
#we want to paint a house

#step 1:   draw a square
width(7)
color("purple")
begin_fill()
forward(200)
left(90)

forward(200)
left (90)

forward(200)
left(90)

forward(200)
left(90)

#end of square

#drawing a door


forward(70)
end_fill()

color("yellow")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()


penup()
goto(200,200)
pendown()


color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#draw a window
begin_fill()
color("cyan")
penup()
goto(10,170)
pendown()
left(30)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()
left(90)
forward(20)
color("black")
left(90)
forward(40)
penup()
goto(30,170)
pendown()
right(90)
forward(40)
# draw a window2
penup()
goto(150,170)
pendown()
begin_fill()
color("cyan")
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()
right(180)
forward(20)
color("black")
right(90)
forward(40)
penup()
goto(150,150)
pendown()
left(90)
forward(40)


exitonclick()