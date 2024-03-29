import time
import board
import busio
from digitalio import DigitalInOut, Direction
import adafruit_esp32spi.adafruit_esp32spi_socket as socket
from adafruit_esp32spi import adafruit_esp32spi
import adafruit_requests as requests
from adafruit_io.adafruit_io import IO_HTTP, AdafruitIO_RequestError

try:
    from secrets import secrets
except ImportError:
    print("WiFi secrets are kept in secrets.py, please add them there!")
    raise

# AirLift Featherwing
esp32_cs = DigitalInOut(board.D13)
esp32_ready = DigitalInOut(board.D11)
esp32_reset = DigitalInOut(board.D12)

spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
esp = adafruit_esp32spi.ESP_SPIcontrol(spi, esp32_cs, esp32_ready, esp32_reset)

print("Connecting to AP...")
while not esp.is_connected:
    try:
        esp.connect_AP(secrets["ssid"], secrets["password"])
    except RuntimeError as e:
        print("could not connect to AP, retrying: ", e)
        continue
print("Connected to", str(esp.ssid, "utf-8"), "\tRSSI:", esp.rssi)

socket.set_interface(esp)
requests.set_socket(socket, esp)

# Set your Adafruit IO Username and Key in secrets.py
# (visit io.adafruit.com if you need to create an account,
# or if you need your Adafruit IO key.)
aio_username = secrets["aio_username"]
aio_key = secrets["aio_key"]

# Initialize an Adafruit IO HTTP API object
io = IO_HTTP(aio_username, aio_key, requests)

try:
    # Get the 'digital' feed from Adafruit IO
    digital_feed = io.get_feed("digital")
except AdafruitIO_RequestError:
    # If no 'digital' feed exists, create one
    digital_feed = io.create_new_feed("digital")

# Set up LED
LED = DigitalInOut(board.BLUE_LED)
LED.direction = Direction.OUTPUT

while True:
    # Get data from 'digital' feed
    print("getting data from IO...")
    feed_data = io.receive_data(digital_feed["key"])

    # Check if data is ON or OFF
    if int(feed_data["value"]) == 1:
        print("received <- ON\n")
    elif int(feed_data["value"]) == 0:
        print("received <= OFF\n")

    # Set the LED to the feed value
    LED.value = int(feed_data["value"])

    time.sleep(10)
