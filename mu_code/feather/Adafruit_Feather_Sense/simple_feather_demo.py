'''
simple_feather_demo.py
Feb 12, 2021

Simple demo file that reads temperature and barometric pressure from bmp280
and outputs to OLED using just print.
No fancy formatting of OLED display
5 lines - 18 characters each are available
lines autowrap
fills from bottom left corner and scrolls up
'''

print('Running Simple Demo...')

#Simple demo for Adafruit Feather Sense. Prints data from bmp280 sensor.
import time
import board
import adafruit_bmp280
import displayio
import terminalio
from digitalio import DigitalInOut, Direction, Pull
from adafruit_display_text import label
import adafruit_displayio_sh1107

i2c = board.I2C()
bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)

# Set this to sea level pressure in hectoPascals at your location for accurate altitude reading.
bmp280.sea_level_pressure = 1013.25
#bmp280.sea_level_pressure = 1016.25


displayio.release_displays()
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)

# SH1107 is vertically oriented 64x128
WIDTH = 128
HEIGHT = 64
BORDER = 2

display = adafruit_displayio_sh1107.SH1107(display_bus, width=WIDTH, height=HEIGHT)



#setup buttons
button_A = DigitalInOut(board.D9)
button_B = DigitalInOut(board.D6)
button_C = DigitalInOut(board.D5)
#time.sleep(5)

i=0
while True:
#    i+=1
#    print(i, end="")
    print("\nTemp: {:.1f} C".format(bmp280.temperature))
    print("BaP:", bmp280.pressure)
    print("Temp: {:.1f} C".format(bmp280.temperature))
    print("BaP:", bmp280.pressure)
    print("Line 5 here...",end = "")
    time.sleep(5)

# getting input from all other sensors examples below

#    samples = array.array('H', [0] * 160)
#    microphone.record(samples, len(samples))
#    print("Proximity:", apds9960.proximity)
#    print("Red: {}, Green: {}, Blue: {}, Clear: {}".format(*apds9960.color_data))
#    print("Altitude: {:.1f} m".format(bmp280.altitude))
#    print("Magnetic: {:.3f} {:.3f} {:.3f} uTesla".format(*lis3mdl.magnetic))
#    print("Acceleration: {:.2f} {:.2f} {:.2f} m/s^2".format(*lsm6ds33.acceleration))
#    print("Gyro: {:.2f} {:.2f} {:.2f} dps".format(*lsm6ds33.gyro))
#    print("Humidity: {:.1f} %".format(sht31d.relative_humidity))
#    print("Sound level:", normalized_rms(samples))

