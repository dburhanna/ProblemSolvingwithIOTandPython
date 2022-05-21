
<!-- license image not correct......... -->
<!-- Readme intro file for IoT curriculum -->


[![GitHub license](https://img.shields.io/github/license/dburhanna/test)](LICENSE)


# Problem Solving with the Internet of Things and Python

## A Curriculum

The course will take the student on a problem solving journey programming Internet of Things devices with Python.  

This curriculum was specifically built with the new or inexperienced teacher in mind.  I have tried to provide a 
complete package of learning targets, slides and labs with solutions
for a teacher to use and modify.  Each lab, especially the hardware specific labs, will come with extra 
support documentation and videos to help **teach the teacher**.  

While I do believe teaching a class of students in a group setting is advantageous since they will be able to bounce 
ideas off each other and will generally have more fun, this curriculum can also be used by the motivated individual 
student.

## Course Structure and Pedagogy

This curriculum is broken down into 6 units designed to be taught over an entire 15-week semester.  
Each unit is made up of multiple lessons, many of which are labs. The labs are key to providing the hands-on, 
experiential learning which has been proven to help students understand and remember. During this course the students 
will work, most likely in groups, to complete a series of IoT labs which expose them to both BLE and WiFi connected
IoT devices.  

## Prerequisites 
My goal was to make a curriculum with minimal cost. I targeted open source and cost effective solutions so teachers 
everywhere could hopefully benefit without needing to request thousands of dollars for equipment or licensing fees.

### Software - Development Environment
The [Mu editor](https://codewith.mu/en/) was chosen as the integrated development environment for the course.  
Mu is free to download and can be used on multiple platforms.

### Software - Python
This curriculum was originally designed to be a second semester continuation to a first semester introduction to 
programming with [Python](https://www.python.org/).  I wanted to add something hands-on and real-world to better 
engage the class.  Python is one of the most popular programming languages and definitely has easier to understand 
syntax than other languages typically used for IoT such as Arduino, C or C++.  Even if your students do not have 
prior experience with Python, the course contains a unit of Python review as the development environment is introduced 
to the students.  You can choose to spend as much or as little time as necessary in this unit.  There are many Python 
curriculums available already for the teacher that plans on using this course as it was originally designed.
The IoT devices will be programmed in a variant of Python called [CircuitPython](https://www.circuitpython.org/).
### Hardware 

When it comes to adding some real-world experiences for your students, you need to use real-world devices.  
This can be an intimidating and time-consuming process even for an experienced engineer.  Just choosing the 
"thing" you want to use for IoT is not an easy task since there are many possibilities today.  
**I looked for a low-cost "thing' that could be programmed with Python.** 
Thankfully, [Adafruit Industries](https://www.adafruit.com/) has been leading the way by developing small, 
low-cost microcontroller boards that can be programmed with [CircuitPython](https://circuitpython.org/).  
I know much of this "hardware" stuff may be completely foreign to many teachers.  
My curriculum should provide all you need to feel comfortable working with microcontrollers and helping your 
students understand the IoT concepts.  You can read more about the hardware chosen and check on 
current prices on the [hardware page](./hardware.md)

## Each unit includes:

- Clearly defined learning targets
- PowerPoint slides
- Step-by-step lab guides (and solutions) 
- Teach the teacher videos


## Possible pacing guidelines

| Week |                 Unit                 |             Topics             | Learning Objectives                                                              |                            Linked Lessons                            |
|:----:|:------------------------------------:|:------------------------------:|----------------------------------------------------------------------------------|:--------------------------------------------------------------------:|
|  1   | [1 - Introduction to IoT](./1-Unit1) |      Course Introduction       | Learn the basic principles of IoT and the basic building blocks of IoT solutions |    [Welcome to IoT](./1-Unit1/lessons/1-welcome-to-iot/README.md)    |
|  1   | [1 - Introduction to IoT](./1-Unit1) |          What is IoT?          | Learn more about the components of an IoT system,                                | [IoT is all around us](./1-Unit1/lessons/2-iot-all-around/README.md) |
|  1   | [1 - Introduction to IoT](./1-Unit1) |        IoT Connectivity        | Learn about sensors to                                                           |    [Even more about IoT](./1-Unit1/lessons/3-more-iot/README.md)     |
|  2   | [1 - Introduction to IoT](./1-Unit1) |  IoT Communication Protocols   | Learn the basic principles of IoT and the basic building blocks of IoT solutions |    [Welcome to IoT](./1-Unit1/lessons/1-welcome-to-iot/README.md)    |
|  2   | [1 - Introduction to IoT](./1-Unit1) |          IoT Services          | Learn more about the components of an IoT system,                                | [IoT is all around us](./1-Unit1/lessons/2-iot-all-around/README.md) |
|  2   | [1 - Introduction to IoT](./1-Unit1) |          IoT Security          | Learn about sensors to                                                           |    [Even more about IoT](./1-Unit1/lessons/3-more-iot/README.md)     |
|  3   | [2 - Python Programming](./2-Unit2)  |  Intro to the Mu IDE and REPL  | Learn about how to                                                               |           [Python 1](./2-Unit2/lessons/1-python/README.md)           |
|  3   | [2 - Python Programming](./2-Unit2)  |     Python Code Challenges     | Learn how to predict                                                             |           [Python 2](./2-Unit2/lessons/2-python/README.md)           |
|  4   | [2 - Python Programming](./2-Unit2)  |   Python Objects and Methods   | Learn about how to                                                               |           [Python 1](./2-Unit2/lessons/1-python/README.md)           |
|  4   | [2 - Python Programming](./2-Unit2)  |      Python File Handling      | Learn how to predict                                                             |           [Python 2](./2-Unit2/lessons/2-python/README.md)           |
|  5   |    [3 - CircuitPython](./3-Unit3)    |     Intro to CircuitPython     | Learn how to detect                                                              |           [Python 3](./2-Unit2/lessons/3-python/README.md)           |
|  6   |    [3 - CircuitPython](./3-Unit3)    |   Explore the Feather Sense    | Learn about the cloud                                                            |     [CP and Feather 2](./3-Unit3/lessons/2-cp-feather/README.md)     |
|  7   |  [4 - BLE Connectivity](./4-Unit4)   |          Intro to BLE          | Learn about security with IoT                                                    |              [BLE 1](./4-Unit4/lessons/1-ble/README.md)              |
|  8   |  [4 - BLE Connectivity](./4-Unit4)   |        Explore more BLE        | Learn about GPS location                                                         |              [BLE 2](./4-Unit4/lessons/2-ble/README.md)              |
|  9   |  [4 - BLE Connectivity](./4-Unit4)   |   BLE with the MQTT Gateway    | Learn how to store IoT data                                                      |              [BLE 3](./4-Unit4/lessons/3-ble/README.md)              |
|  10  |  [5 - WiFi Connectivity](./5-Unit5)  |     Intro to WiFi and HTTP     | Learn about visualizing location                                                 |             [WiFi 1](./5-Unit5/lessons/1-wifi/README.md)             |
|  11  |  [5 - WiFi Connectivity](./5-Unit5)  | WiFi with HTTP and Adafruit IO | Learn about geofences, and                                                       |             [WiFi 2](./5-Unit5/lessons/2-wifi/README.md)             |
|  12  |  [5 - WiFi Connectivity](./5-Unit5)  | WiFi with MQTT and Adafruit IO | Learn about geofences, and                                                       |             [WiFi 3](./5-Unit5/lessons/3-wifi/README.md)             |
|  13  |  [5 - WiFi Connectivity](./5-Unit5)  |   More Adafruit IO Services    | Learn about using your                                                           |             [WiFi 4](./5-Unit5/lessons/4-wifi/README.md)             |
|  14  |  [6 - IoT Final Project](./6-Unit6)  |         Final Project          | Learn about running                                                              |       [IoT Analytics](./6-Unit6/lessons/1-analytics/README.md)       |
|  15  |  [6 - IoT Final Project](./6-Unit6)  |         Final Project          | Learn how to use                                                                 |     [Final Project](./7-Unit7/lessons/1-final-project/README.md)     |

