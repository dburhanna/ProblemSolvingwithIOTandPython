"""
Filename: lab2_part3.py
Author:
Date:
Description: Makes a few turtles that stamp randomly on the background.
"""
#Imports what is needed.
import turtle
import random

#Defines the predetermined lists of shapes and colors.
colors = ["red", "purple", "blue", "green", "orange", "yellow", "white", "gray"]
shapes = ["arrow", "circle", "triangle", "square", "turtle", "classic"]
bgcolors = ["red", "purple", "blue", "green", "orange", "yellow", "white", "gray", "black"]

#Creats a new window.
my_window = turtle.Screen()

#Names the window.
my_window.title("A cool Turtle pattern")

#creates 3 turtle objects.
turtle1 = turtle.Turtle()
turtle2 = turtle.Turtle()
turtle3 = turtle.Turtle()

#Sets the speed of the 3 turtles.
turtle1.speed(0)
turtle2.speed(0)
turtle3.speed(0)

for x in range(15):
    #Clears the background, randomizes a new color, and changes the bgcolor to the new random one.
    my_window.clearscreen()
    # get a random bgcolor
    bgcolorrand = random.randrange(0, 9)
    my_window.bgcolor(bgcolors[bgcolorrand])

    for x in range(25):
        #Randomizes all x and y values for the turtles.
        x1 = random.randrange(-400, 400)
        x2 = random.randrange(-400, 400)
        x3 = random.randrange(-400, 400)
        y1 = random.randrange(-300, 300)
        y2 = random.randrange(-300, 300)
        y3 = random.randrange(-300, 300)
        #Randomizes all the turtle colors.
        color1 = random.randrange(0,8)
        color2 = random.randrange(0,8)
        color3 = random.randrange(0,8)
        #Randomizes all the turtle shapes.
        shape1 = random.randrange(0,6)
        shape2 = random.randrange(0,6)
        shape3 = random.randrange(0,6)
        #Puts the penup so lines aren't drawn anywhere.
#        turtle1.penup()
        turtle2.penup()
 #       turtle3.penup()
        #Goes to a random position.
        turtle1.goto(x1, y1)
        turtle2.goto(x2, y2)
        turtle3.goto(x3, y3)
        #Puts the pen back down.
        turtle1.pendown()
        turtle2.pendown()
        turtle3.pendown()
        #Changes color and shape to the previously defined random numbers.
        turtle1.color(colors[color1])
        turtle2.color(colors[color2])
        turtle3.color(colors[color3])
        turtle1.shape(shapes[shape1])
        turtle2.shape(shapes[shape2])
        turtle3.shape(shapes[shape3])
        #Stamps the window at the random position.
        turtle1.stamp()
        turtle2.stamp()
        turtle3.stamp()

