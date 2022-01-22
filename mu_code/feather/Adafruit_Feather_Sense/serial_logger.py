#serial data logger script
# use with Mu lab 5
#mac command to find usb port --->ls /dev/tty* | grep usb
#windows use device manager

import serial

ser = serial.Serial('/dev/tty.usbmodem11401')
ser.flushInput()

fh = open("data_log.txt","w")


while True:
    try:
        ser_bytes = ser.readline()
        print("Hit CTRL-C to save and close data file..")
        decoded_bytes = ser_bytes[0:len(ser_bytes)-2].decode("utf-8")
        print(decoded_bytes)

        fh.write(decoded_bytes+"\n")

    except:
        print("keyboard interrupt")
        fh.close()
        break



