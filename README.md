
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

The Introduction to IoT curriculum is broken down into 7 units designed to be taught over an entire 15-17 week semester.  Each unit is made up of
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

|       |              Unit              |                       Topics                       | Learning Objectives                                                                                                                                                 |                                                        Linked Lessons                                                         |
| :---: | :------------------------------------: | :---------------------------------------------------------: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------: |
|  01   | [Getting started](./1-getting-started) |                     Introduction to IoT                     | Learn the basic principles of IoT and the basic building blocks of IoT solutions such as sensors and cloud services whilst you are setting up your first IoT device |                      [Introduction to IoT](./1-getting-started/lessons/1-introduction-to-iot/README.md)                      |
|  02   | [Getting started](./1-getting-started) |                   A deeper dive into IoT                    | Learn more about the components of an IoT system, as well as microcontrollers and single-board computers                                                            |                        [A deeper dive into IoT](./1-getting-started/lessons/2-deeper-dive/README.md)                         |
|  03   | [Getting started](./1-getting-started) | Interact with the physical world with sensors and actuators | Learn about sensors to gather data from the physical world, and actuators to send feedback, whilst you build a nightlight                                           | [Interact with the physical world with sensors and actuators](./1-getting-started/lessons/3-sensors-and-actuators/README.md) |
|  04   | [Getting started](./1-getting-started) |             Connect your device to the Internet             | Learn about how to connect an IoT device to the Internet to send and receive messages by connecting your nightlight to an MQTT broker                               |               [Connect your device to the Internet](./1-getting-started/lessons/4-connect-internet/README.md)                |
|  05   |            [Farm](./2-farm)            |                    Predict plant growth                     | Learn how to predict plant growth using temperature data captured by an IoT device                                                                                  |                          [Predict plant growth](./2-farm/lessons/1-predict-plant-growth/README.md)                           |
|  06   |            [Farm](./2-farm)            |                    Detect soil moisture                     | Learn how to detect soil moisture and calibrate a soil moisture sensor                                                                                              |                          [Detect soil moisture](./2-farm/lessons/2-detect-soil-moisture/README.md)                           |
|  07   |            [Farm](./2-farm)            |                  Automated plant watering                   | Learn how to automate and time watering using a relay and MQTT                                                                                                      |                      [Automated plant watering](./2-farm/lessons/3-automated-plant-watering/README.md)                       |
|  08   |            [Farm](./2-farm)            |               Migrate your plant to the cloud               | Learn about the cloud and cloud-hosted IoT services and how to connect your plant to one of these instead of a public MQTT broker                                   |               [Migrate your plant to the cloud](./2-farm/lessons/4-migrate-your-plant-to-the-cloud/README.md)                |
|  09   |            [Farm](./2-farm)            |         Migrate your application logic to the cloud         | Learn about how you can write application logic in the cloud that responds to IoT messages                                                                          |         [Migrate your application logic to the cloud](./2-farm/lessons/5-migrate-application-to-the-cloud/README.md)         |
|  10   |            [Farm](./2-farm)            |                   Keep your plant secure                    | Learn about security with IoT and how to keep your plant secure with keys and certificates                                                                          |                        [Keep your plant secure](./2-farm/lessons/6-keep-your-plant-secure/README.md)                         |
|  11   |       [Transport](./3-transport)       |                      Location tracking                      | Learn about GPS location tracking for IoT devices                                                                                                                   |                           [Location tracking](./3-transport/lessons/1-location-tracking/README.md)                           |
|  12   |       [Transport](./3-transport)       |                     Store location data                     | Learn how to store IoT data to be visualized or analysed later                                                                                                      |                         [Store location data](./3-transport/lessons/2-store-location-data/README.md)                         |
|  13   |       [Transport](./3-transport)       |                   Visualize location data                   | Learn about visualizing location data on a map, and how maps represent the real 3d world in 2 dimensions                                                            |                     [Visualize location data](./3-transport/lessons/3-visualize-location-data/README.md)                     |
|  14   |       [Transport](./3-transport)       |                          Geofences                          | Learn about geofences, and how they can be used to alert when vehicles in the supply chain are close to their destination                                           |                                   [Geofences](./3-transport/lessons/4-geofences/README.md)                                   |
|  15   |   [Manufacturing](./4-manufacturing)   |               Train a fruit quality detector                | Learn about training an image classifier in the cloud to detect fruit quality                                                                                       |                 [Train a fruit quality detector](./4-manufacturing/lessons/1-train-fruit-detector/README.md)                 |
|  16   |   [Manufacturing](./4-manufacturing)   |           Check fruit quality from an IoT device            | Learn about using your fruit quality detector from an IoT device                                                                                                    |           [Check fruit quality from an IoT device](./4-manufacturing/lessons/2-check-fruit-from-device/README.md)            |
|  17   |   [Manufacturing](./4-manufacturing)   |             Run your fruit detector on the edge             | Learn about running your fruit detector on an IoT device on the edge                                                                                                |             [Run your fruit detector on the edge](./4-manufacturing/lessons/3-run-fruit-detector-edge/README.md)             |
|  18   |   [Manufacturing](./4-manufacturing)   |        Trigger fruit quality detection from a sensor        | Learn about triggering fruit quality detection from a sensor                                                                                                        |        [Trigger fruit quality detection from a sensor](./4-manufacturing/lessons/4-trigger-fruit-detector/README.md)         |
|  19   |          [Retail](./5-retail)          |                   Train a stock detector                    | Learn how to use object detection to train a stock detector to count stock in a shop                                                                                |                        [Train a stock detector](./5-retail/lessons/1-train-stock-detector/README.md)                         |
|  20   |          [Retail](./5-retail)          |               Check stock from an IoT device                | Learn how to check stock from an IoT device using an object detection model                                                                                         |                     [Check stock from an IoT device](./5-retail/lessons/2-check-stock-device/README.md)                      |
|  21   |        [Consumer](./6-consumer)        |             Recognize speech with an IoT device             | Learn how to recognize speech from an IoT device to build a smart timer                                                                                             |                  [Recognize speech with an IoT device](./6-consumer/lessons/1-speech-recognition/README.md)                  |
|  22   |        [Consumer](./6-consumer)        |                     Understand language                     | Learn how to understand sentences spoken to an IoT device                                                                                                           |                        [Understand language](./6-consumer/lessons/2-language-understanding/README.md)                        |
|  23   |        [Consumer](./6-consumer)        |           Set a timer and provide spoken feedback           | Learn how to set a timer on an IoT device and give spoken feedback on when the timer is set and when it finishes                                                    |                 [Set a timer and provide spoken feedback](./6-consumer/lessons/3-spoken-feedback/README.md)                  |
|  24   |        [Consumer](./6-consumer)        |                 Support multiple languages                  | Learn how to support multiple languages, both being spoken to and the responses from your smart timer                                                               |                   [Support multiple languages](./6-consumer/lessons/4-multiple-language-support/README.md)                   |

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

