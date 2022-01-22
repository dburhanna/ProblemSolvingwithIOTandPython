#esp local time getter

import time
import board
import busio
from digitalio import DigitalInOut
import neopixel
from adafruit_esp32spi import adafruit_esp32spi
from adafruit_esp32spi import adafruit_esp32spi_wifimanager
import rtc

# Get wifi details and more from a secrets.py file
try:
    from secrets import secrets
except ImportError:
    print("WiFi secrets are kept in secrets.py, please add them there!")
    raise

print("ESP32 local time")

TIME_API = "http://worldtimeapi.org/api/ip"

# If you have an AirLift Featherwing or ItsyBitsy Airlift:
esp32_cs = DigitalInOut(board.D13)
esp32_ready = DigitalInOut(board.D11)
esp32_reset = DigitalInOut(board.D12)

spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
esp = adafruit_esp32spi.ESP_SPIcontrol(spi, esp32_cs, esp32_ready, esp32_reset)
"""Use below for Most Boards"""
#status_light = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.2) # Uncomment for Most Boards
"""Uncomment below for ItsyBitsy M4"""
#status_light = dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=0.2)
# Uncomment below for an externally defied RGB LED
import adafruit_rgbled
from adafruit_esp32spi import PWMOut
RED_LED = PWMOut.PWMOut(esp, 26)
GREEN_LED = PWMOut.PWMOut(esp, 27)
BLUE_LED = PWMOut.PWMOut(esp, 25)
status_light = adafruit_rgbled.RGBLED(RED_LED, BLUE_LED, GREEN_LED)
status_light.color = (0,255,0)
time.sleep(5)

wifi = adafruit_esp32spi_wifimanager.ESPSPI_WiFiManager(esp, secrets, status_light)

the_rtc = rtc.RTC()

response = None
while True:
    try:
        print("Fetching json from", TIME_API)
        response = wifi.get(TIME_API)
        break
    except (ValueError, RuntimeError) as e:
        print("Failed to get data, retrying\n", e)
        continue

json = response.json()
current_time = json['datetime']
the_date, the_time = current_time.split('T')
year, month, mday = [int(x) for x in the_date.split('-')]
the_time = the_time.split('.')[0]
hours, minutes, seconds = [int(x) for x in the_time.split(':')]

# We can also fill in these extra nice things
year_day = json['day_of_year']
week_day = json['day_of_week']
is_dst = json['dst']

now = time.struct_time((year, month, mday, hours, minutes, seconds, week_day, year_day, is_dst))
print(now)
the_rtc.datetime = now

while True:
    print(time.localtime())
    time.sleep(28)
