# CP lab 1 code samples

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

for i in range(100):
    led.value = 1
    pixel[0] = (0,0,255)
    time.sleep(.5)
    led.value = 0
    pixel[0] = (255,127,0)
    time.sleep(.5)

