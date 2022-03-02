#
count = 0
#
with open("sample.txt") as fileobject:
#
    for line in fileobject:
#
        words = line.split()
#
        count = count + len(words)
#
print("There are "+str(count)+" words in the file")

