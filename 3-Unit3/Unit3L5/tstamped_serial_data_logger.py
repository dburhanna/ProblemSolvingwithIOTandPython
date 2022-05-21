#serial data logger
import serial

# mac  - command to find usb port --->ls /dev/tty* | grep usb
ser = serial.Serial('/dev/tty.usbmodem11301') #create mac serial object

# windows  - use device manager to help find the right COM port
#ser = serial.Serial('COM4')		#create windows serial object

#clear the serial port
ser.flushInput()

fh = open("data_log.txt","w")
fh.close()


try:
    while True:
        ser_bytes = ser.readline()
        decoded_bytes = ser_bytes[0:len(ser_bytes)-2].decode("utf-8")
        print("Hit CTRL-C to exit data logging...")
        print(decoded_bytes)
        fh = open("data_log.txt","a")
        fh.write(decoded_bytes + "\n")
        fh.close()
except KeyboardInterrupt:
    print("keyboard interrupt - data logging halted")
    fh.close()
