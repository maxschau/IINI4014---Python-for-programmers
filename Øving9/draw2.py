from tkinter import *
import random

class Dice:
    def __init__(self, x_pos, y_pos, size):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.size = size


    def randomValue(self):
        return random.randint(1,6)

    def create_circle(self, x, y, r, canvasName, fillInp = "black"):  # center coordinates, radius
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        return canvasName.create_oval(x0, y0, x1, y1, fill=fillInp)



    def drawDice(self, color_dice = "white", color_dots = "black"):
        master = Tk()
        canvas_width = self.size + 10 ;
        canvas_height = self.size + 10;
        w = Canvas(master, width = canvas_width, height = canvas_height)
        w.create_rectangle(self.x_pos, self.y_pos, self.x_pos + self.size, self.y_pos + self.size, fill = color_dice)

        number = self.randomValue()

        if number == 1:
            self.create_circle((self.x_pos + self.size)/2, (self.y_pos + self.size)/2, (self.size/20), w, fillInp=color_dots)
        elif number == 2:
            self.create_circle((self.x_pos + self.size)/2, (self.y_pos + self.size)/3, (self.size/20), w, fillInp=color_dots)
            self.y_pos+= self.size/1.02
            self.create_circle((self.x_pos + self.size)/2, (self.y_pos + self.size)/3, (self.size/20), w, fillInp=color_dots)
        elif number == 3:
            x = self.x_pos + self.size/3
            y = self.y_pos + self.size/3
            self.create_circle(x, y, (self.size/20), w, fillInp=color_dots)
            self.create_circle((self.x_pos + self.size) / 2, (self.y_pos + self.size) / 2, (self.size / 20), w, fillInp=color_dots)
            x += (self.size * (1/3))
            y += (self.size * (1/3))
            self.create_circle(x,y,(self.size/20), w, fillInp=color_dots)
        elif number == 4:
            x = self.x_pos + self.size / 4
            y = self.y_pos + self.size / 4
            self.create_circle(x, y, (self.size/20), w, fillInp=color_dots)
            self.create_circle(x + (self.size/2), y, (self.size / 20), w, fillInp=color_dots)
            self.create_circle(x, y + (self.size/2), (self.size / 20), w, fillInp=color_dots)
            self.create_circle(x + (self.size/2), y + (self.size/2), (self.size / 20), w, fillInp=color_dots)
        elif number == 5:
            x = self.x_pos + self.size / 4
            y = self.y_pos + self.size / 4
            self.create_circle(x, y, (self.size / 20), w, fillInp=color_dots)
            self.create_circle(x + (self.size / 2), y, (self.size / 20), w, fillInp=color_dots)
            self.create_circle(x, y + (self.size / 2), (self.size / 20), w, fillInp=color_dots)
            self.create_circle(x + (self.size / 2), y + (self.size / 2), (self.size / 20), w, fillInp=color_dots)
            self.create_circle((self.x_pos + self.size)/2, (self.y_pos + self.size)/2, (self.size/20), w, fillInp=color_dots)
        else:
            x = self.x_pos + self.size / 4
            y = self.y_pos + self.size / 4
            self.create_circle(x, y, (self.size/20), w, fillInp=color_dots)
            self.create_circle(x + (self.size/2), y, (self.size / 20), w, fillInp=color_dots)
            self.create_circle(x, (y + self.size) / 2.45 , self.size / 20, w, fillInp=color_dots)
            self.create_circle(x + (self.size / 2), (y + self.size) / 2.45, self.size / 20, w, fillInp=color_dots)
            self.create_circle(x, y + (self.size/2), (self.size / 20), w, fillInp=color_dots)
            self.create_circle(x + (self.size/2), y + (self.size/2), (self.size / 20), w, fillInp=color_dots)



        w.pack()
        mainloop()


dice = Dice(5,5, 800)
dice.drawDice(color_dice="pink", color_dots="yellow")