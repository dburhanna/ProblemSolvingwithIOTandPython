'''
simple_menu_demo.py
Feb 15, 2021

Simple demo file that uses buttons A,B, and C for a simple menu on OLED

No fancy formatting of OLED display
5 lines - 18 characters each are available
lines autowrap
fills from bottom left corner and scrolls up
'''

print('Running Menu Demo...')

import time
import board
import displayio
from digitalio import DigitalInOut, Direction, Pull
from adafruit_display_text import label
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

def select_A():
    time.sleep(.2)
    print("\nA selected")
    print("Hit A again end")
    while button_A.value:
        pass
    time.sleep(.2)


def select_B():
    time.sleep(.2)
    print("\nB selected")
    print("Hit B again end")
    while button_B.value:
        pass
    time.sleep(.2)


def select_C():
    time.sleep(.2)
    print("\nC selected")
    print("Hit C again end")
    while button_C.value:
        pass
    time.sleep(.2)


def show_menu():
    time.sleep(.2)
    print("A:Select A")
    print("B:Select B")
    print("C:Select C")
    while button_A.value and button_B.value and button_C.value:
        pass
    if button_A.value == False:
        time.sleep(.2)
        select_A()
    elif button_B.value == False:
        time.sleep(.2)
        select_B()
    else:
        time.sleep(.2)
        select_C()
    return

'''
led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT
# blinky code
while True:
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(0.5)
'''
count=0
while True:
    count+=1

#    print(button_A.value,button_B.value,button_C.value)

    print("\ncount = ",count)
    print("\nHit A for menu")
    if button_A.value == False:
        time.sleep(.2)
        show_menu()
    time.sleep(1)
    if count>=999:
        count = 0
