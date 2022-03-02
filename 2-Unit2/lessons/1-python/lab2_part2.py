#
import turtle

# lots of possible colors can be found online
# e.g. https://www.discogcodingacademy.com/turtle-colours
#
colors = ["red", "purple", "blue", "green", "orange", "yellow"]
#
colors1 = ["pink", "cyan", "white", "coral", "indigo", "gold"]
#
my_window = turtle.Screen()
#
my_window.bgcolor("black")
#
print(my_window.bgcolor())
#
my_window.title("A cool Turtle pattern")
#
bob = turtle.Turtle()
sue = turtle.Turtle()
#
bob.speed(0)
sue.speed(0)
#
for x in range(360):
    #
    bob.color(colors[x % 6])
    sue.color(colors1[(x + 2) % 6])
    #
    bob.width(x / 100 + 1)
    #
    bob.forward(x)
    sue.forward(x + 5)
    #
    bob.left(59)
    sue.right(144)
