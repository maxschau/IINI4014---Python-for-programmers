import turtle


def hermann_grid(grid_colour, squares_colour, circle_colour, image_size, squares_size, grid_size):
    '''
    hermann_grid will draw the hermann grid illusion based on the parameters given by the user
    :param grid_colour: the colour of the grid which is drawen
    :param squares_colour: the colour of the squares
    :param circle_colour: the colour of the circle in the intersections
    :param image_size: the size of the image (both length and width)
    :param squares_size: the size of each square
    :param grid_size: the size of each grid
    :return:
    '''

    '''
    Defining the turtle
    '''
    t = turtle.Turtle()
    screen = turtle.Screen()
    screen.setup(width=1.0, height=1.0)  # Sets the screen to fullscreen

    x_values = []  # List to keep track of the x-values of the grids
    y_values = []  # List to keep track of the y-values of the grids

    startY = 200  # The start-position (Y) of the square
    startX = -100  # The start-position (X) of the square

    x = startX  # Variable which will be used to change the position (x) later
    y = startY  # Variable which will be used to change the position (y) later
    t.speed(1000)

    t.penup()
    t.setpos(x, y)  # Initializes the turtle
    t.pendown()

    t.fillcolor(squares_colour)
    t.begin_fill()
    for i in range(4):  # Draws the square
        t.forward(image_size)
        t.left(270)

    t.end_fill()
    t.pencolor(grid_colour)
    t.pensize(grid_size)

    '''
    Draws the horizontal lines of the grid
    Will run until we reach the side of the square
    '''

    while y > startY - image_size + squares_size:
        t.penup()
        y -= squares_size  # Updates the y-variable
        t.setpos(startX, y)  # Moves the turtle
        t.pendown()
        y_values.append(y)  # Want to keep track of each y-value
        t.setpos(startX + image_size, y)  # Draws the line by moving the turtle to the side of the square

    '''
    Draws the vertical lines of the grid
    Will run until we reach the side of the square
    '''

    while x < startX + image_size - squares_size:
        t.penup()
        x += squares_size  # Updates the x-variable
        t.setpos(x, startY)  # Moves the turtle
        t.pendown()
        x_values.append(x)  # Want to keep track of each x-value
        t.setpos(x, startY - image_size)  # Draws the line by moving the turtle to the bottom of the square

    '''
    Draws the circles in the intersections
    For each x-value we want to draw an circle per y-value, which will be the intersections
    '''
    for i in range(len(x_values)):
        t.pencolor(circle_colour) #Chooses the colur of the circles
        t.penup()
        for j in range(len(y_values)):
            t.setpos(x_values[i], y_values[j]) #Moves to each intersection
            t.pendown()
            t.circle(1) #Draws the circle
            t.penup()

    turtle.done()


hermann_grid("white", "black", "grey", 500, 30, 2)
