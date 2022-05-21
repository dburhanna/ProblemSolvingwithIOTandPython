# Lab4_part2.py
# blinking both red led and neopixel

# import necessary modules
import board
import digitalio
import neopixel
import time

#create a digitalio object called led - an instance of digitalio.DigitalInOut
led = digitalio.DigitalInOut(board.RED_LED)

# set the led direction to an OUTPUT
led.direction = digitalio.Direction.OUTPUT

#create a neopixel object called pixel - an instance of neopixel.NeoPixel
pixel = neopixel.NeoPixel(board.NEOPIXEL,1,brightness = .25)

# create a for loop
for i in range(100):
    led.value = 1           # turn led on
    pixel[0] = (0,0,255)    # turn neopixel blue
    time.sleep(.5)          # delay .5 seconds
    led.value = 0           # turn led off
    pixel[0] = (255,127,0)  # turn neopixel yellow'ish
    time.sleep(.5)          # delay .5 seconds

