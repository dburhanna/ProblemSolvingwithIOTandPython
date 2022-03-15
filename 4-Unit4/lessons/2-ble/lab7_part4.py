# feather ble uart code
# put on feather sense board

import board
import neopixel
import time
# import module for pressure, temperature sensors
import adafruit_bmp280
from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService

# create an I2C object which will be used to talk to the many I2C connected sensors
i2c = board.I2C()

# create a bmp280 object for access to pressure and temperature sensors
bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)

ble = BLERadio()
# this will be the advertisement name when advertising begins
ble.name = "LAB7_FEATHER"

uart = UARTService()
advertisement = ProvideServicesAdvertisement(uart)

pixels = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.05)
off_color = (0,0,0)
pixels.fill(off_color)
on_color = (255,0,0)

transmit = False
delay_time = 5

while True:
    ble.start_advertising(advertisement)
    print("Waiting to connect")
    while not ble.connected:
        pass
    print("Connected")
    while ble.connected:
        if uart.in_waiting:
            command = uart.readline().decode("utf-8")
            print(command)
            if "temp_on" in command:
                print(ble.name+ " received: " +command)
                #uart.write("Beginning data transmission")
                transmit = True

            if "temp_off" in command:
                print(ble.name+ " received: " +command)
                transmit = False

            if "delay" in command:
                print(ble.name+ " received: " +command)
                command_aslist = command.split()
                delay_time = int(command_aslist[-1])
                print("setting delay to: " +str(delay_time))

        if transmit:
            pixels.fill(on_color)
            tempf = bmp280.temperature*1.8 +32
            uart.write("{:.2f}".format(tempf))
            #print("{:.2f} {:.2f} {:.2f}".format(tempf,bmp280.pressure,sht31d.relative_humidity))
            pixels.fill(off_color)
            time.sleep(delay_time)

