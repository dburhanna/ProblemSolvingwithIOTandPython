import time
import board
import busio
import neopixel
import random
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

status_light = neopixel.NeoPixel(
    board.NEOPIXEL, 1, brightness=0.2
)

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
    # Get the 'output' feed from Adafruit IO
    output_feed = io.get_feed("output")
except AdafruitIO_RequestError:
    # If no 'output' feed exists, create one
    output_feed = io.create_new_feed("output")

try:
    # Get the 'random_value' feed from Adafruit IO
    random_val_feed = io.get_feed("random-value")
except AdafruitIO_RequestError:
    # If no 'output' feed exists, create one
    random_val_feed = io.create_new_feed("random-value")

try:
    # Get the 'output' feed from Adafruit IO
    tx_feed = io.get_feed("tx")
except AdafruitIO_RequestError:
    # If no 'output' feed exists, create one
    tx_feed = io.create_new_feed("tx")

first_run = True
response = io.send_data(output_feed["key"],"RUN")

while True:
    # create new random value
    rand_data = random.randint(25,50)
    print("sending data to AIO...")
    response = io.send_data(random_val_feed["key"],rand_data)

    # check output feed for PAUSE command
    print("reading output data feed from AIO...")
    response = io.get_feed(output_feed["key"])
#    print(response)
    # on first run, get the last update time
    if first_run == True:
            last_update = response.get('updated_at')
#            print(last_update)
            first_run = False
    # if no new update, no command
    if response.get('updated_at') == last_update:
        command = ""
    else:  # if new update, get the command from the output feed
        last_update = response.get('updated_at')
        command = response.get('last_value')
        print("Got new command:",command)

    # if command is to PAUSE, then do it!
    if command == "PAUSE":
        print("pausing now...")
        for i in range(30):
            status_light.fill((255,0,0))
            time.sleep(1)
            status_light.fill(0)
            time.sleep(1)
        commmand = ""
        print("resume transmission...")
        response = io.send_data(output_feed["key"],"RUN")
    else:
        time.sleep(10)

