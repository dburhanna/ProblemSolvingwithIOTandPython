'''
Spend some time introducing the students to the Mu editor and then the Python REPL.

Use the REPL - Read, Evaluate, Print, Loop to do some on the fly calculations.

Do some math.

make and use variables

Output with the print() command.

Use the input() command to get some input values.

Use an if statement to control an output.

Demonatrate a while loop

Demonstrate a for loop

create random tuple values and use the "plotter" in Mu to visualize the data

'''
import random
import time

while True:
    val1 = random.randrange(15,25)
    val2 = random.randrange(5,15)
    data_tuple = (val1,val2)
    print(data_tuple)
    time.sleep(1)
