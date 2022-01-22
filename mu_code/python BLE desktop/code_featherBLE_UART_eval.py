# Provide an "eval()" service over BLE UART.

from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService

print("creating a BLE radio object...")
ble = BLERadio()

print("creating a UART service... ")
uart = UARTService()

print("create advertising for the UART service... ")
advertisement = ProvideServicesAdvertisement(uart)

while True:
    ble.start_advertising(advertisement)
    print("Waiting to connect")
    while not ble.connected:
        pass
    print("Connected")
    while ble.connected:
        s = uart.readline()
        print(s)
        if s:
            try:
                result = str(eval(s))
            except Exception as e:
                result = repr(e)
            uart.write(result.encode("utf-8"))
