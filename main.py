from turtle import Screen
#wanted to practice working with 3 clases, so 3 files as well.
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
#adjusted so that the segments divide evenly
screen.setup(width=680, height=680)
screen.bgcolor("black")
screen.title('My snake game')

#turn off automatic screen updates
screen.tracer(0)
#when we create a turtle 40 pixels wide and 40 pixels tall
#first square at 0,0, second is 40 pixels to the left, and third is another 40 pixels to the left from the middle one
snake = Snake()
scoreboard = Scoreboard()
food = Food()

#controlling the movement of the snake
screen.listen()
# Faster reaction time for direction changes
screen.onkeypress(snake.up, "w")
screen.onkeypress(snake.down, "s")
screen.onkeypress(snake.left, "a")
screen.onkeypress(snake.right, "d")
game_is_on = True

while game_is_on:
    
    snake.move()

    #detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()
    screen.update()

    # detect collision with wall
    if snake.head.xcor() > 320 or snake.head.xcor() < -320 or snake.head.ycor() > 320 or snake.head.ycor() < -320:
        scoreboard.reset()
        snake.reset()
    screen.update()

    #can slice the list to make it less wordy
    #(piano_keys[2:] to the end
    #(piano_keys[:5] start to numer
    #pianokeys[::-1]
    #reverse the list

    #detect collision with tail

    for segment in snake.segments[1:(len(snake.segments)-1)]:
        #dont need the len snake segments can use [1:] instead
        # if segment == snake.head:
        #     pass
        if snake.head.distance(segment) <10:
            scoreboard.reset()
            snake.reset()

    screen.update()
    time.sleep(0.09)


screen.exitonclick()