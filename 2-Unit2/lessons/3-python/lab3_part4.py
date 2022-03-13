# create a file object for the output file
outputfile = open("numbered_sample.txt","w")
# initialize a variable to count lines
linenum = 0
# create a file object for the input file
with open("sample.txt") as inputfile:
# read a line from the inputfile
    for line in inputfile:
        # print it just to see what we got
        print(line)
        # increment linenum
        linenum = linenum +1
        # add linenum to the string read from the inputfile
        updatedline = str(linenum) +" " + line
        # print the updatedline, to confirm
        print(updatedline)
        # use .write method to save the updatedline to outputfile
        outputfile.write(updatedline)
# use .close() method to close the outputfile
outputfile.close()
