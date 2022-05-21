
import time
import board
import busio
import neopixel
from random import randint
from digitalio import DigitalInOut
from adafruit_esp32spi import adafruit_esp32spi
from adafruit_esp32spi import adafruit_esp32spi_wifimanager
import adafruit_esp32spi.adafruit_esp32spi_socket as socket
import adafruit_minimqtt.adafruit_minimqtt as MQTT
from adafruit_io.adafruit_io import IO_MQTT

# Get wifi details and more from a secrets.py file
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

# set up neopixel as wifi status_light
status_light = neopixel.NeoPixel(
    board.NEOPIXEL, 1, brightness=0.2
)

# initialize wifi manager
wifi = adafruit_esp32spi_wifimanager.ESPSPI_WiFiManager(esp, secrets, status_light)

# Connect to WiFi
print("*"*70)
print("\tConnecting to WiFi...", end=" ")
wifi.connect()
print("Connected!")
print("*"*70)

# Define callback functions which will be called when certain events happen.
def connected(client):
    # Connected function will be called when the client is connected to Adafruit IO.
    # This is a good place to subscribe to feed changes.  The client parameter
    # passed to this function is the Adafruit IO MQTT client so you can make
    # calls against it easily.

    print("Connected to Adafruit IO!")
    print("*"*70)
    # Subscribe to changes on random-value feed
    client.subscribe("random-value")

def subscribed(client, userdata, topic, granted_qos):
    # This method is called when the client subscribes to a new feed.
    print("Subscribed to {0} with QOS level {1}".format(topic, granted_qos))

def unsubscribed(client, userdata, topic, pid):
    # This method is called when the client unsubscribes from a feed.
    print("Unsubscribed from {0} with PID {1}".format(topic, pid))

def disconnected(client):
    # Disconnected function will be called when the client disconnects.
    print("Disconnected from Adafruit IO!")

def message(client, feed_id, payload):
    # Message function will be called when a subscribed feed has a new value.
    # The feed_id parameter identifies the feed, and the payload parameter has
    # the new value.
    print("Feed {0} received new value: {1}".format(feed_id, payload))

# Initialize MQTT interface with the esp interface
MQTT.set_socket(socket, esp)

# Initialize a new MQTT Client object
mqtt_client = MQTT.MQTT(
    broker="io.adafruit.com",
    username=secrets["aio_username"],
    password=secrets["aio_key"],
)

# Initialize an Adafruit IO MQTT Client
io = IO_MQTT(mqtt_client)

# Connect the callback functions defined above to Adafruit IO MQTT client
io.on_connect = connected
io.on_disconnect = disconnected
io.on_subscribe = subscribed
io.on_unsubscribe = unsubscribed
io.on_message = message

# Connect to Adafruit IO
print("\tConnecting to Adafruit IO...", end=" ")
io.connect()
print("*"*70)

# initialize variable for delay loop
last = 0
# this is a blocking loop, any code below this while loop will never run
print("Publishing a new random_value every 10 seconds...")
while True:
    try:
        # Explicitly pump the message loop.
        io.loop()

    except (ValueError, RuntimeError) as e:
        print("Failed to get data, retrying\n", e)
        wifi.reset()
        io.reconnect()
        continue
    # Send a new message every 10 seconds.
    if (time.monotonic() - last) >= 10:
            value = randint(25, 50)
            print("Publishing {0} to random_value.".format(value))
            io.publish("random-value", value)
            last = time.monotonic()
