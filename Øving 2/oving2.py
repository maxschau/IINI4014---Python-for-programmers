import math

#A possibility is to to run the function until a specific amount of decimals are similar

#The parameter i will determine how many times we will run the for loop, the larger i, the more accurate the anser
def ArchimedesPI(i):
    if i > 0:
        new_side = 1 #Start value for new_side
        n = 6 #Start value for number of sides
        for numbers in range(0, i):
            s = new_side
            half_of_s = s/2
            a = math.sqrt(1-(math.pow(half_of_s, 2)))
            b = 1-a
            new_side = math.sqrt((math.pow(b, 2) + math.pow(half_of_s, 2)))
            p = n*s
            estimate = p/2
            n = n * 2  #Updating the number of sides
        return estimate
    else:
        return "i must be over 0"





