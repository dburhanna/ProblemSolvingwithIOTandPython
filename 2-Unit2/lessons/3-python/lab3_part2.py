# initialize a count variable
count = 0
# "with" keyword is a better way to open a file because it automatically takes care of closing
# this opens the file and creates the fileobject
with open("sample.txt") as fileobject:
# the fileobject itself is iterable, so we can loop over it without reading all data into a list
    for line in fileobject:
# for the current line read from the fileobject, split the string into a list of words
        words = line.split()
# increment the count variable to add the number of words from current line
        count = count + len(words)
# display the total number of words counted in the file
print("There are "+str(count)+" words in the file")

