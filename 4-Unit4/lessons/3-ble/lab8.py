import digitalio
import board
import random
import time
from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService

ble = BLERadio()
uart = UARTService()
advertisement = ProvideServicesAdvertisement(uart)

#prepare to use RED_LED - ideas from lab 4
led = digitalio.DigitalInOut(board.RED_LED)
led.direction = digitalio.Direction.OUTPUT
led.value = False # make sure RED_LED is off

# starting value for delay between streamed data points
delay = 9

while True:
    ble.start_advertising(advertisement)
    while not ble.connected:
        pass

    #  Now we're connected

    while ble.connected:
        x = str(random.randrange(25,50))
        uart.write(x)
        print(x)
        time.sleep(1)
        if uart.in_waiting:
            command = uart.readline().decode("utf-8")
            print(command)
            if command == "PAUSE":
                print("Over limit, pausing for 1 minute...")
                for i in range(30):
                    led.value = 1
                    time.sleep(1)
                    led.value = 0
                    time.sleep(1)
                print("Resuming...")
            elif "FASTER" in command:
                delay = delay -5
                if delay <5:
                    delay = 4
                print("Sampling faster. Current delay = {}".format(delay+1))
                time.sleep(delay)
            elif "SLOWER" in command:
                delay = delay + 5
                if delay >30:
                    delay = 29
                print("Sampling slower. Current delay = {}".format(delay+1))
                time.sleep(delay)
            else:
                time.sleep(delay)
        else:
            time.sleep(delay)
 # If we got here, we lost the connection. Go up to the top and start
# advertising again and waiting for a connection.
