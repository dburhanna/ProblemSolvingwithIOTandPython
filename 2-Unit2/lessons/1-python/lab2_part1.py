"""
Filename: 
Author(s):
Date:
Description:  
"""

# import the python turtle graphics module
import turtle

# make a list of colors
colors = ["red", "purple", "blue", "green", "orange", "yellow"]
# create an instance of a turtle screen called my_window
my_window = turtle.Screen()
# "set" the background color attribute of my_window to black
my_window.bgcolor("black")
# "get" the background color attribute from the my_window object
print(my_window.bgcolor())
# set the title attribute of my_window
my_window.title("A cool Turtle pattern")
# create a turle object called bob, an instance of a "Turtle"
bob = turtle.Turtle()
# set bob speed attribute to 0 - the fastet speed a turtle can go
bob.speed(0)
# create a for loop, x will take values 0-359
for x in range(360):
    # set bob color attribute by grabbing a color from colors list
    # use a little math trick (modulus) to keep cycling through 0,1,2,3,4,5
    bob.color(colors[x % 6])
    # set bob width attribute to (x/100 +1), gets "thicker" as we loop
    bob.width(x / 100 + 1)
    # move the turtle object forward the distance x each time through the loop
    bob.forward(x)
    # turn bob left 59 degrees
    bob.left(59)
