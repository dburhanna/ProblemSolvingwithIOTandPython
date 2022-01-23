
<!-- license image not correct......... -->
<!-- Readme intro file for IoT curriculum -->


[![GitHub license](https://img.shields.io/github/license/dburhanna/test)](LICENSE)


# An Introduction to Problem Solving with IoT and Python

## A Curriculum

The course will take the student on an educational journey from the basics of the Internet of Things to programming their own working IoT devices.  

This curriculum was specifically built with the new or inexperienced teacher in mind.  I have tried to provide a complete package of lessons, labs,
and assessments for a teacher to use and modify.  Each lesson, especially the hardware specific lessons, will come with extra support documentation 
and videos to help teach the teacher.  

While I do believe teaching a class of students in a group setting is advantageous since they will be able to bounce ideas off each other and will 
generally have more fun, this curriculum can also be used by the motivated individual student.

## Course Structure and Pedagogy

The Introduction to IoT curriculum is broken down into XXX units designed to be taught over an entire 15-17 week semester.  Each unit is made up of
multiple lessons with labs. The labs are key to providing the hands-on, experiential learning which has been proven to help students understand and
remember. During this course the students will work, most likely in groups, to complete a series of IoT labs which expose them to IoT from the basic 
connections up to cloud based analytics.  Another key to the curriculum is frequent small assessments.  Each unit has multiple quick quizzes to test the 
students on the most important ideas being presented. 

## Prerequisites 
My goal was to make a curriculum with a very low overhead. I targeted cost effective solutions so teachers everywhere could hopefully benefit without
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

We have two choices of IoT hardware to use for the projects depending on personal preference, programming language knowledge or preferences, learning goals and availability. We have also provided a 'virtual hardware' version for those who don't have access to hardware, or want to learn more before committing to a purchase. You can read more and find a 'shopping list' on the [hardware page](./hardware.md), including links to buy complete kits from our friends at Seeed Studio.


**Teachers**, we have [included some suggestions](for-teachers.md) on how to use this curriculum. If you would like to create your own lessons, we have also included a [lesson template](lesson-template/README.md).
> **Students**, to use this curriculum on your own, fork the entire repo and complete the exercises on your own, starting with a pre-lecture quiz, then reading the lecture and completing the rest of the activities. Try to create the projects by comprehending the lessons rather than copying the solution code; however that code is available in the /solutions folders in each project-oriented lesson. Another idea would be to form a study group with friends and go through the content together. For further study, we recommend [Microsoft Learn](https://docs.microsoft.com/users/jimbobbennett/collections/ke2ehd351jopwr?WT.mc_id=academic-17441-jabenn).
For a video overview of this course, check out this video:

[![Promo video](https://img.youtube.com/vi/bccEMm8gRuc/0.jpg)](https://youtube.com/watch?v=bccEMm8gRuc "Promo video")

> 🎥 Click the image above for a video about the project!
## Pedagogy

We have chosen two pedagogical tenets while building this curriculum: ensuring that it is project-based and that it includes frequent quizzes. By the end of this series, students will have built a plant monitoring and watering system, a vehicle tracker, a smart factory setup to track and check food, and a voice-controlled cooking timer, and will have learned the basics of the Internet of Things including how to write device code, connect to the cloud, analyze telemetry and run AI on the edge.

By ensuring that the content aligns with projects, the process is made more engaging for students and retention of concepts will be augmented.

In addition, a low-stakes quiz before a class sets the intention of the student towards learning a topic, while a second quiz after class ensures further retention. This curriculum was designed to be flexible and fun and can be taken in whole or in part. The projects start small and become increasingly complex by the end of the 12 week cycle.

Each project is be based around real-world hardware available to students and hobbyists. Each project looks into the specific project domain, providing relevant background knowledge. To be a successful developer it helps to understand the domain in which you are solving problems, providing this background knowledge allows students to think about their IoT solutions and learnings in the context of the kind of real-world problem that they might be asked to solve as an IoT developer. Students learn the 'why' of the solutions they are building, and get an appreciation of the end user.

## Hardware

We have two choices of IoT hardware to use for the projects depending on personal preference, programming language knowledge or preferences, learning goals and availability. We have also provided a 'virtual hardware' version for those who don't have access to hardware, or want to learn more before committing to a purchase. You can read more and find a 'shopping list' on the [hardware page](./hardware.md), including links to buy complete kits from our friends at Seeed Studio.

> 💁 Find our [Code of Conduct](CODE_OF_CONDUCT.md), [Contributing](CONTRIBUTING.md), and [Translation](TRANSLATIONS.md) guidelines. We welcome your constructive feedback!
## Each lesson includes:

- sketchnote
- optional supplemental video
- pre-lesson warmup quiz
- written lesson
- for project-based lessons, step-by-step guides on how to build the project
- knowledge checks
- a challenge
- supplemental reading
- assignment
- post-lesson quiz

> **A note about quizzes**: All quizzes are contained [in this app](https://brave-island-0b7c7f50f.azurestaticapps.net), for 48 total quizzes of three questions each. They are linked from within the lessons but the quiz app can be run locally; follow the instruction in the `quiz-app` folder. They are gradually being localized.
## Lessons

|       |              Project Name              |                       Concepts Taught                       | Learning Objectives                                                                                                                                                 |                                                        Linked Lesson                                                         |
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

### Slides

There are slide decks for some of the lessons in the [slides](./slides) folder.

## Help Wanted!

Would you like to contribute a translation? Please read our [translation guidelines](TRANSLATIONS.md) and add input [to one of the translations issues](https://github.com/microsoft/IoT-For-Beginners/issues?q=is%3Aissue+is%3Aopen+label%3Atranslation). If you want to translate into a new language, please raise a new issue for tracking.

## Other Curricula

Our team produces other curricula! Check out:

- [Web Dev for Beginners](https://aka.ms/webdev-beginners)
- [ML for Beginners](https://aka.ms/ml-beginners)
- [Data Science for Beginners](https://aka.ms/datascience-beginners)

## Image attributions

You can find all the attributions for the images used in this curriculum where required in the [Attributions](./attributions.md).
