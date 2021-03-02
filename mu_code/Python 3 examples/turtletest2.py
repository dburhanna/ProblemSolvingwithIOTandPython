# Write your code here :-)
#import turtle as t
import turtle
t1 = turtle.Turtle()
t2 = turtle.Turtle()
t1.speed(0)
t2.speed(0)
wn = turtle.Screen()
wn.bgcolor("light green")
wn.title("My Super Duper Turtle")
skk = turtle.Turtle()

color1="red"
color2 ="green"
t1.color(color1)
#color(color1)
'''
for i in range(67):
    t1.forward(67)
    t2.right(59)
    t1.right(59)
    t2.forward(67)
'''
# Python program to draw hexagon
# using Turtle Programming

polygon = turtle.Turtle()

num_sides = 10
side_length = 50
angle = 360.0 / num_sides

for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)

skk = turtle.Turtle()
skk.color("blue")

def sqrfunc(size):
    for i in range(4):
        skk.fd(size)
        skk.left(90)
        size = size-5

sqrfunc(146)
sqrfunc(126)
sqrfunc(106)
sqrfunc(86)
sqrfunc(66)
sqrfunc(46)
sqrfunc(26)
