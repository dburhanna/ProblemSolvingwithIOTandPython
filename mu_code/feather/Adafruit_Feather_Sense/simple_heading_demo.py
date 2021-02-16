'''
simple_heading_demo.py
Feb 15, 2021

Simple demo that displays a heading on OLED
using magnetometer data

No fancy formatting of OLED display
5 lines - 18 characters each are available
lines autowrap
fills from bottom left corner and scrolls up
'''

print('Running Heading Demo...')

import time
import array
from math import atan2, degrees
import board
import adafruit_lis3mdl
import adafruit_lsm6ds.lsm6ds33
import displayio
from digitalio import DigitalInOut, Direction, Pull
import adafruit_displayio_sh1107

#set up I2C for OLED display and initialize the display
i2c = board.I2C()
displayio.release_displays()
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)

# OLED SH1107 is vertically oriented 64x128
WIDTH = 128
HEIGHT = 64
BORDER = 2

# after this line, the OLED should display print statements
display = adafruit_displayio_sh1107.SH1107(display_bus, width=WIDTH, height=HEIGHT)

sensor = adafruit_lis3mdl.LIS3MDL(i2c)

def vector_2_degrees(x, y):
    angle = degrees(atan2(y, x))
    if angle < 0:
        angle += 360
    return angle


def get_heading(_sensor):
    magnet_x, magnet_y, magnet_z = sensor.magnetic
    return vector_2_degrees(magnet_x, magnet_y)


while True:
    print("heading: {:.2f}".format(get_heading(sensor)))
    time.sleep(0.2)
