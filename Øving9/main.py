import random
import turtle

class Dice:
    def __init__(self, x_pos, y_pos, size):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.size = size


    def randomValue(self):
        return random.randint(1,6)

    def drawDie(self):
        t = turtle.Turtle()
        t.penup()
        t.setpos(self.x_pos, self.y_pos)
        t.pendown()
        '''
        Draws the square
        '''
        for i in range(4):
            t.forward(self.size)
            t.right(90)

        number = self.randomValue()

        if number == 1:
            t.penup()

        turtle.done()



dice = Dice(-100,200,200)
dice.drawDie()

