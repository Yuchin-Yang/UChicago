from array204 import *
from ListException import *

class List:
  def __init__(self):
    self._array = Array(2)
    self._capacity = 2
    self._size = 0
  
  def __len__(self):
    return self._size
  
  def __str__(self):
    s = "["

    if self._size == 0:
        return s + "]"
    else:
        for index in range(self._size):
            s += str(self._array[index]) + ", "
        return s[:-2] + "]"
  
  def insert(self, item, index):
    # When run out of room
    if self._capacity == self._size:
      new_array = Array(self._capacity * 2)
      for pos in range(self._capacity):
          new_array[pos] = self._array[pos]
      self._array = new_array
      self._capacity *= 2
    
    # Correct the index
    if index < 0:
        index = 0
    elif index >= self._size:
        index = self._size
    
    # Insert the item
    for pos in range(self._size - 1, index - 1, -1):
        self._array[pos + 1] = self._array[pos]
    self._array[index] = item
    self._size += 1
  
  def delete(self, index):
    if index < 0 or index >= self._size:
        raise ListException("Index error")
    else:
        for pos in range(index, self._size - 1):
            self._array[pos] = self._array[pos + 1]
        self._array[self._size - 1] = None
        self._size -= 1
  
  def peek(self, index):
    if index < 0 or index >= self._size:
        raise ListException("Index error")
    else:
        return self._array[index]
