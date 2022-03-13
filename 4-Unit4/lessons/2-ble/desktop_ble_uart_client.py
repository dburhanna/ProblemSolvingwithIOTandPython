# SPDX-FileCopyrightText: 2020 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

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
        UARTService in connection for connection in ble.connections):
        for connection in ble.connections:
            if UARTService not in connection:
                continue
            print("sending echo")
            uart = connection[UARTService]
            uart.write(b"echo")
            # Returns b'' if nothing was read.
            one_byte = uart.readline()
            if one_byte:
                # convert bytearray to string
                data_string = ''.join([chr(b) for b in one_byte])
                #print(data_string,end='')
                print("I received "+data_string,end='')
            print()
        time.sleep(1)

    print("disconnected, scanning")
    for advertisement in ble.start_scan(ProvideServicesAdvertisement, timeout=1):
            print(advertisement.address, advertisement.complete_name)
        if UARTService not in advertisement.services:
            continue
        if advertisement.complete_name == "LAB7_FEATHER":
            ble.connect(advertisement)
            print("connected to:",advertisement.complete_name)
        break
    ble.stop_scan()
