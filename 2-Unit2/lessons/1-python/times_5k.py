import random
# times are stored as floats where 20.5 would be equl to 20 minutes, 30 seconds

# random list of 50 5k times
times_5k = []

for i in range(49):
    times_5k.append(round(random.randrange(18,36)+random.random(),2))
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
        return (listoftimes[(length//2)-1] + listoftimes[(length//2)])/2

print("average = ", find_average(times_5k))
print("minimum = ",find_min(times_5k))
print("maximum = ",find_max(times_5k))
print("median = ",find_median(times_5k))


