from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time 
import random 

screen = Screen()
screen.setup(width=700, height=700)
screen.bgcolor("black")
screen.title("This is Harsh's Snake Game.")

segment = []
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
game_is_on = True

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")  

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect colison with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extent()
        scoreboard.increase_score()

    # Detect colison with screen
    if snake.head.xcor() > 330 or snake.head.xcor() < -330 or snake.head.ycor() > 330 or snake.head.ycor() < -330:
        game_is_on = False
        scoreboard.game_over()


    # Detect colison with tail
    # for segment in snake.segment:
        # if segment == snake.head:
        #     pass
        # elif snake.head.distance(segment) < 10:
        #     game_is_on = False
        #     scoreboard.game_over()

        ## we can also use the slice method to do this.
    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
    

    

        
    



































screen.exitonclick()
