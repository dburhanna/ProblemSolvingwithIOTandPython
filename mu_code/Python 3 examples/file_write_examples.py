# writing data to a csv file example
my_file = open("coolfile.txt","a")

my_file.write("cheese is good\n")
my_file.write("hotdogs are ok too\n")
my_file.close()

with open('do_re_mi.txt', 'a') as f:
    f.write('Doe, a deer, a female deer\n')
    f.write('Ray, a drop of golden sun\n')

import json

my_details = {
    'name': 'John Doe',
    'age': 29
}

with open('personal.json', 'a') as json_file:
    json.dump(my_details, json_file)

import csv

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
sales = ['10', '8', '19', '12', '25']

with open('sales.csv', 'a') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    csv_writer.writerow(weekdays)
    csv_writer.writerow(sales)
