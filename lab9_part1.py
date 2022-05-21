# import board specific definitions
import board
# import busio module
import busio
# import DigitalInOut from digitalio module
from digitalio import DigitalInOut
# import esp32spi from the adafruit_esp32spi module
from adafruit_esp32spi import adafruit_esp32spi

# assign SPI communication pins for the ESP32 Airlift
esp32_cs = DigitalInOut(board.D13)
esp32_ready = DigitalInOut(board.D11)
esp32_reset = DigitalInOut(board.D12)

# create an SPI object with Feather Sense predfined pins
spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
# create an esp object tying the spi object and the esp communication pins together
esp = adafruit_esp32spi.ESP_SPIcontrol(spi, esp32_cs, esp32_ready, esp32_reset)


# notification to user...
print("Running ESP32 SPI hardware test...")

# check esp32 status to see if it is in idle mode
if esp.status == adafruit_esp32spi.WL_IDLE_STATUS:
    print("ESP32 found and in idle mode")

# acquire and print the airlift firmware verison
print("Firmware vers.", esp.firmware_version.decode("utf-8"))

#acquire and print the airlift MAC address
print("MAC addr:", [hex(i) for i in esp.MAC_address_actual])

# iterate over all access points found
# list each access point and the RSSI signal strength
for ap in esp.scan_networks():
    print("\t%s\t\tRSSI: %d" % (str(ap['ssid'], 'utf-8'), ap['rssi']))

# end program
print("Done!")
