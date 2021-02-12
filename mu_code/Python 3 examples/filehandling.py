# Python code to illustrate split() function
with open("pillow_example.py", "r+") as file:
    data = file.readlines() # reads all lines in file into a list "data"
    print(len(data), " lines in the file!")
    count=0
    for line in data:
        word = line.split() #split individual line at spaces into a list "words"
        count = count + len(word)
        print (word)
    print(count, " total words in the file!")

    file.write("\n#adding a comment at the END of the file!!!")