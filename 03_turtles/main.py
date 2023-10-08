from turtle import Turtle, Screen
from hirst_painting import color_list
import random

tur = Turtle()
screen = Screen()
screen.colormode(255)
tur.pensize(1)
tur.speed(11)
tur.penup()
tur.hideturtle()

# for _ in range(4):
#     tur.fd(100)
#     tur.lt(90)
#
# for _ in range(15):
#     tur.fd(10)
#     tur.penup()
#     tur.fd(10)
#     tur.pendown()
#
def change_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color
#
#
#
#
# for _ in range(3, 11):
#     for x in range(_):
#         tur.fd(100)
#         tur.rt(360 / _)
#     change_color()
#
# #
# for _ in range(100):
#     tur.seth(random.randint(0, 360))
#     tur.fd(random.randint(0, 50))
#     tur.color(change_color())
#     tur.pencolor(change_color())

for _ in range(0, 361, int(360 / 100)):
    tur.pencolor(change_color())
    tur.seth(_)
    tur.circle(100)

# n = 0
# x = -280
# y = -260
#
# while n < 100:
#     tur.setpos(x, y)
#     for _ in range(10):
#         tur.dot(20, random.choice(color_list))
#         n += 1
#         tur.fd(50)
#     y += 50


screen.exitonclick()
