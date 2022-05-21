
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


## Possible pacing guidelines:

| Week |                 Unit                 |             Topics             |                 Lesson Links                  |
|:----:|:------------------------------------:|:------------------------------:|:---------------------------------------------:|
|  1   | [1 - Introduction to IoT](./1-Unit1) |      Course Introduction       |    [Unit 1.0](./1-Unit1/Unit1.0/README.md)    |
|  1   | [1 - Introduction to IoT](./1-Unit1) |          What is IoT?          |    [Unit 1.1](./1-Unit1/Unit1.1/README.md)    |
|  1   | [1 - Introduction to IoT](./1-Unit1) |        IoT Connectivity        |    [Unit 1.2](./1-Unit1/Unit1.2/README.md)    |
|  2   | [1 - Introduction to IoT](./1-Unit1) |  IoT Communication Protocols   |    [Unit 1.3](./1-Unit1/Unit1.3/README.md)    |
|  2   | [1 - Introduction to IoT](./1-Unit1) |          IoT Services          |    [Unit 1.4](./1-Unit1/Unit1.4/README.md)    |
|  2   | [1 - Introduction to IoT](./1-Unit1) |          IoT Security          |    [Unit 1.5](./1-Unit1/Unit1.5/README.md)    |
|  3   | [2 - Python Programming](./2-Unit2)  |  Intro to the Mu IDE and REPL  |  [Unit 2 Lab 0](./2-Unit2/Unit2L0/README.md)  |
|  3   | [2 - Python Programming](./2-Unit2)  |     Python Code Challenges     |  [Unit 2 Lab 1](./2-Unit2/Unit2L1/README.md)  |
|  4   | [2 - Python Programming](./2-Unit2)  |   Python Objects and Methods   |  [Unit 2 Lab 2](./2-Unit2/Unit2L2/README.md)  |
|  4   | [2 - Python Programming](./2-Unit2)  |      Python File Handling      |  [Unit 2 Lab 3](./2-Unit2/Unit2L3/README.md)  |
|  5   |    [3 - CircuitPython](./3-Unit3)    |     Intro to CircuitPython     |  [Unit 3 Lab 4](./3-Unit3/Unit2L4/README.md)  |
|  6   |    [3 - CircuitPython](./3-Unit3)    |   Explore the Feather Sense    |  [Unit 3 Lab 5](./3-Unit3/Unit2L5/README.md)  |
|  7   |  [4 - BLE Connectivity](./4-Unit4)   |          Intro to BLE          |  [Unit 4 Lab 6](./4-Unit4/Unit4L6/README.md)  |
|  8   |  [4 - BLE Connectivity](./4-Unit4)   |        Explore more BLE        |  [Unit 4 Lab 7](./4-Unit4/Unit4L7/README.md)  |
|  9   |  [4 - BLE Connectivity](./4-Unit4)   |   BLE with the MQTT Gateway    |  [Unit 4 Lab 8](./4-Unit4/Unit4L8/README.md)  |
|  10  |  [5 - WiFi Connectivity](./5-Unit5)  |     Intro to WiFi and HTTP     |  [Unit 5 Lab 9](./5-Unit5/Unit5L9/README.md)  |
|  11  |  [5 - WiFi Connectivity](./5-Unit5)  | WiFi with HTTP and Adafruit IO | [Unit 5 Lab 10](./5-Unit5/Unit5L10/README.md) |
|  12  |  [5 - WiFi Connectivity](./5-Unit5)  | WiFi with MQTT and Adafruit IO | [Unit 5 Lab 11](./5-Unit5/Unit5L11/README.md) |
|  13  |  [5 - WiFi Connectivity](./5-Unit5)  |   More Adafruit IO Services    | [Unit 5 Lab 12](./5-Unit5/Unit5L12/README.md) |
|  14  |  [6 - IoT Final Project](./6-Unit6)  |         Final Project          |  [Unit 6 Final Project](./6-Unit6/README.md)  |
|  15  |  [6 - IoT Final Project](./6-Unit6)  |         Final Project          |  [Unit 6 Final Project](./6-Unit6/README.md)  |

