# CTI 110
# M5T1 - Turtle Shapes
# Chanell Custodio
# 10/24/17
# Create a turtle and get it to create a triangle and square

def main():

    import turtle               # Allows us to use turtles
    wn = turtle.Screen()        # Creates a playground for turtles
    billybob = turtle.Turtle()  # Create a turtle, assign to billybob

    # Display options
    billybob.pensize(3)         # increase pensize (takes integer)
    billybob.pencolor("orange")   # set pencolor (takes string)
    billybob.shape("turtle")

    # Create variable for loop
    loop = 0

    # Create loop to that repeats the steps to make the square
    while loop < 5:
        billybob.forward(50)
        billybob.left(90)
        loop = loop + 1
    
    billybob.forward(50)
    billybob.left(30)
    billybob.forward(50)
    billybob.left(120)
    billybob.forward(50)
    billybob.left(30)
    
    # End commands
    wn.mainloop()             # Wait for user to close window


# Run program
main()
