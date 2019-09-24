import math
import turtle


def PointsInCircum(r, n=150):
    return [(math.cos(2*math.pi/n*x)*r, math.sin(2*math.pi/n*x)*r) for x in range(0, n+1)]


def draw_times_table(multiplier, amt):
    homex = -0
    homey = -250


    list1 = PointsInCircum(250, amt)

    #turtle.setpos(list1[0][0], list1[0][1])
    turtle.penup()
    turtle.speed(10)
    turtle.color("cyan")
    turtle.goto(homex, homey)
    turtle.pendown()
    turtle.circle(250)
    turtle.penup()

    turtle.goto(homex,homey)
    turtle.goto(list1[0][0], list1[0][1])
    counter = 0

    for i in list1:
        turtle.penup()
        turtle.setpos(i[0], i[1])
        turtle.dot()
        turtle.pendown()

        new_pos_index = ((multiplier * counter) % amt)

        turtle.setpos(list1[new_pos_index][0], list1[new_pos_index][1])
        turtle.dot()
        counter += 1

    turtle.done()


draw_times_table(2, 10)

