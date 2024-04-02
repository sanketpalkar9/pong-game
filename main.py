from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


game_is_on = True

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong game")
screen.tracer(0)


ball = Ball()
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
scoreboard =Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()


    #Collision with right paddle

    if (ball.distance(r_paddle) <50 and ball.xcor() > 320) or (ball.distance(l_paddle) <50 and ball.xcor()) < -320:
        ball.bounce_x()



    #detect when right paddle misses

    if ball.xcor() >380:
        ball.reset_position()
        scoreboard.l_point()

# left paddle collsion

    if ball.xcor() <-380:
        ball.reset_position()
        scoreboard.r_point()


    # Collision with walls
    if ball.ycor() > 280 or ball.ycor() <-280:
        ball.bounce_y()

    if scoreboard.l_score== 10 or scoreboard.r_score == 10:
        game_is_on=False


screen.clear()
screen.bgcolor("black")
scoreboard.game_over()

screen.exitonclick()