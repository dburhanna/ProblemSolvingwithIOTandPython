# SPDX-FileCopyrightText: 2020 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT
#
"""Sensor demo for Adafruit Feather Sense. Prints data from each of the sensors."""
# import time module
import time
#import array module - used with sound sensor
import array
# import math module - use math.sqrt for sound level calculation
import math
# import board module - pin definitions for Feather Sense
import board
# import audiobusio module for recording sound
import audiobusio
# import module for light, color sensors
import adafruit_apds9960.apds9960
# import module for pressure, temperature sensors
import adafruit_bmp280
# import module for magnetic field sensors
import adafruit_lis3mdl
# import module for acceleration and gyro
import adafruit_lsm6ds.lsm6ds33
# import module for humidity sensor
import adafruit_sht31d

# create an I2C object which will be used to talk to the many I2C connected sensors
i2c = board.I2C()

# create an apds9960 object for access to the light and color sensors
apds9960 = adafruit_apds9960.apds9960.APDS9960(i2c)
# create a bmp280 object for access to pressure and temperature sensors
bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)
# create a lis3mdl object for access to magnetic field sensors
lis3mdl = adafruit_lis3mdl.LIS3MDL(i2c)
# create a lsm6ds33 object for access to acceleration and gyro sensors
lsm6ds33 = adafruit_lsm6ds.lsm6ds33.LSM6DS33(i2c)
# create an sht31d object for access to humidity sensor
sht31d = adafruit_sht31d.SHT31D(i2c)
# create a microphone object for access to sound data
microphone = audiobusio.PDMIn(board.MICROPHONE_CLOCK, board.MICROPHONE_DATA,
                              sample_rate=16000, bit_depth=16)

# define a function to normalize / average an arry of sampled sounds from the microphone sensor
def normalized_rms(values):
    minbuf = int(sum(values) / len(values))
    return int(math.sqrt(sum(float(sample - minbuf) *
                             (sample - minbuf) for sample in values) / len(values)))

# enable the apds9960 proximity sensor
apds9960.enable_proximity = True
# enable the apds9960 color sensor
apds9960.enable_color = True

# Set this to sea level pressure in hectoPascals at your location for accurate altitude reading.
bmp280.sea_level_pressure = 996.406

# create an infinite loop to read and display sensor values
while True:
    # initialize a samples array to hold sound samples
    samples = array.array('H', [0] * 160)
    # fill the samples array with the microphone.record method
    microphone.record(samples, len(samples))

# output
    print("\nFeather Sense Sensor Demo")
    print("---------------------------------------------")
# use the apds9960.proximity method to get current proximity value and display
    print("Proximity:", apds9960.proximity)
# use the apds9960.color_data method to get a tuple of the current color_data values
# unpack tuple with * operator and display
    print("Red: {}, Green: {}, Blue: {}, Clear: {}".format(*apds9960.color_data))
# use the bmp280.temperature method to get current temperature value and display
    print("Temperature: {:.1f} C".format(bmp280.temperature))
# use the bmp280.pressure method to get current barometric pressure value and display
    print("Barometric pressure:", bmp280.pressure)
# use the bmp280.altitude method to get current altitude value and display
    print("Altitude: {:.1f} m".format(bmp280.altitude))
# use the lis3mdl.magnetic method to get a tuple of the current magnetic field values
# unpack tuple with * operator and display
    print("Magnetic: {:.3f} {:.3f} {:.3f} uTesla".format(*lis3mdl.magnetic))
# use the lsm6ds33.acceleration method to get a tuple of the current acceleration values
# unpack tuple with * operator and display
    print("Acceleration: {:.2f} {:.2f} {:.2f} m/s^2".format(*lsm6ds33.acceleration))
# use the lsm6ds33.gyro method to get a tuple of the current gyro values
# unpack tuple with * operator and display
    print("Gyro: {:.2f} {:.2f} {:.2f} dps".format(*lsm6ds33.gyro))
# use the sht31d.relative_humidity method to get current humidity value and display
    print("Humidity: {:.1f} %".format(sht31d.relative_humidity))
# call the normalized_rms function on the sound samples array to get an average sound level and display
    print("Sound level:", normalized_rms(samples))
# pause the program 5 seconds
    time.sleep(5)
