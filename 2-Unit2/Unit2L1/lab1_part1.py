"""
Filename:
Author(s):
Date:
Description:
"""

# given strings
capitals = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowers = "abcdefghijklmnopqrstuvwxyz"
specials = "~!@#$^&*()<>?{}[]|\/"
numbers = "0123456789"

"""
Write the function count_caps that will count the total number of capital letters in a given input
string and will return that number.  If no capital letters are present it should return -1.
"""
def count_caps(my_string):
    count = 0
    for char in my_string:
        if char in capitals:
            count = count +1
    if count>0:
        return count
    else:
        return -1

"""
Write a function password_checker that will check  to make sure a password is “strong”.

For a password to be considered strong it needs to include the following:

Password has at least one capital letter
Password has at least one lower case letter
Password has at least one special character as defined above
Password has at least one number
Password is at least 10 characters long
The function should return True if the password is strong or False otherwise.
"""
def password_checker(passwd):
    capsflag = False
    lowflag = False
    specflag = False
    numflag = False
# check length first and return if condition not met
    if len(passwd) < 10:
        return False

    for char in passwd:
        if char in specials:
            specflag = True
        elif char in capitals:
            capsflag = True
        elif char in lowers:
            lowflag = True
        elif char in numbers:
            numflag = True
    # in one of flags is still false, then not all conditions were met and returns false
    return capsflag and lowflag and specflag and numflag

#test count_caps()
user_string = input("Please enter a phrase and I will count the number of capital letters: ")
print("Phrase: {} ".format(user_string))
print("Contains: {} capitals letters".format(count_caps(user_string)))

#test password_checker with one of the following

#user_password="CheeseBurger*12"

user_password=input("\nEnter a password to be checked: ")

if password_checker(user_password):
    print("Password tested is STRONG")
else:
    print("That is a weak password...")

