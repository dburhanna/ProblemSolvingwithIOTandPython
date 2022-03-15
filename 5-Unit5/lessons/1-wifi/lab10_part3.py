# SPDX-FileCopyrightText: 2019 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import busio
import random
from digitalio import DigitalInOut
import neopixel
from adafruit_esp32spi import adafruit_esp32spi
from adafruit_esp32spi import adafruit_esp32spi_wifimanager

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

status_light = neopixel.NeoPixel(
    board.NEOPIXEL, 1, brightness=0.2
)

wifi = adafruit_esp32spi_wifimanager.ESPSPI_WiFiManager(esp, secrets, status_light)

print("*"*60)
print("\tFeather Airlift HTTP to AIO test")
print("*"*60)

first_run = True

while True:
    try:
        print("Posting data...", end="")
        data = random.randint(25,50)
        feed = "random-value"
        payload = {"value": data}
        response = wifi.post(
            "https://io.adafruit.com/api/v2/"
            + secrets["aio_username"]
            + "/feeds/"
            + feed
            + "/data",
            json=payload,
            headers={"X-AIO-KEY": secrets["aio_key"]},
        )
#        print(response.json())
        response.close()
        print("OK")
    except (ValueError, RuntimeError) as e:
        print("Failed to get data, retrying\n", e)
        wifi.reset()
        continue
    response = None
    try:
        print("Getting data...", end="")
        feed = "output"
        response = wifi.get(
            "https://io.adafruit.com/api/v2/"
            + secrets["aio_username"]
            + "/feeds/"
            + feed,
            headers={"X-AIO-KEY": secrets["aio_key"]},
        )
#        print(response.json())
#        print(response.json()['last_value'])
        if first_run == True:
            last_update = response.json().get('updated_at')
#            print(last_update)
            first_run = False
        if response.json().get('updated_at') == last_update:
            command = ""
        else:
            last_update = response.json().get('updated_at')
            command = response.json().get('last_value')
            print("Got new command:",command, end="...")
#        print(response.json().get('last_value'))
        response.close()
        print("OK")
    except (ValueError, RuntimeError) as e:
        print("Failed to get data, retrying\n", e)
        wifi.reset()
        continue
    response = None
#    print(command)
    if command == "PAUSE":
        print("pausing now...")
        for i in range(30):
            status_light.fill((255,0,0))
            time.sleep(1)
            status_light.fill(0)
            time.sleep(1)
        commmand = ""
        print("resume transmission...")
    else:
        time.sleep(10)
