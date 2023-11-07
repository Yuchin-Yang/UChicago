from random import randint
from quicksort import *
# from quicksort import sort,sortm

""" Controls the creation of lists, calling of quicksort, and data output.

  ____________Lab Hints____________
  Recall that the exponent operator in Python 3.5 is ** so 2**3 is 8.

  You might want to use either a global variable or a class attribute to count key comparisons.

  Use a list comprehension to get a list of all the sizes you need to test.

  Use randint(from,to_inclusive), such as randint(0,20000) to get random integers between 0 and 20,000.

  Use range(to_exclusive) to get sorted integers. Convert the resulting iterator
  into a list using list().

  Because Python 3.2 has a maximum depth for the recursive calls it allows, you
  will only be able to test sizes 2^3..2^9 for the sorted, unmodified. You can test
  the full 2^3..2^14 for the other three cases.

  You should write seperate code to generate all four cases since you will need to
  run them repeatedly. (Do not delete code for one case to write the next one).

  Write the output for your four cases into the four files using the open(), write(),
  and close() methods. If you need to print a line break, remember that \n is a
  newline character.

  Print a test run of 10 numbers to standard output for each case to make sure your
  Quicksort is still actually sorting. (use the numbers 0..9 for both the random and
  sorted so you can eyeball the results and know they are ok).
"""
# TODO: write your tests here...

# # create 10 random number list and sort it
# test = []
# for i in range(10):
#   test.append(randint(0, 10))
# print(test)
# sort(test)
# print(test)

# newlist = [x for x in range(10) ]
# print(newlist) 
# sort(newlist)
# print(newlist)


doubling_list = [(2**x) for x in range(15) if x>2]
# print(doubling_list)

with open('outru', 'w') as the_file:
  for i in doubling_list:
    number_list = [randint(0, 20000) for x in range(i)]
    # print(number_list)
    c = sort(number_list)
    the_file.write(f'{i} {c}\n')
  
  # print(number_list)

doubling_list_limit = [(2**x) for x in range(10) if x>2]
# print(doubling_list_limit)



with open('outsu', 'w') as the_file: 
  for i in doubling_list_limit:
    number_list = [x for x in range(i)]
    # print(number_list)
    c = sort(number_list)
    the_file.write(f'{i} {c}\n')
  # print(number_list)


# Uncomment below to show a graph (Task 7-8)!
import plotm # Plot Modified
# import plotu # Plot Unmodified


'''copy'''

# create 10 random number list and sort it
test = []
for i in range(10):
  test.append(randint(0, 10))
print(test)
sortm(test)
print(test)

newlist = [x for x in range(10) ]
print(newlist) 
sortm(newlist)
print(newlist)


doubling_list = [(2**x) for x in range(15) if x>2]
print(doubling_list)

with open('outrm', 'w') as the_file:
  for i in doubling_list:
    number_list = [randint(0, 20000) for x in range(i)]
    # print(number_list)
    c = sortm(number_list)
    the_file.write(f'{i} {c}\n')
  
  # print(number_list)



with open('outsm', 'w') as the_file: 
  for i in doubling_list:
    number_list = [x for x in range(i)]
    # print(number_list)
    c = sortm(number_list)
    the_file.write(f'{i} {c}\n')