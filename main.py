import colorgram
import turtle as t
from random import randint, choice
timmy = t.Turtle()
screen = t.Screen()
timmy.setposition(0, 0)
timmy.shape("turtle")
timmy.color("red")
timmy.speed(0)
t.colormode(255)

color_list = [(198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5), (229, 159, 46), (27, 40, 157),
              (215, 74, 12), (15, 154, 16), (199, 14, 10), (243, 33, 165), (229, 17, 121), (73, 9, 31), (60, 14, 8),
              (224, 141, 211), (10, 97, 61), (221, 160, 9), (17, 18, 43), (46, 214, 232), (11, 227, 239), (81, 73, 214),
              (238, 156, 220), (74, 213, 167), (77, 234, 202), (52, 234, 243), (3, 67, 40)]
timmy.penup()
timmy.setheading(225)
timmy.fd(300)
timmy.setheading(0)
timmy.hideturtle()
for i in range(10):
    for i in range(10):
        timmy.dot(20, choice(color_list))
        timmy.fd(50)
    timmy.setheading(90)
    timmy.fd(50)
    timmy.setheading(180)
    timmy.fd(500)
    timmy.setheading(0)





screen.exitonclick()





# for i in range(200):
#     timmy.color(rand_col())
#     timmy.fd(30)
#     timmy.setheading(choice(directions))

# for i in range(50):
#     timmy.color(rand_col())
#     timmy.left(10)
#     timmy.circle(100)

# def rand_col():
#     r = randint(0, 255)
#     g = randint(0, 255)
#     b = randint(0, 255)
#     randcol = (r, g, b)
#     return randcol


# colors = colorgram.extract("image.jpg", 30)
# new = []
# for a in range(len(colors)):
#     ne = colors[a]
#     rbg = ne.rgb
#     temp = (rbg[0], rbg[1], rbg[2])
#     new.append(temp)
#
# print(new)






