# Write your code here :-)
"""
Used with ble_uart_echo_test.py. Transmits "echo" to the UARTService and receives it back.
"""

import time

from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService

ble = BLERadio()
while True:
    while ble.connected and any(
        UARTService in connection for connection in ble.connections
    ):
        for connection in ble.connections:
            if UARTService not in connection:
                continue
            print("cheeseburger")
            uart = connection[UARTService]
            uart.write(b"cheeseburger")
            # Returns b'' if nothing was read.
            one_byte = uart.read(12)
            if one_byte:
                print(one_byte)
            print()
        time.sleep(1)

    print("disconnected, scanning")
    for advertisement in ble.start_scan(ProvideServicesAdvertisement, timeout=1):
        print(advertisement.complete_name)
        if UARTService not in advertisement.services:
            continue
        ble.connect(advertisement)
        print("connected")
        break
    ble.stop_scan()
