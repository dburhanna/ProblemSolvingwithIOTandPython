import random
# times are stored as floats where 20.5 would be equl to 20 minutes, 30 seconds

# dictionary of 5k, 10k, mile and half-marathon times
times_dict = {"5k": [],"10k": [], "mile": [], "half": []}

for key in times_dict:
    for i in range(20):
        if key == "5k":
            times_dict[key].append(round(random.uniform(18.0,29.99),2))
        elif key == "10k":
            times_dict[key].append(round(random.uniform(45.0,62.99),2))
        elif key == "mile":
            times_dict[key].append(round(random.uniform(5,8.25),2))
        elif key == "half":
            times_dict[key].append(round(random.uniform(95,125),2))
print(times_dict)

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

for key in times_dict:
#one way
#    print(key + " average = ", find_average(times_dict[key]))
#    print(key + " minimum = ",find_min(times_dict[key]))
#    print(key + " maximum = ",find_max(times_dict[key]))
#    print(key + " median = ",find_median(times_dict[key]))
# another way
    print("{0} average = {1:.2f}".format(key,find_average(times_dict[key])))
    print("{0} minimum = {1:.2f}".format(key,find_min(times_dict[key])))
    print("{0} maximum = {1:.2f}".format(key,find_max(times_dict[key])))
    print("{0} median = {1:.2f}".format(key,find_median(times_dict[key])))

