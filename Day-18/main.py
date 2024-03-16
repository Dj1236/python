
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
# tim.color("red")
# for _ in range(4):
#  tim.forward(100)
#  tim.right(90)
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# def draw_shapes(num_sides):
#     angle =360/num_sides
#     for _ in range(num_sides):
#        tim.forward(100)
#        tim.right(angle)

# for shapeside in range(3,20):
#  draw_shapes(shapeside)
directions = [0,90,180,270]
tim.pensize(10)
for _ in range(200):  
 tim.forward(10)
 tim.setheading(random.choice(directions))




screen = Screen()
screen.exitonclick()

# tim.distance
# from turtle import Turtle,screen
# tinny_the_turtle = Turtle()
# tinny_the_turtle.shape("turtle")


# screen = screen()
# screen.exitonclick()
# tinny_the_turtle.done()
