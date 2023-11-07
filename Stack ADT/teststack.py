# Nahom Ayele, Yuqin Yang
from stack import MyStack

test_stack = MyStack()
# test constructor
# print("Expecting [None, None] in underlying array.")
# print(" Is →",test_stack._array)


# # test _expand
# test_stack._expand()
# print("The list content should be [None, None, None, None]")
# print("It is --> ", end = '')
# print(test_stack._array)

# #test _push
# test_stack.push('A')
# test_stack.push('B')
# test_stack.push('C')
# print(test_stack._array)

# #test _pop
# test_stack.pop()
# print(test_stack._array)

# #test _top
# print(test_stack.top())


#overall test
if not test_stack.is_empty(): 
  print("Starting stack should have been empty but isn't")
test_stack.push('q')
top_val = test_stack.top()
if not top_val == 'q': 
  print("Top of stack should be q but was", test_stack.top())
if not top_val == test_stack.pop():
  print("The pop() method has problem(s)")