# CTI 110
# M5T1 - Turtle Initials
# Chanell Custodio
# 11/2/17
# Create a turtle and get it to create the shape of my initials "CC"

def main():

    import turtle               # Allows us to use turtles
    wn = turtle.Screen()        # Creates a playground for turtles
    george = turtle.Turtle()    # Create a turtle, assign to george

    # Display options
    george.pensize(3)           # increase pensize (takes integer)
    george.pencolor("purple")   # set pencolor (takes string)
    george.shape("turtle")
   
    # Create loop to that repeats the steps to make the "C"


    for loop in range(2):
        george.forward(50)
        george.left(90)
        george.forward(25)
        george.backward(25)
        george.right(90)
        george.backward(50)
        george.left(90)
        george.forward(100)
        george.right(90)
        george.forward(50)
        george.right(90)
        george.forward(25)
        george.left(90)
        george.penup()
        george.forward(30)
        george.right(90)
        george.forward(75)
        george.left(90)
        george.pendown()
    
    
    # End commands
    wn.mainloop()             # Wait for user to close window


# Run program
main()

