# feather ble uart code
# put on feather sense board

import board
import neopixel

from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService

ble = BLERadio()
# this will be the advertisement name when advertising begins
ble.name = "LAB7_FEATHER"

uart = UARTService()
advertisement = ProvideServicesAdvertisement(uart)

pixels = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.1)
off_color = (0,0,0)
pixels.fill(off_color)
# default current_color
default_color = (255,255,255)
current_color = default_color

while True:
    ble.start_advertising(advertisement)
    print("Waiting to connect")
    while not ble.connected:
        pass
    print("Connected")
    while ble.connected:
        command = uart.readline().decode("utf-8")
        if command:
            print(command)
            if "on" in command:
                print(ble.name+ " received: " +command)
                uart.write("NeoPixel on.")
                pixels.fill(current_color)

            elif "off" in command:
                print(ble.name+ " received: " +command)
                uart.write("NeoPixel off.")
                pixels.fill(off_color)

            elif "red" in command:
                print(ble.name+ " received: " +command)
                uart.write("NeoPixel is red.")
                current_color = (255,0,0)
                pixels.fill(current_color)

            elif "blue" in command:
                print(ble.name+ " received: " +command)
                uart.write("NeoPixel is blue.")
                current_color = (0,0,255)
                pixels.fill(current_color)

            elif "green" in command:
                print(ble.name+ " received: " +command)
                uart.write("NeoPixel is green.")
                current_color = (0,255,0)
                pixels.fill(current_color)

            elif "default" in command:
                print(ble.name+ " received: " +command)
                uart.write("NeoPixel on default_color.")
                current_color = default_color
                pixels.fill(current_color)

