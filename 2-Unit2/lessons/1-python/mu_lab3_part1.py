##
fileobject = open("sample.txt","r")
#
data = fileobject.readlines()
#
print(len(data), " lines in the file!")

#
count=0
#
for line in data:
    #
    word = line.split()
    #
    count = count + len(word)

#
print("There are "+str(count)+" words in the file")
#
fileobject.close()
