# Unit 3 - CircuitPython

Unit 3 will introduce students to the actual "IoT device" for the first time.  The Adafruit Feather 
Sense is a microcontroller with built-in Bluetooth Low Energy and a long list of sensors.  
An Adafruit Airlift FeatherWing needs to be added to give the IoT device WiFi connectivity for later labs.

Teachers should plan well in advance to prepare the necessary hardware for this and all later 
labs in the curriculum. The first requirement is to acquire the necessary components.  A parts 
list with Adafruit part numbers is provided below.  Adafruit offers both quantity and educational 
discounts to educators.


* Adafruit Feather Sense microcontroller - Adafruit PRODUCT ID: 4516
* Adafruit Airlift FeatherWing - Adafruit PRODUCT ID: 4264
* Stacking headers - Adafruit PRODUCT ID: 2830
* Micro B USB Cable - Adafruit PRODUCT ID: 592 or 3878

With these items students will be able to explore all labs in the curriculum.  You may be able to 
purchase both the Feather Sense microcontroller and the Airlift FeatherWing with the stacking headers 
soldered on already for an added cost.  I typically purchase the headers separately, so I can determine 
how I want to stack my Feathers and FeatherWings. I have provided a brief soldering tips video to help 
those choosing to solder on headers themselves.

Once the Feather Sense and FeatherWing are assembled, teachers will need to update both the version of 
CircuitPython installed on the Feather Sense and install the required libraries onto the Feather Sense.  
The great thing about CircuitPython devices is they appear as USB storage devices when plugged into a 
PC or Apple host computer.  Most files can be moved and copied as if the Feather Sense was a USB thumb 
drive.  I have provided brief videos highlighting both updating CircuitPython and installing the required 
libraries.

To prepare to update CircuitPython go to https://circuitpython.org/board/feather_bluefruit_sense/ and 
download the latest stable release of CircuitPython for the Feather Sense.  Adafruit has a guide for 
updating the version of CircuitPython available here: https://learn.adafruit.com/adafruit-feather-sense/circuitpython-on-feather-sense .

To prepare to install the necessary libraries go to: https://circuitpython.org/libraries and download 
the library bundle that match the version of CircuitPython you used for the update.  You will download 
a zip archive that will decompress into a new folder with a few other folders inside.  You will find all 
the libraries inside the \lib folder.

For labs 4 - 8 the following libraries need to be copied from the downloaded bundle into the \lib folder 
on the CircuitPython device.

Required Libraries:

* adafruit_apds9960
* adafruit_bmp280.mpy
* adafruit_bus_device
* adafruit_lis3mdl.mpy
* adafruit_lsm6ds
* adafruit_register
* adafruit_sht31d.mpy
* neopixel.mpy


To protect the IoT device, teachers can choose to optionally  install the Feather Sense and 
Airlift into an enclosure.  Adafruit provides a guide here: 
https://learn.adafruit.com/3d-printed-case-for-adafruit-feather .  CAD models for the 3D printable 
Feather boxes are provided and are fully parametric. These parametric models can be 
opened and customized in AutoDesk Fusion 360. If 3D printing capabilities are not available in-house, 
teachers can go to: https://www.hubs.com/ or to: https://www.makexyz.com/ to have the enclosures 
printed by locally sourced suppliers.

The following additional video resources are provided to help the teacher prepare the Feather 
Sense and FeatherWing hardware for all future labs:

* Video - Feather and FeatherWing Assembly
* Video - Soldering tips
* Video - Updating CircuitPython on the Feather Sense
* Video - Updating CircuitPython libraries on the Feather Sense

## Unit 3 Labs

4. [Unit 3 Lab 4 - Intro to CircuitPython](Unit3L4/)
5. [Unit 3 Lab 5 - Explore the Adafruit Feather Sense](Unit3L5/)
