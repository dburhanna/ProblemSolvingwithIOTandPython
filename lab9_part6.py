
import board
import busio
from digitalio import DigitalInOut
import neopixel
from adafruit_esp32spi import adafruit_esp32spi
import adafruit_esp32spi.adafruit_esp32spi_wifimanager as wifimanager
import adafruit_esp32spi.adafruit_esp32spi_wsgiserver as server
from adafruit_wsgi.wsgi_app import WSGIApp
import time
import adafruit_bmp280
import adafruit_sht31d

# Get wifi details and more from a secrets.py file
try:
    from secrets import secrets
except ImportError:
    print("WiFi secrets are kept in secrets.py, please add them there!")
    raise

i2c = board.I2C()

bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)
sht31d = adafruit_sht31d.SHT31D(i2c)

# AirLift Featherwing
esp32_cs = DigitalInOut(board.D13)
esp32_ready = DigitalInOut(board.D11)
esp32_reset = DigitalInOut(board.D12)

spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
esp = adafruit_esp32spi.ESP_SPIcontrol(
    spi, esp32_cs, esp32_ready, esp32_reset
)

# Use below for Most Boards
pixel = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.2)

## If you want to connect to wifi with secrets:
wifi = wifimanager.ESPSPI_WiFiManager(esp, secrets, pixel)
wifi.connect()

web_app = WSGIApp()

def web_page():
    html = """<html><head><title>Feather Sense Web Server</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="icon" href="data:,"><style>body { text-align: center; font-family: "Trebuchet MS", Arial;}
    table { border-collapse: collapse; margin-left:auto; margin-right:auto; }
    th { padding: 12px; background-color: #0043af; color: white; }
    tr { border: 1px solid #ddd; padding: 12px; }
    tr:hover { background-color: #bcbcbc; }
    td { border: none; padding: 12px; }
    .sensor { color:white; font-weight: bold; background-color: #bcbcbc; padding: 1px;
    </style></head><body><h1>Feather Sense BMP280</h1>
    <table><tr><th>MEASUREMENT</th><th>VALUE</th></tr>
    <tr><td>Temp. Celsius</td><td><span class="sensor">""" + str(round(bmp280.temperature, 2)) + """ C</span></td></tr>
    <tr><td>Temp. Fahrenheit</td><td><span class="sensor">""" + str(round((bmp280.temperature) * (9/5) + 32, 2))  + """ F</span></td></tr>
    <tr><td>Baro. Pressure</td><td><span class="sensor">""" + str(round(bmp280.pressure, 2)) + """ </span></td></tr>
    <tr><td>Rel. Humidity</td><td><span class="sensor">""" + str(round((sht31d.relative_humidity), 2))  + """ %</span></td></tr>
    </table>
    <form method = "GET" action="/led_on/255/0/0">
            <button name = "LED" value = "/led_on/255/0/0" type="submit" style="height:50px;width:100px">LED ON </button>
        </form>
        <form method = "GET" action="/led_off">
            <button name = "LED" value = "/led_off" type="submit" style="height:50px;width:100px">LED OFF </button>
        </form>
        </body></html>"""
    return html


@web_app.route("/led_on/<r>/<g>/<b>")
def led_on(request, r, g, b):  # pylint: disable=unused-argument
    print("led on!")
    pixel.fill((int(r), int(g), int(b)))
    return ("200 OK", [], "Neopixel on with RGB set to: {},{},{}".format(r,g,b))


@web_app.route("/led_off")
def led_off(request):  # pylint: disable=unused-argument
    print("led off!")
    pixel.fill(0)
    return ("200 OK", [], "Neopixel off!")

@web_app.route("/blink")
def blink(request):  # pylint: disable=unused-argument
    print("blinking neopixel")
    for i in range(5):
        pixel.fill((0,0,255))
        time.sleep(.25)
        pixel.fill(0)
        time.sleep(.25)
    return ("200 OK", [], "Neopixel blinked!")

@web_app.route("/temp")
def temp(request):  # pylint: disable=unused-argument
    print("temperate request received")
    return ("200 OK", [], "Temperature is: {:.2f}".format(current_temp))

@web_app.route("/page")
def page(request):  # pylint: disable=unused-argument
    print("page request received")
    return ("200 OK", [("Content-Type","text/html")], web_page())

# Here we setup our server, passing in our web_app as the application
server.set_interface(esp)
wsgiServer = server.WSGIServer(80, application=web_app)

#print("MAC addr actual:", [hex(i) for i in esp.MAC_address_actual])

print("*"*50)
print("\tAirlift simple web server!")
print("*"*50)
print("open this IP in your browser: ", esp.pretty_ip(esp.ip_address))
print("*"*50)

# Start the server
wsgiServer.start()
while True:
    # Our main loop where we have the server poll for incoming requests
    try:
        wsgiServer.update_poll()

        current_temp = bmp280.temperature*1.8 + 32

    except (ValueError, RuntimeError) as e:
        print("Failed to update server, restarting ESP32\n", e)
        wifi.reset()
        continue
