
<!-- license image not correct......... -->
<!-- Readme intro file for IoT curriculum -->


[![GitHub license](https://img.shields.io/github/license/dburhanna/test)](LICENSE)


# An Introduction to Problem Solving with IoT and Python

## A Curriculum

The course will take the student on an educational journey from the basics of the Internet of Things to programming their own working IoT devices.  

This curriculum was specifically built with the new or inexperienced teacher in mind.  I have tried to provide a complete package of lessons, labs,
and assessments for a teacher to use and modify.  Each lesson, especially the hardware specific lessons, will come with extra support documentation 
and videos to help **teach the teacher**.  

While I do believe teaching a class of students in a group setting is advantageous since they will be able to bounce ideas off each other and will 
generally have more fun, this curriculum can also be used by the motivated individual student.

## Course Structure and Pedagogy

The Introduction to IoT curriculum is broken down into 7 units designed to be taught over an entire 15-week semester.  Each unit is made up of
multiple lessons, many of which are labs. The labs are key to providing the hands-on, experiential learning which has been proven to help students understand and
remember. During this course the students will work, most likely in groups, to complete a series of IoT labs which expose them to IoT from the basic 
connections up to cloud based analytics.  Another key to the curriculum is frequent small assessments.  Each unit has multiple quick quizzes to test the 
students on the most important ideas being presented. 

## Prerequisites 
My goal was to make a curriculum with minimal cost. I targeted open source and cost effective solutions so teachers everywhere could hopefully benefit without
needing to request thousands of dollars for equipment or licensing fees.

### Software - Development Environment
The [Mu editor](https://codewith.mu/en/) was chosen as the intergrated development environment for the course.  Mu is free to download and can be used on multiple platforms.

### Software - Python
This curriculum was originally designed to be a second semester continuation to a first semester introduction to programming with
[Python](https://www.python.org/).  I wanted to add something hands-on and real-world to better engage the class.  Python is one of the most popular 
programming languages and definitely has easier to understand syntax than other languages typically used for IoT such as Arduino, C or C++.  Even if your 
students do not have prior experience with Python, the course contains a unit of Python review as the development environment is introduced to the 
students.  You can choose to spend as much or as little time as necessary in this unit.  There are many Python curriculums available already for the 
teacher that plans on using this course as it was originally designed. 

### Hardware 

When it comes to adding some real-world experiences for your students, you need to use real-world devices.  This can be an intimidating and time 
consuming process even for an experienced engineer.  Just choosing the "thing" you want to use for IoT is not an easy task since there are many 
possibilities today.  **I looked for a low-cost "thing' that could be programmed with Python.** Thankfully, [Adafruit Industries](https://www.adafruit.com/) 
has been leading the way by developing small, low-cost microcontroller boards that can be programmed with [CircuitPython](https://circuitpython.org/), 
a variant of Python.  I know much of this "hardware" stuff may be completely foreign to many teachers.  My curriculum should provide all you need to feel 
comfortable working with microcontrollers and helping your students understand the IoT concepts.  You can read more about the hardware chosen and check on 
current prices on the [hardware page](./hardware.md)

## Each unit includes:

- clearly defined learning objectives
- written lesson plans
- for lab-based lessons, a step-by-step lab guide 
- assignments
- knowledge checks
- supplemental reading and video links
- quick quizzes
- a unit challenge


## Lessons

| Week |                   Unit                    |        Topics        | Learning Objectives                                                              |                            Linked Lessons                            |
|:----:|:-----------------------------------------:|:--------------------:|----------------------------------------------------------------------------------|:--------------------------------------------------------------------:|
|  1   |       [1 - Intro to IoT](./1-Unit1)       |     What is IoT?     | Learn the basic principles of IoT and the basic building blocks of IoT solutions |    [Welcome to IoT](./1-Unit1/lessons/1-welcome-to-iot/README.md)    |
|  1   |       [1 - Intro to IoT](./1-Unit1)       | IoT is all around us | Learn more about the components of an IoT system,                                | [IoT is all around us](./1-Unit1/lessons/2-iot-all-around/README.md) |
|  2   |       [1 - Intro to IoT](./1-Unit1)       | Even more about IoT  | Learn about sensors to                                                           |    [Even more about IoT](./1-Unit1/lessons/3-more-iot/README.md)     |
|  2   |    [2 - Python Programming](./2-Unit2)    |        Python        | Learn about how to                                                               |           [Python 1](./2-Unit2/lessons/1-python/README.md)           |
|  3   |    [2 - Python Programming](./2-Unit2)    |        Python        | Learn how to predict                                                             |           [Python 2](./2-Unit2/lessons/2-python/README.md)           |
|  3   |    [2 - Python Programming](./2-Unit2)    |        Python        | Learn how to detect                                                              |           [Python 3](./2-Unit2/lessons/3-python/README.md)           |
|  4   | [3 - Get to know your "Thing"](./3-Unit3) |    CP and Feather    | Learn how to automate                                                            |     [CP and Feather 1](./3-Unit3/lessons/1-cp-feather/README.md)     |
|  5   | [3 - Get to know your "Thing"](./3-Unit3) |    CP and Feather    | Learn about the cloud                                                            |     [CP and Feather 2](./3-Unit3/lessons/2-cp-feather/README.md)     |
|  6   | [3 - Get to know your "Thing"](./3-Unit3) |    CP and Feather    | Learn about how you c                                                            |     [CP and Feather 3](./3-Unit3/lessons/3-cp-feather/README.md)     |
|  7   |       [4 - IoT with BLE](./4-Unit4)       |         BLE          | Learn about security with IoT                                                    |              [BLE 1](./4-Unit4/lessons/1-ble/README.md)              |
|  8   |       [4 - IoT with BLE](./4-Unit4)       |         BLE          | Learn about GPS location                                                         |              [BLE 2](./4-Unit4/lessons/2-ble/README.md)              |
|  9   |       [4 - IoT with BLE](./4-Unit4)       |         BLE          | Learn how to store IoT data                                                      |              [BLE 3](./4-Unit4/lessons/3-ble/README.md)              |
|  10  |      [5 - IoT with WiFi](./5-Unit5)       |         WiFi         | Learn about visualizing location                                                 |             [WiFi 1](./5-Unit5/lessons/1-wifi/README.md)             |
|  11  |      [5 - IoT with WiFi](./5-Unit5)       |         WiFi         | Learn about geofences, and                                                       |             [WiFi 2](./5-Unit5/lessons/2-wifi/README.md)             |
|  12  |      [5 - IoT with WiFi](./5-Unit5)       |         WiFi         | Learn about geofences, and                                                       |             [WiFi 3](./5-Unit5/lessons/3-wifi/README.md)             |
|  13  |      [5 - IoT with WiFi](./5-Unit5)       |         WiFi         | Learn about using your                                                           |             [WiFi 4](./5-Unit5/lessons/4-wifi/README.md)             |
|  14  |      [6 - IoT Analytics](./6-Unit6)       |         data         | Learn about running                                                              |       [IoT Analytics](./6-Unit6/lessons/1-analytics/README.md)       |
|  15  |    [7 - IoT Final Project](./7-Unit7)     |    Final Project     | Learn how to use                                                                 |     [Final Project](./7-Unit7/lessons/1-final-project/README.md)     |

## Offline access

You can run this documentation offline by using [Docsify](https://docsify.js.org/#/). Fork this repo, [install Docsify](https://docsify.js.org/#/quickstart) on your local machine, and then in the root folder of this repo, type `docsify serve`. The website will be served on port 3000 on your localhost: `localhost:3000`.

### PDF

You can generate a PDF of this content for offline access if needed. To do this, make sure you have [npm installed](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) and run the following commands in the root folder of this repo:

```sh
npm i
npm run convert
```

**Teachers**, I have [included some suggestions](for-teachers.md) on how to get started using the curriculum. 

If you would like to create your own lessons, we have also included a [lesson template](lesson-template/README.md).

