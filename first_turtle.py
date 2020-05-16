import turtle
# print("Hello World, this is Turtle")

wn = turtle.Screen()
alex = turtle.Turtle()
alex.color('green')


angle = 90
for _ in range(250):
    alex.back(20)
    alex.forward(200)
    alex.left(angle+1)             # turn by 90 degrees


# james = turtle.Turtle()
# james.setx(200)

# james.dot(size=5)
# alex.down()
# # james = alex.clone()
# # james.fd(25.00, 50.00)
# james.color('blue')
# col = turtle.pencolor()

# james.fillcolor(col)
# angle = 120
# for _ in range(10):
#     james.back(15)
#     james.forward(120)
#     james.left(angle+1)             # turn by 90 degrees
wn.exitonclick()
