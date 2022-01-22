# This imports the random method
import random
#defines the lists Math and Math 1
Math = ["math"]
math1 = []
#defines the lists Science and Science 1
Science = ["science"]
science1 = []
#defines the lists Reading and Reading 1
Reading = ["reading"]
reading1 = []
#defines the lists Theology and Theology 1
Theology = ["theology"]
theology1 = []
#defines the lists Language and Language 1
Language = ["language"]
language1 = []
#defines the lists History and History 1
History = ["history"]
history1 = []
#defines the lists Art and Art 1
Art = ["art"]
art1 = []


# This will do everything in this loop 15 times, and assigns random numbers to
#each  list 15 times
for i in range(15):

# first gets a random number, then appends it to (Math) the gradebook subject,
#then to (math1) summary subject
    random_number = random.randint(50,100)
    Math.append(random_number)
    math1.append(random_number)

# first gets a random number, then appends it to (Science) gradebook subject,
#then to (science1) summary subject
    random_number = random.randint(50,100)
    Science.append(random_number)
    science1.append(random_number)

# first gets a random number, then appends it to (Reading) gradebook subject,
#then to (reading1) summary subject
    random_number = random.randint(50,100)
    Reading.append(random_number)
    reading1.append(random_number)

# first gets a random number, then appends it to (Theology) gradebook subject,
#then to (theology1) summary subject
    random_number = random.randint(50,100)
    Theology.append(random_number)
    theology1.append(random_number)

# first gets a random number, then appends it to (Language) gradebook subject,
#then to (language1) summary subject
    random_number = random.randint(50,100)
    Language.append(random_number)
    language1.append(random_number)

# first gets a random number, then appends it to (History) gradebook subject,
#then to (history1) summary subject
    random_number = random.randint(50,100)
    History.append(random_number)
    history1.append(random_number)

# first gets a random number, then appends it to (Art) gradebook subject,
#then to (art1) summary subject

    random_number = random.randint(50,100)
    Art.append(random_number)
    art1.append(random_number)
# This is technically the gradebook but without the gradebook name
class_list = [Math, Science, Reading, Theology, Language, History, Art]
print(class_list)

# This prints a giant line between the gradebook with all the grades and the summary
print("------------------------------------------------------------------")

# This will create my function so I can calculate the minimum, the maximum,
#the sum, the length, and the average of each subject grades
def create_summary():

    # gets minimum of math1
    math_minimum = min(math1)

    # gets maximum of math1
    math_maximum = max(math1)

    # gets total of math1
    math_sum = sum(math1)

    # gets the length of math1
    math_length = len(math1)

    # divides the total by the length
    math_average = math_sum/math_length

    # puts everything in order from the minimum to the maximum to the rounded average
    Math = ["math" , math_minimum, math_maximum, round(math_average,1)]

# the science starts here
    # gets minimum of science1
    science_minimum = min(science1)

    # gets maximum of science1
    science_maximum = max(science1)

    # gets total of science1
    science_sum = sum(science1)

    # gets the length of science1
    science_length = len(science1)

    # divides the total by the length
    science_average = science_sum/science_length

    # puts everything in order from the minimum to the maximum to the rounded average
    Science = ["science" , science_minimum, science_maximum, round(science_average,1)]

# the reading starts here
    # gets minimum of reading1
    reading_minimum = min(reading1)

    # gets maximum of reading1
    reading_maximum = max(reading1)

    # gets total of reading1
    reading_sum = sum(reading1)

    # gets the length of reading1
    reading_length = len(reading1)

    # divides the total by the length
    reading_average = reading_sum/reading_length

    # puts everything in order from the minimum to the maximum to the rounded average
    Reading = ["reading" , reading_minimum, reading_maximum, round(reading_average,1)]

# the theology starts here
    # gets minimum of theology1
    theology_minimum = min(theology1)

    # gets maximum of theology1
    theology_maximum = max(theology1)

    # gets total of theology1
    theology_sum = sum(theology1)

    # gets the length of theology1
    theology_length = len(theology1)

    # divides the total by the length
    theology_average = theology_sum/theology_length

    # puts everything in order from the minimum to the maximum to the rounded average
    Theology = ["theology" , theology_minimum, theology_maximum, round(theology_average,1)]

# the language starts here
    # gets minimum of language1
    language_minimum = min(language1)

    # gets maximum of language1
    language_maximum = max(language1)

    # gets total of language1
    language_sum = sum(language1)

    # gets the length of language1
    language_length = len(language1)

    # divides the total by the length
    language_average = language_sum/language_length

    # puts everything in order from the minimum to the maximum to the rounded average
    Language = ["language" , language_minimum, language_maximum, round(language_average,1)]

# the history starts here
    # gets minimum of history1
    history_minimum = min(history1)

    # gets maximum of history1
    history_maximum = max(history1)

    # gets total of history1
    history_sum = sum(history1)

    # gets the length of history1
    history_length = len(history1)

    # divides the total by the length
    history_average = history_sum/history_length

    # puts everything in order from the minimum to the maximum to the rounded average
    History = ["history" , history_minimum, history_maximum, round(history_average,1)]

# the art starts here
    # gets minimum of art1
    art_minimum = min(art1)

    # gets maximum of art1
    art_maximum = max(art1)

    # gets total of art1
    art_sum = sum(art1)

    # gets the length of art1
    art_length = len(art1)

    # divides the total by the length
    art_average = art_sum/art_length

    # puts everything in order from the minimum to the maximum to the rounded average
    Art = ["art" , art_minimum, art_maximum, round(art_average,1)]

# This will put all the subjects and their contents in a list so I can print them out nice and neat

    summary = [Math, Science, Reading, Theology, Language, History, Art]
    print(summary)
#calls the whole function
create_summary()


