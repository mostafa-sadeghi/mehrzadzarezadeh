import turtle
import time
import random


def move_snake():
    if snake_head.dir == "up":
        y = snake_head.ycor()
        y += 20
        snake_head.sety(y)
    if snake_head.dir == "down":
        y = snake_head.ycor()
        y -= 20
        snake_head.sety(y)
    if snake_head.dir == "left":
        x = snake_head.xcor()
        x -= 20
        snake_head.setx(x)
    if snake_head.dir == "right":
        x = snake_head.xcor()
        x += 20
        snake_head.setx(x)


def go_up():
    if snake_head.dir != "down":
        snake_head.dir = "up"


def go_down():
    if snake_head.dir != "up":
        snake_head.dir = "down"


def go_left():
    if snake_head.dir != "right":
        snake_head.dir = "left"


def go_right():
    if snake_head.dir != "left":
        snake_head.dir = "right"


def change_food_position():
    food_x_position = random.randint(-300, 300)
    food_y_position = random.randint(-300, 300)
    food.goto(food_x_position, food_y_position)


window = turtle.Screen()
window.title("Snake game")
window.bgcolor("blue")
window.setup(width=600, height=600)
window.tracer(0)


snake_head = turtle.Turtle()
snake_head.speed("fastest")
snake_head.color("black")
snake_head.shape("square")
snake_head.penup()
snake_head.goto(100, 100)
snake_head.dir = ""

food = turtle.Turtle()
food.speed("fastest")
food.shape("circle")
food.penup()
food.shapesize(0.5, 0.5)
food.color("red")
change_food_position()


window.listen()
window.onkeypress(go_up, "Up")
window.onkeypress(go_down, "Down")
window.onkeypress(go_left, "Left")
window.onkeypress(go_right, "Right")

snake_body = []
while True:
    window.update()

    if snake_head.distance(food) < 15:
        change_food_position()
        new_body = turtle.Turtle()
        new_body.speed("fastest")
        new_body.color("grey")
        new_body.shape("square")
        new_body.penup()
        snake_body.append(new_body)

    for i in range(len(snake_body)-1, 0, -1):
        x = snake_body[i-1].xcor()
        y = snake_body[i-1].ycor()
        snake_body[i].goto(x, y)
    if len(snake_body) > 0:
        x = snake_head.xcor()
        y = snake_head.ycor()
        snake_body[0].goto(x, y)

    if snake_head.xcor() > 290 or snake_head.xcor() < -290 or snake_head.ycor() > 290 or snake_head.ycor() < -290:
        time.sleep(1)
        snake_head.home()
        snake_head.dir = ""
        for body in snake_body:
            body.ht()
            snake_body = []

    move_snake()
    time.sleep(0.1)
