# create a new file object with "w" argument- make it writeable
# OR create a new file object with "a" argument- make it appendable
# if no argument is given after the filename python opens the file as readonly by default
my_file_obj = open("coolfile.txt","w")
# write a string to the open file with the .write method
my_file_obj.write("cheeseburgers are good\n")
# write another string to the open file with the .write method
my_file_obj.write("the footlong hotdogs are ok too\n")
# remember to close the file by using the .close() method
my_file_obj.close()


'''
This could also be done in the following way
this method would handle closing the file automatically

with open("sample.txt","w") as my_file_obj:
    my_file_obj.write("cheeseburgers are good\n")
    my_file_obj.write("the footlong hotdogs are ok too\n")
'''
