# SPDX-FileCopyrightText: 2020 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""
Used with code provided in lab handout for Feather sense.
Transmits word2send to the UARTService and
receives a response from Feather
"""

import time

from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService

ble = BLERadio()

word2send = "hello"
receive = False

while True:
    while ble.connected and any(
        UARTService in connection for connection in ble.connections
    ):
        for connection in ble.connections:
            if UARTService not in connection:
                continue
            command = input("Command to send Feather ('temp_on' to start data streaming) : ")
            print("sending: "+command)
            uart = connection[UARTService]
            uart.write(command.encode("utf-8"))
            if command == "temp_on":
                receive = True
            while receive:
                response = uart.readline()
                if response:
                    # convert bytearray to string
                    data_string = ''.join([chr(b) for b in response])
                    #print(data_string,end='')
                    print(data_string)
            print()
        time.sleep(1)

    print("disconnected, scanning")
    for advertisement in ble.start_scan(ProvideServicesAdvertisement, timeout=1):
        #print(advertisement.address, advertisement.complete_name)
        if UARTService not in advertisement.services:
            continue
        if advertisement.complete_name == "LAB7_FEATHER":
            ble.connect(advertisement)
            print("connected to:",advertisement.complete_name)
        break
    ble.stop_scan()
