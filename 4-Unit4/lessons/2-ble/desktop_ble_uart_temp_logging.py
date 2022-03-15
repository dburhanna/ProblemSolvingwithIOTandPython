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

# open and close the data_log.txt file in write mode ==> clear any old data
fh = open("lab7_data_log.txt","w")
fh.close()

word2send = "hello"
receive = False

while True:
    while ble.connected and any(
        UARTService in connection for connection in ble.connections
    ):
        for connection in ble.connections:
            if UARTService not in connection:
                continue
            command = input("Command to send Feather ('temp_on' to start data streaming, 'delay #' to change delay) : ")
            print("sending: "+command)
            uart = connection[UARTService]
            uart.write(command.encode("utf-8"))
            if command == "temp_on":
                receive = True

            # use try and except so we can exit program with ctrl-c
            try:
                while receive:                     # loop forever

                    response = uart.readline()
                    if response:
                        # convert bytearray to string
                        data_string = ''.join([chr(b) for b in response])
                        # display decoded string
                        print(data_string)
                        # get current time_tuple using .localtime() method
                        time_tuple = time.localtime()
                        # format time as string using .strftime() method
                        time_string = time.strftime("%m/%d/%Y - %H:%M:%S", time_tuple)
                        # open the data logging file in append mode
                        fh = open("lab7_data_log.txt","a")
                        # write the time_string concatenated with data received from the Feather Sense sensors to the data file
                        fh.write(time_string + " " + data_string + "\n")
                        # close the data file
                        fh.close()
                        # inform user of how to exit program
                        print("Hit CTRL-C to exit data logging...")
            # if keyboard interrupt graceully exit, making sure to close the file just in case it was still open
            except KeyboardInterrupt:
                print("keyboard interrupt - data logging halted")
                receive = False
                print("sending: temp_off")
                uart.write("temp_off".encode("utf-8"))
                fh.close()

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
