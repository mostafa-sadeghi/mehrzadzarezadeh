import turtle

s = turtle.Screen()
pen = turtle.Pen()
pen.shape('turtle')
pen.shapesize(3)
pen.color('red', 'green')
pen.pensize(4)
# pen.forward(100)
# pen.backward(100)

# pen.begin_fill()
# for i in range(3):
#     pen.forward(100)
#     pen.left(120)
# pen.end_fill()

# pen.begin_fill()
# for i in range(3):
#     pen.forward(100)
#     pen.right(120)
# pen.end_fill()
# pen.penup()
# pen.goto(100,100)
# pen.stamp()
# pen.home()
# pen.pendown()
# pen.setheading(180)
# pen.forward(150)
# pen.clear()
# pen.circle(30)
# p2 = pen.clone()
# pen.forward(200)

# p2.back(100)

# pen.left(120)
# pen.forward(280)

# p2.left(60)
# p2.forward(280)

# pen.goto(0,200)
# pen.goto(100,200)
# pen.home()


pen.begin_poly()
for i in range(3):
    pen.forward(50)
    pen.left(120)
pen.end_poly()

vertices = pen.get_poly()
s.register_shape('my_shape', vertices)

pen.shape("my_shape")


turtle.done()
