# Provide an "eval()" service over BLE UART.

from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
#from adafruit_ble.services.standard.device_info import DeviceInfoService
from adafruit_ble.services.nordic import UARTService

#device_info = DeviceInfoService(software_revision=adafruit_ble.__version__,manufacturer="Adafruit Industries")

ble = BLERadio()
ble.name = "DCB_FEATHER"  # this will be the advertisement name when advertising begins

uart = UARTService()
advertisement = ProvideServicesAdvertisement(uart)


while True:
    ble.start_advertising(advertisement)
    print("Waiting to connect")
    while not ble.connected:
        pass
    print("Connected")
    while ble.connected:
        s = uart.readline()
        if s:
            data_string = "".join([chr(b) for b in s])
            print(data_string)
        uart.write("yes!\n")

#        if s:
#            try:
#                result = str(eval(s))
#            except Exception as e:
#                result = repr(e)
#            uart.write(result.encode("utf-8"))
