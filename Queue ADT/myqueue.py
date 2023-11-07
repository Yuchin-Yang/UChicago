from array204 import Array

class Queue:
  """Queue ADT implemented as a linked list (options for bounded and unbounded).
  
  Attibutes:
  # Todo, fill in docstrings
  """

  def __init__( self, bound = None ):
    """ Queue starts out empty. If bound == None, the queue
    is unbounded. Otherwise set the capacity of the queue
    to be the integer value of bound. """
    # TODO
    self.head = None
    self.tail = None
    self.count = 0
    self.bound = bound
    
  def __len__( self ):
    """ Return the current size of the queue. """
    # TODO
    return self.count
    
  def is_empty(self):
    """ Returns true if the queue is empty, false otherwise. """
    # TODO
    if self.head == None:
      return True
    else:
      return False
      
  def enqueue(self, item):
    """ If full and bounded, return -1 to indicate failure. """
    # TODO
    if self.bound != None and self.count >= self.bound:
      return -1
    else:
      node = Node(item)
      if self.is_empty():
        self.head = node
      else:
        self.tail.next = node
  
      self.tail = node
      self.count += 1
    
  def dequeue(self):
    """ DeQ and return item. If empty, return None. """
    # TODO
    if self.is_empty() == True:
      return None
    else:
      node = self.head
      if self.head is self.tail:
        self.tail = None
        
      self.head = self.head.next
      self.count -= 1
      return node.data
    
  def peek(self):
    """ Return the item that would be dequeue'd next.
        If empty, return None. """
    # TODO
    if self.is_empty() == True:
      return None
    return self.head


class Node:
  def __init__(self, data):
    self.data = data
    self.next = None