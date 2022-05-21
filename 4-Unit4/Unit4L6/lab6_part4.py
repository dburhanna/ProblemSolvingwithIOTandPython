
import board
import neopixel
from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService

from adafruit_bluefruit_connect.packet import Packet
from adafruit_bluefruit_connect.button_packet import ButtonPacket
from adafruit_bluefruit_connect.color_packet import ColorPacket

ble = BLERadio()
ble.name = "TEST_FEATHER"

uart = UARTService()
advertisement = ProvideServicesAdvertisement(uart)

#prepare neopixel
pixels = neopixel.NeoPixel(board.NEOPIXEL,1,brightness = .25)
#initialize current_color variable with black/off
current_color = (0,0,0)
pixels.fill(current_color)

while True:
    ble.start_advertising(advertisement)
    while not ble.connected:
        pass

    # Now we're connected

    while ble.connected:
        if uart.in_waiting:
            packet = Packet.from_stream(uart)
            if isinstance(packet, ButtonPacket):
                if packet.pressed:
                    if packet.button == ButtonPacket.BUTTON_1:
                        #pixel[0] = (255,0,0)
                        # The 1 button was pressed.
                        print("1 button pressed!")
                    elif packet.button == ButtonPacket.UP:
                        pixels.fill(current_color)
                        # The UP button was pressed.
                        print("UP button pressed!")
                    elif packet.button == ButtonPacket.DOWN:
                        pixels.fill((0,0,0))
                        # The DOWN button was pressed.
                        #led.value = False
                        print("DOWN button pressed!")
                    elif packet.button == ButtonPacket.LEFT:
                        # The LEFT button was pressed.
                        print("LEFT button pressed!")
                    elif packet.button == ButtonPacket.RIGHT:
                        # The RIGHT button was pressed.
                        print("RIGHT button pressed!")
                    elif packet.button == ButtonPacket.BUTTON_2:
                        #pixel[0] = (0,255,0)
                        # The 2 button was pressed.
                        print("2 button pressed!")
                    elif packet.button == ButtonPacket.BUTTON_3:
                        #pixel[0] = (0,0,255)
                        # The 3 button was pressed.
                        print("3 button pressed!")
                    elif packet.button == ButtonPacket.BUTTON_4:
                        #pixel[0] = (255,255,255)
                        # The 4 button was pressed.
                        print("4 button pressed!")
            elif isinstance(packet, ColorPacket):
                current_color=packet.color
                pixels.fill(current_color)
# If we got here, we lost the connection. Go up to the top and start
# advertising again and waiting for a connection.
