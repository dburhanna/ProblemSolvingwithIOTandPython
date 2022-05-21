
# create the fileobject by opening the "sample.txt" file as readable
fileobject = open("sample.txt","r")
# read all the lines from the fileobject into the variable "data" which is a list of strings
filedata = fileobject.readlines()
# display the number of lines read into the data list
print(len(data), " lines in the file!")

# initialize a counter variable
count=0
# create an enhanced for loop to access all strings in the data list
for line in filedata:
    # split the current line (a string) into a list of words saved in words
    words = line.split()
    # add the number of words from current line to the count
    count = count + len(words)

# display the total number of words in the file
print("There are "+str(count)+" words in the file")
# close the fileobject - close the file sample.txt
fileobject.close()
