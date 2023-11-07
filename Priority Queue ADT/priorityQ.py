#Yuqin Yang
""" Priority Queue lab: CSCI 204 """

""" This class implements a linked priority queue with a head.
        Priorities are positive integers where the highest priority
        is zero. This queue is a linked list.
        Assume the base class Queue has been implemented as
        linked list."""

"""This class should implement nodes for a singly linked list with a priority."""  
from myqueue import Queue, Node

# Implement your PriorityQueue class using inheritance from your Queue class

class PriorityQueue( Queue ):
  def __init__(self):
    Queue.__init__(self)

  def enqueue( self, priority, item ):
    # Best Case: O(1), Worst Case: O(N)
    new_Node = PNode(item, priority)

    if self.is_empty():
      self.head = new_Node
      self.tail = new_Node
    else:
      if self.tail.priority > new_Node.priority:
        new_Node.next = self.tail
        self.tail = new_Node
      else:
        temp = self.tail
        while temp.next != None and temp.next.priority <= new_Node.priority:
          temp = temp.next
        new_Node.next = temp.next
        temp.next = new_Node
    self.size += 1

  def __str__( self ):
    return "PriorityQueue"

  def dequeue( self ):
    # Best Case: O(1), Worst Case: O(1)
    return Queue.dequeue(self)
  
class PNode(Node):
  def __init__(self, data, priority):
      Node.__init__(self, data)
      self.priority = priority

