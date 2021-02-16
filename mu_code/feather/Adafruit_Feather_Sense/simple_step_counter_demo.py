'''
simple_step_counter_demo.py
Feb 15, 2021

Simple demo mimics a step counter and displays current steps on OLED
looks at x axis acceleration only here

A button resets count to 0

C button shows .pedometer_steps from accelerometer

No fancy formatting of OLED display
5 lines - 18 characters each are available
lines autowrap
fills from bottom left corner and scrolls up
'''

print('Running Step Demo...')

import time
import array
import math
import board
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

lsm6ds33 = adafruit_lsm6ds.lsm6ds33.LSM6DS33(i2c)

#setup buttons
button_A = DigitalInOut(board.D9)
button_B = DigitalInOut(board.D6)
button_C = DigitalInOut(board.D5)
button_A.direction = Direction.INPUT
button_A.pull = Pull.UP
button_B.direction = Direction.INPUT
button_B.pull = Pull.UP
button_C.direction = Direction.INPUT
button_C.pull = Pull.UP

# enable built in pedometer mode of accelerometer
lsm6ds33.pedometer_enable = True

count = 0
print("\n\ncount = ",count)
oldacc_x,oldacc_y,oldacc_z = lsm6ds33.acceleration
while True:

#    print("Acceleration: {:.2f} {:.2f} {:.2f} m/s^2".format(*lsm6ds33.acceleration))
#    print("Gyro: {:.2f} {:.2f} {:.2f} dps".format(*lsm6ds33.gyro))
    acc_x,acc_y,acc_z = lsm6ds33.acceleration
#    print("(",acc_x,",",acc_y,",",acc_z,")")
    delta_acc_x = acc_x-oldacc_x
    oldacc_x,oldacc_y,oldacc_z = acc_x,acc_y,acc_z
    if delta_acc_x > 4.5:
        count = count+1
        print("\n\ncount = ",count)
    time.sleep(.05)
    if button_A.value ==False:
        time.sleep(.2)
        count = 0
        print("\n\ncount = ",count)
    time.sleep(.05)

    if button_C.value == False:
        print("\n\nsteps =",lsm6ds33.pedometer_steps)
        time.sleep(5)
