#serial data logger

# import the serial module
import serial

# mac  - command to find usb port --->ls /dev/tty* | grep usb
ser = serial.Serial('/dev/tty.usbmodem11301') #create mac serial object

# windows  - use device manager to help find the right COM port
#ser = serial.Serial('COM4')		#create windows serial object

# clear the serial port
ser.flushInput()

# open and close the data_log.txt file in write mode ==> clear any old data
fh = open("data_log.txt","w")
fh.close()

# use try and except so we can exit program with ctrl-c
try:
    while True:                     # loop forever
# use .readline() method to read data from serial buffer
        ser_bytes = ser.readline()
# ser_bytes are encoded utf-8 so do a quick decoding
        decoded_bytes = ser_bytes[0:len(ser_bytes)-2].decode("utf-8")
# inform user of how to exit program
        print("Hit CTRL-C to exit data logging...")
# display decoded string
        print(decoded_bytes)
# open the data logging file in append mode
        fh = open("data_log.txt","a")
# write the data recived from the Feather Sense sensors to the data file
        fh.write(decoded_bytes + "\n")
# close the data file
        fh.close()
# if keyboard interrupt graceully exit, making sure to close the file just in case it was still open
except KeyboardInterrupt:
    print("keyboard interrupt - data logging halted")
    fh.close()
