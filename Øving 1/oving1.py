#Input from user
name = input("Write your name: ")

#Checks wether input is valid or not
if name != "":
    # Splits the name into firstname(s) and lastname(s)
    names = name.split(" ")
    initals = ""
    for n in names:
        #Adds the first char of each name to the variable initals
        initals += (n[0].upper())

    #Prints the initials and the message welcomming the user to Python
    print("The initials of your name are: " + initals)
    print("Welcome to Python Programming, " + name)