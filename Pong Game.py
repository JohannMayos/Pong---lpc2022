
import turtle
import winsound
import os

# draw screen
screen = turtle.Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# draw paddle 1
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("white")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.penup()
paddle_1.goto(-350, 0)
paddle_1.movingUp = False
paddle_1.movingDown = False

# draw paddle 2
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("white")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.penup()
paddle_2.goto(350, 0)
paddle_2.movingUp = False
paddle_2.movingDown = False

# draw ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.5
ball.dy = 0.5

# score
score_1 = 0
score_2 = 0

# head-up display
hud = turtle.Turtle()
hud.speed(0)
hud.shape("square")
hud.color("white")
hud.penup()
hud.hideturtle()
hud.goto(0, 260)
hud.write("0 : 0", align="center", font=("Press Start 2P", 24, "normal"))


def paddle_1_up():
    y = paddle_1.ycor()

    if paddle_1.movingUp:

        if y < 250:
            y += 0.5

    paddle_1.sety(y)


def paddle_1_set_moving_up_true():
    paddle_1.movingUp = True


def paddle_1_set_moving_up_false():
    paddle_1.movingUp = False


def paddle_1_down():
    y = paddle_1.ycor()

    if paddle_1.movingDown:

        if y > -250:
            y -= 0.5

    paddle_1.sety(y)


def paddle_1_set_moving_down_true():
    paddle_1.movingDown = True


def paddle_1_set_moving_down_false():
    paddle_1.movingDown = False


def paddle_2_up():
    y = paddle_2.ycor()

    if paddle_2.movingUp:

        if y < 250:
            y += 0.5

    paddle_2.sety(y)


def paddle_2_set_moving_up_true():
    paddle_2.movingUp = True


def paddle_2_set_moving_up_false():
    paddle_2.movingUp = False


def paddle_2_down():
    y = paddle_2.ycor()

    if paddle_2.movingDown:

        if y > -250:
            y -= 0.5

    paddle_2.sety(y)


def paddle_2_set_moving_down_true():
    paddle_2.movingDown = True


def paddle_2_set_moving_down_false():
    paddle_2.movingDown = False


# keyboard
screen.listen()
screen.onkeypress(paddle_1_set_moving_up_true, "w")
screen.onkeypress(paddle_1_set_moving_down_true, "s")
screen.onkeyrelease(paddle_1_set_moving_up_false, "w")
screen.onkeyrelease(paddle_1_set_moving_down_false, "s")

screen.onkeypress(paddle_2_set_moving_up_true, "Up")
screen.onkeypress(paddle_2_set_moving_down_true, "Down")
screen.onkeyrelease(paddle_2_set_moving_up_false, "Up")
screen.onkeyrelease(paddle_2_set_moving_down_false, "Down")

while True:
    screen.update()

    # paddles movement
    paddle_1_up()
    paddle_1_down()
    paddle_2_up()
    paddle_2_down()

    # ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # collision with the upper wall
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        ball.dx *= 1
        winsound.PlaySound("impact_sound.wav", winsound.SND_ASYNC)
        os.system("afplay impact_sound.wav&")

    # collision with lower wall
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        ball.dx *= 1
        winsound.PlaySound("impact_sound.wav", winsound.SND_ASYNC)
        os.system("afplay impact_sound.wav&")

    # collision with left wall
    if ball.xcor() < -330 and paddle_1.ycor() + 50 > ball.ycor() > paddle_1.ycor() - 50:
        ball.dx *= -1
        os.system("afplay impact_sound.wav&")
        winsound.PlaySound("impact_sound.wav", winsound.SND_ASYNC)

    # collision with right wall
    if ball.xcor() > 330 and paddle_2.ycor() + 50 > ball.ycor() > paddle_2.ycor() - 50:
        ball.dx *= -1
        os.system("afplay impact_sound.wav&")
        winsound.PlaySound("impact_sound.wav", winsound.SND_ASYNC)

    # collision with the paddle 1
    if ball.xcor() < -370:
        score_2 += 1
        hud.clear()
        hud.write("{} : {}" .format(score_1, score_2),
                  align="center", font=("Press Start 2p", 24, "normal"))
        ball.goto(0, 0)
        ball.dx = -1
        ball.dy = 1

    # collision with the paddle 2
    if ball.xcor() > 370:
        score_1 += 1
        hud.clear()
        hud.write("{} : {}" .format(score_1, score_2),
                  align="center", font=("Press Start 2p", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1
        ball.dy *= 1
