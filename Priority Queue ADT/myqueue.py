# Yuqin Yang
class Queue:
  """Queue ADT implemented as a linked list (options for bounded and unbounded).
  
  Attibutes:
  # Todo, fill in docstrings
  """

class Queue:
    def __init__( self ):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty( self ):
        return self.size == 0

    def __len__( self ):
        return self.size

    def enqueue( self, item ):
        node = Node(item)

        if self.is_empty():
            self.tail = node
        else:
            self.head.next = node

        self.head = node
        self.size = self.size + 1

    def dequeue( self ):
        assert not self.is_empty(), "Cannot dequeue from an empty queue."

        data = self.tail.data
        
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.next
        
        self.size -= 1
        return data

    def peek( self ):
        return self.tail.data

class Node:
    def __init__( self, data ):
        self.data = data
        self.next = None