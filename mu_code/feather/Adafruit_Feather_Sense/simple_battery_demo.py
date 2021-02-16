'''
simple_battery_demo.py
Feb 15, 2021

Simple demo file that checks battery_voltage of connected battery
and displays in a while loop
No fancy formatting of OLED display just text from print statements
5 lines - 18 characters each are available
lines autowrap
fills from bottom left corner and scrolls up
'''

print('Running Battery Demo...')

import board
from analogio import AnalogIn
import time
import displayio
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

vbat_voltage = AnalogIn(board.VOLTAGE_MONITOR)


def get_voltage(pin):
    return (pin.value * 3.3) / 65536 * 2

while True:
    battery_voltage = get_voltage(vbat_voltage)
    print("\n\n\nVBat voltage:{:.2f}".format(battery_voltage))
    time.sleep(5)

