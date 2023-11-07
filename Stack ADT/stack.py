# Nahom Ayele, Yuqin Yang
""" CSCI204 Stack lab
Last Modified by: Prof. Fuchsberger, March 2021
"""

from array204 import *

class MyStack:
  """ Implement this Stack ADT using an Array to hold elements.
  """

  def __init__( self ):
    """ Initialize an empty stack.
    Initial capacity should be 2, size should be zero, all items in the array should be None. """
    #TODO
    
    self._capacity =2
    self._array=Array(self._capacity)
    self._size = 0

  def is_empty( self ):
    """ Is the stack empty?
    Return:
      True if the stack is empty; False otherwise. """
    #TODO
    return self._size == 0

  def _expand(self):
    """ Stack is full, expand the capacity. """

    self._capacity= 2 * self._capacity
    tempArray= Array(self._capacity)
    for i in range(len(self._array)):
      tempArray[i]= self._array[i]
    self._array=tempArray
      
  def push( self, item ):
    """ Push the item onto the top of the stack. 
    Parameters:
      item; item to add to top of stack.
    Return: None."""
    #TODO
    # also don't forget to check if array is full and if so call _expand()
    if self._capacity == self._size:
      self._expand()
      
    self._array[self._size] = item
    self._size += 1
   

  def pop( self ):
    """ Pop the top item off the stack (i.e., remove from stack) and return it. 
    Parameters:
      self, instance of MyStack.
    Return:
      item; item at the top of the stack.
    """
    #TODO
    if self._size == 0:
      return None

    last = self._array[self._size - 1]
    # self._array[self._size - 1] = None # Not sure need this or not
    self._size -= 1

    return last

  def top( self ):
    """ Return the top item on the stack (does not change the stack). 
    Parameters:
    self, instance of MyStack.
    Return:
    item; item at the top of the stack.
    """
    #TODO
    return self._array[self._size - 1]

