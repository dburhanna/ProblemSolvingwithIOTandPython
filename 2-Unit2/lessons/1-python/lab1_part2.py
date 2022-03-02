import random
# times are stored as floats where 20.5 would be equl to 20 minutes, 30 seconds

# random list of 50 5k times
times_5k = []

for i in range(50):
# one way to get floating point random value in range 18.0 - 35.99
#    times_5k.append(round(random.randrange(18,35)+random.random(),2))
# second way
#    times_5k.append(round(random.uniform(18.0,35.99),2))
# third way
    times_5k.append(round((18 + random.random()*18),2))

print(times_5k)

def find_average(listoftimes):
    sum = 0
    for time in listoftimes:
        sum = sum + time
    return round(sum/len(listoftimes),2)

def find_min(listoftimes):
    min = listoftimes[0]
    for time in listoftimes:
        if time < min:
            min = time
    return min

def find_max(listoftimes):
    max = listoftimes[0]
    for time in listoftimes:
        if time > max:
            max = time
    return max

def find_median(listoftimes):
    sortedtimes = listoftimes
    sortedtimes.sort()
    length = len(listoftimes)
    if length % 2 == 1:
        return listoftimes[length//2 +1]
    else:
        return round((listoftimes[(length//2)-1] + listoftimes[(length//2)])/2,2)
# one way to output
print("average = ", find_average(times_5k))
print("minimum = ",find_min(times_5k))
print("maximum = ",find_max(times_5k))
print("median = ",find_median(times_5k))
# another way
print("{} average = {:.2f}".format("5k time ",find_average(times_5k)))
print("{} minimum = {:.2f}".format("5k time ",find_min(times_5k)))
print("{} maximum = {:.2f}".format("5k time ",find_max(times_5k)))
print("{} median = {:.2f}".format("5k time ",find_median(times_5k)))

