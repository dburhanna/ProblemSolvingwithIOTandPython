import digitalio
import board
import random
import time
from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService

ble = BLERadio()
ble.name = "LAB8_FEATHER"
uart = UARTService()
advertisement = ProvideServicesAdvertisement(uart)

#prepare to use RED_LED - ideas from lab 4
led = digitalio.DigitalInOut(board.RED_LED)
led.direction = digitalio.Direction.OUTPUT
led.value = False # make sure RED_LED is off

# starting value for delay between streamed data points
delay = 10

while True:
    ble.start_advertising(advertisement)
    print("Waiting to connect")
    while not ble.connected:
        pass

    #  Now we're connected

    while ble.connected:
        x = str(random.randrange(25,50))
        uart.write(x)
        print(x)
        time.sleep(delay)

# If we got here, we lost the connection. Go up to the top and start
# advertising again and waiting for a connection.
