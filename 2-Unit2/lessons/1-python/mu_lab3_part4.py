outputfile = open("numbered_sample.txt","w")

linenum = 0

with open("sample.txt") as inputfile:
#
    for line in inputfile:
        print(line)
        linenum = linenum +1
        updatedline = str(linenum) +" " + line
        print(updatedline)
        outputfile.write(updatedline)

outputfile.close()
