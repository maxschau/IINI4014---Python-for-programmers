from tkinter import *
import random


class Dice:
    def __init__(self, x_pos, y_pos, size):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.size = size

    '''
    Method to get a random value between 1 and 6
    '''

    def randomValue(self):
        return random.randint(1, 6)

    '''
    Method to draw a circle based on tkinter's method create oval
    '''

    def create_circle(self, x, y, r, canvasName, fillInp="black"):  # center coordinates, radius
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        return canvasName.create_oval(x0, y0, x1, y1, fill=fillInp)

    '''
    Method to draw the dice
    '''

    def drawDice(self, color_dice="white", color_dots="black"):
        master = Tk()
        canvas_width = self.size + 10  # I want the height and width of the canvas to be sligthly higher than the size
        # of the dice
        canvas_height = self.size + 10
        w = Canvas(master, width=canvas_width, height=canvas_height)
        #Creates a rectangle which will be the dice itself
        w.create_rectangle(self.x_pos, self.y_pos, self.x_pos + self.size, self.y_pos + self.size, fill=color_dice)

        number = self.randomValue()

        #Several if/else sentences to draw the dots based on the number of dots we need

        if number == 1:
            #Draws a dot at the center of the dice
            self.create_circle((self.x_pos + self.size) / 2, (self.y_pos + self.size) / 2, (self.size / 20), w,
                               fillInp=color_dots)
        elif number == 2:
            #Draws to circle at the middle of the screen
            self.create_circle((self.x_pos + self.size) / 2, (self.y_pos + self.size) / 3, (self.size / 20), w,
                               fillInp=color_dots)
            self.y_pos += self.size / 1.02
            self.create_circle((self.x_pos + self.size) / 2, (self.y_pos + self.size) / 3, (self.size / 20), w,
                               fillInp=color_dots)
        elif number == 3:
            #Divides the dice in three and places each dot in that part. Moves to y-position down when we draw the next dot
            x = self.x_pos + self.size / 3
            y = self.y_pos + self.size / 3
            self.create_circle(x, y, (self.size / 20), w, fillInp=color_dots)
            self.create_circle((self.x_pos + self.size) / 2, (self.y_pos + self.size) / 2, (self.size / 20), w,
                               fillInp=color_dots)
            x += (self.size * (1 / 3))
            y += (self.size * (1 / 3))
            self.create_circle(x, y, (self.size / 20), w, fillInp=color_dots)
        elif number == 4:
            #Divides the dice into four and places the dots
            x = self.x_pos + self.size / 4
            y = self.y_pos + self.size / 4
            self.create_circle(x, y, (self.size / 20), w, fillInp=color_dots)
            self.create_circle(x + (self.size / 2), y, (self.size / 20), w, fillInp=color_dots)
            self.create_circle(x, y + (self.size / 2), (self.size / 20), w, fillInp=color_dots)
            self.create_circle(x + (self.size / 2), y + (self.size / 2), (self.size / 20), w, fillInp=color_dots)
        elif number == 5:
            #Draws a four-dice and a one-dice to get the five-dice.
            x = self.x_pos + self.size / 4
            y = self.y_pos + self.size / 4
            self.create_circle(x, y, (self.size / 20), w, fillInp=color_dots)
            self.create_circle(x + (self.size / 2), y, (self.size / 20), w, fillInp=color_dots)
            self.create_circle(x, y + (self.size / 2), (self.size / 20), w, fillInp=color_dots)
            self.create_circle(x + (self.size / 2), y + (self.size / 2), (self.size / 20), w, fillInp=color_dots)
            self.create_circle((self.x_pos + self.size) / 2, (self.y_pos + self.size) / 2, (self.size / 20), w,
                               fillInp=color_dots)
        else:
            #Draws the three dots on one side, and the rest on the other.
            x = self.x_pos + self.size / 4
            y = self.y_pos + self.size / 4
            self.create_circle(x, y, (self.size / 20), w, fillInp=color_dots)
            self.create_circle(x + (self.size / 2), y, (self.size / 20), w, fillInp=color_dots)
            self.create_circle(x, (y + self.size) / 2.45, self.size / 20, w, fillInp=color_dots)
            self.create_circle(x + (self.size / 2), (y + self.size) / 2.45, self.size / 20, w, fillInp=color_dots)
            self.create_circle(x, y + (self.size / 2), (self.size / 20), w, fillInp=color_dots)
            self.create_circle(x + (self.size / 2), y + (self.size / 2), (self.size / 20), w, fillInp=color_dots)

        w.pack()
        mainloop()


dice = Dice(5, 5, 800)
dice.drawDice(color_dice="pink", color_dots="yellow")
