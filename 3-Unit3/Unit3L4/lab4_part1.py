# lab4_part1


# These should have been imported already in working through part 1

import board
import digitalio
import time

# should have already been created
#create a digitalio object called led - an instance of digitalio.DigitalInOut
led = digitalio.DigitalInOut(board.RED_LED)
# should have already been set
# set the led direction to an OUTPUT
led.direction = digitalio.Direction.OUTPUT

# add this to the REPL to blink the RED_LED

for i in range(100):
    led.value = 1
    time.sleep(.5)
    led.value = 0
    time.sleep(.5)

