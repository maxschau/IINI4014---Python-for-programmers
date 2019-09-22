import math
import turtle

def PointsInCircumList(r, n=150, multiplier=2): #Method which generates a list with the x and y positions of the dots on the perimeter
    return [(math.cos(2*math.pi/n*x)*r, math.sin(2*math.pi/n*x)*r) for x in range(0, n+1)]


def PointsInCircum(r, n=150, multiplier=2):
    for x in range(0, n+1):
        yield ((math.cos(2*math.pi/n*x)*r), (math.sin(2*math.pi/n*x)*r))
        next_pos = ((multiplier * x) % n)



def draw_times_table(multiplier, amt):
    homex = -0
    homey = -250

    list1 = PointsInCircumList(250, amt)

    turtle.penup()
    turtle.speed(10)
    turtle.color("cyan")
    turtle.goto(homex, homey)
    turtle.pendown()
    turtle.circle(250)
    turtle.penup()

    turtle.goto(homex,homey)
    counter = 0

    for i in PointsInCircum(250, amt, multiplier):
        turtle.setpos(i[0], i[1])
        turtle.pendown()
        turtle.dot()

        new_pos_index = ((multiplier * counter) % amt)
        turtle.pendown()
        turtle.setpos(list1[new_pos_index][0], list1[new_pos_index][1])
        turtle.penup()

        turtle.dot()
        counter += 1

    turtle.done()


draw_times_table(34, 200)




