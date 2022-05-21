# SPDX-FileCopyrightText: 2020 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT
#
"""Sensor demo for Adafruit Feather Sense. Prints data from each of the sensors."""
# import time module
import time
# import board module - pin definitions for Feather Sense
import board
# import module for pressure, temperature sensors
import adafruit_bmp280
# import module for humidity sensor
import adafruit_sht31d

# create an I2C object which will be used to talk to the many I2C connected sensors
i2c = board.I2C()

# create a bmp280 object for access to pressure and temperature sensors
bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)
# create an sht31d object for access to humidity sensor
sht31d = adafruit_sht31d.SHT31D(i2c)

# Set this to sea level pressure in hectoPascals at your location for accurate altitude reading.
bmp280.sea_level_pressure = 996.406

# create an infinite loop to read and display sensor values
while True:
# convert temperature to fahrenheit
    tempf = bmp280.temperature*1.8 +32
# output
    print("{:.2f} {:.2f} {:.2f}".format(tempf,bmp280.pressure,sht31d.relative_humidity))

# following left for reference
# use the bmp280.temperature method to get current temperature value and display
#    print("Temperature: {:.1f} C".format(bmp280.temperature))
# use the bmp280.pressure method to get current barometric pressure value and display
 #   print("Barometric pressure:", bmp280.pressure)
# use the bmp280.altitude method to get current altitude value and display
# use the sht31d.relative_humidity method to get current humidity value and display
#    print("Humidity: {:.1f} %".format(sht31d.relative_humidity))
# call the normalized_rms function on the sound samples array to get an average sound level and display



# pause the program 5 seconds
    time.sleep(10)
