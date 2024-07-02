from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
from restgame import RestartGame 
import time
screen = Screen()
screen.setup(600, 600)
screen.title("Snake Game")

def main_game_loop():
    global game_is_on
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreBoard.increase()

        # Detect collision with wall
        if (
            snake.head.xcor() > 280 or 
            snake.head.xcor() < -280 or 
            snake.head.ycor() > 280 or 
            snake.head.ycor() < -280
        ):
            game_is_on = False
            scoreBoard.game_over()
            setup_restart_button()

        # Detect collision with self
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                scoreBoard.game_over()
                setup_restart_button()

def restart_game(x, y):
    if -77 <= x <= 73 and -112 <= y <= -62:  # Adjust coordinates for button hit box
        screen.clear()
        setup_game()

def setup_restart_button():
    restart_button = RestartGame()
    screen.onclick(restart_game)

def setup_game():
    global snake, food, scoreBoard
    screen.bgcolor("black")
    screen.tracer(0)
    
    snake = Snake()
    food = Food()
    scoreBoard = ScoreBoard()
    
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    main_game_loop()

# Initial game setup
setup_game()

screen.mainloop()
