#Turtle Square
# print(another.another_variable)

from turtle import Turtle, Screen
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("red")
#turtle will move in square dimension
my_screen = Screen()
timmy.forward(200)
timmy.right(90)
timmy.forward(200)
timmy.right(90)
timmy.forward(200)
timmy.right(90)
timmy.forward(200)
timmy.right(90)
for a in range(4):
    timmy.forward(200)
    timmy.right(90)


print(my_screen.canvwidth)
print(my_screen.canvheight)
#my_screen is object and canvwidth is the attribute
my_screen.exitonclick()