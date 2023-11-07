# Yuqin Yang
""" Priority Queue lab: CSCI 204 """

from myqueue import Queue

class FastPriorityQueue:
  """ This class implements a fast priority queue. Priorities are positive
    integers where the highest priority is zero. The lowest priority
    (highest number) must be known when the queue is initialized."""
  
  def __init__( self, min_priority = 15 ):
    """ The queue must have a known minimum priority.
      It is initialized to hold a list for each priority.
      The lists are each initialized to be empty. """

    prio_list_size = min_priority + 1
    self.prio_lists = [ None ] * prio_list_size
    for i in range(prio_list_size):
      self.prio_lists[i] = Queue()
    self.min_priority = min_priority
  
  def __str__( self ):
    """Return the name of the queue"""
    return "FastPriorityQueue"
  
  def __len__( self ):
    """ Returns the number of items in the queue. """
    total = 0
    for i in range(self.min_priority + 1):
      total += len(self.prio_lists[i])
    return total
  
  def enqueue( self, priority, item ):
    # Best Case: O(1), Worst Case: O(1)
    """ Enqueue the given item with the given priority. Precondition:
        0 <= priority <= least priority. """
    self.prio_lists[priority].enqueue(item)
  
  def dequeue(self):
    # Best Case: O(1), Worst Case: O(min_priority)
    """ Dequeue and return the highest priority item. Returns None
        if the queue is empty. """        
    for i in range(self.min_priority + 1):
      if not self.prio_lists[i].is_empty():
        return self.prio_lists[i].dequeue()
    return None
