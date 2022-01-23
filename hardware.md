# The T in IoT

To truly learn about IoT students should use a real "thing", a real device that interacts with the world around them. Beginning with Unit 3, every IoT lab in 
my curriculum is based on real-world hardware available to the school or students from Adafruit Industries. 

The physical hardware chosen from Adafruit is the **Adafruit Feather Sense** plus the **Adafruit AirLift FeatherWing**.  The Feather Sense board is great 
because it is completely packed with sensors for the students to use. During this course, students will not have to worry about wiring diagrams and connecting 
external sensors.  The Feather Sense has everything built right in.  The Feather Sense combined with the AirLift provide the student the ability to:

- connect via Bluetooth Low Energy (BLE)
- connect via WiFi
- sense temperature
- sense barometric pressure/altitude
- sense humidity
- sense sound
- sense light, proximity, color and gestures
- sense 9-DoF motion with an acceleration/gyroscopic + a magnetometer

All of this for about $50! Do not forget to check into Adafruits educational discounts as well.

## Check out current prices at Adafruit 

**[Adafruit Feather Sense](https://www.adafruit.com/product/4516)**
[![Feather Sense Image](https://cdn-shop.adafruit.com/970x728/4516-08.jpg)](https://www.adafruit.com/product/4516)





## 

![The Seeed studios logo](./images/seeed-logo.png)

Seeed Studios have very kindly made all the hardware available as easy to purchase kits:

### Arduino - Wio Terminal

**[IoT for beginners with Seeed and Microsoft - Wio Terminal Starter Kit](https://www.seeedstudio.com/IoT-for-beginners-with-Seeed-and-Microsoft-Wio-Terminal-Starter-Kit-p-5006.html)**

[![The Wio Terminal hardware kit](./images/wio-hardware-kit.png)](https://www.seeedstudio.com/IoT-for-beginners-with-Seeed-and-Microsoft-Wio-Terminal-Starter-Kit-p-5006.html)

### Raspberry Pi

**[IoT for beginners with Seeed and Microsoft - Raspberry Pi 4 Starter Kit](https://www.seeedstudio.com/IoT-for-beginners-with-Seeed-and-Microsoft-Raspberry-Pi-Starter-Kit.html)**

[![The Raspberry Pi Terminal hardware kit](./images/pi-hardware-kit.png)](https://www.seeedstudio.com/IoT-for-beginners-with-Seeed-and-Microsoft-Raspberry-Pi-Starter-Kit.html)

## Arduino

All the device code for Arduino is in C++. To complete all the assignments you will need the following:

### Arduino hardware

* [Wio Terminal](https://www.seeedstudio.com/Wio-Terminal-p-4509.html)
* *Optional* - USB-C cable or USB-A to USB-C adapter. The Wio terminal has a USB-C port and comes with a USB-C to USB-A cable. If your PC or Mac only has USB-C ports you will need a USB-C cable, or a USB-A to USB-C adapter.

### Arduino specific sensors and actuators

These are specific to using the Wio terminal Arduino device, and are not relevant to using the Raspberry Pi.

* [ArduCam Mini 2MP Plus - OV2640](https://www.arducam.com/product/arducam-2mp-spi-camera-b0067-arduino/)
* [ReSpeaker 2-Mics Pi HAT](https://www.seeedstudio.com/ReSpeaker-2-Mics-Pi-HAT.html)
* [Breadboard Jumper Wires](https://www.seeedstudio.com/Breadboard-Jumper-Wire-Pack-241mm-200mm-160mm-117m-p-234.html)
* Headphones or other speaker with a 3.5mm jack, or a JST speaker such as:
  * [Mono Enclosed Speaker - 2W 6 Ohm](https://www.seeedstudio.com/Mono-Enclosed-Speaker-2W-6-Ohm-p-2832.html)
* microSD Card 16GB or less, along with a connector to use the SD card with your computer if you don't have one built-in. **NOTE** - the Wio Terminal only supports SD cards up to 16GB, it does not support higher capacities.

## Raspberry Pi

All the device code for Raspberry Pi is in Python. To complete all the assignments you will need the following:

### Raspberry Pi hardware

* [Raspberry Pi](https://www.raspberrypi.org/products/raspberry-pi-4-model-b/)
  > 💁 Versions from the Pi 2B and above should work with the assignments in these lessons. If you are planning on running VS Code directly on the Pi, then a Pi 4 with 2GB or more of RAM is needed. If you are going to access the Pi remotely then any Pi 2B and above will work.
* microSD Card (You can get Raspberry Pi kits that come with a microSD Card), along with a connector to use the SD card with your computer if you don't have one built-in.
* USB power supply (You can get Raspberry Pi 4 kits that come with a power supply). If you are using a Raspberry Pi 4 you need a USB-C power supply, earlier devices need a micro-USB power supply.

### Raspberry Pi specific sensors and actuators

These are specific to using the Raspberry Pi, and are not relevant to using the Arduino device.

* [Grove Pi base hat](https://www.seeedstudio.com/Grove-Base-Hat-for-Raspberry-Pi.html)
* [Raspberry Pi Camera module](https://www.raspberrypi.org/products/camera-module-v2/)
* Microphone and speaker:

  Use one of the following (or equivalent):
  * Any USB Microphone with any USB speaker, or speaker with a 3.5mm jack cable, or using HDMI audio output if your Raspberry Pi is connected to a monitor or TV with speakers
  * Any USB headset with a built in microphone
  * [ReSpeaker 2-Mics Pi HAT](https://www.seeedstudio.com/ReSpeaker-2-Mics-Pi-HAT.html) with
    * Headphones or other speaker with a 3.5mm jack, or a JST speaker such as:
    * [Mono Enclosed Speaker - 2W 6 Ohm](https://www.seeedstudio.com/Mono-Enclosed-Speaker-2W-6-Ohm-p-2832.html)
  * [USB Speakerphone](https://www.amazon.com/USB-Speakerphone-Conference-Business-Microphones/dp/B07Q3D7F8S/ref=sr_1_1?dchild=1&keywords=m0&qid=1614647389&sr=8-1)
* [Grove Light sensor](https://www.seeedstudio.com/Grove-Light-Sensor-v1-2-LS06-S-phototransistor.html)
* [Grove button](https://www.seeedstudio.com/Grove-Button.html)

## Sensors and actuators

Most of the sensors and actuators needed are used by both the Arduino and Raspberry Pi learning paths:

* [Grove LED](https://www.seeedstudio.com/Grove-LED-Pack-p-4364.html) x 2
* [Grove humidity and temperature sensor](https://www.seeedstudio.com/Grove-Temperature-Humidity-Sensor-DHT11.html)
* [Grove capacitive soil moisture sensor](https://www.seeedstudio.com/Grove-Capacitive-Moisture-Sensor-Corrosion-Resistant.html)
* [Grove relay](https://www.seeedstudio.com/Grove-Relay.html)
* [Grove GPS (Air530)](https://www.seeedstudio.com/Grove-GPS-Air530-p-4584.html)
* [Grove Time of flight Distance Sensor](https://www.seeedstudio.com/Grove-Time-of-Flight-Distance-Sensor-VL53L0X.html)

## Optional hardware

The lessons on automated watering work using a relay. As an option, you can connect this relay to a water pump powered by USB using the hardware listed below.

* [6V water pump](https://www.seeedstudio.com/6V-Mini-Water-Pump-p-1945.html)
* [USB terminal](https://www.adafruit.com/product/3628)
* Silicone pipes
* Red and black wires
* Small flat-head screwdriver

## Virtual hardware

The virtual hardware route will provide simulators for the sensors and actuators, implemented in Python. Depending on your hardware availability, you can run this on your normal development device, such as a Mac, PC, or run it on a Raspberry Pi and simulate only the hardware you don't have. For example, if you have the Raspberry Pi camera but not the Grove sensors, you will be able to run the virtual device code on your Pi and simulate the Grove sensors, but use a physical camera.

The virtual hardware will use the [CounterFit project](https://github.com/CounterFit-IoT/CounterFit).

To complete these lessons you will need to have a web cam, microphone and audio output such as speakers or headphones. These can be built in or external, and need to be configured to work with your operating system and available for use from all applications.
