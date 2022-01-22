#
import turtle

#
colors = ["red", "purple", "blue", "green", "orange", "yellow"]
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
#
# print(bob.speed())
sue.speed(0)
#
for x in range(360):
    #
    bob.color(colors[x % 6])
    sue.color(colors[(x + 2) % 6])
    #
    #    print(bob.color())
    #
    bob.width(x / 100 + 1)
    #
    bob.forward(x)
    sue.forward(x + 5)
    #
    #    print(bob.position())
    #
    bob.left(59)
    sue.right(144)
