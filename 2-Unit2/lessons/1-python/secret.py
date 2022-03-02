import random
#Key Project Objectives:
#Store the names in an array/list
#Pair participants and output the pairs

#the potential participants
the_office = ['Michael Scott', 'Dwight Schrute', 'Jim Halpert', 'Pam Beesly', 'Jan Levinson', 'Kevin Malone', 'Toby Flenderson', 'Angela Martin', 'Andy Bernard', 'Stanley Hudson', 'Ryan Howard', 'Kelly Kapoor']

#the potential santas
the_office_santas = the_office.copy()

#function for secret santa matching
def secret_santa(lst1, lst2):
#shuffle the gift receivers list
  random.shuffle(lst2)
  #check if any santa is matched with themself
  #if yes, shuffle both lists (sorry, Kevin)
  for i in range(len(lst2)):
    for j in range(len(lst1)):
      if lst2[i] == lst1[j]:
        random.shuffle(lst2)
        random.shuffle(lst1)
  combine_lsts = zip(lst1, lst2)
  #prints combined list instead of address
  the_secret = list(combine_lsts)
  return print(the_secret)

print("Your secret santa pairings are (Santa, Gift Receiver): ")

secret_santa(the_office_santas, the_office)
